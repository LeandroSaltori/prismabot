Copiar

Nesta página

1. [Configuração Superadmin](/configuracao-superadmin)
2. [Canais Superadmin](/configuracao-superadmin/canais-superadmin)

# Facebook Login incorporado (waba/insta/messenger)

## Login do Facebook Incorporado (WABA)

A funcionalidade de **Login do Facebook** permite que seus clientes conectem contas de WhatsApp Business API (WABA) ao Prismabot de forma simplificada.

Ao configurar seu aplicativo da Meta no Superadmin, o cliente não precisará gerar tokens manuais. Ele apenas clicará em um botão "Logar com Facebook", aceitará as permissões e selecionará os números disponíveis para criar o canal.

**Vídeo Tutorial:**

---

### Parte 1: Configuração na Meta (Facebook Developers)

Para que o login funcione, você precisa configurar um aplicativo no painel de desenvolvedores do Facebook.

#### 1. Criar e Configurar o App

1. Acesse [developers.facebook.com](https://developers.facebook.com) e crie um aplicativo do tipo **Empresa (Business)**.
2. No painel do app, vá em **Configurações Básicas** e copie o **ID do Aplicativo** e a **Chave Secreta (App Secret)**. Você precisará deles depois.
3. Adicione o domínio do seu Prismabot (onde o front-end roda) no campo **Domínios do Aplicativo**.

#### 2. Adicionar o Produto "Login do Facebook"

1. No menu lateral ou em "Adicionar Produto", selecione **Login do Facebook**.
2. Vá em **Configurações** (dentro de Login do Facebook).
3. Ative a opção **Login com o SDK do JavaScript**.
4. Em **Domínios permitidos para o SDK do JavaScript**, insira o domínio do seu painel (ex: `https://app.seusistema.com.br`).
5. **IMPORTANTE:** No campo **URIs de redirecionamento do OAuth**, adicione o caminho do arquivo de embed: `https://app.seusistema.com.br/facebook_embed_signup.html` *(Substitua* `app.seusistema.com.br` *pelo seu domínio real).*

#### 3. Configurar Permissões e Casos de Uso

Dependendo da versão do painel da Meta, vá em **Revisão do App > Permissões e Recursos** ou **Casos de Uso**. Certifique-se de adicionar e conceder acesso avançado (ou standard para testes) às seguintes permissões:

* `email`
* `public_profile`
* `whatsapp_business_management`
* `business_management`

#### 4. Configuração do Cadastro Incorporado (Embedded Signup)

1. Adicione o produto **WhatsApp** ao seu app.
2. Vá em **Configuração > Cadastro Incorporado**.
3. Crie uma nova configuração (Config ID).
4. Selecione as permissões citadas acima e marque a opção **"Token nunca expira"**.
5. Ao salvar, ele gerará um código de **Config ID**. Copie este número.

#### 5. Gerar Token do Sistema (Business Manager)

1. Acesse o **Gerenciador de Negócios** (Business Manager) vinculado ao app.
2. Vá em **Usuários > Usuários do Sistema**.
3. Adicione um usuário (se não houver) e clique em **Gerar Novo Token**.
4. Selecione o Aplicativo que você criou.
5. Marque as permissões (`whatsapp_business_management`, `business_management`) e gere o token.
6. Copie este token (ele é o Token Permanente do Sistema).

---

### Parte 2: Configuração no Prismabot (Superadmin)

Agora que você tem os dados da Meta, vamos configurar no seu sistema.

1. Acesse o painel **Superadmin** do Prismabot.
2. No menu lateral, localize a opção **Apps WABA** (ou Configurações do Facebook).
3. Clique em **Adicionar** e preencha os campos com os dados obtidos na Parte 1:

   * **App ID:** (Copiado da Configuração Básica).
   * **App Secret:** (Copiado da Configuração Básica).
   * **Token:** (Gerado no Business Manager - Usuário do Sistema).
   * **Config ID:** (Gerado no Cadastro Incorporado do WhatsApp).
   * **Versão da API:** Utilize a versão atual (ex: `v21.0` ou a mais recente disponível no seu app Meta).
4. Salve a configuração.

---

### Parte 3: Como o Cliente Utiliza (Tenant)

Com tudo configurado, o processo para o seu cliente é extremamente simples:

1. O cliente acessa o painel da empresa dele (Admin).
2. Vai em **Configurações > Integrações**.
3. Na sessão do Facebook/Meta, ele verá o botão **"Login com Facebook"** (ou "Continuar com Facebook").
4. Ao clicar, abrirá um popup da Meta pedindo autorização.
5. Após autorizar, o sistema listará as contas de WhatsApp Business vinculadas ao usuário.
6. O cliente seleciona a conta e o número desejado.
7. O sistema cria o canal **WABA** automaticamente, pronto para uso.

**Nota sobre Permissões:** Se o cliente encontrar erros ao logar, verifique se o seu Aplicativo na Meta está no modo **"Ao Vivo" (Live)** e se o "Acesso à Empresa" foi concluído. Apps em modo de "Desenvolvimento" só funcionam para administradores do próprio app.

Atualizado há 7 meses

Isto foi útil?