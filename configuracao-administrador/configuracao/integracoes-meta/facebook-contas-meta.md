# Facebook — Contas Meta

{% hint style="warning" %}
**Disponível para o perfil: Administrador**
{% endhint %}

{% hint style="info" %}
Esta página detalha a sub-aba Login / OAuth. Para uma visão geral das Integrações Meta, acesse [Integrações Meta.](/configuracao-administrador/configuracao/integracoes-meta.md)
{% endhint %}

A sub-aba Facebook permite gerenciar a recepção de mensagens do Facebook Messenger e personalizar como a empresa se apresenta no chat oficial — configurando mensagem de boas-vindas e personas de atendentes.

[Tutorial completo de como integrar o facebook](/facebook-e-instagram-nativo/canal-instagram-nativo-beta.md)

### Como acessar

Acesse **Configurações → Integrações Meta → Contas Meta → Facebook**.

<figure><img src="/files/W03dFQajlYRyR4XGJ3R4" alt="" width="375"><figcaption></figcaption></figure>

### Você verá a seguinte tela

<figure><img src="/files/1mysyuNPIpuGBOoiwnHa" alt=""><figcaption></figcaption></figure>

### Pré-requisitos

* Deve existir uma **Página do Facebook** associada à conta
* O usuário deve ter permissão de **administrador da Página**
* A autenticação OAuth deve estar concluída na sub-aba Login / OAuth

### Verificando a conexão

1. Selecione a Página do Facebook no menu suspenso **Páginas do Facebook**
2. Clique em **Verificar Página**
3. O painel **Informações da Conexão** exibirá:

| Campo                                | Descrição                                    |
| ------------------------------------ | -------------------------------------------- |
| **Nome**                             | Nome da Página do Facebook                   |
| **Status**                           | Estado da conexão (CONNECTED / DISCONNECTED) |
| **Page ID**                          | Identificador da Página no Meta              |
| **App próprio / OAuth TechProvider** | Tipo de autenticação utilizada               |

### Ações disponíveis

| Botão                    | O que faz                                                             |
| ------------------------ | --------------------------------------------------------------------- |
| **Revalidar webhook**    | Reenvia a validação do webhook do Messenger para a Meta               |
| **Alterar origem**       | Define se os webhooks serão entregues via App Próprio ou TechProvider |
| **Diagnosticar conexão** | Verifica token e ticket de ativação da conexão                        |

### Mensagem de Boas-vindas

Configure o texto exibido automaticamente na tela inicial do Messenger antes do usuário enviar a primeira mensagem.

* Clique em **Carregar** para buscar a mensagem atual cadastrada na Meta
* Edite o texto no campo (limite de **160 caracteres**)
* Clique em **Salvar** para aplicar
* Clique em **Remover** para excluir a mensagem de boas-vindas

### Personas

Personas são remetentes alternativos que permitem exibir o nome e foto de um atendente específico no Messenger, em vez de apenas o nome da Página.

**Para criar uma persona:**

1. Clique em **Carregar lista** para verificar as personas existentes
2. Preencha o **Nome** da persona (ex: Atendente Ana)
3. Informe a **URL da foto** (opcional)
4. Clique em **+ Criar**

{% hint style="info" %}
As personas são úteis para humanizar o atendimento via Messenger — o cliente visualiza o nome e foto do atendente em vez da identidade genérica da Página.
{% endhint %}

{% hint style="warning" %}
**Webhook do Messenger (TechProvider):**

* URL: `https://oauth.techprovider.com.br/messenger-webhook`
* Segredo: `2f5b5b457e2febbc3c2333e2ebc84df926a45c36f76f3bedc0d1994f749413f1`
  {% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/configuracao/integracoes-meta/facebook-contas-meta.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
