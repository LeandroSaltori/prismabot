# Barra de ferramenta geral

{% hint style="warning" %}
**Disponível para o perfil:** Todos os perfis
{% endhint %}

A **Barra de Ferramentas Superior** é um componente global e permanente do sistema Prismabot. Localizada no canto superior direito de todas as telas, ela reúne utilitários essenciais para a operação, permitindo que o usuário gerencie notificações, tarefas e comunicações rápidas sem interromper sua navegação atual.

#### Caso de uso

Durante a análise de um Dashboard, um gestor percebe a necessidade de delegar uma ação imediata. Sem sair da tela de métricas, ele utiliza o ícone de **Lista de Tarefas** na barra superior para criar um lembrete ou utiliza o **Avião de Papel** para iniciar uma nova conversa com um parceiro comercial, mantendo o foco na análise principal.

#### Como acessar a página

A barra de ferramentas é fixada no topo da interface, estando sempre acessível independentemente do módulo que o usuário esteja utilizando.

<figure><img src="/files/4q5lLYNwMiCmaQQ1UWsi" alt=""><figcaption></figcaption></figure>

***

#### Detalhamento dos Ícones e Funcionalidades

Abaixo, cada recurso da barra de ferramentas é explicado com sua respectiva forma de uso:

**1. Bolinha Verde (Status do Usuário)**

Indica que o Usuário está ativo e com conexão estável com o servidor do Prismabot. Caso a cor mude ou o ícone desapareça, pode indicar problemas de conexão local ou necessidade de reautenticação.

**2. Ícone de Relógio (Histórico de Ações)**

Fornece um log de auditoria simplificado das operações realizadas pelo usuário na sessão.

* **Como usar:** Ao clicar, um painel lateral exibe ações como *DELETE* (exclusão), *POST* (criação) ou *PUT* (edição). Cada registro mostra o recurso afetado (ex: tickets, mensagens) e há quanto tempo ocorreu.
* **Atualização:** Clique no ícone de seta circular no topo do painel para carregar novas ações registradas.

<figure><img src="/files/JwYlrAmmFQjMroQ6Mhor" alt="" width="375"><figcaption></figcaption></figure>

**3. Ícone de Linguagem (Seleção de Idioma)**

Permite traduzir a interface do sistema para diferentes idiomas de forma global.

* **Como usar:** Clique na sigla do idioma atual (ex: PT). Uma lista suspensa será exibida com opções como Inglês, Espanhol, Alemão, entre outros. Ao selecionar, o sistema aplica a tradução imediatamente.

<figure><img src="/files/GQ55v1252SKpsfRbHKbw" alt="" width="157"><figcaption></figcaption></figure>

**4. Ícone de Sino (Notificações)**

Centraliza alertas de novos Tickets aguardando atendimento ou interações no Chat Privado.

* **Funcionamento:** O círculo vermelho com número indica a quantidade de notificações não lidas. Ao clicar, o sistema exibe os detalhes e permite navegar diretamente para a conversa em questão.

<figure><img src="/files/vLWAY66E97pVIYAzcJmA" alt="" width="265"><figcaption></figcaption></figure>

**5. Balão de Mensagem (Mensagens Internas/Avisos)**

Espaço reservado para comunicados enviados diretamente pelo **Superadmin** do sistema.

* **Como usar:** Utilize este ícone para ler informativos sobre atualizações do sistema, manutenções programadas ou avisos administrativos gerais da plataforma.

**6. Ícone de Prancheta (Lista de Tarefas)**

Ferramenta de organização pessoal para o colaborador.

* **Como usar:** Ao clicar, abre-se um resumo das tarefas pendentes. Caso precise de uma gestão completa, clique no botão **"Ver todas as tarefas"** para ser redirecionado à página de Tarefas do sistema.

<figure><img src="/files/ctZTCNv9yZb25YZwf44I" alt="" width="375"><figcaption></figcaption></figure>

**7. Ícone de Avião de Papel (Nova Conversa Avulsa)**

Permite iniciar um chat com um contato que ainda não possui um atendimento aberto, utilizando um Canal específico.

* **Passo a passo:**
  1. Clique no ícone.
  2. Selecione a **Sessão WhatsApp** (canal) desejada.
  3. Digite o **Número** do destinatário (com código do país).
  4. Selecione um **Template caso for o canal WABA**
  5. Clique em **Enviar**

<figure><img src="/files/6MxJinKdJFMVXj0qyOqZ" alt="" width="375"><figcaption></figcaption></figure>

**8. Ligação Wavoip**

**Como usar:** Clique no ícone e irá aparecer um botão de ligação no canto inferior esquerdo.&#x20;

<figure><img src="/files/TSOCYku6yNMjYpp5NPCl" alt=""><figcaption></figcaption></figure>

Ao clicar nesse ícone irá abrir um discador para realizar a ligação.

<figure><img src="/files/F8Snop7dliodHe3uZyiG" alt="" width="232"><figcaption></figcaption></figure>

{% hint style="info" %}
Para ter o ícon de ligações Wavoip é preciso ter o canal configurado em:&#x20;
{% endhint %}

**9. Tutorias**

**Como usar:** Clique no ícone para verificar os vídeos de tutorial que foram adicionados.

<figure><img src="/files/2wbQTlKxsSuGBiqSPARw" alt="" width="375"><figcaption></figcaption></figure>

**10.Ícone de Headset (Chat com Suporte)**

Canal de comunicação direta com a equipe de suporte do Prismabot.

* **Como usar:** Clique para abrir uma janela de chat flutuante. É possível enviar mensagens de texto e arquivos para sanar dúvidas técnicas sobre a plataforma.

<figure><img src="/files/4XIqbPzAbIb5bqK6vw4u" alt="" width="307"><figcaption></figcaption></figure>

{% hint style="warning" %}
**Configuração de Tenant:** O ícone de **Chat com Suporte** pode não estar visível para todos os usuários se não tiver sido habilitado nas configurações da empresa (*Tenant*).
{% endhint %}

**11.Avatar de Usuário (Perfil e Sessão)**

<figure><img src="/files/qdVlnsEyUwMGApDWhfcd" alt=""><figcaption></figcaption></figure>

Localizado na extremidade direita da barra, este ícone exibe a inicial do usuário e centraliza informações de conta, status de licença e gerenciamento de sessão.

* **Identificação do Usuário:** No topo do menu, são exibidos o nome completo, e-mail de acesso e a tag correspondente ao [perfil de acesso](https://www.google.com/url?sa=E\&q=link-para-perfis) (ex: admin, user).
* **Informações de Sistema:** Exibe a versão atual do software Prismabot e o status da **Licença** (Ativa ou Inativa).
* **Status de Disponibilidade (Online):** Indica o estado atual do atendente no sistema.
* **Meu Perfil:** Atalho direto para a página de [Configurações de Perfil](https://www.google.com/url?sa=E\&q=link-para-perfil), onde é possível alterar senha, foto e dados pessoais.
* **Limpar cookies:** Executa a limpeza dos arquivos temporários de navegação exclusivos do sistema.
  * Uso: Recomendado para resolver problemas de carregamento de interface ou atualizar permissões recém-alteradas sem a necessidade de deslogar.
* **Sair:** Encerra a sessão atual do usuário e retorna para a tela de login.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/home-e-dashboard/barra-de-ferramenta-geral.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
