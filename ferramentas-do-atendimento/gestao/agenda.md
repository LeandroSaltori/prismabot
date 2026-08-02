# Agenda

Agenda

{% hint style="warning" %}
**Disponível para o perfil:** Administrador e Usuário
{% endhint %}

A página **Agenda** é a ferramenta central de organização de compromissos e automação de notificações do sistema Prismabot. Através dela, é possível realizar o agendamento de consultas, visualizar o cronograma em formato de calendário e configurar réguas de lembretes automáticos via WhatsApp para reduzir o absenteísmo.

#### Principais funções

* **Gestão de Consultas:** Registro detalhado de compromissos com clientes.
* **Visualização em Calendário:** Painel mensal para controle visual de datas.
* **Lembretes Automáticos:** Configuração de disparos de mensagens com antecedência programada.
* **Integração com Contatos:** Vinculação direta com a base de dados do sistema.

#### Caso de uso

Uma clínica de estética utiliza a Agenda para marcar procedimentos. Ao criar uma "Nova Consulta" para uma cliente na próxima terça-feira, o sistema identifica a regra de lembrete configurada para "24 horas antes" e envia automaticamente uma mensagem pelo Canal WhatsApp selecionado, confirmando o horário e diminuindo as faltas não justificadas.

#### Como acessar a página

No menu lateral, clique no Menu **Gestão** e selecione a aba **Agenda**.

<figure><img src="/files/2wGBeI7aoFP4CjJwLf2N" alt="" width="278"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

A página é dividida em três sub-abas principais: **Consultas**, **Calendário** e **Lembretes**.

<figure><img src="/files/LbyT3JIP2bud81oovvjg" alt=""><figcaption></figcaption></figure>

**Explicação dos campos e ícones (Aba Consultas)**

* **Botão + Nova Consulta:** Abre o formulário para criar um novo agendamento.
* **Título:** Nome identificador do compromisso.
* **Contato:** Nome do cliente vinculado à consulta.
* **Data/Hora:** Momento exato do início do compromisso.
* **Status:** Indica a situação atual (ex: Pendente, Confirmado, Cancelado).
* **Ações (Ícones):**
  * **Lápis:** Editar os dados da consulta.
  * **Lixeira:** Excluir o agendamento permanentemente.

***

#### Detalhamento das Funcionalidades

**1. Criar uma Nova Consulta**

Ao clicar em **+ Nova Consulta**, o sistema exibe um formulário detalhado:

* **Título (Obrigatório):** Assunto da consulta.
* **Descrição:** Detalhamento adicional sobre o compromisso.
* **Contato:** Campo de busca para selecionar um Contato já cadastrado.
* **Nome/Telefone do contato:** Caso o contato não exista na base, estes campos permitem o preenchimento manual para o envio do lembrete.
* **Data e Hora início/fim:** Definição do período de duração.
* **Status:** Classificação da consulta.
* **Observações internas:** Notas que não são enviadas ao cliente, visíveis apenas para a equipe.

<figure><img src="/files/V9L4g8EI2ebBlZpmx5x0" alt="" width="375"><figcaption></figcaption></figure>

**2. Visualização por Calendário**

A aba **Calendário** oferece uma visão macro de todos os agendamentos do mês. É possível navegar entre os meses e clicar sobre um evento específico para ver seus detalhes.

<figure><img src="/files/i9P8DeAF43ulI3WJvhs8" alt=""><figcaption></figcaption></figure>

**3. Configuração de Lembretes Automáticos**

Na aba **Lembretes**, o administrador define as regras de automação que serão aplicadas a todas as consultas.

<figure><img src="/files/nUp8lHTShSPUtZVEG515" alt=""><figcaption></figcaption></figure>

* **Nome:** Identificação da regra (ex: Lembrete 24h antes).
* **Horas antes do evento:** Define com quanto tempo de antecedência o sistema deve realizar o disparo.
* **Tipo de mensagem:** Escolha entre "Mensagem de texto" (comum) ou "Template WABA" (para API Oficial).
* **Mensagem:** Campo para escrita do texto. Você pode usar variáveis dinâmicas como:
  * `{{nome}}`: Nome do cliente.
  * `{{data}}`: Data da consulta.
  * `{{hora}}`: Horário da consulta.
  * `{{titulo}}`: Assunto da consulta.
* **Canal WhatsApp:** Seleciona por qual Conexão a mensagem será enviada.

<figure><img src="/files/pl1514nHvbapLNQyUJ4B" alt="" width="375"><figcaption></figcaption></figure>

***

#### Funcionamento da Automação

O motor de automação do Prismabot realiza uma verificação a cada **15 minutos** para identificar consultas que se enquadram nas regras de lembretes configuradas.

* **Segurança:** O sistema garante que cada lembrete específico (ex: regra de 24h) seja enviado apenas **uma única vez** por consulta, evitando duplicidade de mensagens para o cliente.
* **Status Ativo:** As regras de lembrete só funcionam se a chave "Ativo" estiver habilitada no cadastro da regra.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/gestao/agenda.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
