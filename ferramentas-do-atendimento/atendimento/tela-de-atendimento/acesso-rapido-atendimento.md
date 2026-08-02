# Acesso Rápido - Atendimento

A barra de **Ícones de Acesso Rápido**, localizada no canto superior direito de cada conversa aberta, centraliza as ferramentas de controle de fluxo e produtividade do atendimento. Através destes comandos, o atendente pode gerenciar a jornada do cliente, desde a transferência entre setores até a finalização do protocolo.

#### Como acessar a funcionalidade

Os ícones estão localizados no topo superior direito da janela de chat, após selecionar um ticket na aba de Atendimentos.

<figure><img src="/files/DNDSrmw7q1MCkalxOthV" alt=""><figcaption></figcaption></figure>

***

#### Detalhamento dos Ícones e Funcionalidades

Abaixo, explicamos a função de cada comando e como aplicá-los na rotina de atendimento:

**1. Retornar à Fila (Ícone Seta para Esquerda)**

* **O que faz:** Remove o atendente atual como responsável pelo ticket e o move de volta para a aba **Pendentes**.
* **Uso:** Utilize quando precisar que outro colega da mesma fila assuma o atendimento (ex: ao encerrar seu turno).

**2. Resolver (Ícone Check Verde)**

* **O que faz:** Encerra o atendimento atual, movendo-o para a aba **Fechados**.
* **Configuração:** Se houver uma Mensagem de Fechamento cadastrada ou se o sistema exigir um Motivo de Fechamento, um modal será exibido para preenchimento antes da conclusão.

<figure><img src="/files/ydim397oLkgw0sD5EHwD" alt="" width="189"><figcaption></figcaption></figure>

**Para habilitar o uso do** [**Motivo (Demanda)**](/configuracao-administrador/configuracoes-painel-admin/crm/demanda.md) **Configure no painel admin > Configurações Gerais > Forçar definição de demanda no fechamento de atendimento**

<figure><img src="/files/FDgrynjS6cNC910ol4WC" alt=""><figcaption></figcaption></figure>

**3. Transferir (Ícone de Setas Inversas)**

* **O que faz:** Direciona o contato para outra Fila ou para um Usuário específico.
* **Como usar:** Selecione o destino no menu suspenso e, opcionalmente, escreva uma mensagem interna que será lida apenas pelo próximo atendente para dar contexto ao caso.
*

```
<figure><img src="/files/rTFWNKrhHBTpjJ8DGV6r" alt="" width="375"><figcaption></figcaption></figure>
```

**4. Transferir Canal (Ícone de Antena/Sinal)**

* **O que faz:** Migra a conversa para outro Canal conectado ao sistema.
* **Uso:** Útil quando você deseja continuar o atendimento por um número de WhatsApp diferente do que o cliente iniciou o contato.
*

```
<figure><img src="/files/3NvtYq21l0nSvese0pxG" alt="" width="375"><figcaption></figcaption></figure>
```

**5. Mídias, Links e Documentos (Ícone de Galeria)**

* **O que faz:** Abre um painel centralizador com todos os arquivos trocados naquela conversa, divididos em abas.
* **Uso:** Facilita a localização de comprovantes, fotos de produtos ou manuais enviados anteriormente sem precisar rolar todo o histórico do chat.

<figure><img src="/files/HE5toBqxtI8FNPyqVcjy" alt="" width="375"><figcaption></figcaption></figure>

**6. Compartilhar Ticket (Ícone de Conexões/Nodos)**

* **O que faz:** Permite selecionar outros usuários da equipe para "espiar" a conversa sem que eles se tornem os responsáveis pelo ticket.
* **Uso:** Ideal para treinamentos ou pedidos de auxílio pontual à supervisão.
*

```
<figure><img src="/files/2Nudn72x6Sv4k44CBcFo" alt="" width="140"><figcaption></figcaption></figure>
```

**7. Buscar nas Mensagens (Ícone Lupa)**

* **O que faz:** Abre um campo de texto no topo do chat para filtrar palavras-chave dentro do histórico da conversa ativa.

**8. Convites Compartilhados (Ícone de Envelope)**

* **O que faz:** Exibe uma lista de tickets que outros colegas compartilharam com você. Funciona como uma caixa de entrada de colaboração.
*

```
<figure><img src="/files/q0i6QaCmuqcPxOGsYuRh" alt="" width="328"><figcaption></figcaption></figure>
```

**9. Opções Extras (Três Pontinhos)**

Este menu agrupa funções complementares que não possuem ícone direto na barra principal:

* **Ver detalhes do contato:** Atalho para abrir o painel lateral com dados do CRM.
* **Transferir p/ Chatbot:** Envia o cliente de volta para o fluxo de automação do ChatFlow.

<figure><img src="/files/62N2gUjTNbk6krnUcd66" alt="" width="373"><figcaption></figcaption></figure>

* **Agendar mensagem:** Abre o modal para programar o envio de um texto para data e hora futura.

<figure><img src="/files/xl1jNv2DXwhRhsurMXJ0" alt="" width="373"><figcaption></figcaption></figure>

* **Pausar atendimento:** Interrompe a contagem de tempo de resposta do ticket (se habilitado).

<figure><img src="/files/8l1uHpK17nDU5TXgeNz1" alt="" width="373"><figcaption></figcaption></figure>

* **Parar rolagem automática:** Trava a tela do chat para que novas mensagens recebidas não "empurrem" a visualização para baixo enquanto você lê o histórico.

<figure><img src="/files/7QtrBECRvMx3m0ZS5Qcp" alt="" width="169"><figcaption></figcaption></figure>

***

#### Avisos e precauções

{% hint style="warning" %}
**Atenção ao Resolver:** Uma vez resolvido, o ticket só pode ser reaberto se o cliente enviar uma nova mensagem ou se o atendente utilizar a função de "Reabrir" (se permitido pelo administrador).
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/atendimento/tela-de-atendimento/acesso-rapido-atendimento.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
