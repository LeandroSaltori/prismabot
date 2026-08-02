# Configurações — Integrações Meta

{% hint style="warning" %}
**Disponível para o perfil: Administrador**
{% endhint %}

{% hint style="info" %}
Esta página detalha a sub-aba Login / OAuth. Para uma visão geral das Integrações Meta, acesse [Integrações Meta.](/configuracao-administrador/configuracao/integracoes-meta.md)
{% endhint %}

A aba Configurações centraliza os parâmetros técnicos de backend da integração com a Meta — URLs de webhook, token de acesso à API e verificação da conta WABA. Estas configurações são necessárias para que o sistema receba e envie mensagens pelos canais oficiais.

### Como acessar

Acesse **Configurações → Integrações Meta → Configurações**.

<figure><img src="/files/P5QoVYfpLTvU9enraXCL" alt=""><figcaption></figcaption></figure>

### Você verá a seguinte tela

<figure><img src="/files/LcNrfolNyyhR31oOzeEh" alt=""><figcaption></figcaption></figure>

***

### URLs de Webhook

Exibe as URLs de recebimento de notificações da Meta para cada canal. Essas URLs devem ser cadastradas no painel Meta Developers quando você utiliza um **App próprio** (Opção 2 de conectividade).

| Canal                            | URL                                        |
| -------------------------------- | ------------------------------------------ |
| **WABA (WhatsApp Business API)** | `https://[seu-dominio]/metaWebhook/1`      |
| **Instagram**                    | `https://[seu-dominio]/instagramWebhook/1` |
| **Messenger (Facebook)**         | `https://[seu-dominio]/messengerWebhook/1` |

Use o ícone de **copiar** ao lado de cada URL para copiá-la rapidamente.

{% hint style="info" %}
Se você utiliza o **App TechProvider (OAuth Prismabot)**, as URLs de webhook já estão configuradas automaticamente pelo proxy da Prismabot. Você não precisa cadastrá-las manualmente no Meta Developers.

As URLs só precisam ser configuradas manualmente se você operar com **App próprio** no Meta Developers.
{% endhint %}

***

### BSUID Estrito (compliance WABA 2026)

Configuração de conformidade com a especificação Meta de 2026. Quando ativado, mensagens enviadas para usuários com **username privado** usam o campo dedicado `recipient` (BSUID) conforme exigido pela Meta.

| Opção                         | Descrição                                                          |
| ----------------------------- | ------------------------------------------------------------------ |
| **Ativar modo estrito BSUID** | Ativa o uso do campo BSUID para destinatários com username privado |

{% hint style="warning" %}
Mantenha esta opção **desativada** até que a Meta libere o GA (General Availability) do envio por BSUID no seu portfolio. Ativar antes do prazo não muda o comportamento atual de envio e pode causar inconsistências.
{% endhint %}

***

### Token Meta

Local para salvar e renovar o token de acesso permanente à API da Meta. Este token é necessário para que o sistema se comunique com a Graph API.

| Ação                 | Descrição                                          |
| -------------------- | -------------------------------------------------- |
| **Salvar Token**     | Salva o token inserido no campo                    |
| **Gerar Novo Token** | Gera um novo token de acesso via autenticação Meta |

Use o ícone de **olho** para visualizar o token salvo e o ícone de **copiar** para copiá-lo.

{% hint style="warning" %}
Mantenha o token atualizado para evitar interrupções nos canais. Um token expirado ou inválido interrompe o recebimento e envio de mensagens em todos os canais oficiais conectados.
{% endhint %}

***

### Verificação WABA

Ferramenta para validar a conta WABA e confirmar que a Business Manager e a versão da API estão configuradas corretamente.

Preencha os campos e clique em **Verificar BM**:

| Campo             | Descrição                                          |
| ----------------- | -------------------------------------------------- |
| **WABA ID**       | Identificador da conta WhatsApp Business no Meta   |
| **Versão da API** | Versão da Graph API configurada (ex: v19.0)        |
| **WABA Token**    | Token de acesso da conta WABA (formato EAAxxxx...) |

{% hint style="info" %}
Use a Verificação WABA quando suspeitar que a conta está com problemas de autenticação ou após atualizar as credenciais. O resultado indica se a Business Manager está verificada e se a versão da API está compatível.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/configuracao/integracoes-meta/configuracoes-integracoes-meta.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
