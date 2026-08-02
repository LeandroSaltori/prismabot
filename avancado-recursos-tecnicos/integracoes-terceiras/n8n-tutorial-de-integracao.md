# N8N - Tutorial de integração

O N8N é uma ferramenta de automação de fluxos de trabalho (workflows). Ao integrá-lo ao Prismabot, você pode centralizar processos e conectar a plataforma a múltiplos sistemas externos, como CRMs, planilhas, agendas e agentes de Inteligência Artificial.

Abaixo está o passo a passo da integração nativa, que é a forma mais simples e recomendada de conectar as duas ferramentas.

***

## Passo 1: Habilitar o N8N no Prismabot

O primeiro passo é ativar o módulo do N8N dentro do painel administrativo.

1. Acesse o **Painel Admin**.
2. Vá em **Configurações Gerais** > aba **Bots e IA**.
3. Localize a seção do N8N e ative a opção **Ativar integração com N8N**.

{% hint style="info" %}
&#x20;O campo para inserir a URL no seu canal (descrito no Passo 3) **só aparecerá** se esta chave de integração estiver ativada nas Configurações Gerais.
{% endhint %}

<figure><img src="/files/D7JTMG7Zpek1ShaEZhRC" alt="" width="280"><figcaption></figcaption></figure>

<figure><img src="/files/J9O6XRJgjdw0hv3Nnzwu" alt=""><figcaption></figcaption></figure>

***

## Passo 2: Criar o fluxo e obter a URL no N8N

Para que o Prismabot consiga enviar os dados para o N8N, você precisa criar um fluxo para receber o Webhook.

### Acessando o n8n

1\. Acesse o n8n no navegador em <http://localhost:5678> ou no endereço configurado na sua instalação.

2\. Faça login com o usuário e senha configurados (se aplicável).

### Criando um Workflow no n8n

1\. No painel do n8n, clique em "New" para criar um novo workflow.

2\. No painel de nós (nodes), procure por "Webhook" e arraste o nó "Webhook" para o espaço de trabalho.

### Configurando o Nó Webhook

1\. Selecione o nó "Webhook" que você adicionou ao espaço de trabalho.

2\. Configure as seguintes opções: o Method: POST o Path: /meu-webhook

3\. O nó "Webhook" deve aparecer semelhante a este: o Method: POST o Path: /meu-webhook

### Adicionando um Nó de Resposta

1\. No painel de nós (nodes), procure por "Set" e arraste o nó "Set" para o espaço de trabalho.

2\. Conecte a saída do nó "Webhook" à entrada do nó "Set".

3\. Configure o nó "Set" para definir uma resposta simples:

* Clique em "Add Field".
* Selecione "String".
* &#x20;No campo "Name", digite message.
* No campo "Value", digite Webhook received!.

<figure><img src="/files/qzSYpu4ZrBzcDDnIl54T" alt=""><figcaption></figcaption></figure>

### Salvando e Executando o Workflow

1\. Clique em "Save" para salvar o workflow.

2\. Com o nó "Webhook" selecionado, clique em "Execute Node" para iniciar a escuta do webhook.

3.Você verá a URL do webhook gerada, algo como <http://localhost:5678/webhook-test/meu-webhook>.

4\. Copie essa URL.

***

## Passo 3: Adicionar a URL no Canal do Prismabot

Com a URL do N8N copiada e a opção ativada no admin, você fará a integração diretamente no canal.

1. No Prismabot, vá em **Canais** e edite a conexão desejada.

<figure><img src="/files/rQ5hHuf68Ol7xqNdoMSB" alt="" width="280"><figcaption></figcaption></figure>

2. Role a janela de configurações até localizar a área **Configurações do N8N**.
3. No campo **URL do N8N**, cole o endereço do Webhook que você gerou no passo anterior.
4. Clique em Salvar.

<figure><img src="/files/QKpEo6NdWytnnCr7FlAs" alt="" width="375"><figcaption></figcaption></figure>

***

## Como acionar o N8N durante a operação?

O Prismabot permite que o N8N atue nos seus atendimentos de diferentes formas:

* **Ativação Global:** Você pode marcar a opção *"Ativar integração com N8N para todos os atendimentos por Padrão"* nas Configurações Gerais. Assim, o N8N escutará e interagirará com todos os novos tickets.

<figure><img src="/files/a66xhHdZ9XZ9EwLIeh2z" alt=""><figcaption></figcaption></figure>

* **Pelo Chatbot (Flowbuilder):** É possível direcionar o contato para o N8N em uma etapa específica da sua automação interna, adicionando a interação **"Nó N8N"** ou **"Adicionar Webhook"** no construtor de fluxo. *(Lembre-se: integrações externas devem ser a última ação do bloco)*

<figure><img src="/files/AYOpBgWhBm60ItOAvEkr" alt="" width="375"><figcaption></figcaption></figure>

* **Manualmente no Atendimento:** Na tela de chat, o atendente pode ativar ou desativar a chave do N8N individualmente para aquele contato usando o menu lateral direito em "Detalhes do contato" aba "Integr."

<figure><img src="/files/F9LZekjFe69UCILhwXMW" alt="" width="375"><figcaption></figcaption></figure>

* **Desligamento Automático:** Para evitar que o fluxo automatizado atrapalhe o operador, você pode habilitar a opção *"Habilitar desligamento automático das integrações externas"*. Com isso, o N8N é desligado no momento em que um atendente humano assume a conversa. Configuração realizada dentro do canal:

<figure><img src="/files/FiHMRjrX2ecO6quqe5zJ" alt="" width="375"><figcaption></figcaption></figure>

***

{% hint style="warning" %}
&#x20;**Escopo do Suporte Técnico**

A Prismabot fornece os pontos de conexão para a integração com o N8N

**Não faz parte do nosso escopo de suporte:**

* A criação, lógica, depuração (debug) ou otimização de fluxos dentro do N8N.
* A configuração, manutenção e estabilidade do servidor ou conta onde o N8N do cliente está hospedado.
  {% endhint %}

#### Exemplo de fluxo n8n para agendamento

{% embed url="<https://www.youtube.com/watch?t=407s&v=0I-52eP61ng>" %}

#### Exemplo de fluxo no N8N + API Prismabot + WABA

{% embed url="<https://www.youtube.com/watch?v=jfF7h_7q8tY>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracoes-terceiras/n8n-tutorial-de-integracao.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
