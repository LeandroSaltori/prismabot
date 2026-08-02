# Agendamentos

{% hint style="warning" %}
**Disponível para o perfil: Administrador e Supervisor**
{% endhint %}

A página de **Agendamentos** é uma ferramenta de automação que permite programar o envio de mensagens para datas e horários futuros. Com ela, o gestor ou atendente pode garantir que comunicações importantes, cobranças ou lembretes sejam entregues ao destinatário no momento oportuno, sem a necessidade de intervenção manual no horário do disparo.

#### Principais funções

* **Programação de Mensagens:** Definição exata de dia e hora para o envio.
* **Gestão de Recorrência:** Configuração de disparos repetitivos em intervalos pré-definidos.
* **Monitoramento de Status:** Acompanhamento em tempo real se a mensagem foi enviada ou se houve falha.

#### Caso de uso

Um escritório de contabilidade precisa enviar um lembrete de vencimento de impostos para um cliente todo dia 10 de cada mês. O administrador utiliza a página de **Agendamentos**, seleciona o Contato, define a **Recorrência** para mensal e escreve a mensagem. O sistema cuidará do disparo automático, garantindo a pontualidade da entrega.

#### Como acessar a página

No menu lateral, clique no Menu **Automação** e selecione a aba **Agendamentos**.

<figure><img src="/files/kTLKZflQu1xE2ANHCJBr" alt="" width="254"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/HhdcetQO2vhU3Hj2xsdE" alt=""><figcaption></figcaption></figure>

**Colunas da Tabela:**

* **# (ID):** Código identificador único do agendamento (UUID).
* **Contato:** Nome do cliente ou número que receberá a mensagem.
* **Mensagem:** Prévia do texto que será enviado.
* **Agendado para:** Data e hora programada para o disparo.
* **Criado em:** Registro de quando o agendamento foi configurado.
* **Status:** Indica a situação da mensagem (**Pendente**, **Enviado**, **Falhou** ou **Cancelado**).
* **Ações:** Ícones para editar agendamentos pendentes ou excluir registros.

***

#### Passo a passo de uso

**Criar um novo agendamento**

1. Clique no botão **+ Novo Agendamento**.
2. **Conexão:** Selecione por qual Canal a mensagem deve sair.
3. **Contato:** Pesquise pelo nome ou número do contato na sua base de dados.
4. **Quando:** Escolha um período pré-definido ou selecione **Personalizado** para habilitar os campos de **Data** e **Hora**.
5. **Recorrência:** Defina se a mensagem deve ser enviada apenas uma vez (**Sem repetição**) ou se deve se repetir em intervalos específicos (ex: a cada 5, 10 ou 15 dias).
6. **Mensagem:** Digite o texto desejado. Você pode utilizar emojis e habilitar a **Assinatura** do atendente se desejar.
7. Clique em **Agendar**.

<figure><img src="/files/wMJrpY3NYAxqD3L8squp" alt="" width="375"><figcaption></figcaption></figure>

***

#### Detalhamento

* **Status de Falha:** Se um agendamento aparecer com o status "Falhou", verifique se o Canal selecionado estava conectado no momento do disparo ou se o número do contato é válido.
* **Mensagens Recorrentes:** Uma mensagem configurada com recorrência gerará um novo registro na lista automaticamente após o envio do ciclo atual, respeitando o intervalo definido.

#### Avisos e precauções

{% hint style="warning" %}
**Atenção:** Para interromper uma sequência de mensagens recorrentes, você deve localizar o agendamento na lista e realizar a exclusão manual.
{% endhint %}

{% hint style="info" %}
Certifique-se de que a **Conexão** escolhida esteja ativa e com bateria/internet estável no celular (em casos de APIs não oficiais) para garantir a entrega.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/automacao/agendamentos.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
