# Chat Flow - Exemplo: Menu Departamentos

Este exemplo mostra como montar um fluxo completo de menu inicial com três setores de atendimento — do nó Início até a transferência. É o fluxo mais comum e serve como base para a maioria das operações.

**Cenário:** clínica odontológica com três setores — Agendamento, Financeiro e Suporte.

***

### Estrutura do fluxo

```
Início
  └─► Boas-vindas (menu)
        ├─ 1 → Agendamento  → [etiqueta + transfere + bloqueia bot]
        ├─ 2 → Financeiro   → [etiqueta + transfere + bloqueia bot]
        ├─ 3 → Suporte      → [etiqueta + transfere + bloqueia bot]
        └─ Qualquer outra   → volta para Boas-vindas (reenvia o menu)
```

***

### Passo 1 — Configure o nó Configurações primeiro

Antes de montar as etapas, clique no lápis do nó **Configurações** e preencha:

| Campo                                | Valor sugerido                                                     |
| ------------------------------------ | ------------------------------------------------------------------ |
| **Mensagem de saudação**             | "Transferindo para um atendente. Em breve alguém irá te atender!"  |
| **Opção inválida**                   | "Opção inválida. Por favor, escolha 1, 2 ou 3."                    |
| **Tempo de inatividade**             | 10 minutos → Fechar                                                |
| **Mensagem ao encerrar por timeout** | "Atendimento encerrado por inatividade. Se precisar, é só chamar!" |
| **Máximo de tentativas**             | 3 → Transferir para fila "Geral"                                   |

***

### Passo 2 — Etapa Boas-vindas (menu principal)

Esta é a etapa inicial — o cliente vê isso ao iniciar a conversa.

**Interações:**

1. Mensagem:

   > "Olá, {{firstName}}! 😊 Seja bem-vindo(a) à Clínica Sorriso.
   >
   > Por favor, escolha uma opção: 1️⃣ Agendamento 2️⃣ Financeiro 3️⃣ Suporte"

**Condições (nessa ordem):**

| Tipo              | Valor | Ação                                         |
| ----------------- | ----- | -------------------------------------------- |
| Igual a           | `1`   | Próxima etapa → Agendamento                  |
| Igual a           | `2`   | Próxima etapa → Financeiro                   |
| Igual a           | `3`   | Próxima etapa → Suporte                      |
| Qualquer resposta | —     | Próxima etapa → Boas-vindas (reenvia o menu) |

{% hint style="info" %}
A condição "Qualquer resposta" deve ser sempre a **última** da lista. Ela funciona como padrão — qualquer resposta não prevista cai aqui e o cliente vê o menu novamente.
{% endhint %}

***

### Passo 3 — Etapa Agendamento

**Interações (em ordem):**

1. Etiqueta: `Agendamento`
2. Transferir: Fila "Agendamento"
3. Bloquear Chatbot

**Condições:** nenhuma necessária — esta é uma etapa terminal. O fluxo encerra aqui para esse cliente.

***

### Passo 4 — Etapa Financeiro

**Interações (em ordem):**

1. Etiqueta: `Financeiro`
2. Transferir: Fila "Financeiro"
3. Bloquear Chatbot

***

### Passo 5 — Etapa Suporte

**Interações (em ordem):**

1. Etiqueta: `Suporte`
2. Transferir: Fila "Suporte"
3. Bloquear Chatbot

***

### Por que usar "Bloquear Chatbot" após transferir?

Sem o Bloquear Chatbot, se o cliente enviar uma nova mensagem após a transferência (como "Olá" ou "Ok"), o bot pode reinterpretar a mensagem e responder novamente — mesmo com o atendente já no ticket.

Com o Bloquear Chatbot, o bot é desativado para aquele contato e o atendente assume o controle sem interferência.

***

### Resultado esperado

1. Cliente inicia conversa no canal
2. Recebe o menu de boas-vindas com as 3 opções
3. Responde `2`
4. Recebe a etiqueta "Financeiro"
5. É transferido para a fila "Financeiro"
6. Bot é bloqueado para esse contato
7. Atendente do Financeiro recebe o ticket com a etiqueta já aplicada

***

### Variações deste fluxo

**Quero adicionar um quarto setor:** crie uma nova etapa, adicione uma nova condição "Igual a `4`" apontando para ela, e configure as interações da mesma forma.

**Quero coletar o nome antes de mostrar o menu:** adicione uma etapa antes de "Boas-vindas" com uma pergunta de nome, configure a variável `nome_cliente` e use `{{nome_cliente}}` no menu. Veja o exemplo de qualificação de lead para o passo a passo.

**Quero restringir o menu ao horário comercial:** adicione um nó **Tabela de horários** logo após o Início, apontando para o menu em horário comercial e para uma mensagem de ausência fora do horário. Veja o exemplo de fluxo com horário.

***

### Páginas relacionadas

* [Chat Flow — Boas práticas e solução de problemas](/configuracao-administrador/automacao/chat-flow/chat-flow-boas-praticas-e-solucao-de-problemas.md)
* [Interações disponíveis](/configuracao-administrador/automacao/chat-flow/chat-flow-interacoes-disponiveis.md)
* [Configurações do Fluxo](/configuracao-administrador/automacao/chat-flow/chat-flow-configuracoes-do-fluxo.md)
* [Exemplo: Qualificação de lead com captura de dados](/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-qualificacao-de-lead-com-captura-de-dados.md)
* [Exemplo: Fluxo com horário de atendimento](/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-fluxo-com-horario-de-atendimento.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-menu-departamentos.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
