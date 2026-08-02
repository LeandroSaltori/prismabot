# Typebot autohospedado

### Passo 1: Acessando o Painel do Typebot

1\. Acesse o painel do Typebot autohospedado no seu navegador. A URL será algo como <http://seu-servidor> ou o endereço que você configurou.

2.Faça login com suas credenciais administrativas.

### Passo 2: Criando um Novo Bot

1.Após fazer login, você será direcionado ao painel de controle.

2.Clique no botão "New Bot" ou similar (geralmente um botão com o símbolo de "+").

3.No campo "Bot Name", insira o nome do seu bot.

4.Clique em "Create" para criar o bot.

### Passo 3: Configurando o Bot

1.Você será levado para o editor de bots. Aqui, você pode configurar o fluxo de conversa do seu bot.

2.Adicione e configure os blocos de diálogo conforme necessário, utilizando a interface de arrastar e soltar.

3.Certifique-se de salvar suas configurações periodicamente clicando no botão "Save".

### Passo 4: Publicando o Bot

1\. Após configurar o bot, clique no botão "Publish" para publicar o bot.

2\. A URL de compartilhamento do bot será gerada após a publicação. Esta URLserá algo como <http://seu-servidor> /bot/nome-do-bot.

3.Copie essa URL para usá-la em suas plataformas de comunicação.

### Passo 5: Obtendo o Nome do Bot

1.O nome do bot é o mesmo que você definiu durante a criação do bot.

2.Você pode visualizar e alterar o nome do bot na página de configurações do bot, geralmente acessível através do painel de controle ou das opções de configuração dentro do editor de bots.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras/typebot-autohospedado.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
