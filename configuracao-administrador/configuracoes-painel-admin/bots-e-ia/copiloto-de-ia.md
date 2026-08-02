# Copiloto de IA

{% hint style="warning" %}
**Disponível para o perfil: Administrador**
{% endhint %}

O Copiloto de IA é um assistente inteligente integrado à tela de atendimento do Prismabot. Ele utiliza modelos de linguagem avançados (como ChatGPT, Gemini ou Claude) para auxiliar o atendente em tempo real, analisando o sentimento das conversas, sugerindo respostas contextuais, reescrevendo textos e resumindo históricos longos.

#### Principais funções

* Sugestão de Resposta: Gera sugestões baseadas no contexto da conversa atual.
* Análise de Sentimento: Identifica o tom do cliente (neutro, engajado, impaciente).
* Reescrita de Mensagem: Ajusta o tom da resposta (ex: tornar mais simpático ou formal).
* Resumo de Conversa: Cria uma síntese de diálogos extensos para facilitar a leitura rápida.

#### Caso de Uso

Um atendente recebe um ticket com um histórico de 50 mensagens. Para não perder tempo lendo tudo, ele utiliza a função Resumir. Após entender o problema, ele pede uma Sugestão de Resposta ao Copiloto e usa a Reescrita para deixar a mensagem com um tom mais acolhedor antes de enviar ao cliente.

{% embed url="<https://www.loom.com/share/318e4ee827e240019874f51942fbe618>" %}

***

#### Como acessar a página

1. No menu lateral, clique em Configurações;

<figure><img src="/files/xUlz68NqyllEPO34iesE" alt="" width="375"><figcaption></figcaption></figure>

2. Selecione a aba Bots IA;
3. Clique na sub-aba Copiloto de IA.

#### Você verá a seguinte tela:

<figure><img src="/files/bdKEsTjakCJkBaR7HLKb" alt=""><figcaption></figcaption></figure>

***

#### Explicação dos campos e ícones

* Habilitar Copiloto: Chave para ativar ou desativar a função na tela de atendimento.
* Provedor: Seleção da plataforma de IA (OpenAI, Anthropic, Google Gemini, Groq).
* API Key: Campo para colar a chave secreta gerada no provedor escolhido.
* Modelo: Identificação técnica da versão da IA (ex: `gpt-4o`, `gemini-1.5-pro`).
* Prompt de Contexto: Espaço para descrever como a IA deve se comportar e quais informações sobre a empresa ela deve conhecer.

***

#### Passo a passo de uso

**Passo 1: Obter a API Key**

Antes de configurar no Prismabot, você deve gerar uma chave no site do provedor:

* OpenAI (ChatGPT): Acesse `platform.openai.com`, vá em *API Keys* e crie uma nova.
* Google (Gemini): Acesse o *Google AI Studio*, clique em *Get API Key*.
* Outros: Acesse os portais de desenvolvedor da Anthropic ou Groq.

**Passo 2: Configurar o Provedor no Prismabot**

1. Cole a API Key no campo correspondente.
2. Insira o Modelo exato conforme as diretrizes do provedor.

{% hint style="info" %}
Modelos Recomendados: Para OpenAI use `gpt-4o` ou `gpt-3.5-turbo`. Para Gemini, use `gemini-1.5-flash` ou similar conforme a documentação oficial do provedor.
{% endhint %}

**Passo 3: Contextualizar o Copiloto**

No campo Prompt, defina o papel da IA.

* *Exemplo:* "Você é um assistente de suporte da empresa X. Seja direto, educado e use informações do nosso catálogo de produtos para sugerir respostas."

**Passo 4: Utilizar no Atendimento**

Com tudo salvo, vá até a tela de atendimento:

1. Abra um chat e clique no ícone de três pontinhos (Mais Opções).
2. Selecione Copiloto.

<figure><img src="/files/199FMSCvrcFhtbyvz6eb" alt=""><figcaption></figcaption></figure>

3. Use os botões Analisar Sentimento ou Sugerir Resposta.

***

#### Detalhamento das Funções Adicionais

* Reescrita com IA: Abaixo do campo de digitação, ao clicar no ícone de IA, você pode pedir para "Tornar mais simpático", "Mais formal" ou "Corrigir gramática".
* Resumo de Diálogo: Localizado no menu de opções do chat, permite escolher entre resumir as mensagens do cliente, do atendente ou de ambos.

<figure><img src="/files/wkEcVwICumRZNvGtomev" alt=""><figcaption></figcaption></figure>

***

#### Avisos e precauções

{% hint style="warning" %}
Consumo de Créditos: O uso da API gera custos diretamente no provedor escolhido (OpenAI, Google, etc.). Monitore seu consumo nas plataformas originais.

Privacidade: Evite enviar dados sensíveis de clientes para a IA se a política de privacidade da sua empresa não permitir o processamento de dados em nuvens de terceiros.

Revisão Humana: O Copiloto sugere respostas, mas o atendente deve sempre revisar o texto antes de enviar para garantir a precisão das informações
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/configuracoes-painel-admin/bots-e-ia/copiloto-de-ia.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
