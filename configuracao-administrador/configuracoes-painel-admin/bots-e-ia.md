# Bots e IA

{% hint style="warning" %}
**Disponível para o perfil:** Administrador
{% endhint %}

No painel de **Configurações Gerais > Bots e IA**, você pode centralizar e gerenciar todas as ferramentas de automação e modelos de linguagem que irão operar no seu sistema.

A plataforma possui integração nativa com os seguintes serviços:

* **Construtores de Fluxo e Automação:** Typebot, N8N, Dify e DialogFlow.
* **Modelos de Inteligência Artificial (LLMs):** ChatGPT, Grok, Gemini, Qwen, Claude, Deepseek, Ollama e LM Studio.

#### Como acessar a página

Clique no Menu **Configurações** e selecione a aba **Bots IA**.

<figure><img src="/files/cyRUguCeVg0LPt2Y1XEY" alt="" width="375"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/woYr2RLYCxuWlLuiKY0V" alt=""><figcaption></figcaption></figure>

***

#### 1. Idioma Padrão da IA

Nesta seção, define-se a linguagem que a inteligência artificial utilizará para interpretar e descrever mídias recebidas nos atendimentos.

* **Idioma das respostas:** Define o idioma que a IA usará ao descrever imagens e extrair textos de mídias via ChatGPT (GPT-4o) ou Gemini.
* **Como configurar:** Selecione o idioma principal do seu público (ex: Português). Se nenhum for selecionado, o sistema adotará o Português como padrão.

***

#### 2. [Copiloto de IA](/configuracao-administrador/configuracoes-painel-admin/bots-e-ia/copiloto-de-ia.md)

O Copiloto é um assistente virtual que monitora as conversas em tempo real para apoiar o trabalho do agente humano.

* **Configuração Técnica:** Escolha o provedor (OpenAI, Groq, Claude ou Gemini), insira a **API Key** correspondente e defina o modelo (ex: `gpt-4o-mini` ou `llama-3.3-70b`).
* **Prompt de Sistema:** Personalize o comportamento do assistente definindo o tom de voz e as regras de negócio da sua empresa.

**Novas funcionalidades de IA incluídas no Copiloto:**

* **Tradução Inline:** Traduz mensagens recebidas e enviadas em até 8 idiomas diretamente no chat.
* **Sugestões Rápidas:** Sugere respostas baseadas no contexto atual da conversa no painel lateral.
* **Resumo de Contato:** Gera um resumo do perfil e das dores do cliente na aba Perfil do Ticket.
* **Geração de Campanhas:** Auxilia na criação de textos para Disparo em Massa.
* **Detecção de Urgência:** Identifica sentimentos de frustração e adiciona badges de prioridade nos tickets.

{% hint style="info" %}
Para um detalhamento completo de cada campo do assistente, acesse a página: [Documentação Detalhada do Copiloto de IA](https://prismatelecomservicos.com/configuracao-administrador/configuracoes-painel-admin/bots-e-ia/copiloto-de-ia).
{% endhint %}

***

#### 3. Integração com Provedores (ChatGPT, Gemini, etc.)

Para cada provedor de IA listado no menu lateral (Typebot, ChatGPT, Grok, Gemini, Qwen, Claude, DeepSeek, N8N, Dify, Ollama, LM Studio e Dialogflow), o sistema apresenta duas chaves de ativação essenciais:

* **Habilitar \[Nome da IA]:** Ativa tecnicamente a integração com aquele provedor no sistema. Sem isso, a IA não aparecerá como opção nos canais.
* **Habilitar para todos os tickets:** Quando ativado, a IA passará a processar e responder automaticamente todos os novos atendimentos do sistema, sem necessidade de ativação manual ticket a ticket.

{% hint style="info" %}
💡 **Nota Importante:** Ativar a integração nesta tela é o primeiro passo. Para que as ferramentas de IA funcionem corretamente, lembre-se de que é necessário acessar o menu **Canais** e inserir as respectivas credenciais (como API Keys e Tokens) dentro das configurações de cada número ou conexão que utilizará a inteligência.
{% endhint %}

**Exemplo de Ativação (Caso ChatGPT):**

1. Clique em **ChatGPT** no menu lateral de Bots IA.
2. Ative a chave **Habilitar ChatGPT**.
3. Configure a **API Key** da OpenAI.
4. Se desejar automação total, ative **Habilitar para todos os tickets**.

<figure><img src="/files/gITUxN9xoM5WO9LjXXI9" alt=""><figcaption></figcaption></figure>

***

#### Avisos e precauções

{% hint style="warning" %}
**A ativação dos provedores de IA é por conta do assinante. É preciso criar uma conta e configurar por fora e depois habilitar dentro do Prismabot**
{% endhint %}

{% hint style="info" %}
As alterações realizadas nesta página são salvas automaticamente pelo sistema assim que os campos são preenchidos ou os botões de seleção são alterados.
{% endhint %}

***


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/configuracoes-painel-admin/bots-e-ia.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
