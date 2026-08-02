# Chat Flow - Exemplo: Fluxo com horário de atendimento

Este exemplo mostra como usar a **Tabela de Horários** para direcionar o cliente de forma diferente conforme o horário e o dia da semana — sem precisar ativar e desativar o bot manualmente.

**Cenário:** empresa com atendimento humano de segunda a sexta, das 08h às 18h. Fora desse horário, o bot envia uma mensagem de ausência e encerra o ticket.

***

### Estrutura do fluxo

```
Início
  └─► Tabela de Horários
        ├─ Seg–Sex 08h–18h → Boas-vindas (menu)
        │                         ├─ 1 → Comercial → [transfere]
        │                         └─ 2 → Suporte   → [transfere]
        └─ Fora do horário (padrão) → Mensagem de ausência → [encerra]
```

***

### Passo 1 — Adicionar a Tabela de Horários

No canvas, clique no botão **"Tabela de horários"** na barra superior para adicionar esse nó.

Conecte a linha que sai do nó **Início** para a Tabela de Horários (ao invés de apontar direto para "Boas vindas!").

***

### Passo 2 — Configurar as branches da Tabela de Horários

Clique no lápis do nó Tabela de Horários para editar.

**Branch 1 — Horário comercial:**

| Campo       | Valor                                 |
| ----------- | ------------------------------------- |
| Dias        | Segunda, Terça, Quarta, Quinta, Sexta |
| Hora início | 08:00                                 |
| Hora fim    | 18:00                                 |
| Ação        | Próxima etapa → Boas-vindas (menu)    |

**Branch Padrão — Fora do horário:**

| Campo | Valor                                |
| ----- | ------------------------------------ |
| Tipo  | Padrão (sem restrição de dia/hora)   |
| Ação  | Próxima etapa → Mensagem de ausência |

{% hint style="warning" %}
**Atenção à janela:** o horário é **\[início, fim)** — início inclusivo, fim exclusivo. Uma mensagem recebida exatamente às 18:00 **não** entra na janela das 08h–18h.

A Tabela de Horários usa o **fuso horário do servidor** onde o Prismabot está instalado. Confirme o fuso antes de configurar as janelas — se o servidor estiver em UTC, as 08h do servidor podem não corresponder às 08h da sua operação.
{% endhint %}

***

### Passo 3 — Etapa Boas-vindas (menu — horário comercial)

**Interações:**

1. Mensagem:

   > "Olá, {{firstName}}! 😊 Estamos disponíveis para te atender.
   >
   > Escolha uma opção: 1️⃣ Comercial 2️⃣ Suporte"

**Condições:**

| Tipo              | Valor | Ação                                         |
| ----------------- | ----- | -------------------------------------------- |
| Igual a           | `1`   | Próxima etapa → Comercial                    |
| Igual a           | `2`   | Próxima etapa → Suporte                      |
| Qualquer resposta | —     | Próxima etapa → Boas-vindas (reenvia o menu) |

***

### Passo 4 — Etapas Comercial e Suporte

**Etapa Comercial — Interações:**

1. Etiqueta: `Comercial`
2. Transferir: Fila "Comercial"
3. Bloquear Chatbot

**Etapa Suporte — Interações:**

1. Etiqueta: `Suporte`
2. Transferir: Fila "Suporte"
3. Bloquear Chatbot

***

### Passo 5 — Etapa Mensagem de ausência (fora do horário)

**Interações:**

1. Mensagem:

   > "Olá, {{firstName}}! Nosso atendimento funciona de **segunda a sexta, das 08h às 18h**.
   >
   > Recebemos sua mensagem e retornaremos assim que estivermos disponíveis. 🙏"
2. Transferir: Fila "Fora do Horário" *(opcional — para registrar o lead e fazer follow-up)* **ou** use a ação Encerrar na condição para fechar o ticket diretamente.

***

### Resultado esperado

**Mensagem recebida às 14h de uma quarta-feira:**

1. Tabela de Horários → branch "Seg–Sex 08h–18h" → vai para Boas-vindas
2. Cliente vê o menu e escolhe o setor
3. Etiqueta aplicada, ticket transferido, bot bloqueado

**Mensagem recebida às 20h de uma sexta-feira:**

1. Tabela de Horários → nenhuma branch de horário casa → usa o Padrão → vai para Mensagem de ausência
2. Cliente recebe a mensagem de ausência
3. Ticket encerrado (ou entra na fila "Fora do Horário" para follow-up)

**Mensagem recebida no sábado às 10h:**

1. Tabela de Horários → sábado não está nas branches de horário → usa o Padrão → vai para Mensagem de ausência

***

### Variações deste fluxo

**Quero um aviso diferente para finais de semana:**

Adicione uma segunda branch na Tabela de Horários:

* Dias: Sábado, Domingo
* Hora início: 00:00 / Hora fim: 00:00 (dia inteiro)
* Ação: Próxima etapa → Mensagem de final de semana

**Quero encaminhar para fila de plantão fora do horário:**

Na etapa "Mensagem de ausência", substitua o Encerrar por Transferir para a fila "Plantão".

**Quero encadear duas tabelas de horário:**

A Tabela de Horários pode apontar para outra tabela como ação. Use isso para criar regras mais complexas — ex: primeira tabela verifica o dia, segunda verifica o turno. O sistema suporta até 3 tabelas encadeadas.

***

### Páginas relacionadas

* [Chat Flow — Boas práticas e solução de problemas](/configuracao-administrador/automacao/chat-flow/chat-flow-boas-praticas-e-solucao-de-problemas.md)
* [Interações disponíveis](/configuracao-administrador/automacao/chat-flow/chat-flow-interacoes-disponiveis.md)
* [Configurações do Fluxo](/configuracao-administrador/automacao/chat-flow/chat-flow-configuracoes-do-fluxo.md)
* [Exemplo: Menu de departamentos](/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-menu-departamentos.md)
* [Exemplo: Qualificação de lead com captura de dados](/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-qualificacao-de-lead-com-captura-de-dados.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-fluxo-com-horario-de-atendimento.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
