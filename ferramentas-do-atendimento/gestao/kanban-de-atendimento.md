# Kanban de atendimento

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

O Kanban é uma ferramenta de gestão visual que transforma a tradicional lista de conversas em um painel dinâmico. Ele permite organizar seus atendimentos e tickets em estágios (colunas) ou agrupá-los por etiquetas, facilitando o acompanhamento visual do progresso de cada cliente.

#### Principais funções

* Visualização panorâmica de todos os contatos ativos separados por etapas ou etiquetas.
* Movimentação rápida de clientes entre as fases do funil através do recurso de arrastar e soltar.
* Acesso a ações rápidas diretamente no cartão do cliente (espiar conversa, começar atendimento ou finalizar).

#### Caso de uso

* **CRM e Vendas:** Acompanhar o fluxo de clientes no funil de vendas (ex: *Lead, Em Negociação, Aguardando Pagamento, Fechado*).
* **Suporte Técnico:** Organizar chamados por nível de triagem ou resolução (ex: *Triagem, Suporte Nível 1, Aguardando Peça, Resolvido*).
* **Gestão de Prioridades:** Visualizar rapidamente quais contatos precisam de atenção imediata e evitar que atendimentos fiquem esquecidos.

{% hint style="info" %}
**Aviso: Qual Kanban Utilizar?**

O Prismabot possui duas visualizações de Kanban distintas, cada uma com um propósito diferente:

* **Kanban de Atendimentos (Esta Página):** Utiliza **Etiquetas (Tags)** para organizar visualmente os *atendimentos em andamento*. É ideal para a gestão operacional da equipe de suporte.
* [**Kanban de Oportunidades:**](broken://pages/sMg3QwP8Cr2KhJWfcihM) Utiliza as **Etapas do Funil** para organizar as *oportunidades de negócio*. É a ferramenta para a gestão de processos comerciais. Consulte a documentação aqui.
  {% endhint %}

#### Como acessar a página

No menu lateral esquerdo do painel de atendimento, clique na opção **Kanban**.

<figure><img src="/files/jVUEPxSJX13EBUfiLzbg" alt="" width="227"><figcaption></figcaption></figure>

#### Você verá a seguinte tela

<figure><img src="/files/BqkoG6k7HLKE8nuAOKGY" alt=""><figcaption></figcaption></figure>

***

#### Detalhamento das Funcionalidades/abas

A tela do Kanban é dividida em duas abas principais de visualização e possui ações específicas para os cartões de atendimento:

**1. Aba "Quadro" (Lanes)**

Organiza os atendimentos com base nas **Lanes** (etapas de funil/colunas) que você configurou no sistema. É a visualização clássica de fluxo de trabalho.

* ⚙️ **Criando e configurando colunas:** As colunas do seu Kanban não são criadas na própria tela do Kanban. Para adicionar, renomear, alterar cores ou modificar a ordem das etapas, acesse a documentação: [Gerenciar Kanban.](/configuracao-administrador/configuracoes-painel-admin/crm/gerenciar-kanban.md)

**2. Aba "Tags"**

Organiza os atendimentos agrupando-os em colunas de acordo com as **Etiquetas (Tags)** atribuídas a cada contato.

* 🏷️ **Gerenciando etiquetas:** Para aprender a criar e administrar essas etiquetas, acesse a documentação: Página de Etiquetas.

**3. Interagindo com os Cards (Cartões)**

Cada cliente no Kanban é representado por um "Card" (cartão). Você pode realizar as seguintes operações:

* **Movimentar pelo Funil (Arrastar e Soltar):** Clique, segure e arraste o card do cliente para a coluna desejada.
  * ⚠️ **Atenção:** Depois de arrastar e soltar os cards (alterar os cards de coluna), você **precisa apertar no botão "Salvar alterações"** na tela para gravar a movimentação no sistema.
* **Ações Rápidas do Card:** No canto direito de cada cartão, você encontra três ícones de atalho:
  * **Olho (Espiar):** Permite visualizar a última mensagem ou o histórico sem assumir o ticket ou marcá-lo como lido para o cliente.
  * **Balão (Começar Atendimento):** Atribui o ticket a você e abre imediatamente a tela de chat para iniciar a conversa com o contato.
  * **X (Finalizar):** Encerra o ticket de atendimento daquele contato, removendo-o do quadro Kanban atual.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/gestao/kanban-de-atendimento.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
