# Perfis de Acesso

{% hint style="warning" %}
**Disponível para o perfil:** Administrador
{% endhint %}

A página de **Perfis de Acesso** permite a criação de templates de permissões reutilizáveis e granulares. Em vez de configurar cada usuário individualmente, o administrador define um perfil padrão (ex: "Suporte Nível 1") e o atribui a vários colaboradores.

#### Caso de uso

Uma empresa deseja criar um perfil específico para estagiários que apenas respondem chats, mas não podem excluir contatos ou exportar relatórios. O administrador cria o perfil "Estagiário", desmarca as opções de "Excluir" e "Exportar", e vincula todos os novos estagiários a este template. Se futuramente a empresa decidir que estagiários podem acessar o Kanban, basta editar o perfil uma única vez.

#### Como acessar a página

Caminho clicando no Menu  **Administração**, aba **Usuários** e no botão superior direito **Gerenciar Perfis**.

<figure><img src="/files/rXNWFj6wQLhKEuRb8NFa" alt=""><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/TONKQt4ljyQfegjerUN9" alt="" width="563"><figcaption></figcaption></figure>

**Explicação dos campos e ícones**

* **Botão + Novo Perfil:** Abre o formulário para criação de um novo template de acesso.
* **Nome do Perfil:** Identificação do template (ex: Atendente Noturno).
* **Contador de Usuários:** Exibe quantos colaboradores estão vinculados àquele perfil no momento.
* **Ícone Editar (Lápis):** Permite alterar as permissões e o nome do perfil.
* **Ícone Excluir (Lixeira):** Remove o perfil do sistema

***

#### Passo a passo de uso

**1. Criar um Perfil com IA (Copiloto)**

1. Clique em **+ Novo Perfil**.
2. No campo **Sugerir com IA**, descreva o que o usuário fará. *Exemplo: "Atendente que responde tickets e vê contatos, mas não pode deletar nada nem exportar".*
3. Clique em **Sugerir**. O Copiloto marcará automaticamente os campos correspondentes.
4. Revise as marcações manuais antes de salvar.

<figure><img src="/files/5RLB2o9cyTDK5Qf920OK" alt="" width="375"><figcaption></figcaption></figure>

**2. Configuração Manual**

1. Insira o **Nome do perfil** e uma **Descrição** opcional.
2. Navegue pelas seções de **Módulos Visíveis** para definir o que aparecerá no menu lateral do usuário.
3. Navegue pela seção **Permissões** para definir as ações permitidas (ex: resolver ticket, deletar mensagem).
4. Clique em **Salvar**.

**3. Atribuir o Perfil ao Usuário**

1. Volte para a página de Usuários.
2. Edite o usuário desejado, mude o campo **Perfil** para **Personalizado**.
3. No novo campo que surgirá (**Perfil de acesso**), selecione o template criado.

***

#### Detalhamento das Permissões

Abaixo estão os agrupamentos de permissões disponíveis para configuração:

**Módulos Visíveis (Sidebar)**

* **Principal:** Ter acesso aos menus atendimento, chat-privado, contatos, mensagens-rápidas, painel-atendimento, tarefas e wavoip.
* **Organização:** Ter acesso aos menus agenda, campanhas, funil, galeria, grupo e kanban.
* **Configuração:** Ter acesso aos menus agendamentos, aniversários, auto-resposta, avaliações, chat-flow, etiquetas, fechamento, filas, horário-Atendimento, notas e protocolos.
* **Relatórios:** Ter acesso aos menus audit-log, dashboard, log- ligação e relatórios.
* **Integrações e Canais:** Ter acesso aos menus api-service, sessões e woocommerce-produtos.
* **Redes Sociais:** Ter acesso aos menus de gestão de comentários do facebook, instagram, tiktok e youtube, além de menções no instagram.
* **Administração:** Ter acesso aos menus de equipes e usuários.

<figure><img src="/files/0gW8rthf0V6tOz8TphZn" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="/files/zZ6lwsdritzqtOYkzj6t" alt="" width="375"><figcaption></figcaption></figure>

**Permissões de Ação**

* **Atendimentos:** Permissões para atribuir tickets (assign), usar o copiloto de IA (copilot), criar (create), deletar (delete), reabrir (reopen), resolver (resolve), visualizar todos (view\_all) e visualizar via chatbot (view\_chatbot).
* **Contatos:** Permissões para criar (create), deletar (delete), editar (edit), exportar base (export) e visualizar todos os detalhes (view\_full).
* **Mensagens:** Permissões para deletar mensagens enviadas (delete), encaminhar mensagens (forward) e gerenciar respostas rápidas públicas (quickreplies\_manage\_public).
* **Tarefas:** Permissões para criar (create), deletar (delete), editar (edit) e visualizar todas (view\_all).
* **Kanban e Funil:** Permissões para visualizar o painel de atendimentos geral (attendance\_panel\_view\_all), gerenciar o funil (funnel\_manage) e gerenciar o kanban (kanban\_manage).
* **Relatórios:** Permissões para exportar dados (export) e visualizar relatórios (view).
* **Configurações:** Permissão para acessar as configurações gerais do sistema (settings\_general).
* **Módulos Diversos:** Permissões para gerenciar horários (business\_hours), campanhas (campaigns), chatflow (chat\_flow), motivos de fechamento (closure\_reasons), galeria (gallery), grupos (groups), envios em massa (mass\_send), notas (notes), notificações (notifications), acesso ao chat privado (private\_chat), protocolos (protocols), filas (queues), avaliações (ratings), mensagens agendadas (scheduled\_messages) e etiquetas (tags).
* **Administração Avançada:** Permissões para gerenciar serviços de API (api\_service\_access), visualizar logs de auditoria (audit\_log\_view), gerenciar sessões/canais (sessions\_manage) e gerenciar ou visualizar usuários (users\_manage / users\_view).
* **VoIP:** Permissões para uso do serviço WaVoIP (voip\_wavoip) e acesso ao webphone (voip\_webphone).

<figure><img src="/files/e0CkYN8UH2MP73kVbYZf" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="/files/PbkmjAII6LtIEdm5rHNW" alt="" width="375"><figcaption></figcaption></figure>

***

#### Avisos e precauções

{% hint style="warning" %}
**Regra de Exclusão:** Um perfil que esteja sendo utilizado por pelo menos um usuário ativo não poderá ser excluído. Para deletá-lo, você deve primeiro reatribuir esses usuários a outro perfil.
{% endhint %}

{% hint style="danger" %}
**Segurança:** Ao usar a sugestão por IA, sempre revise manualmente se as permissões críticas (como `tickets_delete` ou `audit_log_view`) foram marcadas corretamente para evitar exposição de dados sensíveis.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/administracao-painel-admin/usuarios/perfis-de-acesso.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
