# Home

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

A página **Home** é o ponto de partida do sistema Prismabot após o login. Ela funciona como um cockpit de navegação, oferecendo atalhos visuais e informações resumidas para facilitar o início da jornada de trabalho do colaborador.

#### Principais funções

* **Navegação Ágil:** Atalhos diretos para os módulos mais utilizados.
* **Histórico de Navegação:** Exibição de páginas visitadas recentemente.
* **Central de Avisos:** Painel com informações rápidas e dicas sobre os recursos do sistema.
* **Identificação de Perfil:** Exibição clara do nome do usuário e nível de acesso.

#### Caso de uso

Ao iniciar o turno, um atendente utiliza a página Home para acessar instantaneamente a tela de Atendimentos ou verificar o Chat Privado em busca de comunicados internos. Em vez de navegar por todos os menus laterais, ele utiliza os cards centrais para economizar tempo e otimizar a produtividade.

#### Como acessar a página

Clique no Menu **Principal** e na aba **Home**.

<figure><img src="/files/kC2M3oySFpKiPRpiVRaQ" alt="" width="272"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/Vyz7kMiUsOXBO4B8oFJ7" alt=""><figcaption></figcaption></figure>

**Explicação dos campos e ícones**

* **Banner de Saudação:** Exibe o nome do usuário logado e o seu nível de permissão (ex: User ou Admin).
* **Cards de Acesso Principal:**
* **Páginas Recentes:** Lista as últimas telas acessadas pelo usuário, permitindo um retorno rápido a uma atividade interrompida.
* **Informações Rápidas:** Seção informativa com lembretes&#x20;
* **Acesso Rápido:** Menu lateral direito com links em lista para Campanhas, Dashboard e outros recursos essenciais.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/home-e-dashboard/home.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
