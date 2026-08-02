# Aniversários

{% hint style="warning" %}
**Disponível para o perfil: Administrador e Supervisor**
{% endhint %}

## Aniversários

{% hint style="info" %}
**Disponível para o perfil:** Administrador e Supervisor
{% endhint %}

A página de **Aniversários** é uma ferramenta de relacionamento voltada para a fidelização de clientes. Nela, o sistema centraliza todos os contatos que possuem data de nascimento cadastrada, permitindo o acompanhamento cronológico dos aniversariantes e o envio de mensagens comemorativas manuais ou automatizadas.

#### Como acessar a página

No menu lateral, clique no Menu **Automação** e selecione a aba **Aniversários**.

<figure><img src="/files/m0PpPnpQ7ioAgRmDlQ4N" alt="" width="254"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/YKYb8cyg76vsOKjDQXlA" alt="" width="375"><figcaption></figcaption></figure>

**Explicação dos campos e ícones**

* **Barra de Busca:** Localiza um contato específico pelo nome ou parte dele.
* **Contador de Contatos:** Exibe o total de pessoas na base que possuem data de nascimento preenchida.
* **Colunas da Tabela:**
  * **Nome:** Identificação do contato.
  * **Número:** Telefone vinculado ao cadastro.
  * **Data de Nascimento:** Dia, mês e ano registrados no Contato.
  * **Idade:** Cálculo automático da idade atual.
  * **Dias Restantes:** Cronômetro regressivo para a próxima celebração.
* **Ações (Ícone de Balão):** Abre o modal para envio de uma mensagem rápida de felicitação.

***

**Enviar Mensagem Manual**

1. Identifique o aniversariante na lista e clique no ícone de **Balão (Responder)** na coluna Ações.
2. No modal que será aberto, selecione a **Conexão** (canal de saída) desejada.
3. Certifique-se de que a mensagem padrão (ou a que você digitar) está correta.
4. Clique em **Enviar**.

<figure><img src="/files/q3p9eok9hNtQbS7p4WyY" alt="" width="375"><figcaption></figcaption></figure>

***

#### Avisos e precauções

{% hint style="warning" %}
**Cadastro de Dados:** A página de Aniversários só exibirá contatos que tenham o campo "Data de Nascimento" preenchido corretamente no módulo de Contatos.
{% endhint %}

{% hint style="info" %}
O envio de mensagens através desta tela segue as mesmas regras de segurança das Campanhas, dependendo da estabilidade da conexão selecionada.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/automacao/aniversarios.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
