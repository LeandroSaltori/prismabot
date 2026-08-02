# API Oficial WABA

Tudo sobre a API Oficial do WhatsApp (WABA) no Prismabot: como funciona, formas de conectar, templates HSM, custos Meta e recursos exclusivos.

O Prismabot possui integração nativa com a **API Oficial do WhatsApp (WABA)**, mantida e homologada pela Meta. O Prismabot é um **Tech Provider certificado pela Meta**, o que permite que assinantes conectem números de WhatsApp Business por meio do aplicativo da Prisma Telecom, sem necessidade de criar um App próprio.

Para quem já possui um App aprovado no Facebook Developers, o Prismabot também oferece suporte à integração via App próprio.

**Custos da API Oficial:** os custos de uso da API Oficial (cobranças por conversas fora da janela de 24 horas) são faturados diretamente pela Meta na **Business Manager (BM) do número conectado**. O pagamento dessas taxas é responsabilidade do assinante. O Prismabot cobra exclusivamente a licença do software. Veja mais em [Cobranças da Meta.](api-oficial-waba/cobrancas-da-meta-whatsapp-business-platform.md)

**Risco de bloqueio:** o uso da API Oficial elimina o risco de banimento por uso de software não autorizado. No entanto, o número ainda está sujeito às avaliações de qualidade da Meta — bloqueios por envio de spam ou violação das políticas de mensageria são de responsabilidade do operador, independentemente da ferramenta utilizada. Siga sempre as [diretrizes da Meta](https://www.whatsapp.com/legal/business-policy/).

---

### Como o Prismabot conecta na API Oficial

Ao conectar pela API Oficial, o número passa a operar em **modo de coexistência**: funciona simultaneamente no aplicativo WhatsApp Business do celular e no painel do Prismabot. A conexão utiliza a arquitetura de "Dispositivos Conectados" da Meta — o processo inclui leitura de QR Code no celular, de forma semelhante ao WhatsApp Web.

Há duas opções de integração disponíveis:

---

#### Opção 1 — Via App Prismabot (usando o App da Prisma Telecom como Tech Provider)

O Prismabot disponibiliza seu próprio App (aprovado como Tech Provider na Meta) para que assinantes façam a conexão OAuth diretamente pelo painel, sem precisar de um App próprio.

**Como funciona:**

1. No painel, acesse **Canais → Adicionar Canal → WhatsApp OAuth**
2. Selecione o aplicativo da Prisma Telecom
3. Faça login com o Facebook, selecione a conta WhatsApp Business e escaneie o QR Code no celular
4. O número fica conectado em modo de coexistência

Ao conectar pelo App da Prisma Telecom, a permissão de **ligações de voz** (`calls`) já está aprovada automaticamente.

Números com alto índice de denúncias (status Red na Meta) podem ser desconectados do App compartilhado da Prisma Telecom para proteger os demais assinantes. 
**Tutorial completo:** [WhatsApp Oficial OAuth (login)](configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/whatsapp-oficial-oauth-app-prismabot-com-coexistencia.md)

---

#### Opção 2 — Via App Próprio (para quem já tem um App aprovado na Meta)

Assinantes que já possuem um App aprovado no Facebook Developers — ou que desejam criar um — podem integrar o Prismabot usando as próprias credenciais. Nesse caso, o login incorporado exibe a marca do assinante (não a Prisma Telecom) para os usuários finais.

**O que é necessário:**

* App criado e aprovado no Facebook Developers com status de Tech Provider
* Configuração do App no painel Administrador

O processo de App Review da Meta exige envio de documentos e vídeos demonstrativos. O suporte do Prismabot não realiza esse processo, mas pode indicar profissionais especializados.

**Tutorial completo:** [Cadastro Incorporado e Coexistência com App Próprio](api-oficial-waba/whatsapp-oficial-cadastro-incorporado-e-coexistencia-com-app-proprio.md)


---

### Vocabulário essencial

Termo

O que significa

**WABA**

WhatsApp Business API — a API Oficial mantida e homologada pela Meta

**Tech Provider**

Empresa certificada pela Meta para fornecer soluções WABA a terceiros. O Prismabot tem esse status

**OAuth / Cadastro Incorporado**

Tecnologia de conexão via login do Facebook — vincula o número ao sistema sem configuração manual de webhooks

**Coexistência**

O número funciona simultaneamente no app do celular e no painel do Prismabot

**Business Manager (BM)**

Painel da Meta onde a empresa gerencia contas, ativos e métodos de pagamento

**Template (HSM)**

Mensagem pré-aprovada pela Meta para iniciar conversas fora da janela de 24 horas

**APIs não oficiais também são suportadas.** O Prismabot permite conexão via QR Code por APIs não oficiais (Baileys, Evolution API, Z-API, entre outras). Cada modalidade tem características e riscos distintos. Veja: [API Oficial vs. APIs Não Oficiais](diretrizes-e-politicas/api-oficial-vs-api-nao-oficial.md)

---

### Documentação por área

#### Conectar e gerenciar o canal

* [WhatsApp Oficial OAuth (login com coexistência)](configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/whatsapp-oficial-oauth-app-prismabot-com-coexistencia.md): passo a passo para conectar um número em modo de coexistência usando o App da Prisma Telecom
* [Integrações Meta — configurações do canal](configuracao-administrador/configuracao/integracoes-meta.md): painel de configurações do canal após a conexão: webhook, roteamento de chamadas, número de teste e outras opções
* [Contas WhatsApp na Meta](configuracao-administrador/configuracao/integracoes-meta/whatsapp-contas-meta.md) — visualização e gestão dos números WABA vinculados à Business Manager

#### Templates e disparos

* [Gerenciar Templates HSM](configuracao-administrador/configuracao/integracoes-meta/templates-integracoes-meta.md) — criação, edição e aprovação de templates de mensagem na Meta diretamente pelo painel
* [Envio em Massa — Template API Oficial](ferramentas-do-atendimento/comunicacao-e-marketing/envio-em-massa/envio-em-massa-template-api-oficial.md) — disparo em massa usando um template fixo para uma lista de contatos
* [Envio em Massa — Template com Variáveis](ferramentas-do-atendimento/comunicacao-e-marketing/envio-em-massa/envio-em-massa-template-variavel-api-oficial.md) — disparo em massa com preenchimento dinâmico de variáveis do template por contato

#### Atendimento com canal WABA

* [Painel de atendimento — recursos exclusivos WABA](ferramentas-do-atendimento/atendimento/tela-de-atendimento/atendimento-waba-api-oficial.md) — funcionalidades disponíveis na tela de atendimento para canais API Oficial: reações, edição de mensagens, templates e ligações

#### Ligações de voz

* [Ligações de voz na API Oficial (WABA)](api-oficial-waba/ligacoes-de-voz-na-api-oficial-waba.md) — como ativar o recebimento de chamadas WebRTC, solicitar permissão de chamada para ligar, e configurar o roteamento entre atendentes

#### Rastreamento e integrações avançadas

* [Rastreamento de Conversões (Meta Pixel)](configuracao-administrador/configuracoes-painel-admin/integracoes/rastreamento-de-conversoes.md) — integração com o Meta Pixel para rastrear eventos de conversão originados em atendimentos via WABA
* [Exemplo de fluxo N8N + API Prismabot + WABA](api-oficial-waba/exemplo-de-fluxo-no-n8n-+-api-prismabot-+-waba.md) — exemplo prático de automação integrando N8N com a API do Prismabot em canais WABA

#### Cobrança da Meta

* [Como funciona a cobrança de mensagens na Meta](api-oficial-waba/cobrancas-da-meta-whatsapp-business-platform.md) — modelo de precificação por categorias de conversa, janela de 24 horas e como gerenciar o faturamento na Business Manager

---

### Perguntas frequentes

**O Prismabot cobra taxa por mensagem na API Oficial?** Não. O Prismabot cobra a licença do software. Os custos de uso do WhatsApp são faturados pela Meta diretamente na Business Manager do número conectado.

**A API Oficial elimina completamente o risco de bloqueio?** Elimina bloqueios por uso de software não autorizado. O número permanece sujeito às avaliações de qualidade da Meta: spam, violação de políticas e acúmulo de denúncias podem resultar em penalidades — independentemente da API utilizada.

**Posso manter o celular ativo e usar o Prismabot ao mesmo tempo?** Sim. O modo de coexistência permite que o número opere simultaneamente no app WhatsApp Business e no painel do Prismabot.

**Como oferecer a conexão WABA para os clientes da minha cliente com a minha marca?** É necessário criar e aprovar um App próprio no Facebook Developers. Veja a Opção 2 acima.



Atualizado há 1 mês

Isto foi útil?