# Tarefas

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

Crie e gerencie tarefas com prioridades, prazos, responsáveis e recorrência. As tarefas podem ser visualizadas em lista ou em um quadro Kanban, facilitando o acompanhamento do progresso pela equipe.

### Como acessar

Acesse **Gestão → Tarefas**.

<figure><img src="/files/fDLcsEWqKfOZUQ88lQxQ" alt="" width="225"><figcaption></figcaption></figure>

### Você verá a seguinte tela

<figure><img src="/files/CV1wsU3M1cROCZSSATrD" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/JJp002yQ1FkNR3O6Inks" alt=""><figcaption></figcaption></figure>

### Visualizações disponíveis

Use os botões no topo da página para alternar entre as duas formas de visualizar as tarefas:

* **Lista** — exibe todas as tarefas em formato de tabela, com colunas de Tarefa, Prioridade, Prazo, Status e Responsável
* **Kanban** — exibe as tarefas em colunas por status (Pendente, Atrasada e Concluída), permitindo arrastar os cards entre as colunas

### Criando uma tarefa

1. Clique em **+ Nova Tarefa**
2. Preencha os campos do formulário:

| Campo           | Descrição                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------- |
| **Nome**        | Título da tarefa — obrigatório                                                                |
| **Descrição**   | Detalhamento do que precisa ser feito — opcional                                              |
| **Comentários** | Campo para registrar observações ou atualizações — opcional                                   |
| **Prioridade**  | Nível de urgência da tarefa (Baixa, Média ou Alta) — obrigatório                              |
| **Status**      | Situação atual: Pendente, Atrasada ou Concluída — obrigatório                                 |
| **Prazo**       | Data limite para conclusão — obrigatório                                                      |
| **Recorrência** | Define se a tarefa se repete automaticamente (Sem recorrência, Diária, Semanal, Mensal, etc.) |
| **Responsável** | Usuário designado para executar a tarefa — obrigatório                                        |

3. Clique em **Salvar** — a tarefa aparecerá na lista com status **Pendente**

<figure><img src="/files/gzPA1gvn8SBRmp0ibXZY" alt="" width="335"><figcaption></figcaption></figure>

### Gerenciando tarefas

* Clique no ícone de **lápis** para editar qualquer campo de uma tarefa
* Clique no ícone de **lixeira** para excluir uma tarefa
* Na visualização **Kanban**, arraste os cards entre as colunas para atualizar o status visualmente
* Use a **barra de busca** para localizar rapidamente uma tarefa pelo nome

### Status das tarefas

| Status        | Descrição                                           |
| ------------- | --------------------------------------------------- |
| **Pendente**  | Tarefa criada, aguardando início                    |
| **Atrasada**  | Prazo vencido sem conclusão — destacada em vermelho |
| **Concluída** | Tarefa finalizada                                   |

{% hint style="info" %}
Use a recorrência para tarefas que se repetem com frequência — como relatórios semanais ou revisões mensais — e evite recriar manualmente a cada ciclo.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/gestao/tarefas.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
