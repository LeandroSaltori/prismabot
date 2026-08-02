# Instagram e Facebook Messenger via OAuth (login)

Essa é a forma mais rápida e recomendada de realizar a integração com Instagram e Facebook Messenger, pois dispensa a necessidade de criar e aprovar um aplicativo próprio no painel de desenvolvedores da Meta.

{% embed url="<https://youtu.be/_6SmcZ96_cM>" %}

***

### Etapa 0: Liberação no Painel Super Admin (Para ambos os canais)

A liberação da integração via aplicativo nativo precisa ser feita individualmente para cada empresa (Tenant) dentro do painel global. Esta etapa serve tanto para o Messenger quanto para o Instagram.

1. Faça o login no Prismabot com o seu usuário **Super Admin**.
2. Acesse o menu **Tenants** e clique em **Editar** na empresa onde deseja ativar os canais.

<figure><img src="/files/dZC7HihcSoBfPYD1wU1s" alt="zpro - tela de gestão de Tenants - como editar tenant"><figcaption></figcaption></figure>

Role a página até encontrar a seção de **Autenticação (OAuth)**.

1. **Habilite a chave** de ativação do OAuth.
2. Preencha os campos com as informações do aplicativo nativo:

   * **URL / Domínio:**&#x20;

   [<mark style="color:$tint;">https://oauth.techprovider.com.br</mark>](https://oauth.techprovider.com.br)

   * **Webhook do Messenger:**

   [<mark style="color:$tint;">https://oauth.techprovider.com.br/messenger-webhook</mark>](https://oauth.techprovider.com.br/messenger-webhook)<mark style="color:$tint;">/</mark>

   * **Webhook do Instagram:**&#x20;

   [<mark style="color:$tint;">https://oauth.techprovider.com.br/instagram-wehbhook</mark>](https://oauth.techprovider.com.br/instagram-wehbhook)<mark style="color:$tint;">/</mark>

   * **Chave Secreta** (é a mesma tanto para instagram quanto para messenger)**:**

   <mark style="color:$primary;">2f5b5b457e2febbc3c2333e2ebc84df926a45c36f76f3bedc0d1994f749413f1</mark>
3. Clique em **Salvar**.

<figure><img src="/files/2bWcWcTRVchci8fF8O1n" alt="zpro - tela de configuração do Tenant - oauth instagram e facebook messenger" width="375"><figcaption></figcaption></figure>

Obs: Volte mais acima, na seção de liberação de canais, certifique-se de que o **WhatsApp**, **Facebook** e **Instagram** estão habilitados para este tenant.

<figure><img src="/files/V6jrqirMSIgJ43sk2mxK" alt="zpro - tela de configuração do Tenant - canais liberados"><figcaption></figcaption></figure>

Clique em **Salvar**.

***

### Etapa 1: Permissões de ADM da Página do Facebook (Especificamente para o canal Facebook Messenger)

Antes de ir para a tela de canais fazer a conexão, existe uma regra obrigatória **apenas para o Facebook Messenger**.

(Se você vai conectar apenas o Instagram, pule para a Etapa 2).

{% hint style="danger" %}
**ATENÇÃO: O ACESSO DE ADM VIA GERENCIADOR DE NEGÓCIOS NÃO É SUFICIENTE PARA O MESSENGER**
{% endhint %}

Para conectar o Messenger ao Prismabot, o seu perfil pessoal do Facebook precisa estar adicionado como **Administrador Direto da Página** (Com perfil pessoal do facebook).

Ter "Acesso Total" através do Portfólio Empresarial (Gerenciador de Negócios / Meta Business Suite) **não** é suficiente para liberar a conexão. Se houver apenas esse acesso via portfólio / gerenciador, o sistema retornará um erro na hora de conectar.

#### Como corrigir e se adicionar como Administrador da Página do Facebook:

Se você já tem o acesso gerencial da página, siga estes passos no Facebook para se dar a permissão correta:

1. Abra o Facebook e **mude para o perfil da Página** (Logar como a página).
2. Acesse as **Configurações** da página.
3. No menu lateral, clique em **Acesso à Página** (ou Configuração da Página > Acesso à Página).
4. Na primeira seção, chamada **"Pessoas com acesso do Facebook"**, clique em **Adicionar novo**.
5. Pesquise pelo **seu perfil pessoal** (o perfil que você usa para logar no Facebook) e conceda **Controle Total**.
6. Volte para o seu perfil pessoal do Facebook, abra suas notificações e **Aceite o convite**.

<figure><img src="/files/tMsKpEF2dXtT1OeggXcb" alt="fanpage facebook - configurações e permissões da página - acesso admin"><figcaption></figcaption></figure>

### Etapa 2: Criando as Conexões no Painel Admin

Com o OAuth liberado no Tenant (e as permissões do Facebook ajustadas, caso vá usar o Messenger), vamos realizar a conexão final no painel de atendimento.

Acesse o Prismabot com o seu usuário **Administrador** da conta (Tenant) e vá em **Administração > Canais > Adicionar Canal**.

#### Conectando o Instagram

<figure><img src="/files/9yeZhisey65jRtUae5QT" alt="zpro - conectar canal instagram" width="375"><figcaption></figcaption></figure>

O processo do Instagram é extremamente simples e não exige configurações avançadas de página.

1. No tipo de canal, selecione **Instagram**.
2. No campo "Aplicativo Meta", clique no menu suspenso e **selecione a integração OAuth** que liberamos no Super Admin (meta.zdg.com.br).
3. Clique no botão azul **Conectar via Instagram OAuth**.
4. **No Pop-up da Meta:** Uma janela do Facebook será aberta. Siga as etapas na tela para vincular a conta do Instagram Business.
   * Dica: Certifique-se de estar logado na sua conta do Instagram Business em outra aba do mesmo navegador para que o pop-up a reconheça e faça a vinculação automaticamente.

#### Opção B: Conectando o Facebook Messenger

<figure><img src="/files/H0HBHqYuBJPpca1sYLKV" alt="zpro - conectar canal facebook messenger" width="375"><figcaption></figcaption></figure>

1. No tipo de canal, selecione **Facebook**.
2. No campo "Aplicativo Meta", clique no menu suspenso e **selecione a integração Oauth** que liberamos no super-admin (meta.zdg.com.br).
3. Clique no botão azul **Conectar via Facebook OAuth**.
4. **No Pop-up da Meta:** Uma janela do Facebook será aberta.
   * Faça o login com o seu **perfil pessoal** (aquele que colocamos como administrador da página na Etapa 2).
   * Clique em **Continuar como \[Seu Nome]**.
   * Selecione a Página que você deseja conectar ao Prismabot e conceda as permissões solicitadas.

#### Pronto!

Se tudo estiver correto, a janela pop-up se fechará e o seu canal (Instagram ou Messenger) aparecerá como **Conectado** na sua lista de canais.

A partir de agora, todas as mensagens e directs dos canais instagram / facebook messenger chegarão diretamente na sua tela de atendimento do Prismabot!


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/instagram-e-facebook-messenger-via-oauth-login.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
