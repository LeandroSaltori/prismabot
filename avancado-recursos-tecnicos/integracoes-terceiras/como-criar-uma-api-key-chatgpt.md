# Como criar uma API Key ChatGPT

### Passo 1: Criando uma Conta no OpenAI

1\. Acesse o site da *OpenAI*.

2\. Clique em "Sign Up" para criar uma nova conta ou "Log In" se você já tiver uma conta.

3\. Complete o processo de cadastro, verificando seu e-mail e fornecendo as informações necessárias.

### Passo 2: Acessando a Área de APIs

1\. Após fazer login, vá para o *Dashboard do OpenAI.*

2\. No menu lateral, clique em "API" para acessar a área de APIs.

### Passo 3: Criando uma API Key

1\. No Dashboard do OpenAI, clique em "API Keys".

2\. Clique no botão "Create API Key".

3\. Dê um nome para sua chave e clique em "Create".

4\. Sua nova API Key será gerada. Copie e salve esta chave em um local seguro, pois você não poderá visualizá-la novamente.

### Passo 4: Obtendo o Organization ID

1\. No Dashboard do OpenAI, clique em "Organization".

2\. O Organization ID estará listado na seção de informações da organização. Copie este ID, pois você precisará dele para autenticação em algumas chamadas de API.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras/como-criar-uma-api-key-chatgpt.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
