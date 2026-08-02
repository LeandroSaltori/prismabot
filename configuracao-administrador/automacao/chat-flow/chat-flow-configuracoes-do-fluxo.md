# Chat Flow - Configurações do Fluxo

O nó **Configurações** é o painel de controle global do fluxo. Ele não envia mensagens nem aguarda resposta do cliente — define como o bot se comporta em situações especiais: quando o cliente erra, quando não responde, quando usa uma palavra-chave, e como encerrar.

Para acessar, clique no ícone de lápis no nó **Configurações** dentro do canvas.

## Configurações do Fluxo

O nó **Configurações** é o painel de controle global do fluxo. Ele não envia mensagens nem aguarda resposta do cliente — define como o bot se comporta em situações especiais: quando o cliente erra, quando não responde, quando usa uma palavra-chave, e como encerrar.

Para acessar, clique no ícone de lápis no nó **Configurações** dentro do canvas.

<figure><img src="/files/gsHS0LPdYcXrRyJveZ1v" alt=""><figcaption></figcaption></figure>

Todos os campos são opcionais — mas configurar os principais garante que o fluxo se comporte de forma previsível em qualquer situação.

<figure><img src="/files/i8sfgIEHWTu2W9gA9SL5" alt=""><figcaption></figcaption></figure>

***

### Mensagem de saudação (Fila/Usuário)

**O que faz:** enviada automaticamente quando o bot direciona o atendimento para uma fila ou usuário (ação Transferir).

**Exemplo:**

> "Perfeito! Estou te conectando com um atendente do Comercial. Em instantes alguém irá te atender. 😊"

**Quando configurar:** sempre que o fluxo tiver uma ação de transferência — evita que o cliente fique sem retorno ao ser encaminhado para um humano.

***

### Opção inválida

**O que faz:** enviada quando o cliente responde algo que não corresponde a nenhuma condição da etapa atual. Também chamada de mensagem de fallback.

**Exemplo:**

> "Não entendi sua resposta. Por favor, escolha uma das opções disponíveis: 1 para Comercial ou 2 para Suporte."

**Quando configurar:** em qualquer fluxo com menu de opções. Sem esse campo, o cliente fica parado sem orientação ao errar.

{% hint style="info" %}
Após enviar a mensagem de opção inválida, o bot reenvia as interações da etapa atual — o cliente vê o menu novamente e pode escolher de novo. Esse ciclo se repete até atingir o **máximo de tentativas**.
{% endhint %}

***

### Palavra-chave de ativação

**O que faz:** quando o cliente envia essa palavra, o fluxo é acionado (ou reativado) — mesmo durante um atendimento em andamento com outro bot ou após uma transferência.

**Exemplos de palavras:** `menu`, `iniciar`, `voltar`, `atendimento`, `ajuda`

**Quando configurar:** quando você quer permitir que o cliente volte ao menu principal a qualquer momento, sem precisar abrir uma nova conversa.

{% hint style="info" %}
A comparação é flexível — a palavra pode aparecer em qualquer parte da mensagem do cliente e não diferencia maiúsculas de minúsculas. Exemplo: "Quero o menu de opções" também ativa o fluxo se a palavra-chave for `menu`.
{% endhint %}

***

### Sem resposta (timeout)

**O que faz:** define o que acontece quando o cliente não responde dentro de um tempo limite.

**Campos:**

| Campo               | Descrição                              |
| ------------------- | -------------------------------------- |
| **Tempo (min)**     | Quantos minutos aguardar antes de agir |
| **Encaminhar para** | Fila / Agente / Fechar / Canal         |

**Exemplo:**

> Tempo: 15 minutos → Fechar

**Quando configurar:** sempre. Sem timeout, tickets ficam abertos indefinidamente quando o cliente abandona o atendimento no meio do fluxo.

***

### Aviso antes do timeout

**O que faz:** ativa uma mensagem de aviso enviada ao cliente antes de executar a ação de timeout.

**Exemplo:**

> "Olá! Percebemos que você ainda não respondeu. Estamos aqui caso precise de ajuda. 😊"

