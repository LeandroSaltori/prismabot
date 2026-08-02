# API - Configurações

{% hint style="warning" %}
**Disponível para o perfil:** Administrador
{% endhint %}

A página de **API** do sistema Prismabot é o ambiente destinado à integração técnica entre a plataforma e sistemas externos (como CRMs, sites, ERPs ou automações de marketing). Através desta tela, o administrador gera chaves de acesso, consulta a documentação técnica e testa as rotas de comunicação em tempo real.

{% hint style="warning" %}
**Uma API por canal:** cada integração criada em **+ Nova API** é vinculada a uma única Sessão (canal de WhatsApp). Se você precisa disparar por mais de um canal, crie uma API separada para cada um — não é possível usar a mesma chave/token para múltiplos canais.
{% endhint %}

#### Principais funções

* **Gestão de Tokens:** Criação e revogação de chaves de autenticação.
* **Documentação Interativa:** Acesso direto à lista de endpoints e parâmetros.
* **Sandbox:** Ambiente de teste para validar requisições sem sair do painel.
* **Webhooks:** Configuração de disparos automáticos de eventos do sistema para URLs externas.

#### Caso de uso

Uma empresa utiliza um CRM externo para gerenciar suas vendas. Através da **API**, o desenvolvedor integra os sistemas para que, toda vez que um negócio for movido para "Fechado" no CRM, o Prismabot envie automaticamente uma mensagem de boas-vindas ao Contato utilizando uma Sessão WhatsApp específica.

#### Como acessar a página

No menu lateral, clique no Menu **Configuração** e na aba **API**.

<figure><img src="/files/V5dnFrMlhuHtzAD09nDr" alt="" width="272"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/R5iPJbicwRon6QrSwiUQ" alt=""><figcaption></figcaption></figure>

**Explicação dos campos e ícones**

* **Botão Postman:** Atalho para baixar a coleção de requisições pré-configuradas para uso no software Postman.
  * <https://www.postman.com/comunidade-zdg/z-pro/collection/s16subg/postman-v3-x-x-x?action=share&creator=25151510&sideView=agentMode>
* **Botão + Nova API:** Abre o formulário para gerar uma nova integração vinculada a um canal.
* **URL de Integração:** O endereço base que deve ser utilizado nas chamadas externas.
* **Bearer Token:** A chave secreta de autenticação.
* **Ícones de Ação:**
  * **Atualizar (Seta circular):** Gera um novo token para a API selecionada (o anterior é invalidado imediatamente).
  * **Editar (Lápis):** Permite alterar o nome da integração.
  * **Excluir (Lixeira):** Remove a integração e invalida o acesso externo permanentemente.
  * **Olho / Copiar:** Permite visualizar o token oculto e copiá-lo para a área de transferência.

***

#### Criando uma API

1. Clique no botão **+ Nova API** no canto superior direito.
2. No modal que aparecerá, dê um **Nome** identificador para a integração (ex: CRM Vendas).
3. Selecione a **Sessão** (canal de WhatsApp) que será utilizada para os disparos desta API.
4. Clique em **Salvar**.
5. **Importante:** Copie o token gerado imediatamente. Por questões de segurança, recomenda-se o armazenamento em local seguro, pois ele é a chave de acesso ao seu sistema.

<figure><img src="/files/62sr03TLuhh3Nfaw97ds" alt="" width="375"><figcaption></figcaption></figure>

#### Usando a API e Documentação

Para facilitar o desenvolvimento, o Prismabot disponibiliza uma documentação completa e testável dentro da própria interface:

1. Consulte a seção **Documentação de rotas** para visualizar todos os [Endpoints disponíveis](https://prismatelecomservicos.com/central-do-assinante/referencia-da-api).
2. Utilize o **Sandbox** selecionando uma API ativa no menu suspenso. Isso permite que você preencha os parâmetros e teste a requisição diretamente na página para ver a resposta do servidor.
3. A autenticação de todas as chamadas deve ser feita via Header: `Authorization: Bearer {seu_token}`.

<figure><img src="/files/39l2IbrAURvMOUyy9dZa" alt=""><figcaption></figcaption></figure>

#### Webhooks e Eventos

Os **Webhooks** permitem que o Prismabot "fale" com o seu sistema externo em tempo real quando algo acontece:

* **Configuração:** Informe a URL de callback no campo de destino.
* **Eventos Disponíveis:** O sistema pode notificar sobre novas mensagens recebidas, tickets abertos, alterações de status e confirmações de entrega.
* **Otimização:** Filtre apenas os eventos que são estritamente necessários para sua integração, reduzindo o tráfego de dados desnecessário.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/configuracao/api.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
