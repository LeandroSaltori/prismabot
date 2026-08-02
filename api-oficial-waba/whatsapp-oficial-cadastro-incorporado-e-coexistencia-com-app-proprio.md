Copiar

Nesta página

1. [API Oficial WABA](/api-oficial-waba)

# Whatsapp Oficial- Cadastro Incorporado e Coexistência com APP próprio

Como conectar o WhatsApp Business pela API Oficial usando um App Próprio no Facebook Developers com Embedded Signup e coexistência.

#### Tutorial de como aprovar seu APP Próprio na meta:

[Como aprovar seu App da Meta](/api-oficial-waba/whatsapp-oficial-cadastro-incorporado-e-coexistencia-com-app-proprio/como-aprovar-seu-app-da-meta)

#### Parte 1: Configurações no Facebook Developers

Antes de cadastrar no Prismabot, é necessário ajustar as configurações do seu aplicativo na Meta e gerar os dados necessários.

**1. Domínios do Aplicativo**

1. Acesse as **Configurações Básicas** do seu App.
2. Adicione os domínios da sua instalação: **Subdomínio do Front**, **Subdomínio do Back** e o **Domínio do Site**.
3. Caso necessário, adicione também no campo "URL do Site" na parte inferior.

**2. Gerar Token de Sistema (Business Manager)**

1. No seu Business Manager, vá em **Usuários do Sistema**.
2. Adicione o seu Aplicativo aos ativos.
3. Gere um novo Token selecionando o app e marcando as seguintes permissões obrigatórias:

   * business\_management
   * whatsapp\_business\_messaging
   * whatsapp\_business\_management
4. **Copie o Token** gerado (ele será usado no Superadmin).

**3. Configuração do Cadastro Incorporado (Config ID)**

1. No painel do App, vá em **WhatsApp** > **Configuração**.
2. Em "Configuração de Login", clique em **Criar Configuração**.
3. Selecione os produtos: **Cloud API** e **API de mensagens de marketing**.
4. Em permissões, selecione todas (Set) e garanta que as 3 permissões do passo anterior estejam marcadas, mais a permissão:

   * whatsapp\_business\_management\_events
5. Salve e **copie o número da "ID da configuração"** (Config ID).

---

#### Parte 2: Configuração no Superadmin

Com os dados em mãos, vamos configurar o aplicativo dentro do sistema.

1. Acesse o painel **Superadmin** > **App Waba**.
2. Clique em **Adicionar** e preencha os campos:

   * **App ID:** Encontrado no cabeçalho do Facebook Developers.
   * **Versão da API:** Utilize a versão atual (ex: v24.0).
   * **Token:** Cole o Token de Sistema gerado na Parte 1.
   * **Config ID:** Cole o ID da configuração gerado na Parte 1.
   * **App Secret:** Encontrado nas configurações básicas do App (clique em "Mostrar").
3. **Importante:** Copie a **URL de Redirecionamento** (Redirect URI) que o sistema exibe nesta tela.
4. Volte ao Facebook Developers > **Facebook Login** > **Configurações** e cole essa URL no campo "URIs de redirecionamento do OAuth válidos".
5. Salve o cadastro no Superadmin.

---

#### Parte 3: Utilizando a Integração (Tenant)

Agora que o app está configurado, o cliente final pode conectar as contas.

1. No painel do cliente, vá em **Integrações** > **Meta**.
2. Clique no botão **Cadastro Incorporado**.
3. Uma janela do Facebook se abrirá. Siga o fluxo de login ("Continuar como...").

**Cenário A: Criar/Adicionar Novo Número**

1. Siga o passo a passo para criar uma nova conta de WhatsApp Business ou selecionar uma existente.
2. Após concluir, o número aparecerá na lista de integrações.
3. **Atenção:** Se for um número novo, ele aparecerá como "Não Registrado". Clique em **Registrar Telefone**, insira um PIN de 6 dígitos e conclua a ativação para poder enviar mensagens.

**Cenário B: Modo Coexistência (Requer App Aprovado)**

1. No fluxo do pop-up, selecione a opção de usar um número existente.
2. O sistema identificará se o número é elegível para coexistência (deve ser uma conta Business).
3. Se já estiver conectado no WhatsApp Business App, o fluxo pulará a verificação de SMS e conectará automaticamente.
4. Ao finalizar, o canal será criado e você poderá ver o status "Conectado".
5. O número funcionará tanto no painel (API) quanto no celular (App Business) simultaneamente.

[AnteriorAPI Oficial WABA](/api-oficial-waba)[PróximoComo aprovar seu App da Meta](/api-oficial-waba/whatsapp-oficial-cadastro-incorporado-e-coexistencia-com-app-proprio/como-aprovar-seu-app-da-meta)

Atualizado há 23 dias

Isto foi útil?