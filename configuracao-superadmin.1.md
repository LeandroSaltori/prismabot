Copiar

Nesta página

1. [Configuração Superadmin](/configuracao-superadmin)

# Visão geral Superadmin

Este é o painel de administração de mais alto nível, projetado para o gerenciamento centralizado de toda a instância da plataforma Prismabot.

O **Painel Superadmin** é a área administrativa de mais alto nível do Prismabot. É aqui que o dono da instalação gerencia a infraestrutura, as licenças, a personalização plataforma de atendimento, os tenants (empresas clientes) e as conexões globais que alimentam toda a plataforma.

Este painel é exclusivo para o **dono da instalação** (dono da servidor em nuvem ou do SaaS). Não deve ser confundido com o painel de atendimento nem com o painel Admin de cada tenant.

---

### [Tenants e Licença](/configuracao-superadmin/tenants-e-licenca)

O coração do seu SaaS. Aqui você valida a licença Prismabot, cria e gerencia as empresas (tenants) cadastradas na plataforma, define planos de serviço, controla pagamentos e gerencia os usuários de cada conta.

* **Gerenciar Licença Prismabot** — ativação e status da licença oficial
* **Gestão de Tenants** — criar, editar e desativar empresas clientes
* **Planos** — criar planos de serviço e gerar chave API de cobrança (Asaas)
* **Pagamentos dos Tenants** — histórico e controle de cobranças
* **Usuários por Tenant** — limites e gestão de usuários por empresa
* **Chat Suporte** — canal de suporte interno entre o superadmin e os tenants

---

### [Configurações Superadmin](/configuracao-superadmin/configuracoes)

Identidade visual e configurações globais do servidor — afetam todos os tenants da instância.

* **Customizar (plataforma de atendimento)** — nome, cor, logo e domínio da plataforma
* **E-mail SMTP** — servidor de e-mail para envios transacionais do sistema
* **Notificações Internas** — alertas e notificações globais da plataforma
* **Apps Google** — credenciais do Google para integrações que dependem de OAuth

---

### [Canais Superadmin](/configuracao-superadmin/canais-superadmin)

Configurações globais de canais e integrações que se aplicam à instância inteira — não a um tenant específico.

* **Sessões dos Tenants** — visão consolidada das sessões ativas de todos os tenants
* **Facebook Login Incorporado** — credenciais do App Meta para WABA, Instagram e Messenger
* **Domínio OAuth Customizado** — configurar domínio próprio para o fluxo de autenticação OAuth
* **Provedores de IA Globais** — chaves de API de IA disponíveis para todos os tenants
* **API do Tenant** — configurações de API expostas no nível da instância

---

### [Redes Sociais e Marketplaces](/configuracao-superadmin/redes-sociais-e-marketplaces)

Configuração dos aplicativos de plataformas externas que precisam ser registrados no nível do superadmin para ficarem disponíveis aos tenants. Cada item representa um App cadastrado na plataforma de origem.

* **App WABA** — aplicativo da API Oficial do WhatsApp (Meta)
* **Google** — App Google para Calendar, Drive e integrações OAuth
* **LinkedIn** — App LinkedIn para integração de canal
* **TikTok** — App TikTok para comentários e DMs
* **Mercado Livre** — App MercadoLivre para atendimento de compras
* **OLX** — App OLX para integração de anúncios
* **WooCommerce** — App WooCommerce para atendimento de e-commerce
* **Rocket.Chat** — integração com Rocket.Chat

---

### [Sistema](/configuracao-superadmin/sistema)

Monitoramento e manutenção técnica da instância. Use esta seção para tarefas operacionais: backup, migração, armazenamento e diagnóstico.

**Operação:**

* **Monitor** — visão em tempo real do estado dos serviços da instância
* **Terminal** — acesso ao terminal do servidor direto pelo painel
* **Backup** — criar e restaurar backups da instância
* **Migração de Tenants** — mover tenants entre instâncias

**Dados e configuração:**

* **Dados Internos** — Redis, cache e dados internos do sistema
* **Storage S3** — configurar armazenamento externo de mídia
* **Log de Auditoria** — histórico de ações administrativas na instância

[AnteriorPrimeiro Acesso ao Sistema](/primeiro-acesso/primeiro-acesso-ao-sistema)[PróximoTenants e Licença](/configuracao-superadmin/tenants-e-licenca)

Atualizado há 26 dias

Isto foi útil?