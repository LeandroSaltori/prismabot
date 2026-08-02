# Chat Flow - Exemplo: Qualificação de lead com captura de dados

Este exemplo mostra como montar um fluxo que coleta nome, interesse e e-mail do contato, aplica etiquetas e cria uma oportunidade automaticamente no Funil de Vendas — sem intervenção humana até o momento certo.

**Cenário:** empresa de software B2B que recebe leads via WhatsApp.

***

### Estrutura do fluxo

```
Início
  └─► Boas-vindas
        └─► Captura de nome
              └─► Captura de interesse
                    ├─ 1 ou "básico" → Etapa Básico → Captura de e-mail
                    ├─ 2 ou "pro"    → Etapa Pro    → Captura de e-mail
                    └─ Qualquer      →               → Captura de e-mail
                                                           └─► Finalização
                                                                 └─► [etiqueta + oportunidade + nota + transfere]
```

***

### Passo 1 — Etapa Boas-vindas

**Interações:**

1. Mensagem:

   > "Olá! 👋 Obrigado pelo interesse no nosso sistema.
   >
   > Vou te fazer algumas perguntas rápidas para entender como podemos ajudar.
   >
   > Pode começar me dizendo seu **nome**?"

**Variável (opcional):**

* Chave: `nome_lead`
* Rótulo: Nome do lead

**Condição:**

| Tipo              | Valor | Ação                                 |
| ----------------- | ----- | ------------------------------------ |
| Qualquer resposta | —     | Próxima etapa → Captura de interesse |

{% hint style="info" %}
A variável `nome_lead` salva exatamente o que o cliente digitar como resposta. Por isso, faça perguntas diretas esperando respostas curtas e objetivas.
{% endhint %}

***

### Passo 2 — Etapa Captura de interesse

**Interações:**

1. Mensagem:

   > "Ótimo, {{nome\_lead}}! 😊
   >
   > Qual plano você tem interesse? 1️⃣ Básico 2️⃣ Pro"

**Condições:**

| Tipo              | Valor              | Ação                                                   |
| ----------------- | ------------------ | ------------------------------------------------------ |
| Igual a           | `1`                | Próxima etapa → Plano Básico                           |
| Contém            | `basico`, `básico` | Próxima etapa → Plano Básico                           |
| Igual a           | `2`                | Próxima etapa → Plano Pro                              |
| Contém            | `pro`              | Próxima etapa → Plano Pro                              |
| Qualquer resposta | —                  | Próxima etapa → Captura de e-mail (sem plano definido) |

{% hint style="info" %}
Use a condição **Contém** para capturar variações naturais de resposta, como "quero o básico" ou "estou interessado no Pro". Isso torna o fluxo mais robusto sem precisar listar todas as combinações possíveis.
{% endhint %}

***

### Passo 3 — Etapas Plano Básico e Plano Pro

Crie uma etapa para cada plano. Elas apenas aplicam a etiqueta correta e seguem para a mesma próxima etapa.

**Etapa Plano Básico — Interações:**

1. Etiqueta: `Plano Básico`
2. *(sem mensagem aqui — a próxima etapa já continua a conversa)*

**Condição:** Qualquer resposta → Captura de e-mail

***

**Etapa Plano Pro — Interações:**

1. Etiqueta: `Plano Pro`

**Condição:** Qualquer resposta → Captura de e-mail

{% hint style="info" %}
Essas etapas intermediárias são "etapas de ação silenciosa" — apenas aplicam a etiqueta e encaminham para a próxima, sem enviar mensagem ao cliente. O cliente não percebe a transição.
{% endhint %}

***

### Passo 4 — Etapa Captura de e-mail

**Interações:**

1. Mensagem:

   > "Para finalizar, pode me informar seu **e-mail**?"

**Variável (opcional):**

* Chave: `email_lead`
* Rótulo: E-mail do lead

**Condição:**

| Tipo              | Valor | Ação                        |
| ----------------- | ----- | --------------------------- |
| Qualquer resposta | —     | Próxima etapa → Finalização |

***

### Passo 5 — Etapa Finalização

Esta etapa fecha o ciclo de qualificação: agradece, cria a oportunidade, registra uma nota interna e transfere para o comercial.

**Interações (em ordem):**

1. Mensagem:

   > "Obrigado, {{nome\_lead}}! Suas informações foram registradas.
   >
   > Um especialista entrará em contato em breve. 🚀"
2. Oportunidade:
   * Nome: `Lead - {{nome_lead}}`
   * Pipeline: "Novos Leads"
   * Etapa: "Qualificado"
3. Notas:
   * Conteúdo: `Lead qualificado pelo bot. E-mail: {{email_lead}}`
4. Transferir: Fila "Comercial"
5. Bloquear Chatbot

**Condições:** nenhuma — etapa terminal.

***

### Resultado esperado

| Etapa                  | O que o cliente vive                               |
| ---------------------- | -------------------------------------------------- |
| Boas-vindas            | Vê a pergunta de nome                              |
| Responde "Maria"       | Bot salva `{{nome_lead}} = Maria`                  |
| Captura de interesse   | Vê: "Ótimo, Maria! Qual plano..."                  |
| Responde "quero o pro" | Etiqueta "Plano Pro" aplicada silenciosamente      |
| Captura de e-mail      | Vê a pergunta de e-mail                            |
| Responde o e-mail      | Bot salva `{{email_lead}}`                         |
| Finalização            | Recebe a mensagem de confirmação                   |
| —                      | Oportunidade criada automaticamente no Funil       |
| —                      | Nota interna registrada para o atendente           |
| —                      | Ticket transferido para fila "Comercial"           |
| —                      | Bot bloqueado — atendente assume sem interferência |

***

### Dica: regra das variáveis sequenciais

Capture a variável em uma etapa e use na próxima. Não tente usar `{{nome_lead}}` duas etapas antes de capturá-lo — o valor ainda não existe naquele momento.

Para enviar todos os dados coletados para um CRM ou sistema externo, use um **Webhook Avançado** na etapa de Finalização — ele consegue montar o payload completo com `{{nome_lead}}`, `{{email_lead}}` e outras variáveis capturadas durante o fluxo.

***

### Páginas relacionadas

* [Chat Flow — Boas práticas e solução de problemas](/configuracao-administrador/automacao/chat-flow/chat-flow-boas-praticas-e-solucao-de-problemas.md)
* [Interações disponíveis](/configuracao-administrador/automacao/chat-flow/chat-flow-interacoes-disponiveis.md)
* [Configurações do Fluxo](/configuracao-administrador/automacao/chat-flow/chat-flow-configuracoes-do-fluxo.md)
* [Exemplo: Menu de departamentos](/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-menu-departamentos.md)
* [Exemplo: Fluxo com horário de atendimento](/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-fluxo-com-horario-de-atendimento.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/automacao/chat-flow/chat-flow-exemplo-qualificacao-de-lead-com-captura-de-dados.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
