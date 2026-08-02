Copiar

Nesta página

1. [Configuração Superadmin](/configuracao-superadmin)
2. [Redes Sociais e Marketplaces](/configuracao-superadmin/redes-sociais-e-marketplaces)

# Rocket.chat - Superadmin

**Funcionalidade em beta:** este recurso foi lançado recentemente e ainda está em fase de testes. Alguns comportamentos podem apresentar instabilidade ou não funcionar como esperado em todos os cenários. Estamos coletando feedback e aplicando melhorias e correções ao longo das próximas versões. Se encontrar algum problema, entre em contato com o suporte.

Esta documentação detalha o processo para integrar um servidor **Rocket.Chat** ao **Prismabot**, permitindo que os agentes acessem o chat interno do Rocket.Chat diretamente pelo painel, sem precisar alternar entre plataformas.

**Configuração global vs. por tenant:** os apps cadastrados aqui ficam disponíveis para todos os tenants. A conexão e o gerenciamento do número WABA de cada tenant é feito individualmente pelo Administrador em Configurações → Integrações

**Pré-requisitos:**

* Um servidor **Rocket.Chat** instalado e acessível via URL pública.
* Acesso de **administrador** no servidor Rocket.Chat.
* Acesso de **Super Admin** na sua instalação do Prismabot.

**Página de referência da tela do admin:**
Apps — Rocket.Chat

---

#### Como funciona a integração

Após a configuração, os agentes passam a acessar o Rocket.Chat **embutido diretamente no Prismabot** via **Comunicação e Marketing → Redes Sociais → Rocket.Chat**, sem precisar abrir outra aba ou sistema.

Diferente das integrações de marketplace (Mercado Livre, OLX), o Rocket.Chat **não cria tickets** no painel de atendimento. O acesso é direto ao chat interno do servidor RC.

---

#### Etapa 1: Criar o Bot User no Rocket.Chat

No painel de administração do seu servidor Rocket.Chat:

1. Acesse **Administração → Usuários → Novo Usuário**.
2. Crie um usuário dedicado para a integração com as seguintes **roles (funções)**:

   * `bot`
   * `livechat-agent`
3. Anote o **Username** e o **User ID** deste usuário.

Use um usuário exclusivo para a integração — evita conflitos e facilita o monitoramento da conta no RC.

---

#### Etapa 2: Gerar o Personal Access Token

Ainda no servidor Rocket.Chat, gere o token que o Prismabot usará para autenticar:

1. Faça login com o usuário admin (ou com o bot user criado na Etapa 1).
2. Clique no avatar do usuário → **Perfil → Tokens de Acesso Pessoal**.
3. Clique em **Adicionar** e dê um nome ao token (ex: "Prismabot Integration").
4. Copie e guarde o **User ID** e o **Token** gerados — eles não serão exibidos novamente.

---

#### Etapa 3: Habilitar Iframe Integration no Rocket.Chat

Para que o Rocket.Chat seja embutido corretamente no Prismabot:

1. No painel de administração do RC, acesse **Administração → Geral**.
2. Localize a seção **Iframe Integration**.
3. Ative a opção **Enable Send** e/ou **Enable Receive** conforme necessário.
4. Salve as configurações.

Sem esta configuração habilitada no servidor Rocket.Chat, o iframe não carregará corretamente dentro do Prismabot.

---

#### Etapa 4: Configurando no Painel Super Admin

Com as informações do servidor em mãos, acesse o Prismabot:

1. Faça login com o usuário **Super Administrador**.
2. No menu lateral, localize **Redes Sociais / Marketplace → App Rocket.Chat**.
3. Clique em **+ Novo App RC** e preencha:

Campo

Como preencher

**Tenant**

Selecione **Global** ou um tenant específico

**URL do servidor**

URL base do servidor Rocket.Chat — ex: `https://chat.suaempresa.com`

**Admin User ID (X-User-Id)**

User ID obtido na Etapa 2

**Admin Auth Token (X-Auth-Token)**

Personal Access Token obtido na Etapa 2

**Descrição**

Identificação opcional — ex: "RC principal da empresa"

**Criar usuários automaticamente**

Quando ativo, cria automaticamente uma conta no RC para cada agente que acessar o chat pela primeira vez

**Ativo**

Mantenha ativado

1. Clique em **Criar**.

**Global vs. Tenant específico:** A configuração **Global** funciona como fallback — qualquer tenant sem configuração própria utilizará a global. Para clientes individuais (revendedores SaaS), o ideal é configurar **por tenant**.

---

#### Etapa 5: Ativando para o Tenant no Painel Admin

Após criar a configuração no Super Admin, é necessário **ativar a integração para o tenant** no painel administrativo:

1. Acesse o **painel administrativo** do tenant.
2. Vá em **Configurações → Integrações → Rocket.Chat**.
3. Ative o toggle **Habilitar Rocket.Chat**.
4. Salve.

---

#### Etapa 6: Acesso dos Agentes

Após a ativação, os agentes passam a visualizar o Rocket.Chat embutido no Prismabot:

**Caminho de acesso:** **Comunicação e Marketing → Redes Sociais → Rocket.Chat**

O chat interno do servidor RC ficará disponível diretamente nessa seção, sem necessidade de abrir outro sistema.

Se **"Criar usuários automaticamente"** estiver ativo, a conta no RC é criada automaticamente na primeira vez que o agente acessar esta seção.

---

#### Resumo das Funcionalidades

Funcionalidade

Onde acessar

Configurar integração com Rocket.Chat

Super Admin > App Rocket.Chat

Configurar credenciais por tenant

Painel Admin > Configurações > Apps > Rocket.Chat

Ativar para o tenant

Painel Admin > Configurações > Integrações > Rocket.Chat

Acessar o chat interno

Painel Admin > Comunicação e Marketing > Redes Sociais > Rocket.Chat

---

#### Possíveis Erros e Soluções

**Iframe não carrega dentro do Prismabot**

**Causa:** Iframe Integration desabilitada no servidor Rocket.Chat.

**Solução:** Acesse **Administração → Geral → Iframe Integration** no RC e habilite as opções de Send/Receive.

**Erro de autenticação ao salvar a configuração**

**Causa:** User ID ou Auth Token incorretos.

**Solução:** Gere um novo Personal Access Token no RC (**Perfil → Tokens de Acesso Pessoal**) e atualize a configuração no Prismabot.

**Agentes não visualizam o Rocket.Chat no menu**

**Causa:** Toggle de ativação não foi habilitado para o tenant.

**Solução:** Acesse **Configurações → Integrações → Rocket.Chat** no painel admin e ative o toggle **Habilitar Rocket.Chat**.

[AnteriorOLX - Superadmin](/configuracao-superadmin/redes-sociais-e-marketplaces/olx-superadmin)[PróximoTiktok - Superadmin](/configuracao-superadmin/redes-sociais-e-marketplaces/tiktok-superadmin)

Atualizado há 22 horas

Isto foi útil?