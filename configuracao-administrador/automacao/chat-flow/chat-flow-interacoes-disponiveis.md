# Chat Flow - Interações disponíveis

As interações são as ações que o bot executa dentro de uma etapa. Uma etapa pode ter várias interações, executadas em ordem, de cima para baixo. Use o menu **"Adicionar interação"** dentro de qualquer etapa para incluí-las.

{% hint style="warning" %}
**Regra importante para integrações externas:** interações que passam o controle para sistemas externos (Typebot, ChatGPT, n8n, VAPI etc.) devem sempre ser a **última interação da etapa**. Veja detalhes na seção Integrações externas.
{% endhint %}

***

### Mensagens e mídia

Interações que enviam conteúdo diretamente ao contato.

| Interação             | O que faz                                                      | Quando usar                                                           |
| --------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Mensagem**          | Envia texto. Aceita variáveis como `{{name}}` e `{{greeting}}` | Saudações, menus de opções, perguntas, instruções                     |
| **Mídia**             | Envia imagem, vídeo, áudio, PDF ou documento                   | Catálogo de produtos, tutorial em vídeo, comprovante, contrato        |
| **Botões**            | Envia até 3 botões de resposta rápida clicáveis                | Menus simples com 2 ou 3 opções — guia o cliente para escolhas claras |
| **Lista**             | Envia um menu organizado em seções com múltiplos itens         | Menus com muitas opções — departamentos, produtos, serviços           |
| **Contato**           | Envia um cartão de contato (vCard)                             | Compartilhar número de um atendente, parceiro ou fornecedor           |
| **Localização**       | Envia um ponto no mapa                                         | Endereço da loja, ponto de encontro, local de entrega                 |
| **Sticker**           | Envia uma figurinha                                            | Comunicação mais descontraída com o cliente                           |
| **Botão PIX**         | Envia uma chave PIX formatada como botão                       | Cobrança rápida durante o atendimento automatizado                    |
| **Vídeo Conferência** | Gera e envia link de videochamada (Jitsi ou Google Meet)       | Agendar reunião ou suporte visual em tempo real                       |

{% hint style="info" %}
**Botões** e **Lista** funcionam com interações clicáveis em conexões Baileys, WABA e UazAPI. Em canais sem suporte nativo a esses recursos, o conteúdo pode ser enviado como texto numerado.
{% endhint %}

***

### Roteamento

Interações que definem o destino do ticket ou encerram a atuação do bot.

| Interação            | O que faz                                                                     | Quando usar                                                            |
| -------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Transferir**       | Encaminha o ticket para uma fila, usuário específico ou encerra o atendimento | Após qualificação, para direcionar o cliente ao humano certo           |
| **Sub-fluxo**        | Transfere o atendimento para outro fluxo existente                            | Modularizar fluxos — ex: um fluxo "Menu" chama um fluxo "Suporte"      |
| **Razões**           | Define o motivo de encerramento do ticket                                     | Registrar o motivo de fechamento para relatórios e análises            |
| **Bloquear Chatbot** | Impede que o bot responda futuras mensagens daquele contato                   | Após transferir para humano — evita que o bot interfira no atendimento |

{% hint style="warning" %}
**Transferir** encaminha o ticket mas **não** bloqueia o bot automaticamente. Se o cliente enviar uma nova mensagem após a transferência, o bot pode reinterpretar e responder. Use **Bloquear Chatbot** logo após o Transferir quando não quiser mais que o bot atue naquele contato.
{% endhint %}

***

### CRM e automação

Interações que registram informações e avançam processos internos sem enviar mensagens ao cliente.

| Interação           | O que faz                                                         | Quando usar                                                          |
| ------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Etiqueta**        | Aplica uma etiqueta ao contato                                    | Qualificar lead, marcar interesse, segmentar para campanhas futuras  |
| **Kanban**          | Move o contato para uma coluna do Kanban                          | Avançar o contato em uma esteira de atendimento ou vendas            |
| **Oportunidade**    | Cria uma oportunidade no Funil de Vendas vinculada ao contato     | Registrar automaticamente um lead qualificado no pipeline comercial  |
| **Notas**           | Cria uma nota interna no ticket (não enviada ao contato)          | Registrar dados coletados para o atendente que vai assumir           |
| **Agendamento**     | Agenda o envio de uma mensagem para um momento futuro             | Lembrete automático, follow-up após 24h, mensagem programada         |
| **Consulta Agenda** | Cria um compromisso vinculado ao contato                          | Registrar agendamento de serviço, reunião ou visita                  |
| **Google Agenda**   | Cria um evento no Google Calendar (requer integração configurada) | Agendar reunião automaticamente na agenda do atendente ou da empresa |

***

### Integrações externas

Interações que passam o controle da conversa para sistemas externos ou acionam automações fora do Prismabot.

{% hint style="danger" %}
**Regra de ouro:** posicione sempre como **última interação da etapa**.\
Quando a integração externa assume o controle, o fluxo interno não deve ter mais ações após ela na mesma etapa — caso contrário, ambos respondem em paralelo, gerando mensagens duplicadas ou comportamento inesperado.
{% endhint %}

| Interação            | O que faz                                                                     | Quando usar                                                              |
| -------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **ChatGPT**          | Entrega o atendimento para uma IA com prompt configurado                      | Atendimento inteligente, FAQ automatizado, triagem por IA                |
| **Typebot**          | Entrega o atendimento para um fluxo do Typebot                                | Formulários complexos, coleta estruturada de dados                       |
| **n8n**              | Aciona uma automação no n8n via webhook                                       | Processos complexos, integrações com outros sistemas                     |
| **Webhook**          | Faz uma requisição GET simples a uma URL externa                              | Notificações básicas, acionar automações simples                         |
| **Webhook Avançado** | HTTP completo (GET/POST/PUT/DELETE) com headers, body, retentativas e timeout | Integrar com CRMs, ERPs, APIs externas — enviar dados coletados no fluxo |
| **SMS**              | Envia um SMS para o contato pelo serviço configurado                          | Confirmações ou alertas fora do WhatsApp                                 |
| **VAPI**             | Inicia uma ligação telefônica com IA de voz                                   | Qualificação automatizada por telefone, confirmações de agendamento      |

***

### Utilitários

| Interação  | O que faz                                                  | Quando usar                                                                                           |
| ---------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Atraso** | Pausa a execução por N segundos antes da próxima interação | Dar tempo de leitura entre mensagens longas — simula digitação humana e torna a conversa mais natural |

***

### Páginas relacionadas

* [Chat Flow — Boas práticas e solução de problemas](/configuracao-administrador/automacao/chat-flow/chat-flow-boas-praticas-e-solucao-de-problemas.md)
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
GET https://prismatelecomservicos.com/configuracao-administrador/automacao/chat-flow/chat-flow-interacoes-disponiveis.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
