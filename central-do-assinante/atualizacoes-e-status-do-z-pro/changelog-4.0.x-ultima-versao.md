Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Atualizações e Status do Prismabot](/central-do-assinante/atualizacoes-e-status-do-z-pro)

# Changelog (4.0.x última versão)

Notas de versão do Prismabot 4.0.x: novidades, correções e breaking changes de cada atualização. Leia antes de atualizar.

### Manter seu sistema atualizado é fundamental para a segurança, performance e acesso a novas funcionalidades.

### Para acompanhar as novas versões entre no [canal de avisos do Telegram](https://prismatelecomservicos.com/ rel=)

[Aula - Atualização Passo a Passo](https://prismatelecomservicos.com/ rel=)

**AVISO: FAÇA UM SNAPSHOT DO SERVIDOR**

Antes de iniciar qualquer procedimento de atualização, é **mandatório** criar um **snapshot** (um ponto de restauração) do seu servidor servidor em nuvem.

Um snapshot é a sua única garantia de que poderá reverter o sistema ao estado anterior de forma rápida e segura em caso de qualquer falha ou imprevisto durante o processo de atualização.

---

## Última Versão

### v4.0.4

**🚀 UPDATE OFICIAL (HOMOLOG) | 17/08/2026**

Esta versão altera **permissões, visibilidade de atendimentos e regras de criação de usuários** — inclusive na API. Os detalhes estão explicados abaixo.

**⚠️ BREAKING CHANGE — Permissões, visibilidade e segurança**

As notificações agora seguem **exatamente** as mesmas permissões da tela de Atendimentos: o usuário só recebe avisos de conversas que pode abrir. A segurança no servidor também foi reforçada — atendimentos fora do alcance do usuário não podem mais ser abertos nem respondidos por link direto.

**O que muda no comportamento atual**

* **Criação de usuários:** agora exige permissão de gestão e não permite criar perfil superior ao próprio. **Scripts que criavam usuários com credencial comum podem parar de funcionar.**
* **API:** não cria mais contas de nível plataforma. Administrador, supervisor, atendente e perfil personalizado continuam funcionando normalmente.
* **Edição do próprio cadastro:** usuários sem permissão de gestão não podem mais alterar filas, canais, horário, e-mail, senha e outras configurações do próprio cadastro.
* **Canais:** usuários com canais definidos acessam somente esses canais — o servidor também bloqueia o acesso direto aos demais.
* **Visualização por Departamento:** agora é validada no servidor. Supervisor restrito não acessa outra fila por link direto; supervisor sem fila definida continua sem restrição.
* **Conversas do robô:** ficam ocultas apenas enquanto estão com o robô. Após o encaminhamento para uma fila, voltam a aparecer.
* **Carteira:** o dono da carteira volta a visualizar e a receber avisos dos atendimentos do contato.

**Regras por perfil**

Perfil

Situação

O que passa a ver

**Supervisor**

Sem restrições

Vê tudo.

Com departamento + filas

Apenas suas filas, além dos próprios atendimentos, convites e grupos.

Sem filas definidas

Sem restrição.

Com restrição de canal

Apenas os canais atribuídos.

**Atendente**

Com filas

Suas filas + atendimentos próprios, convites, carteira e grupos.

Sem filas

Continua vendo os atendimentos não atribuídos.

Sem canais definidos

Todos os canais.

Com canais definidos

Somente esses canais.

**Administrador / Plataforma**

Uso normal

Nada muda: acesso completo aos atendimentos.

**Perfil personalizado**

Com acesso total

Mantém a visão completa.

Sem acesso total

Segue as regras de fila e canal.

**Dois detalhes importantes:** o supervisor **não pode mais alterar a própria "Visualização por Departamento"**, e o atendimento próprio do atendente continua acessível mesmo se o canal for excluído.

**Correções ligadas a permissões**

* Corrigido o "acesso restrito" ao clicar em notificações.
* Convites removidos deixam de gerar avisos.
* Alterações de permissões passam a valer em até 30 segundos.
* Corrigido o alerta duplicado em Nuvemshop e WooCommerce.
* As telas de usuário não oferecem mais opções que o servidor vai recusar.
* Permissões de menu escolhidas na criação do usuário agora são salvas corretamente — antes o usuário era criado com todos os menus liberados. O horário de atendimento definido na criação também passa a ser respeitado.
* Corrigido o erro ao salvar a edição do próprio cadastro (nome, e-mail, telefone) — perfil e permissões agora aparecem bloqueados para o próprio usuário, com aviso.
* Atendentes sem restrição de conexão voltam a receber notificações push, e a redistribuição automática passa a considerar corretamente quem pode ver o número.

**⚠️ BREAKING CHANGE — Perfis personalizados**

* **Entram no roteamento automático.** Antes eram invisíveis para o bot e para a distribuição de fila — nunca recebiam atendimento automático. Se você modelou um perfil personalizado de supervisão, essas pessoas passam a receber atendimento.
* **Ações que exigem marcar uma nova permissão** no perfil personalizado (sem ela, param de funcionar): criar, editar e excluir canal — inclusive o Login com Facebook — → **Gerenciar sessões**; salvar qualquer configuração da empresa → **Configurações gerais**; salvar horário de atendimento e feriados → **Gerenciar horários**; marcar todos como não lidos → **Atribuir atendimentos**.
* **Agenda:** a página passou a ser limitada pela capability **agenda** do plano, e não mais por `funnelKanban`. Um plano que tenha Funil mas não Agenda passa a bloquear a Agenda — antes ela entrava de carona.
* Perfis personalizados agora funcionam de ponta a ponta em Integração Meta, Dashboard, Campanhas e Configurações, e a tela de perfis passou a avisar quando falta marcar a permissão que a página exige.

**⚠️ BREAKING CHANGE — Eventos do painel em tempo real**

* **Payload enxuto:** os eventos do painel passam a chegar com dados reduzidos — menos consumo de banda e mais velocidade, especialmente em equipes grandes. Se você tem integração lendo os eventos do socket, revise os campos utilizados.

**💬 Atendimento e Tickets**

* **Mais confiável e rápido:** mensagens que falham não somem mais e podem ser reenviadas com um clique, o upload de arquivos mostra progresso e novos atalhos de teclado agilizam o dia a dia.
* **Colar arquivos com Ctrl+V** no atendimento — PDF, Word, Excel e outros documentos, além de imagens e vídeos.
* **Reabertura com aviso de duplicidade:** ao reabrir um atendimento encerrado, o sistema avisa se o contato já tem uma conversa em andamento (no mesmo canal ou em outro), para quem o atendimento vai e se a janela de 24 horas está fechada — antes de criar um atendimento duplicado. A lista também deixou de esconder um dos atendimentos quando o mesmo contato tem dois em aberto.
* **Etiquetas definidas por API ou pelo chatbot** aparecem no atendimento na hora, sem esperar a próxima mensagem nem recarregar a página.
* **Botão (x) da lista volta a encerrar de forma direta** — sem pesquisa de satisfação, sem demanda obrigatória e sem mensagem de despedida. A pesquisa continua sendo enviada pelo "Resolver" do atendimento e pelo painel do contato, conforme o comportamento configurado em Avaliações.
* **Espiar conversa do contato:** o histórico é exibido exatamente como no chat do atendimento — imagens ampliam em tela cheia, PDFs abrem em popup, áudios ganham o player completo e mensagens de botões, listas e templates aparecem formatadas.
* **Notas do atendimento com links clicáveis:** URLs, endereços www e e-mails abrem direto da nota, e códigos PIX e linha digitável continuam intactos para copiar. O chat privado também passou a exibir links clicáveis.
* **Mensagem rápida com apenas arquivo:** a "/" usada para buscar não vai mais junto na conversa — some sozinha ao escolher a mensagem — e o botão de enviar aparece normalmente também no celular.
* Ao abrir um atendimento, a conversa sempre carrega na mensagem mais recente: sem abrir no meio nem exigir clique na seta para descer.
* A lista de conversas não volta mais ao tamanho inicial depois de usar "carregar mais" — as páginas carregadas são preservadas nas atualizações em tempo real e após ações em massa.
* Ao ampliar a foto de perfil, contatos sem foto (ou com foto expirada) exibem as iniciais coloridas em vez de um popup vazio.
* O botão **"Enviar template"** do aviso de janela de 24h agora se ajusta automaticamente ao tema e às cores da marca, ficando legível também no modo claro.
* O **PDF de exportação da conversa** apresenta as mensagens em ordem cronológica, da mais antiga para a mais recente.
* Corrigido: a conversa não fecha mais sozinha ao enviar mensagem em atendimento atribuído a outro usuário da mesma fila.
* Corrigido: cliente com atendente fixo (carteira) que chamava por um número fora da visão do atendente ficava sem atendimento — agora o atendimento vai para outro responsável da carteira ou para a fila, normalmente.
* Corrigido: erro intermitente ao enviar respostas rápidas com botões/lista no WhatsApp Oficial e mensagens interativas no Instagram/Messenger logo após aceitar o atendimento.
* Corrigido o contador da janela de conversa, que em alguns casos exibia tempo restante acima de 24 horas.
* Corrigido: documentos PDF com nome contendo pontos duplos (ex.: `arquivo..pdf`) abrem e baixam normalmente no atendimento.
* Corrigido: envio de imagens e arquivos pelo bot quando o nome do arquivo contém espaços ou acentos.
* Corrigido: travamentos do chat privado ao abrir conversas em grupo, além do contador de mensagens não lidas que podia aparecer zerado.
* Corrigido o aviso "Este recurso não está incluído no seu plano", que aparecia sozinho ao abrir um atendimento mesmo sem o usuário acessar o recurso.

**🔔 Notificações e Sininho**

* Ao desativar **"Notificações sonoras"** em Configurações, os alertas de áudio são silenciados imediatamente em todas as sessões abertas — incluindo chat interno, chat de suporte e notificações do sistema, sem precisar recarregar a página.
* Corrigido: com o filtro de tickets no socket ativo, atendentes voltam a receber som, notificação e prévia da mensagem em atendimentos pendentes.
* **Conexões e agendamentos** sinalizam quando apontam para fluxo de bot, fila ou atendente que foi excluído — com aviso automático no sininho dos administradores.
* **Ações automáticas de ticket e do funil** sinalizam quando usam canal, etiqueta, carteira ou etapa que foi excluída — na tela e no aviso diário do sininho.

**📊 Kanban e Funil**

* Corrigido o alerta de fechamento no funil, que exibia "hoje" para oportunidades que venciam no dia seguinte e ignorava as que venciam de fato no dia — datas e contagem de dias agora batem com a data mostrada no card.

**🤖 Chatbot e Chatflow**

* **Editor de fluxo profissional:** desfazer/refazer, aviso de conexões quebradas e ações arrastáveis para dentro dos passos.
* **Variáveis como** `{{name}}` passam a funcionar no corpo, nos títulos e nas opções das listas (WABA, Gupshup e 360Dialog) e na mensagem padrão de tentativa em todos os canais; falhas de envio de lista são sinalizadas no atendimento.
* Transferências para fila, atendente ou canal excluídos não travam mais o atendimento — o sistema avisa no sininho e sinaliza o fluxo com pendência na tela de Chat Flow.
* **Listas do ChatFlow no canal UazAPI** enviam a descrição de cada opção, e o cabeçalho configurado aparece como primeira linha da mensagem.

**📢 Campanhas e Disparo em Massa**

* **Status real por destinatário** nos relatórios de disparo em massa e de campanha — enviada, entregue, lida ou falha — com exportação por número. O relatório também deixa claro quando a mensagem foi apenas aceita pelo provedor, sem confirmação de entrega.
* **Disparo por template** (comum e com variáveis) passa a respeitar a verificação de conversas ativas: contatos em atendimento ou aguardando são pulados e aparecem no resumo e no relatório, sem interromper o atendimento em andamento.
* Agora é possível **editar campanhas agendadas e pausadas**.
* **Importação de números nos Disparos e Grupos:** aceita `.csv` e `.txt` com qualquer divisor (vírgula, ponto e vírgula, tabulação, barra, espaço ou hífen), com detecção automática e pré-visualização antes de importar.

**📱 Canais Oficiais Meta (WABA / Instagram / Messenger)**

* **Cobrança pelo WhatsApp (WABA):** escolha o template de cobrança, informe os itens e o valor, e o cliente recebe uma ficha de pagamento com Pix, boleto ou link. Disponível no atendimento, em nova conversa, disparo em massa, campanhas, agendamentos, funil e chatbot.
* **Autocura dos canais Meta:** resolvido o caso em que o canal permanecia conectado mas parava de receber mensagens novas após alguns dias, exigindo reconfiguração manual da origem do webhook.
* **Instagram e Messenger:** a pesquisa de satisfação volta a registrar a nota e a encerrar o atendimento automaticamente após a resposta do cliente — e as mensagens de confirmação e despedida agora aparecem no histórico da conversa.
* **Instagram — assumir o controle da conversa:** quando outra ferramenta está "segurando" a conversa (a mensagem chega, mas a resposta falha), o sistema assume o controle automaticamente e reenvia a mensagem. Basta habilitar "Assumir o controle de conversas" nas configurações da Página do Facebook.
* **Instagram via Tech Provider** pode ser usado associado a uma conta do Facebook ou apenas com o Instagram.
* Instagram conectado via Facebook agora conclui a configuração do webhook — antes a ativação falhava silenciosamente em contas sem canal Messenger na mesma página.
* Adicionada a hidratação da carga para cobrir o aviso intermitente "Token WABA não encontrado" ao enviar templates e mensagens do WhatsApp Oficial.
* Corrigido o template de mensagem de aniversário em canais WhatsApp Oficial (WABA), que não era salvo ao configurar e não era usado no envio.
* Corrigido: encaminhar mensagem recebida em canais WABA, Instagram e Hub agora entrega de fato ao destinatário (antes aparecia como enviada sem chegar).

**🔌 Integrações Não Oficiais (Baileys, UazAPI, Z-API, EVO, ZAPO, InfiniteAPI)**

* **Nova API liberada: ZAPO** — com opção de transferência nativa de Baileys para ZAPO.
* **Novo atalho "InfiniteAPI"** na tela de Sessões: crie o canal já com a biblioteca de mensagens interativas e escolha o armazenamento da sessão, sem precisar configurar pelo Baileys.
* **WhatsApp/Baileys:** sessão utilizada em outro local (conflito "replaced") agora é detectada e pausada automaticamente após 3 quedas seguidas, eliminando o loop de reconexão que elevava o consumo de memória e podia reiniciar o servidor.
* **Conexões WhatsApp mais estáveis:** canais que ficavam presos em "conectando" ou desconectavam em loop após conflito de sessão agora se recuperam sozinhos, e reconectar manualmente volta a funcionar de primeira.
* Canais **desativados automaticamente** após falhas de conexão voltam a funcionar sozinhos quando reconectam, e o aviso "Inativo" explica o motivo e o que fazer.
* **Z-API:** corrigido apagar e editar mensagens — a exclusão remove a mensagem também no WhatsApp do contato, e a alteração aparece em tempo real na conversa.
* **Z-API e UazAPI:** a foto de perfil dos contatos voltou a carregar, e a criação de canais via API respeita o provedor global configurado.
* **UazAPI:** corrigido o envio de arquivos PDF em instalações que usam armazenamento em nuvem (S3).
* **EVO:** corrigido o encode de mídia.

**🛍️ Marketplaces e Hub (Mercado Livre, OLX, LinkedIn, YouTube)**

* Respostas pelos canais **Mercado Livre, OLX, LinkedIn e YouTube** funcionam de ponta a ponta, e envios que falham passam a mostrar erro claro no chat em vez de constar como entregues.
* **Mercado Livre:** o ticket mostra o nome do comprador e o anúncio/produto da conversa (título, imagem e link), sem precisar abrir o Mercado Livre.

**🔗 API e Integrações Externas**

* Agora é possível **criar a conexão já vinculada ao modo híbrido pela API**, sem precisar editar o canal depois.
* As telas de configuração de integrações avisam quando um **provedor global do sistema** está ativo e tem prioridade sobre os dados preenchidos na página.

**👥 Contatos e Importação**

* **Convenção do 9º dígito (BR):** números de celular com o 9º dígito passam a ser respeitados conforme a configuração da empresa (Configuração Geral → Convenção do 9º dígito (BR)), e envios que falhavam por variação do 9 são reenviados automaticamente na forma correta. Envios de mídia, botões, listas e templates pelos canais oficiais do WhatsApp também se recuperam automaticamente quando o número do contato diverge no 9º dígito.
* **Importação de contatos:** arquivos `.csv` e `.txt` funcionam com qualquer divisor (vírgula, ponto e vírgula, tabulação ou barra), com detecção automática e opção de escolher o divisor na pré-visualização.
* **Importação inteligente:** a área de mapeamento de colunas mostra mais colunas de uma vez e exibe quantas colunas foram detectadas no arquivo.
* **Importação inteligente:** o campo personalizado aparece corretamente ao ser selecionado, pode ser removido com um clique e não permite nomes repetidos entre colunas.
* **Exclusão de contatos** passou a respeitar de fato a configuração "permitir somente admin excluir contatos": com ela desligada, supervisores e atendentes conseguem excluir contatos que já têm atendimento; com ela ligada, a restrição vale também na API, e não só na tela.
* Corrigida a importação de contatos por planilha.

**📈 Relatórios, Dashboard e Indicadores**

* **Novo relatório de Produtividade Diária:** mostra quantos atendimentos cada atendente fez, iniciou e resolveu em cada dia, considerando a data em que o atendimento aconteceu — incluindo conversas abertas em dias anteriores.
* **Painéis com contexto:** comparativo com o período anterior, relatórios ordenáveis e Analytics com gráficos de verdade.
* **Tempos com precisão de segundos** (nada de "0min" para equipes rápidas), TPR e TTE com explicação direto no painel, e correção automática dos registros antigos que zeravam o tempo de primeira resposta.
* Os indicadores **TPR** e **TTE** passam a ser calculados corretamente em todos os canais, inclusive em atendimentos antigos.
* Atendimentos encerrados pelo **botão de resolver da lista** voltam a ser contabilizados em TPR e TTE, e não mudam mais de atendente ao serem encerrados.
* Corrigidos o carregamento do detalhamento por usuário no dashboard e os valores incorretos na linha de totais da tabela de desempenho.

**📅 Agendamento e Aniversários**

* **Lembretes da Agenda** ficam registrados no histórico do atendimento também nos canais WhatsApp QR Code e UazAPI, como já acontecia na API oficial.
* Corrigido: mensagens agendadas com template exibem as variáveis preenchidas na tela de Agendamentos e no chat (o envio ao contato já estava correto).
* Corrigido o horário exibido nas consultas da agenda: a data/hora agora aparece igual na lista, no calendário e na tela de edição (a servidor em nuvem deve estar no timezone `America/Sao_Paulo`).
* Na lista de aniversários, ordenar por qualquer coluna considera todos os contatos, e não apenas os da página aberta.

**⚙️ Superadmin, Planos e Pagamentos**

* **Alterar as funcionalidades de um plano vale na hora** para os clientes que já estão nele — antes só valia para novas contratações.
* **Controle do WaVoIP por empresa.**
* **Pagamentos via Stripe:** o plano contratado fica vinculado à assinatura desde o cadastro, com fatura com vencimento e troca de plano direto pelo menu Meu Plano.
* Corrigido: as notificações de pagamento do Stripe voltaram a ser recebidas corretamente — o status da assinatura é atualizado automaticamente, sem erros de autenticação no webhook.

**👤 Usuários e Senhas**

* **Controle de senha para novos usuários:** exija a troca de senha no primeiro acesso ou envie um convite por e-mail para o próprio usuário criar a senha (Configurações → Gerais → Senha de novos usuários).
* Agora é possível remover a foto de perfil e voltar ao avatar padrão nas páginas de perfil.

**🎨 Interface, Navegação e Configurações**

* **Navegação repensada:** busca **Ctrl+K** com todas as telas, configurações e ações rápidas; troca de tema instantânea.
* **Interface no seu idioma:** datas, horas e números seguem o idioma do usuário, e o modo escuro foi corrigido em todo o sistema.
* **Configurações Gerais:** busca aprimorada com atalho `/`, filtros por tema, seções recolhíveis, revisão das alterações antes de salvar e aviso ao sair sem salvar.
* Listas longas em modais e painéis agora mostram barra de rolagem — corrigidos o popover de atendimentos pausados, o modal de Tarefas e o de encaminhar mensagem, que cortavam a lista sem deixar rolar.
* **Catálogo:** o campo **Imagens extras** agora explica que essas fotos ficam no cadastro e não são enviadas junto com a ficha do produto.

**✉️ E-mail**

* Corrigida a visualização de e-mails em HTML no iPhone/Safari — o conteúdo do e-mail agora abre normalmente no celular.

**🔧 Sistema e Infra**

* **Instalador:** as respostas da API passam a trafegar comprimidas (gzip), reduzindo o consumo de dados e acelerando o carregamento — aplicado automaticamente na próxima atualização.

---

## Versões anteriores

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
* **Community Nodes** para n8n (`n8n-nodes-zpro` e `n8n-nodes-zpro-admin`).
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

* Customização plataforma de atendimento:

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
🔗 Integrações nativas com [Instagram, Facebook](/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/instagram-e-facebook-messenger-via-oauth-login) e [WhatsApp API oficial](/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/whatsapp-oficial-oauth-app-zpro-com-coexistencia) - Oauth próprio do Zpro
🤖 [Copiloto de I.A](/configuracao-administrador/configuracoes-painel-admin/bots-e-ia/copiloto-de-ia) - Resumos, sugestões de respostas, análises de sentimento...
📱 Novos canais - Mercado Livre, Woocommerce, OLX, Tiktok, Youtube, Linkedin, Rocket.Chat
📈 Rastreamento de conversões Pixel Meta e Google GA4
🎧 Novos recursos de [atendimento](/configuracao-administrador/gestao-comercial/analises-e-registros/painel-de-atendimentos)
👤 [Perfil personalizado de usuários](/configuracao-administrador/administracao-painel-admin/usuarios/perfis-de-acesso)
🔌 Novos [Endpoints API](/central-do-assinante/referencia-da-api)
🎨 [Personalizações](/configuracao-superadmin/configuracoes/customizar-plataforma de atendimento)
☁️ Armazenamento externo ([Storage AmazonS3](/configuracao-superadmin/sistema/sistema-dados-e-configuracao/storage-s3), etc)
⚡️ [Autoinstalador melhorado](https://prismatelecomservicos.com/ rel=)
💳 Novos gateways de pagamento (stripe, mercadopago, etc)
🚀 Modo Cluster - Infraestrutura para escala com múltiplos núcleos de processamento
📧 Integração com [SMTP](/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/e-mail-imap-smtp) para envio e recebimento de email nos tickets
✨ Recursos premium baileys / uazapi - botões, listas, etc

### Histórico das versões antigas (antes da v4.0)

Nas páginas seguintes você encontra o histórico completo das versões anteriores.

[AnteriorAtualizações e Status do Prismabot](/central-do-assinante/atualizacoes-e-status-do-z-pro)[Próximo3.1.5.x](/central-do-assinante/atualizacoes-e-status-do-z-pro/changelog-4.0.x-ultima-versao/3.1.5.x)

Atualizado há 11 dias

Isto foi útil?