Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Atualizações e Status do Prismabot](/central-do-assinante/atualizacoes-e-status-do-prismabot)

# Changelog (4.0.x última versão)

Notas de versão do Prismabot 4.0.x: novidades, correções e breaking changes de cada atualização. Leia antes de atualizar.

### Manter seu sistema atualizado é fundamental para a segurança, performance e acesso a novas funcionalidades.

### Para acompanhar as novas versões entre no [canal de avisos do Telegram](https://portal.zdg.com.br/270021-sistema-prismabot/5179500-links-termos-de-uso-e-informacoes-gerais)

[Aula - Atualização Passo a Passo](https://portal.zdg.com.br/270021-sistema-prismabot/5179468-atualizacao-automatica-via-terminal)

**AVISO: FAÇA UM SNAPSHOT DO SERVIDOR**

Antes de iniciar qualquer procedimento de atualização, é **mandatório** criar um **snapshot** (um ponto de restauração) do seu servidor VPS.

Um snapshot é a sua única garantia de que poderá reverter o sistema ao estado anterior de forma rápida e segura em caso de qualquer falha ou imprevisto durante o processo de atualização.

---

## Última Versão

---

### v4.0.3

#### 🚀 UPDATE OFICIAL (HOMOLOG) | 24/07/2026

#### ⚠️ BREAKING CHANGE — Assistente OpenAI

* **Novo motor Responses:** tickets novos passam a usar o motor Responses automaticamente; tickets em andamento com thread ativa continuam no motor legado até serem fechados. A partir de **01/08**, toda seleção de threads posta um aviso no ticket; em **26/08** o cutover é forçado (thread zerada, histórico re-semeado a partir da tabela de mensagens, resposta na mesma mensagem). A seleção do **Motor de IA (Assistente OpenAI)** fica em Configurações Gerais.

#### 💬 Atendimento e Tickets

* **Encerramento por inatividade configurável por canal** — escolha e ordene o que enviar (mensagem, arquivo ou pesquisa de avaliação) e decida se, ao final, o atendimento é encerrado ou devolvido ao robô.
* **Distribuição automática:** o robô/assistente de IA agora é encerrado no momento da atribuição ao atendente (quando a opção está ativa na conexão ou na empresa), evitando que o bot continue respondendo junto com o operador.
* **Reabertura automática com destino configurável** — a conversa pode voltar para o mesmo atendente, quem encerrou, uma fila, um atendente fixo ou um chatbot. Definível no padrão geral do sistema, como passo do fluxo do chatbot ou manualmente por atendimento. Cliente que responde dentro do prazo não passa mais pelo menu inicial do robô.
* **Painel de Atendimentos em tempo real** — encerrados (inclusive por robô/IA) saem da tela na hora e novos pendentes aparecem sem apertar F5; o filtro por data virou opcional (por padrão mostra a operação ao vivo). Supervisores passam a ver apenas os atendimentos das filas sob sua responsabilidade.
* **Verificar conversa em outros canais:** avisa quando o contato já possui atendimento aberto ou pendente em outro canal do tenant — nas conversas (Nova Conversa, Contatos, Kanban e Pendentes) exibe aviso; no Disparo em Massa notifica o atendente responsável. Nunca bloqueia o envio, a criação do atendimento nem o disparo.
* Nova opção **"Permitir mensagem duplicada entre canais"** — com dois canais no mesmo grupo ou conversando entre si, a mensagem aparece no atendimento de cada canal.
* **Busca de mensagens** agora navega entre todas as ocorrências do termo (próxima/anterior) com contador de resultados, incluindo mensagens antigas do histórico.
* **Respostas rápidas:** navegação com as setas ↑↓ do teclado e seleção com Enter.
* **Indicador de carregamento** ao abrir a conversa (aviso extra em grupos, que têm histórico maior); **espiar conversa** ganhou limite de mensagens com botão "carregar anteriores".
* **Desempenho:** corrigida a lentidão na entrada de mensagens; envio e recebimento de vídeos do iPhone (.mov) muito mais rápidos e leves — o servidor só reprocessa vídeo quando necessário e campanhas não reconvertem o arquivo a cada contato.
* **Z-API:** mensagens enviadas pelo celular conectado aparecem corretamente na conversa, mesmo quando o WhatsApp oculta o número do destinatário — conversas duplicadas criadas por esse problema são unificadas automaticamente.
* **PDF com impressão automática** (comum em faturas/2ª via) não abre mais o diálogo de imprimir sozinho — o comando é neutralizado na visualização e a pré-visualização carrega somente após um clique, mantendo o download do arquivo original intacto.
* **Notificações:** popup nativo do navegador para ticket novo em pendentes e opção de limitar notificação de chatbot (Configurações Gerais).
* Correção da duplicação de tickets e mensagens em canais híbridos (Uazapi, Evo, EvoGo, Wuzapi e Z-API).
* Listagem dos detalhes do ticket alinhada por última mensagem (`lastMessageAt`, com fallback para `updatedAt`).

#### 📊 Kanban e Funil

* Correção do toast de erro ao atualizar o Kanban de atendimento.
* Corrigido o disparo de **templates com variáveis e botões** nas ações automáticas do funil de oportunidades (erro "actionContent inválido"); a edição da ação agora recupera os valores preenchidos.

#### 🤖 Chatbot e Chatflow

* Correção da renderização da opção de **subfluxo** no Chatflow.
* **Telegram:** mensagens de despedida e de fechamento.

#### 📢 Campanhas e Disparo em Massa

* Com a verificação de conversas em outros canais ativa, contatos que já estão em atendimento ou aguardando **deixam de receber disparos** — o envio é pulado, os pulados aparecem no resumo e no relatório, e quem disparou recebe notificação com a lista. A API externa indica os pulados na resposta e permite ignorar a checagem por chamada.
* Cada usuário agora **só vê os canais liberados para o seu perfil** no envio em massa.
* Corrigida a prévia da última mensagem nos atendimentos (envios de mídia exibiam "Mensagem no Atendimento") e envios que falham não deixam mais atendimentos pendentes vazios — são removidos ao final do disparo.

#### 📱 Canais Oficiais Meta (WABA / Instagram / Messenger)

* **Modo híbrido (coexistência) WABA** — incluindo envio de mensagens de texto pela conexão vinculada mesmo após o fechamento da janela de 24h.
* **Projeção de custos de mensagens WABA** na configuração Meta.
* Limites da WABA aplicados ao tamanho dos inputs (botões, listas e templates) e correção do erro de "credenciais incompletas" ao criar template (exigia F5).
* Correções WABA/Meta: canal duplicado no re-onboarding, resolução número→canal prioriza a linha CONNECTED, envios com erro marcados e logados, app WABA próprio + OAuth Instagram, OAuth Facebook + Instagram em conjunto e login com Facebook preso em "Carregando SDK…".
* Assinatura com `*asterisco*` suprimida em canais não-WhatsApp.
* **Dialog360:** sanitização de payload e log de debug para coexistência via `DIALOG360_RAW_DUMP` (.env do backend). **Gupshup e Dialog360:** base64 no payload do n8n (canal).

#### 🔌 Integrações Não Oficiais (Baileys, EvoGo, Evolution, Uazapi, Meow)

* **Baileys:** recebimento de mensagens sem delay; estabilidade com armazenamento SQLite (reconexões não derrubam mais o backend e a religação automática não compete com reconexões em andamento); novas variáveis opcionais no `.env` do backend: `BAILEYS_PROFILEPIC_TIMEOUT_MS` (3000), `BAILEYS_ONWHATSAPP_TIMEOUT_MS` (5000), `BAILEYS_GROUPMETA_TIMEOUT_MS` (8000), `BAILEYS_GROUPFETCH_TIMEOUT_MS` (10000), `BAILEYS_SQLITE_CREDS_BACKUP_ENABLED=false` e `BAILEYS_LID_SEND=true`.
* Suporte ao **EvoGo** e à extensão **Passkey Linker** com Evolution 2 (depende do microserviço [evo-passkey-injector](https://github.com/pedroherpeto/evo-passkey-injector)).
* Mensagens editadas pelo cliente atualizam corretamente na conversa (Evolution, EvoGo e Meow — novo formato de edição do WhatsApp).
* **Uazapi:** correção da renderização de mídia de aniversário.

#### 🔗 API e Integrações Externas

* Correções: `/getMessagebyId` + `mediaUrl`; envio base64 com caption de mídia; disparo de ligações **Wavoip**.
* Nova rota para disparar a **pesquisa de avaliação** por ticket ou por número.

#### ⚙️ Superadmin, Planos e Pagamentos

* **Provisionamento de tenants via API** agora vincula assinaturas do Stripe, Pagar.me e Mercado Pago (além do Asaas), habilitando a atualização automática de status de pagamento por webhook.
* **Migração de tenants para o gateway global** (Stripe/Mercado Pago) direto na tela de Planos, com criação automática do cliente; corrigido o gateway efetivo que mantinha o tenant no Asaas após a troca (signup, troca de plano e leitura de faturas).
* Correções no faturamento: exibição do plano na lista de tenants e fluxo de cobrança Stripe no cadastro — novo cliente vai direto para a fatura, e contas bloqueadas conseguem ver as faturas e revalidar o pagamento para desbloquear o acesso.
* Opções dos planos do signup refletidas na tela de tenants; **agendamento público** e **motivos de pausa** adicionados à configuração de visibilidade de tenants/planos.
* **Assinatura:** a seção de pontuação do Score do App Tech Provider ganhou link "Guia completo" em popup; números banidos ou bloqueados de outra instalação da mesma licença podem ser bloqueados e removidos do monitor de score pela tela de assinatura — com desregistro real na Meta, consentimento detalhado em três etapas (incluindo reativação com PIN) e liberação do desbloqueio cortesia.

#### 👥 Contatos

* **Mesclagem de duplicatas em massa** (9º dígito/LID) por API, CSV e detecção automática aprimorada, com reversão segura de qualquer mesclagem. As ações Remover Duplicados, Agrupar LIDs e Verificar 9º Dígito preservam todo o histórico e exibem resumo dos contatos afetados; corrigidos o erro que impedia o Remover Duplicados de concluir e a busca via API que retornava cadastro vazio.
* **Fila no cadastro do contato** (como já existe com a carteira) — novos atendimentos entram automaticamente nela quando o direcionamento estiver ativado; filtro por fila, coluna Fila na listagem e fila na importação de contatos.
* Correção da importação inteligente com data de aniversário.

#### 📈 Relatórios, Dashboard e Avaliações

* Novos indicadores: **Tempo de Primeira Resposta (TPR)** e **Tempo Total de Espera (TTE)**; correção do Tempo de Espera, que agora conta a partir da atribuição ao atendente (inclusive na distribuição automática), eliminando os registros falsos de "0 min".
* **TMA** (Tempo Médio de Atendimento) e **TME** (Tempo Médio de 1ª Resposta) por atendente no Resumo de Atendimentos por Usuário, respeitando o escopo de filas do supervisor — disponível também nas exportações (Excel, CSV e impressão).
* **Avaliação:** o administrador define o que acontece após o envio da pesquisa — fechar na hora, manter aberto até o cliente responder, fechar automaticamente após alguns minutos ou perguntar ao atendente. A fila mostra indicador de "aguardando avaliação".
* Correção dos **filtros por período** em Avaliações, Conversões, Log de Ligações, Funil (Kanban), Auditoria e integrações externas — não cortam mais o último dia selecionado e voltam a trazer resultados ao filtrar um dia isolado.

#### 📅 Agendamento e Aniversários

* **Turmas/grupos no agendamento público:** um mesmo horário pode aceitar várias pessoas (vagas por horário), ideal para aulas e atendimentos em grupo — o portal mostra as vagas restantes. Cada serviço define se o limite diário conta alunos ou turmas e se as vagas são por profissional ou em turma única.
* Horários de trabalho repetidos não geram mais opções duplicadas na página de agendamento (cada horário aceita 1 reserva, salvo turmas).
* Detalhes do agendamento público exibidos no calendário da agenda.
* Menu Aniversários adicionado à configuração do perfil supervisor.

#### ✉️ E-mail

* Correção do envio de e-mail com AWS.

#### 🎨 Interface e Permissões

* Toasts de aviso agora aparecem no centro superior da tela; ajuste de resolução para iPads.
* **Perfis personalizados:** o editor de perfis ganhou os toggles de agendamentos e catálogo, e ações sem permissão mostram o aviso "Você não tem permissão" no lugar do botão que não reagia.
* **Tarefas:** corrigido o erro que impedia marcar tarefas como concluídas (lista, kanban e sininho de notificações) e criar tarefas sem descrição.

#### 🔧 Sistema e Infra

* Nova variável no `.env` do backend: `AUDIT_LOGS_RETENTION_DAYS` para definir a retenção dos logs de auditoria (padrão: 90 dias).
* **Instalador:** o modo cluster detecta automaticamente o usuário do PostgreSQL — corrige erros de dreno e de leitura de capacidade em servidores com usuário de banco personalizado.

---

## Versões anteriores

---

### v4.0.2

#### 🚀 UPDATE OFICIAL (HOMOLOG) | 02/07/2026

#### ⚠️ BREAKING CHANGE

* Bloqueio de transferência para canal não liberado ao usuário — passa a valer para interações manuais, chatbot e rotas de API externa.

#### ⚙️ Superadmin, Planos e Faturamento

* Catálogo de **preços de planos** e configurações de planos expandidas.
* Controle por tenant: **menus visíveis** e **quantidade de canais por tipo**.
* Listagem de **usuários** no Superadmin e correção na **edição de tenant**.
* **Trial** alinhado ao pagamento (gateway — cobrança inteligente).
* **Revalidação** de status de pagamento na tela de pagamento em atraso.
* Autoinstalador: **update all backends**.

#### 💬 Atendimento e Tickets

* **Filtro de atendimento** expandido para usuários comuns (`NotViewAssignedTickets` e `restrictedUser` deixam de aparecer) + status **"Fechados"** fica inativo quando "Incluir tickets fechados" está desmarcado.
* **Multiencaminhar flutuante** e **mensagens rápidas** com botão e lista.
* **Trava no botão de fechamento** (evita múltiplas ações) e **fechar forçado** em resolução de ticket (com avaliação automática) e em **tickets pendentes**.
* **Transferência sem fila**; correção na mensagem de transferência; ao remover convite, o ticket some.
* **Motivos de fechamento** com opção de definir **demanda automática**; forçar demanda ao resolver.
* Reações com **estado preservado**; marcação em grupos com `@`; editar contato liberado para **grupos**.
* **Manutenção de tickets** — filtro de etiquetas + novas mensagens recebidas.
* Exportar conversas / espiar / mini-CRM com **visualização alinhada ao histórico e permissões**.
* **Popup automático** para mensagens de sistema não lidas; despausar quando o cliente responder.

#### 📊 Kanban, Funil e Mini-CRM

* **Mini-CRM** nos cards de Kanban e Funil; **suporte a Kanban para todos os canais**.
* **Notificações por etapa** do funil e **log de ações** do funil.
* Uso de **variáveis** no funil de ação e em **ações com mídias**.
* Enviar mensagem de oportunidade com **filtragem por canais permitidos** ao usuário.
* **Google Calendar** no funil/oportunidade (botão + criação de evento).
* Filtro de **tag inativa** no Kanban.

#### 🤖 IA, Chatbot e Chatflow

* **Chatflow (estilo n8n):** conexão de bubbles, envio de **template**, **nó automático** (condição sem guardar resposta), **condição por variável**, **webhook avançado roteável**, captura de variável + webhook, criação de nota, disparo na **primeira interação** com o nó e correção da tabela de horários.
* **Chatbot:** Messenger e Instagram, horário de funcionamento próprio, destino **fora do horário** com fila null, bloquear chatbot em ticket pendente, `fromMe` na mensagem de transferência, correção de subfluxo e de botões no Instagram.
* **IA:** **Wizard de template com IA**, **GroqCloud** como Global Provider, relabel **apiKey × apiUrl** nas integrações, correção do botão de teste do Copiloto + IA customizada.

#### 📢 Campanhas e Disparo em Massa

* **Limite diário** de campanhas e opção de **criar mensagem** para campanha.
* Disparo em massa com **variável** `name` em templates e **aviso de números incompatíveis** (nono dígito).
* **Filtro por data** no relatório de disparos.

#### 📱 Canais Oficiais Meta (WABA / Instagram / Messenger)

* **WABA:** palavra-chave para **fechar atendimento**, filtro de template por **categoria**, **PDF (document)** em templates, **webhooks primário e secundários unificados**, **tabela de custos** com dimensions e totalizadores, transferência entre canais **fecha a janela de 24h**, `validateNumber` em rotas de API externa (ignora validação do nono dígito), ocultar mensagem da janela de 24h.
* **Instagram:** envio de template (inclusive imagem da galeria), **automações** no menu automação, correção de IGSID longos (>2^53) e de instagramPK longos.
* **Messenger:** mensagem de **utilidade**, mensagem de **despedida**.
* **Techprovider Google** definitivamente **depreciado** — mantido apenas o uso de app próprio.
* **Dialog360:** outbound de PDF + MOV. **Gupshup:** templates.

#### 🔌 Integrações Não Oficiais (Baileys, Uazapi, Evo, WWebJS, Passkey)

* **Baileys:** RC13/infinite (correção de grupos), suporte a **SQLite**, receber mensagem editada, ajustes de carrossel e **persistência de sessão**, timeout de consolidação de LID expandido, novas `.envs` avançadas (`BAILEYS_CONNECT_TIMEOUT_MS`, `BAILEYS_QUERY_TIMEOUT_MS`, `BAILEYS_KEEPALIVE_MS`).
* **Uazapi:** correção de desconexão, socket ao editar mensagem, mensagem de aniversário.
* **Evo:** envio/recebimento e render de mídias e áudios, recebimento de edição.
* **WWebJS:** envio com `@lid`.
* **Passkey:** importar sessões não oficiais e conexão com **Baileys, Meow e Uazapi**.

#### 🔗 Integrações Externas e API

* Expansão do uso da **API** para Messenger, Instagram e outros canais; novas rotas (`toDos`, `updateQueue` sem marcar como lido).
* **Community Nodes** para n8n (`n8n-nodes-prismabot` e `n8n-nodes-prismabot-admin`).
* Correção de envio via **Telegram** (API externa) e **extensão de suporte à API do TikTok**.

#### 🛒 E-commerce

* Integração **Nuvemshop (beta)**.
* Correção no envio de produtos (`ERR_OUTSIDE_24H_WINDOW`).

#### 👥 Contatos e Etiquetas

* **Busca inteligente de contatos** expandida a outras áreas da Prismabot.
* Criação de contato **sem canal WhatsApp** (Instagram/Messenger only).
* Listar **carteira**, exportação com filtros e correção de cidade/estado/CEP/CNPJ na visualização.
* **Etiquetas:** atualizar cor ao setar, tag em mensagem encaminhada.

#### 📈 Relatórios e Avaliações (NPS)

* Relatórios de **NPS**, **coluna de agente** nas avaliações, avaliação com **link externo**.
* Relatório de atendimento por parâmetros (dados do usuário); correção na exportação de histórico e no dashboard (filas + personalização).

#### 📅 Agendamento e Aniversários

* **Agendamento público multi-país**; reabrir/rotear ticket com mensagem agendada.
* **Aniversários:** normalização e revisão de datas, mensagem com data correta.

#### ✉️ E-mail (SMTP)

* **Assinatura** e **remetente** no e-mail, persistir corpo dos enviados, abrir link em **popup dedicado**, envio via Gmail com nome contendo `@` e expansão de dados SMTP (nome e usuário).

#### 🖼️ Mídias e Galeria

* **Quota** para a galeria e correção de galeria + templates (busca, listagem e uso).
* Recebimento de **PDF com acentos**.

#### 🎨 Interface, Notificações e Permissões

* **Notificações:** correção de HTML, limite sonoro em tickets de grupos.
* **Perfil customizado** habilitado para gerir tags; supervisor restrito ao canal; supervisão de chat privado sem limitação para admin/supervisor.
* Signup com máscara de **CPF/CNPJ**, cálculo de luminância no ícone do sidebar (hover), scroll em modais e seleção de tags, correção da ordem dos tickets, limite de listagem de tutoriais.

#### 🔧 Sistema e Infra

* **Listagem de backups**, `disableExternalIntegration` em conversa avulsa, auto-desligar integrações ao aceitar, ficar offline ao fechar a aba, ignorar horário de atendimento (expandido).

---

### v4.0.1

#### **🚀 UPDATE OFICIAL (HOMOLOG) | 26/05/2026**

#### ⚙️ Superadmin e Configurações

* Customização White-Label:

  + Tela de Signup padrão internacional (agora customizável).
  + Link do Postman (agora customizável).
  + Customização de cores para o Dark Mode.
  + Adicionada visualização prévia da tipografia.
* Global Providers: Liberado Global Provider para integrações da Meta.
* OAuth: Opção de usar o app padrão do Google OAuth liberada na edição do tenant pelo Superadmin.
* Gestão do Sistema e Usuários:

  + Opções de distribuição nas filas.
  + Novas configurações de restrição de usuários.
  + Compartilhamento de acesso por convite.
  + Link de reset de senha adicionado.
  + Controle de features na tela de configuração.
  + Adicionada a rotina 6 no autoinstalador.

#### 💬 Atendimento, Funil e Kanban

* Novas Regras de Operação e Tickets:

  + Configuração Receptivo apenas por fila: Quando ativado, os atendentes recebem tickets entrantes apenas com base nas filas atribuídas (sem exigir vínculo ao canal). Envios em Nova Conversa continuam exigindo o canal vinculado ao usuário.
  + Configuração Reabrir toma posse do atendimento: Quando ativado, reabrir um ticket finalizado por outro atendente atribui o ticket ao usuário que clicou em Reabrir, em vez de mantê-lo com o atendente anterior.
  + Transferir múltiplos tickets simultaneamente para as filas.
  + Fechar todos os tickets diretamente no painel de atendimento.
* Painel de Conversas:

  + Busca global de mensagens expandida no atendimento.
  + Filtro para buscar mensagem rápida pelo atalho.
  + Filtro "Mostrar todos" no painel de atendimento.
  + Correções de filtros (novas mensagens + combinação de filas).
  + Validação de existência de ticket antes de iniciar conversa avulsa.
* Kanban e Funil:

  + Visualizar conversa diretamente no card do Kanban.
  + Visualizar conversa diretamente no card do funil.
  + Reordenar etapas do funil.
  + Novo "Modo Monitor" de atendimento (Kanban).
  + Correção no filtro do Kanban.
* Notificações: "Sino" de notificações remodelado para separar: Tarefas + Mensagens Internas + Tutoriais. Aviso sonoro passou a respeitar os filtros. Adicionado aviso de erros para webpushs.
* Horários e Status:

  + Horário do usuário agora permite configurar intervalo (*range*).
  + O Superadmin foi excluído da regra de bloqueio de horário.
  + Adicionada opção de setar como Offline ao sair do sistema.
  + Status na abertura de conversa avulsa.
* Chat Privado (Interno): Adicionada chamada (ligação de áudio e vídeo) entre usuários. Ajustada a largura da tela do chat privado.
* Geral do Atendimento: Relatório de conversa exportável em PDF, botão imprimir em relatórios, scroll aprimorado nos logs do ticket, opção de editar contato dentro da tela de atendimento, listar usuários na tela de transferência, e mensagem opcional na transferência de fila.

#### 🤖 Inteligência Artificial e Chatbot

* Integração Dify: Os campos enviados agora devem estar dentro de inputs. No Dify (Studio → app → Variáveis de entrada), adicione as variáveis como `text-input` (opcionais):

  + `ticketId` (string) — `String(ticket.id)`
  + `tenantId` (string) — `String(ticket.tenantId)`
  + `contactNumber` (string) — `ticket.contact?.number ?? ""`
  + `whatsappId` (string) — `String(ticket.whatsappId ?? "")`
* Integração ChatGPT / Copilot: Suporte ao ChatGPT com `baseUrl` genérico (permite uso de LLMs genéricos). Copiloto agora atua na reescrita de mensagens e recebeu extensão de idioma.
* Funcionalidades do Fluxo:

  + Node condicional de dia/horário no chatbot.
  + Condição para transferência de canal.
  + Interação "Delay" (pausa) no chatbot.
  + Definição de audiência para o chatbot.
* Ações do Chatbot:

  + Iniciar chatbot avulso na transferência de atendimento.
  + Transferir chatbot (detalhes do atendimento).
  + Adicionada mensagem de transferência "fora do horário".
  + Legenda disponível para arquivos enviados via chatbot.
  + Fechamento automático de ticket inativo associado ao chatbot (reabertura/reaproveitamento de atendimento).

#### 📱 Integrações e Canais Oficiais (Meta)

* WhatsApp API Oficial (WABA):

  + Suporte a Grupos.
  + Disparo em massa via WABA com opção de definir fila/usuário.
  + Envio de mensagem agendada.
  + Variável de `body` + `header` para template WABA.
  + Suporte a "Palavra-gatilho" no botão.
  + Exclusão de templates WABA.
  + Adicionado webhook para o canal.
  + Controle e roteamento de ligações no WABA.
  + Layer de normalização do nono dígito.
  + Adicionado aviso de número pendente de PIN.
  + Correção no fluxo de adição manual do WABA.
* Redes Sociais: Suporte ao Facebook Page, e tela de diagnóstico de sessões otimizada para Instagram e Messenger.
* Novas Integrações (Beta): Gupshup e Dialog360. Inclusão de recebimento de mídia (inbound) e comando para desconectar/reconectar nesses provedores.

#### 🔌 Integrações e APIs Não Oficiais

* Motor Baileys: Atualizado para a versão `v7rc10`. O usuário agora tem opção de escolher entre: fork, rc10 ou infinite. Nova ferramenta adicionada para "Consolidar LIDs" no Baileys.
* Uazapi: Disparo em massa via arquivo. Recebimento de lista via Uazapi + n8n. Agendamento de mensagem via Uazapi contendo arquivos. Suporte a Grupos no Uazapi. O nome do arquivo recebido na integração foi corrigido.
* QR Codes: Adicionada leitura de QRCode para motores Z-API e Meow.
* WWebJS: Tratamento para início de conversa avulsa + correção de LID.

#### 🛒 E-commerce e Automação

* WooCommerce: Permite consumir os produtos do e-commerce direto na conversa e enviar mensagem vinculada a um pedido específico.
* Telefonia: SIP UDP Bridge.
* ADS: Trackeamento de erros nas conversões de ADS.

#### 🛠️ Melhorias Técnicas e Correções Gerais

* Contatos e Etiquetas: Listagem de etiquetas inativas. Opção para deletar etiqueta que já foi atribuída. Detalhes de contato agora mostra protocolos/avaliações. Correção na importação de contatos via CSV.
* Mídias e Anexos: Limite no carregamento de mídias na Galeria. Paginamento e busca integrados na Galeria. Correção no apontamento de mídia no Storage do frontend. Opção de rolar mídias ao criar template na galeria. Adicionado suporte a colar vídeo Screencast com `Ctrl+V` no atendimento.
* Tickets: Rotina para mover tickets órfãos (whatsapp deletado) para o status `closed`. Correção na funcionalidade de Pause de ticket.
* Sistema e Interface: Truncate (corte) do nome do canal na tela. Contador de não lidas na aba pendentes. Contador de mensagens em grupo. Normalização BR (nono dígito) tornou-se opcional para envio de mensagem avulsa.
* Correções pontuais: Erro de CORS do widget de webchat (quando incorporado em outros sites). Correção ao usar número de teste no chatflow. AutoReassign liberado na edição do canal. Correção ao editar número de telefone. Linguagem padrão para leitura de imagens via IA ajustada.

---

### v4.0.0

**🚀 UPDATE OFICIAL (HOMOLOG) | 04/05/2026**

⚛️ Novo front end React Next.js - interface mais rápida e moderna
🔗 Integrações nativas com [Instagram, Facebook](/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/instagram-e-facebook-messenger-via-oauth-login) e [WhatsApp API oficial](/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/whatsapp-oficial-oauth-app-prismabot-com-coexistencia) - Oauth próprio do Prismabot
🤖 [Copiloto de I.A](/configuracao-administrador/configuracoes-painel-admin/bots-e-ia/copiloto-de-ia) - Resumos, sugestões de respostas, análises de sentimento...
📱 Novos canais - Mercado Livre, Woocommerce, OLX, Tiktok, Youtube, Linkedin, Rocket.Chat
📈 Rastreamento de conversões Pixel Meta e Google GA4
🎧 Novos recursos de [atendimento](/configuracao-administrador/gestao-comercial/analises-e-registros/painel-de-atendimentos)
👤 [Perfil personalizado de usuários](/configuracao-administrador/administracao-painel-admin/usuarios/perfis-de-acesso)
🔌 Novos [Endpoints API](/central-do-assinante/referencia-da-api)
🎨 [Personalizações](/configuracao-superadmin/configuracoes/customizar-white-label)
☁️ Armazenamento externo ([Storage AmazonS3](/configuracao-superadmin/sistema/sistema-dados-e-configuracao/storage-s3), etc)
⚡️ [Autoinstalador melhorado](https://portal.zdg.com.br/270021-sistema-prismabot/5179464-instalacao-automatica-prismabot-pacote-ultima-versao)
💳 Novos gateways de pagamento (stripe, mercadopago, etc)
🚀 Modo Cluster - Infraestrutura para escala com múltiplos núcleos de processamento
📧 Integração com [SMTP](/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/e-mail-imap-smtp) para envio e recebimento de email nos tickets
✨ Recursos premium baileys / uazapi - botões, listas, etc

### Histórico das versões antigas (antes da v4.0)

Nas páginas seguintes você encontra o histórico completo das versões anteriores.

[AnteriorAtualizações e Status do Prismabot](/central-do-assinante/atualizacoes-e-status-do-prismabot)[Próximo3.1.5.x](/central-do-assinante/atualizacoes-e-status-do-prismabot/changelog-4.0.x-ultima-versao/3.1.5.x)

Atualizado há 8 dias

Isto foi útil?