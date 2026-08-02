# Funil de vendas

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

O Funil de Vendas é a ferramenta de gestão de pipeline do Prismabot. Ele permite acompanhar oportunidades de negócio em todas as etapas do processo comercial — desde o primeiro contato até o fechamento — com automações, visões analíticas e controle de follow-up integrados ao atendimento.

Pode ser utilizado para diferentes processos: funil de vendas, onboarding de clientes, esteiras de suporte ou qualquer fluxo com etapas definidas.

### Como acessar

Acesse **Gestão → Funil de Vendas**.

<figure><img src="/files/12rjEiWwmBZitnssShSa" alt="" width="225"><figcaption></figcaption></figure>

### Você verá a seguinte tela

<figure><img src="/files/5V81zmuwMMSR7WTC2QHD" alt=""><figcaption></figcaption></figure>

### Abas disponíveis

<table><thead><tr><th width="144.5">Aba</th><th>Para que serve</th></tr></thead><tbody><tr><td><a href="/pages/w4p3XTl0LBmGSLiLRDHp">Dashboard</a></td><td>Visão analítica com KPIs, taxas de conversão, ticket médio e distribuição por etapa</td></tr><tr><td><a href="/pages/rvI4XNiZsIEFamhYWhlS">Kanban</a></td><td>Quadro visual para mover oportunidades entre etapas e gerenciar o dia a dia do funil</td></tr><tr><td><a href="/pages/iYI55yehi4IXNvZj4TKn">Pipelines</a></td><td>Configuração da estrutura do funil — crie e gerencie pipelines com etapas personalizadas</td></tr><tr><td><a href="/pages/k3sRZnWdl978GAbKHGyq">Calendário</a></td><td>Visão temporal das oportunidades por previsão de fechamento</td></tr><tr><td><a href="/pages/05w2TBdTvWPHTlYZAgzU">Ações</a></td><td>Automações que disparam quando uma oportunidade entra em uma etapa específica</td></tr><tr><td><a href="/pages/cApsFGJUuSpLZecSlzFp">Ações Ticket</a></td><td>Automações de follow-up baseadas em inatividade do ticket</td></tr></tbody></table>

### Tutorial em vídeo

{% embed url="<https://youtu.be/tWOr-6LNdBg>" %}

***

### Caso de uso: venda de seguro

A seguir, um exemplo completo de como usar cada aba do Funil de Vendas em uma operação de venda de seguros.

***

#### 1. Pipelines — Criando a estrutura do processo

Antes de usar o funil, é necessário configurar o pipeline com as etapas do processo comercial.

**Na aba Pipelines:**

Crie um pipeline chamado **"Vendas de Seguro"** com as seguintes etapas:

1. Recebido
2. Qualificação
3. Proposta Enviada
4. Aguardando Retorno
5. Fechado — Ganho
6. Fechado — Perdido

Cada etapa recebe uma cor para identificação visual no Kanban. Após salvar, o pipeline estará disponível para receber oportunidades.

***

#### 2. Kanban — Gerenciando as oportunidades no dia a dia

Com o pipeline configurado, os atendentes trabalham diretamente no Kanban.

**Na aba Kanban:**

Quando um lead entra em contato interessado em contratar um seguro de vida, o atendente clica em **+ Nova Oportunidade** e preenche:

* **Nome:** Seguro de Vida — João Silva
* **Pipeline:** Vendas de Seguro
* **Etapa:** Recebido
* **Contato:** João Silva (já cadastrado no sistema)
* **Valor:** R$ 1.200,00
* **Previsão de Fechamento:** 15/07/2026
* **Responsável:** Atendente Ana

O card aparece na coluna **Recebido**. Conforme o processo avança, Ana arrasta o card para **Qualificação**, depois para **Proposta Enviada** — e assim por diante até o fechamento.

O painel de **Alertas** no topo avisa quando uma oportunidade fica inativa por vários dias, garantindo que nenhum lead seja esquecido.

***

#### 3. Ações do Pipeline — Automatizando mensagens por etapa

Com o funil rodando, é possível automatizar ações para cada movimento no pipeline.

**Na aba Ações:**

Configure as seguintes automações:

* **Ao entrar em "Proposta Enviada"** — enviar automaticamente uma mensagem: *"Olá, {{name}}! Sua proposta de seguro está pronta. Enviamos os detalhes por aqui. Qualquer dúvida, estou à disposição!"*
* **3 dias em "Aguardando Retorno"** — mudar o status da oportunidade para **Perdido** automaticamente se não houver movimentação

Essas ações eliminam tarefas manuais repetitivas e garantem que o cliente sempre receba uma comunicação no momento certo.

***

#### 4. Ações de Ticket — Follow-up automático por inatividade

Para os casos em que o cliente para de responder durante a negociação, as Ações de Ticket entram em ação.

**Na aba Ações Ticket:**

Configure:

* **Após 24h sem resposta** — enviar mensagem automática: *"Oi, {{name}}! Tudo bem? Queria saber se conseguiu verificar a proposta de seguro que enviamos. Estou aqui para tirar qualquer dúvida!"*
* **Após 72h sem resposta** — adicionar a etiqueta **"Lead Frio"** para rastreamento e sinalizar para o gestor revisar o caso

Isso garante que leads não respondam e sejam esquecidos na fila — o sistema age automaticamente enquanto o atendente foca em novas oportunidades.

***

#### 5. Calendário — Acompanhando prazos de fechamento

Com várias oportunidades abertas, o Calendário ajuda a visualizar quais negociações têm previsão de fechamento na semana.

**Na aba Calendário:**

Ana acessa o Calendário e vê que três seguros têm previsão de fechamento nos próximos 5 dias. Ela clica em cada um para revisar os detalhes e decide priorizar o contato com esses clientes antes do prazo.

***

#### 6. Dashboard — Avaliando o desempenho do funil

Ao final do mês, o gestor acessa o Dashboard para analisar os resultados da operação.

**Na aba Dashboard:**

O gestor visualiza:

* **12 oportunidades criadas** no mês
* **7 ganhas** — taxa de conversão de 58%
* **Ticket médio:** R$ 980,00
* **Etapa com mais travamento:** Aguardando Retorno — sinal para revisar a abordagem de follow-up

Com esses dados, o gestor ajusta os intervalos das Ações de Ticket e revisa o script de proposta para o próximo ciclo.

***

{% hint style="info" %}
**Sugestão de jornada de configuração:**

1. Pipelines — crie a estrutura do seu processo
2. Kanban — cadastre as oportunidades e gerencie o dia a dia
3. Ações — automatize mensagens e movimentações por etapa
4. Ações Ticket — configure o follow-up por inatividade
5. Calendário — acompanhe prazos de fechamento
6. Dashboard — analise os resultados e ajuste o processo
   {% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/gestao/funil-de-vendas.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