**Quando configurar:** quando quiser dar uma última chance ao cliente antes de encerrar ou transferir por inatividade — melhora a experiência e pode recuperar contatos que se distraíram.

***

### Mensagem ao encerrar por timeout

**O que faz:** enviada ao cliente quando o ticket é encerrado por inatividade (após o tempo de timeout).

**Exemplo:**

> "Encerramos seu atendimento por inatividade. Se precisar de algo, é só nos chamar novamente. Até logo! 👋"

***

### Máximo de tentativas do bot

**O que faz:** define quantas vezes o cliente pode responder algo inválido antes de o bot tomar uma ação automática.

**Campos:**

| Campo               | Descrição                                                 |
| ------------------- | --------------------------------------------------------- |
| **Tentativas**      | Número de erros permitidos antes da ação. Padrão: 3       |
| **Encaminhar para** | Fila / Agente / Fechar / Canal após esgotar as tentativas |

**Exemplo:**

> 3 tentativas → Transferir para fila "Suporte Geral"

**Quando configurar:** sempre. Sem esse limite, o cliente pode ficar preso em loop indefinidamente ao responder algo que o bot não entende.

***

### Primeira interação

**O que faz:** define para onde rotear o ticket na **primeira mensagem** do cliente, antes de o fluxo apresentar qualquer etapa.

**Quando configurar:** quando quiser triar ou redirecionar imediatamente com base em alguma condição, sem passar pelo fluxo normal. Útil para direcionar de forma diferente dependendo do canal de origem.

***

### Fora do horário

**O que faz:** define a ação executada quando o cliente interage fora do horário de atendimento configurado nas filas.

**Campos:**

| Campo               | Descrição                      |
| ------------------- | ------------------------------ |
| **Encaminhar para** | Fila / Agente / Fechar / Canal |

**Exemplo:**

> Fora do horário → Fechar (e envia a mensagem de despedida)

**Quando configurar:** quando o canal tem horários de atendimento definidos nas filas e você quer que o bot tome uma ação específica para contatos que chegam fora desse horário — em vez de deixar o ticket parado sem resposta.

{% hint style="info" %}
Esta configuração complementa a **Tabela de Horários** (nó do canvas). Use a Tabela de Horários quando quiser rotear dentro do próprio fluxo; use "Fora do horário" aqui quando quiser uma ação global para todo o fluxo baseada no horário das filas.
{% endhint %}

***

### Distribuição automática de tickets

**O que faz:** define como o ticket é distribuído entre os atendentes da fila ao ser transferido pelo bot.

| Opção          | Comportamento                                         |
| -------------- | ----------------------------------------------------- |
| **Nenhuma**    | Ticket entra na fila sem atribuição automática        |
| **Aleatória**  | Atribuído aleatoriamente entre os agentes disponíveis |
| **Balanceada** | Atribuído ao agente com menos tickets abertos         |
| **Sequencial** | Distribuído em ordem, um por um                       |

***

### Parâmetros para fechar ticket

**O que faz:** se o cliente enviar qualquer uma dessas palavras durante o fluxo, o bot encerra o ticket automaticamente e envia a mensagem de despedida.

**Exemplos:** `sair`, `encerrar`, `finalizar`, `cancelar`, `obrigado`

**Quando configurar:** quando o atendimento for totalmente automatizado e você quer dar ao cliente a opção de encerrar a qualquer momento, sem precisar de intervenção humana.

***

### Mensagem de despedida

**O que faz:** enviada ao cliente quando o ticket é encerrado pelo bot — seja por palavra de encerramento, timeout ou condição final de encerramento.

**Exemplo:**

> "Obrigado pelo contato! Se precisar de ajuda novamente, é só nos chamar. Até logo! 😊"

***

### Páginas relacionadas

* [Chat Flow — Boas práticas e solução de problemas](/configuracao-administrador/automacao/chat-flow/chat-flow-boas-praticas-e-solucao-de-problemas.md)
* [Interações disponíveis](/configuracao-administrador/automacao/chat-flow/chat-flow-interacoes-disponiveis.md)
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
GET https://prismatelecomservicos.com/configuracao-administrador/automacao/chat-flow/chat-flow-configuracoes-do-fluxo.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
