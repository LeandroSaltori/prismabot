# Envio em Massa - Wavoip

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

Use esta aba para realizar chamadas de voz em massa via WhatsApp, enviando um arquivo de áudio para uma lista de números através de conexões não oficiais (Baileys).

<figure><img src="/files/MjwZXumurSW4qa4m1Jvw" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Esta página detalha o funcionamento desta aba específica. Para uma visão geral da funcionalidade, tutoriais em vídeo e orientações de uso, [acesse Envio em Massa.](/ferramentas-do-atendimento/comunicacao-e-marketing/envio-em-massa.md)
{% endhint %}

### Configurando o disparo

1. Em **Sessões Disponíveis**, selecione a conexão Baileys que realizará as chamadas — certifique-se de que o status está **Conectado**
2. Em **Números de Telefone**, adicione os números destinatários um por um clicando em **+**
3. Em **Arquivo de Áudio**, clique em **Selecionar arquivo de áudio** e faça o upload do arquivo que será enviado nas chamadas

### Realizando o envio

Após configurar a sessão, os números e o áudio, clique no botão de envio para iniciar as chamadas.

{% hint style="warning" %}
O WaVoIP utiliza conexões não oficiais. A estabilidade do envio depende da conexão Baileys ativa. Mantenha a sessão conectada durante todo o processo.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/comunicacao-e-marketing/envio-em-massa/envio-em-massa-wavoip.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
