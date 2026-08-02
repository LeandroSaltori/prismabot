# Menu dos atendimentos

{% hint style="warning" %}
**Disponível para o perfil:** Administrador, supervisor e Usuário
{% endhint %}

A **Central de Atendimentos** é o núcleo operacional do sistema Prismabot. Nesta página, o agente gerencia todas as interações com os clientes, organiza fluxos de trabalho por meio de filtros avançados e executa ações em massa para otimizar a produtividade da equipe.

#### Como acessar a página

No menu lateral esquerdo, clique no Menu **Atendimento** e selecione a aba **Atendimentos**.

<figure><img src="/files/tbYgt90IGK73B4iU0jNE" alt="" width="276"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/USQDEFErMgqiu450fJ0V" alt=""><figcaption></figcaption></figure>

***

#### Detalhamento de Filtros e Ações

Para uma gestão precisa, o sistema oferece opções detalhadas de segmentação e automação de tarefas em lote:

**Painel de Filtros**

<figure><img src="/files/fsfWKDi8GXodEdwvSjzq" alt="" width="375"><figcaption></figcaption></figure>

Ao clicar no botão **Filtros**, um menu lateral é aberto com as seguintes opções de refinamento:

* **Opções de Visualização:** Marque "Mostrar todos" para ver tickets de outros atendentes (se tiver permissão), "Somente não lidos" para focar em mensagens pendentes, ou "Inverter ordem" para ver as mensagens mais antigas primeiro.
* **Status:** Refine sua busca entre tickets Abertos, Pendentes ou Fechados simultaneamente.
* **Período:** Defina uma data de início (**De**) e fim (**Até**) para localizar atendimentos em um intervalo específico.
* **Filas:** Selecione um ou mais departamentos (Ex: Suporte, Vendas) para filtrar apenas as demandas daquelas áreas.
* **Conexões:** Filtre os atendimentos pela origem da mensagem, selecionando o Canal específico (WhatsApp, Instagram, etc).
* **Usuário:** Filtre para ver os tickets atribuídos a um colaborador específico da Equipe.
* **Etiqueta:** Localize contatos segmentados por Etiquetas específicas (Ex: "Cliente VIP", "Aguardando Pagamento").
* **Kanban:** Filtre tickets que estão em etapas específicas do seu fluxo de Kanban.

<figure><img src="/files/jeWjZ5EipiSAj8bNIRvP" alt="" width="229"><figcaption></figcaption></figure>

<figure><img src="/files/rOxCD2GdegpvcaK91gfU" alt="" width="229"><figcaption></figcaption></figure>

**Menu de Ações**

O botão **Ações** agrupa ferramentas para execução de tarefas rápidas:

* **Selecionar múltiplos:** Habilita caixas de seleção ao lado de cada chat para que você possa fechar ou transferir vários tickets de uma só vez.
* **Iniciar conversa avulsa:** Permite enviar uma mensagem para um número que não possui um ticket aberto no momento.
* **Organizar por não respondido:** Reordena a lista priorizando os clientes que enviaram mensagem e ainda não receberam retorno.
* **Ajuda:** Atalho para a central de documentação e suporte.

<figure><img src="/files/77nnU5K2nFsuRUvNYnya" alt="" width="192"><figcaption></figcaption></figure>

***

### **Elementos de Controle e Busca**

* **Abas Privados e Grupos:** Alterna a visualização entre conversas individuais e chats em grupo.

<figure><img src="/files/IyVIkjwnebITNdveT45W" alt="" width="375"><figcaption></figcaption></figure>

* **Barra de Busca:** Localiza chats por nome do contato, número de telefone ou número do ticket (#).
* **Ícone Três Riscos (Modo Compacto):** Simplifica a lista, removendo o detalhamento da última mensagem e permitindo a seleção rápida de múltiplos chats para ações coletivas.
* **Ícone Atualizar:** Recarrega manualmente a lista de chats para sincronizar novas mensagens.
* **Ícone de Pausa (Pausar Atendimento):** Permite que o agente pare de receber novos tickets automaticamente.
  * Nota: Este ícone só aparece se habilitado nas [Configurações Gerais](https://www.google.com/url?sa=E\&q=link-para-configuracoes-gerais).

<figure><img src="/files/f0cvPnk1x65P27bkiWRe" alt="" width="375"><figcaption></figcaption></figure>

**Abas de Status**

* **Abertos:** Conversas que já estão sob responsabilidade de um atendente.
* **Pendentes:** Novos contatos ou transferências que aguardam um agente aceitar o ticket.
  * Na aba de Pendentes é possível clicar no ícone de olho: **espiar** conversa antes de mover chat para a aba "Abertos"
*

```
<figure><img src="/files/IdzF1PFoKLJgplEQHYkc" alt="" width="375"><figcaption></figcaption></figure>
```

* **Fechados:** Histórico de conversas encerradas&#x20;
  * O sistema por defaul não aparece os tickets na aba Fechados. Para visualizar é preciso habilitar na aba **Filtros**

***

A barra lateral esquerda é a ferramenta de controle da lista de chats. Abaixo, detalhamos cada componente:

#### Detalhamento do Card de Atendimento

<figure><img src="/files/HdUe63YEQ8xOwuFpl8zJ" alt="" width="375"><figcaption></figcaption></figure>

Cada card na lista de chats fornece um resumo imediato do ticket antes mesmo de abri-lo:

* **Avatar e Identificação:** Exibe a foto e o nome/número do contato.
* **Última Mensagem:** Visualização prévia do conteúdo (texto, imagem ou arquivo) da última interação.
* **Ticket ID (#):** Identificador único para rastreio do atendimento.
* **Tempo de Resposta:** Localizado no canto superior direito do card, indica há quanto tempo a última mensagem foi recebida.
* **Informações de Atendimento:** Exibe o nome do **Agente** responsável, a **Conexão** utilizada (ícone e nome do canal) e a **Fila** vinculada.
* **Indicadores Visuais:** Bolinhas coloridas indicam a origem do canal e ícones pequenos podem representar etiquetas ou prioridades atribuídas.

Passando o cursor no chat aparece os seguintes ícones

<figure><img src="/files/2e3nrpd2uai69oRQyRU1" alt="" width="375"><figcaption></figcaption></figure>

* **Fixar conversa:** Mantém o chat permanentemente no topo da lista para acesso prioritário.
* **Marcar como não lido:** Adiciona um alerta visual de pendência no ticket para retorno posterior.
* **Resolver atendimento:** Encerra o ticket e move a conversa automaticamente para a aba **Fechados**.

***

#### Avisos e precauções

{% hint style="warning" %}
**Modo Leitura:** Tickets na aba **Pendentes** não permitem resposta imediata. Você deve clicar no botão **Aceitar** dentro do chat para assumir o ticket e habilitar o campo de escrita.
{% endhint %}

{% hint style="info" %}
As configurações de filtro permanecem salvas durante a sua sessão atual, a menos que você clique em **"Limpar"** no topo do painel de filtros.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/atendimento/tela-de-atendimento/menu-dos-atendimentos.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
