# Chat Flow - Boas práticas e solução de problemas

{% hint style="warning" %}
**Disponível para o perfil:** Administrador e Supervisor
{% endhint %}

***

### Antes de criar: planeje o fluxo primeiro

Abrir o canvas sem planejar é a causa número um de fluxos com comportamento imprevisível. Antes de criar qualquer etapa, responda:

* Qual será a mensagem inicial?
* Quais opções o cliente poderá escolher?
* O que acontece com cada resposta?
* Quando o bot transfere para um humano?
* O que acontece se o cliente não responder?
* O que acontece se o cliente responder algo inválido?
* Como o atendimento é encerrado?

**Um bom fluxo tem começo, meio e fim claros.** Fluxos sem finalização definida são a principal causa de bot respondendo quando não deveria.

***

### Nova etapa precisa estar conectada

Criar uma etapa no canvas **não** faz ela aparecer para o cliente automaticamente.

Para uma etapa funcionar, ela precisa estar apontada por uma **condição da etapa anterior**.

**Exemplo de erro:**

* Você cria a etapa "Suporte"
* Mas na etapa "Menu principal" não há nenhuma condição apontando para "Suporte"
* Resultado: o cliente nunca chega lá

**Como resolver:** após criar uma etapa, vá na etapa anterior, adicione uma condição e aponte para a nova etapa criada.

{% hint style="info" %}
Use o botão **Avisos** no canvas para identificar etapas sem conexão e outros problemas de configuração no fluxo.
{% endhint %}

***

### A ordem das interações dentro de uma etapa importa

O bot executa as interações **de cima para baixo**, em sequência. A ordem que você configura é a ordem que o cliente vive.

**Ordem recomendada dentro de uma etapa:**

1. Mensagens e delays (o que o cliente vai receber)
2. Ações de CRM (etiqueta, kanban, oportunidade, notas)
3. Integrações externas — webhook, n8n, IA (quando necessário)
4. Transferência — sempre como última ação

{% hint style="danger" %}
**Nunca coloque uma integração externa (Typebot, IA, n8n, VAPI) no meio de uma etapa com outras ações depois dela.**\
Quando a integração assume o controle, o fluxo interno pode continuar executando as interações seguintes em paralelo — gerando mensagens duplicadas, tickets extras ou comportamento inesperado.
{% endhint %}

***

### Bot continua respondendo após a transferência

Esse é o problema mais relatado. O bot transfere o atendimento, mas continua respondendo novas mensagens do cliente.

**Causas mais comuns e como resolver:**

| Causa                                                   | Como resolver                                                                                     |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| O fluxo não encerra a atuação do bot após transferir    | Adicione a interação **Bloquear Chatbot** logo após o Transferir                                  |
| Outra automação ativa no canal (Typebot, Dify, n8n, IA) | Verifique se outra integração está respondendo em paralelo no mesmo canal                         |
| A transferência foi usada como encerramento do fluxo    | Transferir encaminha o ticket — não bloqueia o bot. Use sempre Bloquear Chatbot quando necessário |

**Resumo das três ações e o que cada uma faz:**

| Ação                            | O que faz                                                   |
| ------------------------------- | ----------------------------------------------------------- |
| **Transferir**                  | Encaminha o ticket para uma fila ou usuário                 |
| **Bloquear Chatbot**            | Impede que o bot responda futuras mensagens daquele contato |
| **Encerrar (ação da condição)** | Fecha o ticket e envia a mensagem de despedida              |

Para garantir que o bot pare completamente após transferir, use as três em sequência quando necessário: Transferir → Bloquear Chatbot. Se quiser encerrar sem transferir, use a ação Encerrar na condição.

***

### Integrações externas no fluxo

Algumas interações passam o controle da conversa para sistemas externos (Typebot, ChatGPT, n8n, Dify, VAPI). Quando isso acontece, o fluxo interno do Prismabot **não deve continuar executando ações em paralelo**.

**Regra:** posicione sempre como **última interação da etapa**, sem nada depois dela.

**Problemas causados por posicionar errado:**

* Cliente recebe mensagens duplicadas (bot interno + Typebot respondendo juntos)
* n8n reenvia o evento como nova mensagem e cria ticket duplicado
* IA responde depois que o atendimento já foi transferido para um humano
* Webhook dispara múltiplas vezes para a mesma conversa

**Como evitar:** defina claramente qual sistema controla cada momento da conversa. Quando a integração externa assume, o bot interno encerra.

***

