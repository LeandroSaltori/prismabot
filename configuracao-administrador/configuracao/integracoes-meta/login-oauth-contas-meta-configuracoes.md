# Login / OAuth — Contas Meta (Configurações)

{% hint style="warning" %}
**Disponível para o perfil: Administrador**
{% endhint %}

{% hint style="info" %}
Esta página detalha a sub-aba Login / OAuth. Para uma visão geral das Integrações Meta, acesse [Integrações Meta.](/configuracao-administrador/configuracao/integracoes-meta.md)
{% endhint %}

A sub-aba Login / OAuth é o ponto de entrada da integração com a Meta. É aqui que o Prismabot recebe autorização para gerenciar canais oficiais (WhatsApp, Instagram e Facebook) através de autenticação OAuth.

### Como acessar

Acesse **Configurações → Integrações Meta → Contas Meta → Login / OAuth**.

<figure><img src="/files/ztuLzM8n6t8gUPLV8j0h" alt="" width="375"><figcaption></figcaption></figure>

### Você verá a seguinte tela

### Opções de aplicativo

O campo **Aplicativo** define qual app Meta será usado para autenticação e gerenciamento dos canais. Há duas opções:

#### OAuth TechProvider&#x20;

Selecione o aplicativo nativo da Prismabot na lista. O sistema gerencia as credenciais automaticamente via proxy OAuth — não é necessário configurar nada manualmente.

Esta é a opção padrão para a maioria dos licenciados e a mais simples de operar.

#### App próprio

Se sua empresa é um Tech Provider aprovado pela Meta e possui um aplicativo próprio cadastrado no Meta Developers, preencha manualmente:

| Campo                  | Descrição                                       |
| ---------------------- | ----------------------------------------------- |
| **App ID**             | ID do aplicativo no Meta Developers             |
| **Versão da API**      | Versão da Graph API a ser utilizada (ex: v19.0) |
| **ID de Configuração** | ID de configuração do Embedded Signup           |

### Autenticando

1. Com o aplicativo selecionado, clique em **Login com Facebook**
2. Uma janela pop-up da Meta será aberta — authorize as permissões solicitadas para WhatsApp, Instagram e Facebook
3. Após o retorno, clique em **Verificar Status** para confirmar se o token foi gerado com sucesso (Status: *Success*)

{% hint style="warning" %}
O OAuth precisa estar ativo no Super Admin antes de usar esta tela. Se o botão **Login com Facebook** não funcionar ou os canais não aparecerem após a autenticação, verifique se o OAuth está habilitado para o tenant em **Super Admin → Tenants → Editar → OAuth (Login Incorporado)**.
{% endhint %}

{% hint style="info" %}
Para o passo a passo completo de como conectar um número WhatsApp via OAuth, acesse [WhatsApp Oficial — OAuth Login](https://prismatelecomservicos.com/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/whatsapp-oficial-oauth-login).
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/configuracao/integracoes-meta/login-oauth-contas-meta-configuracoes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
