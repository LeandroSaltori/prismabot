# WaVoIP - Gestão comercial

{% hint style="warning" %}
**Disponível para o perfil:** Administrador e Supervisor
{% endhint %}

A página **WaVoIP** é o módulo dedicado à gestão e auditoria de chamadas telefônicas realizadas através da integração de voz sobre IP do sistema Prismabot. Esta interface permite autenticar a conta de telefonia, sincronizar o histórico de comunicações e acessar gravações para monitoria de qualidade.

#### Como acessar a página

Clique no Menu **Gestão Comercial** e selecione a aba **WaVoIP**.

<figure><img src="/files/eu1krKno7SP0wbjdZ4ve" alt="" width="251"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

A página oferece dois métodos de acesso aos dados, divididos em abas superiores:

**Explicação dos campos e ícones**

* **Aba Login e Chamadas:** Utilizada para autenticação padrão via conta de usuário.
  * **E-mail:** Endereço de e-mail cadastrado no serviço WaVoIP.
  * **Senha:** Senha de acesso vinculada à conta.
  * **Botão Autorizar e Carregar Chamadas:** Valida as credenciais e puxa a lista de chamadas recentes para a tela.

<figure><img src="/files/LYrLsobUSeA4Z9ikLSv1" alt=""><figcaption></figcaption></figure>

* **Aba Por Token:** Utilizada para consultas rápidas através de chaves de integração.
  * **Token WaVoIP:** Campo para seleção ou inserção do token de autenticação técnica.
  * **Botão Buscar Chamadas:** Filtra o histórico com base no token informado.

<figure><img src="/files/xWc2CKPGRUGdM0fDtMCv" alt=""><figcaption></figcaption></figure>

***

#### Passo a passo de uso

**Autenticação e Consulta via Login**

1. Acesse a aba **Login e Chamadas**.
2. Insira seu **E-mail** e **Senha** do serviço de telefonia.
3. Clique em **Autorizar e Carregar Chamadas**.
4. O sistema exibirá a tabela com o histórico completo abaixo dos campos de login.

**Consulta via Token**

1. Acesse a aba **Por Token**.
2. Selecione o **Token WaVoIP** desejado no menu suspenso ou insira a chave manual se solicitado.
3. Clique em **Buscar Chamadas** para atualizar a listagem.

**Ouvir Gravações**

1. Na lista de chamadas gerada, identifique o contato desejado.
2. Localize a coluna **Gravação**.
3. Clique no link ou ícone de **Ver/Ouvir** para abrir o reprodutor de áudio da chamada selecionada.

#### Detalhamento

A integração WaVoIP permite que os dados de voz sejam vinculados aos Contatos do Prismabot, facilitando a identificação do cliente na lista de chamadas. Caso uma chamada seja identificada, o nome do contato aparecerá ao lado do número de telefone.

#### Avisos e precauções

{% hint style="warning" %}
**Credenciais:** Certifique-se de que os dados de login informados são os mesmos utilizados no painel administrativo do seu provedor WaVoIP.
{% endhint %}

{% hint style="info" %}
A disponibilidade das gravações depende da retenção de dados configurada em seu plano de telefonia WaVoIP. Caso o áudio não carregue, verifique se a chamada ainda está dentro do prazo de armazenamento do provedor.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/gestao-comercial/analises-e-registros/wavoip.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
