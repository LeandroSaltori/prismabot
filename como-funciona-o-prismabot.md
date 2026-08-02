Copiar

Nesta página

# Como funciona o Prismabot

Visão geral do Prismabot: plataforma omnichannel gerenciado em nuvem com WhatsApp, Instagram, chatbot, multi-tenant e plataforma de atendimento para empresas e cliente final.

O Prismabot é uma plataforma omnichannel de atendimento e automação de conversas. Centraliza em um único painel mensagens de múltiplos canais — WhatsApp, Instagram, Facebook Messenger, Telegram, E-mail e Webchat —, distribui atendimentos entre filas e equipes, automatiza jornadas com chatbot nativo (ChatFlow) e integra com ferramentas externas via API, N8N e provedores de IA. É voltado tanto para empresas que operam o próprio atendimento quanto para empresas e clientes finais que buscam otimizar seu atendimento.

O Prismabot é **gerenciado em nuvem**: o sistema é instalado e roda no servidor (servidor em nuvem) contratado pelo próprio assinante. Isso significa que os dados ficam na infraestrutura do assinante, sem dependência de nuvem da Prisma Telecom. A instalação pode ser feita pela equipe técnica da Prisma Telecom ou pelo próprio assinante usando o auto-instalador disponibilizado após a compra.

**API Oficial do WhatsApp (WABA):** o Prismabot é Tech Provider homologado da Meta. Você conecta números pela API Oficial — o método mais estável, seguro e recomendado para operações profissionais, sem risco de banimento e com suporte direto da Meta.

Em ambos os planos a plataforma é **plataforma de atendimento**: você usa sua própria marca, seu domínio e suas cores. A diferença está na escala — o plano **Uso Próprio** opera com uma única conta, enquanto o plano **cliente final** permite criar contas isoladas para múltiplos clientes (multi-tenant) e comercializá-las como SaaS.

---

### O que está incluso na assinatura

A licença é **anual, sem cobrança por usuário, conexão ou volume de mensagens**. Inclui:

* **Licença de uso** — usuários, conexões e chatbots ilimitados (limitados apenas pela capacidade do seu servidor)
* **Instalação inicial** — nossa equipe faz o primeiro setup no seu servidor, ou você usa o auto-instalador com tutorial em vídeo
* **Portal de treinamento** — área de membros com vídeo-aulas para configurar, operar e escalar
* **Suporte técnico** — via sistema de tickets, segunda a sexta, 8h–18h
* **Atualizações contínuas** — novas funcionalidades e correções enquanto a licença estiver ativa

**Prazo de instalação pela equipe:** 2 a 5 dias úteis após agendamento e envio das credenciais da servidor em nuvem e do domínio. Se preferir mais agilidade, o auto-instalador está disponível com download liberado imediatamente após confirmação do pagamento.

[→ Termos e Condições de Uso](/diretrizes-e-politicas/termos-e-condicoes-gerais-de-uso-e-licenciamento)
[→ Política de Suporte Técnico](/diretrizes-e-politicas/politica-de-suporte-tecnico)

---

### Planos disponíveis

Plano

Para quem

O que inclui

**Uso Próprio**

Quem quer centralizar o próprio atendimento

1 conta (tenant), canais e usuários ilimitados, todos os recursos operacionais

**cliente final (SaaS / plataforma de atendimento)**

Quem quer criar um negócio de software e revender para clientes

Tudo do Uso Próprio + Painel Super Admin para múltiplas contas, plataforma de atendimento com sua marca, integração com gateway de pagamento (Asaas)

**A principal diferença:** o Uso Próprio centraliza o atendimento em uma única conta. O plano de cliente final (Multi-Tenant) permite criar contas isoladas para múltiplos clientes, separando a gestão e os números conectados de cada um. Ambos os planos não possuem limite de números e usuários.

