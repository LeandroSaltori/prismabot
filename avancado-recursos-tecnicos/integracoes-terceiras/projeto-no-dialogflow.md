# Projeto no Dialogflow

### Passo 1: Criação do Projeto no Google Cloud

1\. Acesse o *Google Cloud Console.*

2\. Faça login com sua conta do Google.

3\. Clique no ícone de seleção de projeto no topo da página e depois clique em "Novo Projeto".

4\. Dê um nome ao seu projeto e clique em "Criar".

### Passo 2: Ativando a API Dialogflow

1\. No Google Cloud Console, certifique-se de que você está no projeto criado.

2\. No menu lateral, vá para "API e Serviços" > "Biblioteca".

3\. Pesquise por "Dialogflow API" e clique nela.

4\. Clique no botão "Ativar".

### Passo 3: Criando um Agente no Dialogflow

1\. Acesse o Dialogflow Console.

2\. Clique em "Criar Agente".

3\. Preencha os detalhes do agente:

o Nome do Agente

o Projeto do Google Cloud (selecione o projeto criado anteriormente)

o Idioma Padrão (por exemplo, "Português (Brasil)")

o Fuso Horário

4\. Clique em "Criar".

### Passo 4: Obtendo o ID do Projeto

1\. No Google Cloud Console, vá para o menu "IAM e Administração" > "Configurações".

2\. O ID do Projeto estará listado na seção "Informações do Projeto". Copie este ID.

### Passo 5: Criando Credenciais de API

1\. No Google Cloud Console, vá para "API e Serviços" > "Credenciais".

2\. Clique em "Criar Credenciais" e selecione "Chave de conta de serviço".

3.Na janela que aparece, selecione "Nova conta de serviço".

4.Dê um nome à sua conta de serviço e, opcionalmente, atribua um papel, como "Administrador de Projeto".

5.Clique em "Criar" e depois em "Concluir".

6.Um arquivo JSON será baixado automaticamente para o seu computador. Esse é o seu arquivo de autenticação.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras/projeto-no-dialogflow.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
