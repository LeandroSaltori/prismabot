# Automação Instagram

{% hint style="warning" %}
**Disponível para o perfil: Administrador**
{% endhint %}

{% hint style="danger" %}
**Importante — requer App Próprio com permissões do Instagram aprovadas.**

As automações de Instagram dependem de permissões da Graph API da Meta (como a `instagram_manage_comments`) que precisam estar **aprovadas no seu próprio aplicativo (App Próprio)**.

* Se você conecta o Instagram por um **App Próprio com essas permissões aprovadas pela Meta**, as automações funcionam normalmente.
* Se você utiliza o **App compartilhado da Prisma Telecom**, as automações **ainda não funcionam**: a permissão de gestão de comentários do Instagram **ainda não foi aprovada pela Meta** para o nosso app compartilhado. A liberação dessas funcionalidades para os licenciados depende dessa aprovação, que aguardamos junto à Meta.
  {% endhint %}

O módulo de **Automação Instagram** permite configurar respostas automáticas para eventos do Instagram: comentários em posts e reels, interações em lives, menções e respostas a stories, e posts compartilhados via DM. Cada automação define um gatilho, condições opcionais de filtragem e ações que o sistema executa automaticamente quando o evento ocorre.

***

#### Como acessar

Acesse **Automação → Automação Instagram**.

<figure><img src="/files/IrSAuR97qT5Xl4cEwPIR" alt=""><figcaption></figcaption></figure>

***

#### Você verá a seguinte tela

<figure><img src="/files/cpPHrESntZjYJaGSTvey" alt=""><figcaption></figcaption></figure>

A tela exibe as automações criadas para o canal selecionado. Use o seletor **Canal** para alternar entre diferentes contas do Instagram conectadas.

A tela tem três abas:

| Aba                 | Para que serve                                       |
| ------------------- | ---------------------------------------------------- |
| **Automações**      | Lista e gerencia as automações ativas                |
| **Posts agendados** | Exibe publicações agendadas para o canal selecionado |
| **Histórico**       | Registro de execuções anteriores das automações      |

***

#### Validar permissões

Antes de criar automações, verifique se a conta tem acesso aos recursos necessários. Clique em **Validar permissões** ao lado do seletor de canal.

O sistema testa cada recurso individualmente e exibe o resultado:

| Recurso                                  | O que é validado                                              |
| ---------------------------------------- | ------------------------------------------------------------- |
| **Token de acesso válido**               | Autenticação da conta com a Meta                              |
| **Leitura de publicações (posts/reels)** | Acesso às publicações do perfil                               |
| **Leitura de comentários**               | Permissão para ler comentários nos posts                      |
| **Mensagens (DM)**                       | Permissão para enviar e receber DMs                           |
| **Webhook: comentários**                 | Recebimento de eventos de comentários em posts                |
| **Webhook: comentários em live**         | Recebimento de eventos de comentários em transmissões ao vivo |
| **Webhook: mensagens**                   | Recebimento de eventos de DMs                                 |

{% hint style="warning" %}
Se qualquer item aparecer com erro, reconecte o canal do Instagram em **Canais** e tente novamente. Erros de token indicam que a sessão expirou e o canal precisa ser reautorizado.
{% endhint %}

<div><figure><img src="/files/pNxTTPz5Sjwe5G7FIYmm" alt=""><figcaption></figcaption></figure> <figure><img src="/files/0le3i5SiR9LWt7MA5MTb" alt=""><figcaption></figcaption></figure></div>

***

#### Criando uma automação

Clique em **+ Nova automação**. O assistente de criação tem 4 etapas.

<figure><img src="/files/9utvwDuQBBYgOSWOtXB0" alt=""><figcaption></figcaption></figure>

***

**Etapa 1 — Gatilho**

Define quando a automação será acionada.

| Campo               | Descrição                                                                                                                        |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Nome**            | Identificação interna da automação — ex: "Responder 'eu quero' no post X"                                                        |
| **Tipo de gatilho** | Evento que aciona a automação (ver tabela abaixo)                                                                                |
| **Prioridade**      | Número inteiro. Quando mais de uma automação casar com o mesmo evento, a de maior prioridade é executada — apenas uma por evento |

**Tipos de gatilho disponíveis:**

| Tipo           | Quando dispara                                                  |
| -------------- | --------------------------------------------------------------- |
| **Comentário** | Quando alguém comenta em um post ou reel                        |
| **Live**       | Quando alguém comenta durante uma transmissão ao vivo           |
| **Story**      | Quando alguém menciona ou responde a um story                   |
| **Post em DM** | Quando alguém compartilha um post do perfil via mensagem direta |

***

**Etapa 2 — Publicações**

Define em quais publicações a automação será monitorada. Você pode aplicar a automação a todos os posts ou restringi-la a publicações específicas.

<figure><img src="/files/5bOJjNEyaVr9yPnMd9LX" alt=""><figcaption></figcaption></figure>

***

**Etapa 3 — Condições**

Define filtros opcionais para acionar a automação somente quando a mensagem ou comentário atender a determinados critérios.

| Campo                     | Descrição                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Palavras-chave**        | A automação só dispara se o texto contiver uma das palavras listadas                             |
| **Palavras de exclusão**  | A automação **não** dispara se o texto contiver uma dessas palavras                              |
| **Intervalo por contato** | Tempo mínimo entre disparos para o mesmo contato — evita respostas repetidas para a mesma pessoa |

{% hint style="info" %}
Combine palavras-chave com palavras de exclusão para ter controle preciso sobre quando a automação deve ou não responder.
{% endhint %}

<figure><img src="/files/0cZqrXxcHCwxxMyEZdLm" alt=""><figcaption></figcaption></figure>

***

**Etapa 4 — Ações**

Define o que o sistema faz quando a automação é acionada. Você pode combinar mais de uma ação.

| Ação                 | O que faz                                                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Resposta pública** | Publica uma resposta visível no comentário ou post. Suporta um pool de variações — o sistema alterna entre elas para evitar textos repetidos |
| **DM**               | Envia uma mensagem direta (DM) para o contato que acionou o gatilho                                                                          |
| **ChatFlow**         | Inicia um fluxo de chatbot para o contato via DM, seguindo as etapas configuradas no Chat Flow                                               |

<figure><img src="/files/lX7JtXpPsCIN3S09iFkX" alt=""><figcaption></figcaption></figure>

***

#### Boas práticas

* **Use um pool de respostas públicas** — cadastre várias versões da resposta pública para que o sistema alterne entre elas. Isso evita que o Instagram interprete os comentários repetidos como spam.
* **Combine palavras-chave com exclusões** — se a automação responde a quem digita "preço", exclua palavras como "sem preço" ou "não tem preço" para evitar disparos indevidos.
* **Valide as permissões antes de publicar** — use o botão **Validar permissões** para confirmar que o canal tem acesso a todos os recursos necessários antes de ativar a automação.
* **Use a prioridade para resolver conflitos** — se dois gatilhos podem casar com o mesmo evento, atribua prioridades diferentes e verifique qual ação faz mais sentido para o contexto.

***

#### Limitações

{% hint style="warning" %}
**Comentários em live** só permitem resposta pública. Não é possível enviar DM a partir de um gatilho de live.
{% endhint %}

{% hint style="warning" %}
**DM e ações de ChatFlow** respeitam a janela de 24 horas do Instagram. Fora da janela de conversação ativa, o envio de mensagens diretas pode ser bloqueado pela plataforma.
{% endhint %}

***


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/automacao/automacao-instagram.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