[→ Ver valores e adquirir licença](https://prismabot.zdg.com.br/#oferta)

#### Como funciona a cliente final (plataforma de atendimento)

Com o Plano cliente final, você:

1. Instala o Prismabot no seu servidor com a sua própria marca (logo, cores, domínio)
2. Acessa o Painel Super Admin e cria contas isoladas (**tenants**) para cada cliente
3. Define os recursos e os limites disponíveis para cada conta
4. Revende os acessos com sua marca — o nome Prismabot não aparece para o seu cliente final
5. Integra com o gateway Asaas para cobrar seus clientes automaticamente

A estratégia de preços é 100% sua.

[→ Como aplicar o plataforma de atendimento na prática](/configuracao-superadmin/tenants-e-licenca/artigo-usando-o-plataforma de atendimento-para-varios-clientes)

---

### Servidor (servidor em nuvem) e responsabilidades

**O Prismabot é gerenciado em nuvem.** Você contrata e mantém o servidor (servidor em nuvem) onde o sistema roda. A servidor em nuvem não está inclusa na licença — é um custo de infraestrutura seu, pago diretamente ao provedor de hospedagem.

**Suas responsabilidades:**

* Contratar e manter o servidor online com recursos adequados
* Gerenciar firewall, segurança e controle de acesso
* Executar rotinas de backup
* Aplicar as atualizações do Prismabot no seu ambiente

**Responsabilidades do Prismabot:**

* Fornecer o software funcional e atualizado
* Realizar a instalação inicial no seu servidor
* Prestar suporte técnico focado no funcionamento da plataforma

[→ Pré-requisitos de instalação (especificações mínimas da servidor em nuvem)](/diretrizes-e-politicas/pre-requisitos-de-instalacao-e-utilizacao)

---

### Canais suportados

* **WhatsApp** — API Oficial (WABA) ou APIs não oficiais (Baileys, Evolution, Wuzapi, Z-API, Uazapi, WebJs)
* **Instagram Direct e Facebook Messenger** — integração nativa ou via Hub NotificaMe
* **Webchat** — widget para embutir no seu site
* **E-mail** — integração com Gmail via OAuth2
* **Telegram** — via bot nativo
* **Voz / SIP** — ligações via WhatsApp (Wavoip) ou integração com PABX via protocolo SIP

[→ API Oficial vs. APIs Não Oficiais — qual escolher](/diretrizes-e-politicas/api-oficial-vs-api-nao-oficial)

---

### Automação, IA e integrações

**Chatbot nativo (ChatFlow):** construtor visual interno para criar fluxos automáticos sem ferramentas adicionais.

**IAs suportadas:** ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Grok (xAI), Deepseek, Qwen — e modelos gerenciado em nuvem via Ollama e LM Studio. Basta inserir sua chave de API.

**Integração com sistemas externos:** o Prismabot pode se conectar a outros sistemas de duas formas:

1. **API própria documentada** — rotas disponíveis via Postman para integrações personalizadas com CRMs, ERPs e outros sistemas:
   [→ Ver documentação da API (Postman)](https://www.postman.com/comunidade-zdg/prismabot/collection/s16subg/postman-v3?action=share&creator=25151510)
2. **N8N** — crie automações no N8N e integre ao Prismabot para que o fluxo seja consumido dentro do canal desejado (WhatsApp, Instagram etc.)

A viabilidade de uma integração específica deve ser avaliada por você ou por alguém da sua equipe técnica. O Prismabot não realiza o serviço de desenvolvimento de integrações personalizadas — a construção e a manutenção da conexão são de responsabilidade do assinante.

---

### Custos além da licença

O valor pago ao Prismabot refere-se à licença de uso do software, à instalação inicial, ao suporte e às atualizações no período. Custos adicionais são pagos diretamente aos respectivos provedores:

**Obrigatórios:**

* Servidor (servidor em nuvem) e domínio

**Variáveis (conforme o que você usar):**

* API Oficial do WhatsApp — cobrada pela Meta por janela de conversa
* Tokens de IA (OpenAI, Google, Anthropic etc.)
* Ferramentas externas como N8N, Typebot, Hub NotificaMe

O investimento total dependerá das suas escolhas de ferramentas complementares.

---

### Perguntas frequentes

**A licença é mensal ou anual?**
Anual. O modelo cobre os custos de setup, instalação e horas técnicas dedicadas da nossa equipe.

**Posso testar antes de comprar?**
Sim. Liberamos 7 dias de acesso em um ambiente de demonstração. Solicite pelo canal comercial: <https://zdg.dev.br/contato>

**Há limite de usuários, conexões ou disparos?**
Não. O Prismabot não impõe limites de software. A capacidade depende dos recursos do seu servidor (servidor em nuvem).

**O suporte atende pelo WhatsApp ou faz reuniões?**
Não. O suporte opera exclusivamente por sistema de tickets (segunda a sexta, 8h–18h). Não há atendimento via WhatsApp, call ou consultoria.

**O que o suporte cobre?**
Bugs e falhas nativas da plataforma, dúvidas sobre funcionalidades do Prismabot e auxílio na instalação inicial. **Não cobre** criação de fluxos de chatbot, configuração de ferramentas externas nem problemas de infraestrutura do servidor.
→ Escopo completo da Política de Suporte

**Quanto posso cobrar dos meus clientes?**
A estratégia de preços é 100% sua. O Prismabot não define nem limita o quanto você cobra para revender o serviço.

**O código-fonte é aberto?**
O front-end é acessível e customizável. O back-end é fechado — isso garante a integridade e a segurança contínua da plataforma.

---

### Próximo passo

**Quero testar:** solicite 7 dias de demonstração pelo WhatsApp comercial: <https://zdg.dev.br/contato>

**Quero comprar:** veja os planos e adquira a licença: [prismabot.zdg.com.br](https://prismabot.zdg.com.br/#oferta)

**Já comprei:** acesse o guia com os primeiros passos: → Onboarding para Novos Assinantes

[→ Política de Privacidade](/diretrizes-e-politicas/aviso-de-privacidade)

[AnteriorCentral de Ajuda Prismabot](/)[PróximoDiretrizes e Políticas](/diretrizes-e-politicas)

Atualizado há 1 mês

Isto foi útil?