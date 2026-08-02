# Avançado - Recursos técnicos

- [Banco de dados - Como acessar](https://prismatelecomservicos.com/avancado-recursos-tecnicos/banco-de-dados-como-acessar.md)
- [Como diagnosticar o erro "servidor temporariamente off-line"](https://prismatelecomservicos.com/avancado-recursos-tecnicos/como-diagnosticar-o-erro-servidor-temporariamente-off-line.md)
- [Erro de Autenticação no app Whatsapp Oauth](https://prismatelecomservicos.com/avancado-recursos-tecnicos/erro-de-autenticacao-no-app-whatsapp-oauth.md): Checklist para investigar o erro "PERMISSION CONNECTIONS LIMITED" na hora de se conectar ao tech provider
- [Como liberar espaço em disco na VPS do Prismabot](https://prismatelecomservicos.com/avancado-recursos-tecnicos/como-liberar-espaco-em-disco-na-vps-do-z-pro.md)
- [Customização do Frontend](https://prismatelecomservicos.com/avancado-recursos-tecnicos/customizacao-do-frontend.md)
- [Integrando o chat GPT](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integrando-o-chat-gpt.md): Este tutorial irá guiá-lo pelo processo de integração do ChatGPT em sua plataforma Prismabot, permitindo que você automatize conversas e utilize o poder da inteligência artificial da OpenAI em seus canais
- [Integração Google Calendar](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracao-google-calendar.md)
- [Infraestrutura](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura.md): Boas práticas de Infraestrutura
- [Guia para Instalação com Docker (Autoinstalador e Stacks)](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura/guia-para-instalacao-com-docker.md): Este guia explica como instalar o Prismabot com Docker usando o autoinstalador (Windows e Ubuntu) ou stacks prontas via Portainer
- [Instalação com Docker manual](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura/guia-para-instalacao-com-docker/instalacao-com-docker-manual.md): Este guia explica como instalar e configurar o Prismabot usando Docker Compose
- [Configuração do Traefik com Nginx](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura/configuracao-do-traefik-com-nginx.md): Prepara o ambiente para usar Traefik sem dar conflito com o Nginx
- [Como extrair Logs do Sistema](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura/como-extrair-logs-do-sistema.md)
- [Infra - Recriação do Redis](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura/infra-recriacao-do-redis.md): Redis é a aplicação utilizada pelo Prismabot para armazenar memória rápida (de curto prazo) e gerenciar a execução dos processos do sistema
- [Otimização de Nginx para Alta demanda de mensagem](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura/otimizacao-de-nginx-para-alta-demanda-de-mensagem.md)
- [Proxy IPv4 no Proxy-Seller](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura/proxy-ipv4-no-proxy-seller.md): Como comprar um proxy IPv4 no Proxy-Seller e obter URL, porta, usuário e senha
- [Migração Prismabot entre servidores](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura/migracao-z-pro-entre-servidores.md)
- [Como trocar a senha do Portainer no Prismabot](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura/como-trocar-a-senha-do-portainer-no-z-pro.md): O Portainer é o painel usado para gerenciar os containers Docker da sua instalação do Prismabot (API, frontend, banco de dados, Redis, etc.)
- [Como instalar o Prismabot em Modo Cluster](https://prismatelecomservicos.com/avancado-recursos-tecnicos/infraestrutura/como-instalar-o-z-pro-em-modo-cluster.md)
- [Integrações terceiras](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras.md)
- [N8N - Tutorial de integração](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras/n8n-tutorial-de-integracao.md)
- [API do Google Speech-to-Text](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras/api-do-google-speech-to-text.md): Como usar a API do Google Speech-to-Text e baixar o JSON de autenticação
- [API do site Comtele (SMS)](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras/api-do-site-comtele-sms.md): Como comprar créditos e obter a API do site Comtele (SMS)
- [Como criar uma API Key ChatGPT](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras/como-criar-uma-api-key-chatgpt.md): Como criar uma API Key e obter o Organization ID do ChatGPT
- [Projeto no Dialogflow](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras/projeto-no-dialogflow.md): Como criar um projeto no Dialogflow, obter o ID do projeto, definir a linguagem e baixar o JSON de autenticação
- [Typebot autohospedado](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras/typebot-autohospedado.md): Como criar um bot no Typebot autohospedado e obter a URL de compartilhamento e o nome do bot
- [Erros e Avisos Comuns](https://prismatelecomservicos.com/avancado-recursos-tecnicos/erros-e-avisos-comuns.md)
- [Template (WABA) não chega ao destinatário](https://prismatelecomservicos.com/avancado-recursos-tecnicos/erros-e-avisos-comuns/template-waba-nao-chega-ao-destinatario.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/avancado-recursos-tecnicos.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
