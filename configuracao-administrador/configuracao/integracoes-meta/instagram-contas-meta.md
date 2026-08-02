# Instagram — Contas Meta

{% hint style="warning" %}
**Disponível para o perfil: Administrador**
{% endhint %}

{% hint style="info" %}
Esta página detalha a sub-aba Login / OAuth. Para uma visão geral das Integrações Meta, acesse [Integrações Meta.](/configuracao-administrador/configuracao/integracoes-meta.md)
{% endhint %}

A sub-aba Instagram permite vincular e verificar perfis profissionais do Instagram Business ao Prismabot. Com a conexão ativa, mensagens diretas (DM) e menções em Stories são capturadas e entram como tickets no sistema.

[Tutorial completo de como integrar o facebook](/facebook-e-instagram-nativo/canal-instagram-nativo-beta.md)

### Como acessar

Acesse **Configurações → Integrações Meta → Contas Meta → Instagram**.

<figure><img src="/files/q365Ri3sI3aYZtTbrNNI" alt="" width="375"><figcaption></figcaption></figure>

### Você verá a seguinte tela

<figure><img src="/files/VwqQhL0erGzc25tkrOGw" alt=""><figcaption></figcaption></figure>

### Pré-requisitos

* O perfil do Instagram deve ser uma **conta profissional (Business)**
* A conta profissional deve estar **vinculada a uma Página do Facebook**
* A autenticação OAuth deve estar concluída na sub-aba Login / OAuth

### Verificando a conexão

1. Selecione o perfil Instagram no menu suspenso **Contas do Instagram**
2. Clique em **Verificar Conta**
3. O painel **Informações da Conexão** exibirá os dados da conta:

| Campo                                | Descrição                                    |
| ------------------------------------ | -------------------------------------------- |
| **Nome**                             | Nome do perfil Instagram                     |
| **Status**                           | Estado da conexão (CONNECTED / DISCONNECTED) |
| **ID**                               | Identificador da conta no Meta               |
| **App próprio / OAuth TechProvider** | Tipo de autenticação utilizada               |

### Ações disponíveis

| Botão                    | O que faz                                                             |
| ------------------------ | --------------------------------------------------------------------- |
| **Revalidar webhook**    | Reenvia a validação do webhook do Instagram para a Meta               |
| **Alterar origem**       | Define se os webhooks serão entregues via App Próprio ou TechProvider |
| **Diagnosticar conexão** | Verifica token e ticket de ativação da conexão                        |

{% hint style="info" %}
O status deve estar como **CONNECTED** para que mensagens diretas e menções em Stories sejam recebidas como tickets no Prismabot.
{% endhint %}

{% hint style="warning" %}
**Webhook do Instagram (TechProvider):**

* URL: `https://oauth.techprovider.com.br/instagram-webhook`
* Segredo: `2f5b5b457e2febbc3c2333e2ebc84df926a45c36f76f3bedc0d1994f749413f1`
  {% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/configuracao/integracoes-meta/instagram-contas-meta.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
