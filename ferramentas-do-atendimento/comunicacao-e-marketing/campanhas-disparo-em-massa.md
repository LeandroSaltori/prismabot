# Campanhas (Disparo em Massa)

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

O módulo de **Campanhas** permite planejar e executar envios de mensagens em massa para listas de contatos segmentados. Use-o para comunicados, promoções ou alertas — com agendamento prévio, controle de ritmo de envio e geração de texto por Inteligência Artificial.

***

#### Como acessar

Acesse **Comunicação e Marketing → Campanhas**.

<figure><img src="/files/tIjVDRxtKsEFYa7mJsqU" alt="" width="247"><figcaption></figcaption></figure>

***

#### Você verá a seguinte tela

<figure><img src="/files/42fMMWWHq2zN9jnGT8xj" alt=""><figcaption></figcaption></figure>

A tela principal lista todas as campanhas criadas com as colunas:

* **ID / Nome** — identificador único e título da campanha
* **Sessão** — canal de WhatsApp usado no envio
* **Início** — data e hora programada para os disparos
* **Status** — situação atual: **Pendente**, **Em andamento**, **Concluída** ou **Cancelada**
* **Progresso** — barra visual com percentual de mensagens enviadas sobre o total de contatos

***

#### Criando uma campanha

1. Clique em **+ Nova Campanha**.
2. Preencha os campos do formulário:

| Campo                                            | Descrição                                                                                                                                                 |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nome**                                         | Identificação interna da campanha                                                                                                                         |
| **Sessão/WhatsApp**                              | Canal de saída para o disparo                                                                                                                             |
| **Data/hora de início**                          | Quando os disparos devem começar                                                                                                                          |
| **Delay entre mensagens (seg)**                  | Intervalo entre cada envio em segundos (padrão: 20). Valores abaixo de 15 s aumentam o risco de bloqueio do número                                        |
| **Janela de envio**                              | Restringe os disparos a um horário específico. Se a campanha não terminar no período, ela é pausada e retomada automaticamente no dia seguinte            |
| **Exibir mensagem original ao receber resposta** | Quando ativado: se o contato responder à campanha dentro da janela, a mensagem enviada pela campanha aparece no ticket acima da resposta do cliente       |
| **Limite diário de mensagens**                   | Quando desativado: sem limite diário — a campanha envia até terminar. Quando ativado: define um teto de mensagens por dia para evitar bloqueios do número |

3. Adicione os contatos destinatários usando os filtros disponíveis:
   * **Por nome ou telefone** — busca individual
   * **Por etiqueta** — seleciona todos os contatos com determinada tag
   * **Por estado (UF)** — filtra pelo DDD do número

<figure><img src="/files/nWmTKtvaC7v2wP5uW3fx" alt=""><figcaption></figcaption></figure>

***

#### Configurando as mensagens

Você pode cadastrar até **3 versões de mensagem** (Msg 1, Msg 2, Msg 3). O sistema alterna entre elas nos envios, reduzindo a repetição de conteúdo idêntico.

**Gerando texto com IA**

1. Clique no botão **IA** ao lado do campo de texto (disponível em cada uma das 3 mensagens)
2. Descreva o que quer comunicar — informe o público, o tom desejado, o objetivo e o CTA
3. O texto gerado é aplicado automaticamente ao campo; edite conforme necessário

**Personalizando o conteúdo**

* Clique em **Variáveis** para inserir `{{nome}}` e outros campos dinâmicos do contato
* Anexe uma imagem, vídeo ou PDF no campo **Mídia** (opcional) — o arquivo acompanha todas as mensagens da campanha

**Visualizando o resultado**

O painel de **Preview** à direita do formulário exibe como cada mensagem ficará no celular do destinatário. Alterne entre as abas **Msg 1**, **Msg 2** e **Msg 3** para revisar antes de criar a campanha.

***

#### Gerenciando campanhas existentes

Ao clicar nos três pontinhos na coluna **Ações** de qualquer campanha, você tem as opções:

* **Ver contatos** — lista todos os destinatários e o status individual de cada envio (entregue, pendente ou falha)
* **Duplicar** — cria uma cópia exata da campanha (filtros e mensagens) para facilitar novos disparos semelhantes
* **PDF** — gera um relatório com o resumo e as estatísticas da campanha
* **CSV** — exporta a lista de contatos e resultados para análise em planilha
* **Excluir** — remove a campanha do sistema

Campanhas com status **Pendente** (ainda não iniciadas) podem ser editadas diretamente para ajustar contatos, mensagens ou agendamento antes do disparo.

***

#### Avisos e precauções

{% hint style="danger" %}
**Risco de banimento:** intervalos abaixo de 15 segundos ou conteúdo denunciado pelos destinatários resultam no banimento do número. Use delays adequados e mensagens relevantes para o público.
{% endhint %}

{% hint style="warning" %}
**Canal conectado:** certifique-se de que o canal selecionado esteja **Conectado** no momento do início da campanha. Se estiver offline, as mensagens serão movidas para o status de falha.
{% endhint %}

{% hint style="warning" %}
**Campanhas vs. Disparo em Massa:** Campanhas usam um intervalo **fixo** entre envios e permitem até 3 variações de mensagem. Se precisar de intervalo **aleatório** (ex: entre 10 e 30 segundos), use a funcionalidade **Disparo em Massa**.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/comunicacao-e-marketing/campanhas-disparo-em-massa.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
