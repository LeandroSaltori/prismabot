# API Oficial vs API Não Oficial

Comparação entre API Oficial (WABA) e APIs não oficiais (Baileys, wwebjs, Meow): estabilidade, riscos, custos e qual escolher para sua operação.

O Prismabot oferece a opção de conectar tanto para a API Oficial do WhatsApp quanto as opções de APIs Não Oficiais.

**Nossa recomendação técnica:** Recomendamos fortemente a utilização da **API Oficial (WABA)** devido à sua estabilidade, segurança e conformidade com as políticas da Meta. No entanto, deixamos a definição a critério do assinante. A escolha do método de conexão determina o equilíbrio entre custos operacionais, estabilidade do serviço e os riscos assumidos em relação às diretrizes da plataforma.

Abaixo, detalhamos as características operacionais, os requisitos e os riscos de cada modalidade.

---

### 1. API Oficial (WABA - WhatsApp Business API)

A API Oficial é a infraestrutura homologada, construída e mantida pela própria Meta (WhatsApp).

#### Métodos de Conexão no Prismabot

O Prismabot integra-se à API Oficial permitindo duas formas de configuração:

* **Via App Prismabot (Login Incorporado):** O usuário utiliza o aplicativo oficial da Prisma Telecom para realizar o login via Facebook e conectar o número de forma rápida.
* **Via App Próprio (Tech Provider):** O assinante cria e aprova seu próprio aplicativo no painel *Facebook Developers*. Indicado para operações plataforma de atendimento, permitindo que seus clientes façam o login visualizando a sua marca.

#### Coexistência

O sistema suporta o recurso de **Coexistência** através do método de "Dispositivos Conectados" da Meta. Isso permite que o número funcione simultaneamente no painel do Prismabot e no aplicativo WhatsApp Business no smartphone.

#### Gerenciamento, Pagamentos e Aprovação

* **Vínculo Comercial:** O número conectado permanece vinculado ao **Gerenciador de Negócios (Business Manager - BM)** do cliente (ou do seu tenant).
* **Custos:** O Prismabot não cobra taxas por mensagem. A cobrança é feita diretamente pela Meta na BM do cliente, baseada em "janelas de conversas" de 24 horas (após a cota gratuita mensal).
* **Aprovação:** A utilização exige a verificação da empresa e a aprovação do número pelas políticas de comércio e mensageria da Meta.

#### Diretrizes e Risco de Bloqueio

É fundamental compreender a dinâmica de bloqueios na API Oficial: O bloqueio de números não tem relação com o sistema utilizado (Prismabot), mas sim com as regras da Meta. A API Oficial elimina o risco de banimento por "uso de software não autorizado". No entanto, **o número continua sujeito às avaliações de qualidade da Meta.** A conformidade, a ausência de spam e a qualidade do atendimento não dependem da ferramenta, mas exclusivamente do cumprimento rigoroso das políticas do WhatsApp por parte do usuário.

---

### 2. APIs Não Oficiais

As APIs Não Oficiais são métodos alternativos que emulam o comportamento do WhatsApp Web ou Mobile, geralmente através da leitura de um QR Code. Elas isentam o usuário do custo por mensagem da Meta, mas transferem a responsabilidade da estabilidade para o administrador da infraestrutura.

#### Tipos de APIs Não Oficiais Suportadas

1. **Nativas (Baileys e WWebJS):** Bibliotecas integradas ao código do Prismabot. A conexão é feita diretamente pelo painel através da leitura do QR Code. Não há custos adicionais.
2. **Auto-hospedadas / em nuvem (Ex: Evolution API, Wuzapi):** Aplicações externas de código aberto instaladas e mantidas pelo próprio usuário em um servidor à parte, integradas ao Prismabot via credenciais (Host/Token).
3. **Gerenciadas / Pagas (Ex: Z-API, Uazapi):** Serviços terceirizados fornecidos por outras empresas (SaaS) mediante pagamento de mensalidade. A empresa terceira gerencia a estabilidade do roteamento.

#### Riscos e Responsabilidades Operacionais

Conforme estabelecido nos **Termos e Condições de Uso**, o Prismabot não garante estabilidade (SLA) para conexões realizadas por vias não oficiais e não se responsabiliza por desconexões ou perda de dados.

* **O WhatsApp não tolera SPAM:** Disparos em massa ou mensagens não solicitadas via API não oficial têm altíssima probabilidade de resultar em banimento permanente do número, sem possibilidade de recurso.
* **Riscos de Infraestrutura e IP:** Conectar múltiplos números não oficiais em um único IP (a nuvem) caracteriza comportamento automatizado anômalo. Se a Meta identificar e marcar a infraestrutura, ocorrerá um **bloqueio em cascata**, desconectando ou banindo todos os números de todos os clientes hospedados naquele servidor simultaneamente.
* **Recomendações Técnicas:** Para minimizar riscos, evite disparos em massa. Se operar em escala com múltiplos clientes (SaaS), considere a distribuição horizontal (múltiplos servidores) ou a configuração de proxies dedicados para isolar conexões.
* **Aviso "Aguardando mensagem":** Em conexões não oficiais (especialmente em emulações Web), a sincronização da criptografia de ponta a ponta pode falhar se o aparelho celular principal perder a conexão com a internet. Isso gera o aviso de "Aguardando mensagem". Para o funcionamento correto, o smartphone base deve permanecer ligado, com internet estável e o aplicativo do WhatsApp ativo em segundo plano.

---

### ❓ Perguntas Frequentes (FAQ)

**1. O Prismabot cobra alguma taxa sobre as mensagens enviadas na API Oficial?** Não. O valor pago ao Prismabot refere-se apenas à licença do software. Todos os custos referentes ao tráfego de mensagens na API Oficial são faturados e cobrados diretamente pela Meta no cartão de crédito cadastrado na sua Business Manager.

**2. A API Oficial garante que meu número nunca será bloqueado?** Não. A API Oficial impede bloqueios por "uso de software de terceiros não autorizado". Contudo, se a operação violar as Políticas de Mensageria e Comércio do WhatsApp (ex: envio de SPAM, denúncias de usuários, quebra de regras), a Meta poderá rebaixar a qualidade e banir o número de forma administrativa.

**3. Se a API Oficial é mais segura, por que as opções não oficiais existem?** Para oferecer flexibilidade. Usuários em fase de validação, operações com baixíssimo volume de mensagens ou que aceitam assumir os riscos técnicos e de banimento optam pelas vias não oficiais para evitar o custo por conversa cobrado pela Meta.

**4. A conexão não oficial desconectou. O suporte do Prismabot pode resolver?** Desconexões em APIs não oficiais nativas ocorrem devido a atualizações nos protocolos do WhatsApp. A resolução exige a releitura do QR Code e a garantia de que o celular hospedeiro possui conexão estável. Em casos de quebra estrutural (atualizações massivas da Meta), o Prismabot lança patches corretivos de software, mas não atua individualmente na restauração de sessões.



 2 meses
