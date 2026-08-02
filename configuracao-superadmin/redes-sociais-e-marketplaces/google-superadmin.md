Copiar

Nesta página

1. [Configuração Superadmin](/configuracao-superadmin)
2. [Redes Sociais e Marketplaces](/configuracao-superadmin/redes-sociais-e-marketplaces)

# Google - Superadmin

Funcionalidade em Beta

**Disponível para o perfil:** Super Administrador

Configure as credenciais OAuth 2.0 do Google. Um único app no Google Cloud Console cobre Gmail, Calendar e YouTube simultaneamente.

**Configuração global vs. por tenant:** os apps cadastrados aqui ficam disponíveis para todos os tenants. A conexão e o gerenciamento do número WABA de cada tenant é feito individualmente pelo Administrador em Configurações → Integrações

---

#### Como acessar

No painel Super Admin, acesse **Configurações → Apps Google**.

---

#### Como configurar

1. Acesse [console.cloud.google.com](https://console.cloud.google.com/) e crie um projeto
2. Habilite **Gmail API + Google Calendar API + YouTube Data API v3** no **mesmo projeto**
3. Crie credenciais **OAuth 2.0** (tipo: Aplicativo Web) e copie o **Client ID** e o **Client Secret**
4. Cadastre a **Redirect URI** exibida nesta página como *Authorized redirect URI* no Google Cloud Console

---

#### Campos do formulário

Campo

Descrição

**Tenant**

Selecione **Global** para aplicar a todos os tenants sem configuração própria, ou um tenant específico

**Client ID (OAuth 2.0)**

Client ID gerado no Google Cloud Console

**Client Secret**

Client Secret gerado no Google Cloud Console

**Redirect URI (OAuth callback)**

URL fixa — cadastre exatamente esta URL no Google Cloud Console como Authorized redirect URI

**Gmail**

Habilita o uso deste app para o canal de e-mail com OAuth

**Google Calendar**

Habilita a sincronia de eventos e agendamentos

**YouTube**

Habilita comentários e live chat de canais YouTube

**Intervalo de poll YouTube (seg)**

Frequência com que o sistema busca novos comentários. Padrão: 30s. Mínimo: 15s

**Descrição**

Identificação opcional — ex: "App principal Google da plataforma"

**Ativo**

Ativa ou desativa esta configuração

**Scopes (avançado):** deixe os campos de scopes em branco para usar os defaults. Alterar scopes pode quebrar a integração — só mexa se souber o que está fazendo.

---

#### Hierarquia de fallback

O sistema resolve as credenciais Google em 3 camadas, nesta ordem de prioridade:

1. **App próprio do canal** — se o canal tiver um `clientId` próprio cadastrado, ele tem prioridade
2. **App Google configurado aqui** — substitui o proxy para os tenants cobertos
3. **App hardcoded no proxy** — credenciais padrão da plataforma, usadas quando nenhuma das anteriores estiver configurada

Se este formulário estiver vazio, o sistema usa automaticamente as credenciais hardcoded do proxy (Tech Provider). A configuração **Global** (sem tenant específico) aplica como fallback para todos os tenants sem configuração própria.

---

#### Informações importantes

* Os tokens expiram em 1 hora — o sistema renova automaticamente via `refresh_token`
* **Modo Testing** aceita até 100 test users; produção requer verificação do Google (4–8 semanas)
* Pelo menos um serviço (Gmail, Calendar ou YouTube) precisa estar ativo para salvar

---

[AnteriorRedes Sociais e Marketplaces](/configuracao-superadmin/redes-sociais-e-marketplaces)[PróximoLinkedIn - Superadmin](/configuracao-superadmin/redes-sociais-e-marketplaces/linkedin-superadmin)

Atualizado há 1 mês

Isto foi útil?