### Variáveis — use de forma sequencial

As variáveis capturadas em etapas do fluxo ficam disponíveis para uso nas etapas seguintes.

**Regra prática:** capture na etapa N, use na etapa N+1.

**Funciona bem:**

> Etapa 1 captura o nome → Etapa 2 usa `{{nome_cliente}}` na mensagem

**Evite:**

> Capturar 5 variáveis em etapas diferentes e montar um resumo final várias etapas depois — o comportamento pode não ser o esperado dependendo de como o fluxo se ramifica

**Para enviar todos os dados coletados para um sistema externo:** use um **Webhook Avançado** ao final do fluxo — ele consegue montar o payload completo com todas as variáveis capturadas até aquele ponto.

***

### Configure sempre o fallback e o máximo de tentativas

**Fallback (Opção inválida):** mensagem enviada quando o cliente responde algo que não bate em nenhuma condição da etapa atual.

Sem fallback, o cliente fica parado sem orientação. Configure sempre no **nó Configurações** do fluxo.

> Exemplo: "Não entendi sua resposta. Por favor, escolha 1 para Comercial ou 2 para Suporte."

**Máximo de tentativas:** após N respostas inválidas consecutivas, o bot toma uma ação definida (transferir, encerrar, etc.). O padrão é 3 tentativas.

Sem esse limite, o cliente pode ficar em loop dentro do fluxo respondendo coisas que o bot não entende, indefinidamente.

***

### Dois chatbots respondendo ao mesmo tempo

Quando o canal possui mais de uma automação ativa — por exemplo, o Chat Flow do Prismabot e um Typebot ou uma IA configurada — é preciso garantir que apenas um responda por vez.

**Sinais de que isso está acontecendo:**

* Cliente recebe mensagens duplicadas ou fora de ordem
* Bot responde depois que o atendente já assumiu
* Atendente vê mensagens que não enviou

**Como diagnosticar:** verifique as configurações do canal e confirme quais automações estão ativas. Desative ou organize a ordem de prioridade entre elas.

***

### Checklist de revisão

Antes de ativar um fluxo, verifique cada item:

**Configuração básica**

* [ ] O fluxo está vinculado ao canal correto?
* [ ] O fluxo está marcado como **Ativo**?
* [ ] O número de teste foi removido (ou está correto para o ambiente)?

**Estrutura do fluxo**

* [ ] Todas as etapas têm pelo menos uma condição apontando para algum lugar?
* [ ] Existe uma condição "Qualquer resposta" como última opção em cada etapa com menu?
* [ ] Nenhuma etapa criada ficou sem conexão com a etapa anterior?

**Configurações do fluxo (nó Configurações)**

* [ ] Mensagem de fallback (opção inválida) configurada?
* [ ] Máximo de tentativas definido com ação de saída?
* [ ] Timeout (ausência de resposta) configurado com tempo e ação definidos?
* [ ] Mensagem de despedida configurada (quando o bot encerra o ticket)?

**Finalização**

* [ ] O fluxo tem uma saída clara para cada caminho possível?
* [ ] "Bloquear Chatbot" está sendo usado após as transferências?
* [ ] Integrações externas estão na última posição da etapa?
* [ ] Não há etapas "soltas" no canvas que o cliente nunca alcança?

**Se o fluxo não funcionar como esperado, verifique também:**

* [ ] O canal está conectado e ativo?
* [ ] A conversa foi iniciada pelo cliente (não pelo sistema)?
* [ ] O atendimento já foi assumido por um usuário antes do bot atuar?
* [ ] Existe outra automação ativa no canal (Typebot, IA, n8n, Dify)?
* [ ] A resposta do cliente corresponde exatamente ao valor configurado na condição?

***

### Páginas relacionadas

* [Chat Flow — Como funciona](/configuracao-administrador/automacao/chat-flow.md)
* [Interações disponíveis](/configuracao-administrador/automacao/chat-flow/chat-flow-interacoes-disponiveis.md)
* [Configurações do Fluxo](/configuracao-administrador/automacao/chat-flow/chat-flow-configuracoes-do-fluxo.md)
* [Exemplo: Menu de departamentos](/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-menu-departamentos.md)
* [Exemplo: Qualificação de lead com captura de dados](/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-qualificacao-de-lead-com-captura-de-dados.md)
* [Exemplo: Fluxo com horário de atendimento](/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-fluxo-com-horario-de-atendimento.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/automacao/chat-flow/chat-flow-boas-praticas-e-solucao-de-problemas.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
