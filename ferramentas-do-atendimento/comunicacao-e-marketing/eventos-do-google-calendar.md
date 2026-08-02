# Eventos do Google Calendar

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

{% hint style="info" %}
Para usar esta página é necessário ter ao menos uma conta Google conectada ao sistema. Veja como configurar em [Integração Google Calendar](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracao-google-calendar).
{% endhint %}

Esta página permite visualizar e gerenciar os eventos dos calendários Google conectados ao Prismabot. Os eventos são sincronizados em tempo real — compromissos criados aqui aparecem no Google Calendar e vice-versa.

### Como acessar

Acesse **Comunicação e Marketing → Eventos do Google Calendar**.

<figure><img src="/files/mlkOdh1s8TT5SpXZd8Q3" alt="" width="227"><figcaption></figcaption></figure>

### Você verá a seguinte tela

<figure><img src="/files/cwG8UFnaZitlkTVzGJuB" alt=""><figcaption></figcaption></figure>

### Consultando eventos

1. Selecione o **Calendário** que deseja consultar — o menu lista todas as configurações com status **Ativo** e tokens **Completo**
2. Defina a **Data início** e a **Data fim** do período
3. Informe o número máximo de resultados em **Máx. resultados**
4. Clique em **Buscar**

Os eventos serão listados com título, data de início, data de fim e status.

### Criando um novo evento

1. Clique em **+ Novo evento**
2. Preencha o título, data, horário e demais informações do compromisso
3. Salve — o evento será criado no Prismabot e sincronizado automaticamente com o Google Calendar da conta conectada

<figure><img src="/files/tx9YUWZLzKuIUotg9Gr6" alt="" width="375"><figcaption></figcaption></figure>

### Gerenciando eventos existentes

Cada evento na listagem possui as seguintes ações:

| Ícone        | Ação                                          |
| ------------ | --------------------------------------------- |
| Lápis        | Editar o evento                               |
| Lixeira      | Excluir o evento                              |
| Seta externa | Abrir o evento diretamente no Google Calendar |

### Dicas de uso

* Use filtros de data para buscar eventos em períodos específicos e controle o volume de resultados pelo campo **Máx. resultados**
* Você pode conectar múltiplas contas Google em **Configurações → Integrações → Google Calendar** e alternar entre elas pelo seletor de calendário

{% hint style="warning" %}
Apenas configurações com status **Ativo** e tokens **Completo** aparecem no seletor de calendário. Se sua conta não aparecer na lista, verifique o status da integração em [Configurações → Integrações → Google Calendar](https://prismatelecomservicos.com/avancado-recursos-tecnicos/integracao-google-calendar).
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/comunicacao-e-marketing/eventos-do-google-calendar.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
