Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante/atualizacoes-e-status-do-z-pro)
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

### v4.0.8

**🚀 UPDATE OFICIAL (HOMOLOG) | 10/11/2026**

Nova versão Homolog (v4.0.8.0), cumulativa de todas as correções publicadas desde a v4.0.7.0.

**Faça um BACKUP / SNAPSHOT antes de aplicar esta atualização.**

Esta versão traz os Formulários do WhatsApp (Flows), o envio de templates de marketing pela Marketing Messages API da Meta, o registro de quem recebeu cada atendimento e por quê, a opção "Fora do rodízio de atendimentos", o Agente de IA no Fora do horário do fluxo, a junção de empresas no Superadmin e o instalador para Ubuntu 26.04 LTS.

**Mudanças automáticas nesta atualização:** os templates de marketing do WhatsApp oficial passam a sair pela Marketing Messages API (mesmo preço) e o botão "Enviar Marketing" do envio em massa sai da tela; mensagens antigas do Instagram e do Messenger com mídia trocada entre conversas passam a mostrar "Mídia indisponível"; canais WABA, Instagram e Messenger desconectados continuam gravando as mensagens recebidas (opção ligada por padrão); e trocar o endereço de IA da conexão passa a pedir a chave de novo.

**📝 Formulários do WhatsApp (Flows) (novo)**

* **Formulários nativos do WhatsApp:** lista de formulários da conta, bloco de formulário no fluxo e botão de formulário no template, na posição certa. O formulário agendado será liberado na próxima etapa.

**📣 Marketing Messages API (WhatsApp oficial)**

* **Templates de marketing** passam a sair automaticamente pela Marketing Messages API da Meta, com o mesmo preço e entrega otimizada. Os demais templates seguem pelo envio comum.
* **Aviso no card do canal** quando a conta pode aceitar os termos da Marketing Messages API, com passo a passo e link para o WhatsApp Manager.
* **Ícone de megafone** na mensagem enviada pela Marketing Messages API.
* O **Diagnosticar** do canal mostra a situação na Marketing Messages API e os últimos avisos da Meta sobre a conta (restrição, revisão, alertas, limite e nome).
* No envio em massa, o botão **"Enviar Marketing"** foi removido: a escolha agora é automática.

**🔀 Distribuição de Atendimentos**

* **Registro de quem recebeu cada atendimento e por quê:** aba **Distribuição** no histórico do atendimento e relatório próprio. O atendente definido pelo fluxo não é mais trocado pelo atendente padrão do canal.
* Nova opção **"Fora do rodízio de atendimentos"** no usuário: a pessoa continua online e recebe transferências, mas não é escolhida pela distribuição automática. O administrador nunca entra no sorteio, e em LinkedIn, OLX, TikTok, Nuvemshop, Mercado Livre, YouTube e WooCommerce a conversa fica com o atendente padrão do canal.

**💬 Atendimento e Tickets**

* Atendentes passam a **filtrar a lista por Kanban, Etiquetas e Conexões** mesmo com "Não visualizar atendimentos de outros usuários" ligado. O filtro por Usuário segue oculto nesse caso.
* O botão **Ações** da lista mostra um número quando "Inverter ordem" ou "Organizar por não respondido" está ligado, igual a Filtros, com visto no item ativo.
* **Template do WhatsApp oficial com variáveis nomeadas** aparece no atendimento com os valores preenchidos, e não mais com o nome do contato e campos em branco (envio pelo atendimento e pela API).
* **Imagem, vídeo e documento com legenda enviados pela API** mostram a legenda na conversa e no card do atendimento na hora, sem atualizar a página, no WhatsApp oficial, Dialog360, Gupshup, Instagram e Messenger. Antes só o cliente recebia o texto e o painel mostrava o nome do arquivo.
* **PDFs recebidos com miniatura grande** não travam mais o sistema nem derrubam as conexões, e o PDF enviado como resposta mostra a legenda no lugar do texto citado.
* Mensagens para números com o **9º dígito** deixam de ser bloqueadas por engano no chat das conexões WhatsApp.
* O **protocolo de atendimento** enviado ao cliente sai só com o número, sem o nome do canal no final.

**👥 Contatos**

* **Editar contato não trava mais em número sem WhatsApp:** trocar etiqueta, nome ou e-mail salva sempre, número novo sem WhatsApp é salvo com aviso, e com "Validar Contato" desligado nenhuma conexão é consultada ao criar, editar ou importar.
* Editar o contato pelo atendimento **apaga de verdade** o e-mail, CPF, nomes, aniversário, empresa e IDs de canal que o atendente limpar, e o LID atualizado pelo botão não volta mais ao antigo ao salvar.
* **E-mail de remetente já cadastrado** entra no contato existente em vez de criar um duplicado, sem trocar a foto nem o nome de quem já tem telefone.

**🤖 Chatbot e Chatflow**

* **Agente de IA no Fora do horário:** um agente de IA atende à noite, no fim de semana e nos feriados, e de manhã a conversa vai sozinha para a fila escolhida.
* O **número para teste** do chatbot aceita vários números: digite e aperte Enter ou vírgula para adicionar cada um (até 15).
* **Formulário no modo "Começa no fluxo"** inicia o fluxo pela primeira mensagem quando o cliente responde, sem "não entendi" antes do menu e sem pular a primeira etapa.

**🧠 Agente de IA e IA da plataforma**

* **Agentes de IA pela API:** agente, base de conhecimento e fontes podem ser criados e geridos pela chave da API, com a tela de API, o Postman e o n8n atualizados.
* O agente de IA no **WebChat, Instagram, Messenger e Telegram** envia o link da página de agendamento em vez de prometer horário, e o cliente que entra no WebChat pelo convite do WhatsApp agenda direto pela conversa.
* O **link de cancelar ou remarcar** enviado pelo agente volta a abrir a reserva, mesmo com pontuação no fim.
* O agente de IA, as demais IAs e o Typebot entendem **áudio, imagem e arquivo** do cliente também com a transcrição do GroqCloud ligada, e o **GPT-5** volta a responder pela IA da plataforma.
* **Créditos de IA:** modelos com preço em faixas (OpenAI GPT-5.4 em diante e família 6, Claude, Gemini Pro, Grok, Qwen e DeepSeek) podem ser vendidos, cobrados pelo custo exato de cada resposta.
* **Transcrição dos áudios do atendente:** nova opção na tela da GroqCloud, desligada por padrão ("Transcrever também os áudios enviados pelo atendente").
* A **transcrição do Google** volta a funcionar com armazenamento S3.

**🔐 Segurança**

* **Variável secreta:** a variável da empresa pode ter o valor oculto e ser usada só no nó HTTP do fluxo.
* A **chave de IA** do fluxo ou do agente deixa de ir ao endereço de IA da conexão. Trocar esse endereço agora pede a chave de novo.
* O sistema passa a **conferir se cada mensagem recebida veio mesmo da Meta**.

**📊 Kanban e Funil**

* O valor e a quantidade de cada etapa e os números do topo do quadro mostram o **total real do funil**, mesmo com mais de 100 oportunidades.
* Os **alertas do quadro** explicam o que significam, o "Inativa" considera as mensagens trocadas com o contato e há o novo alerta de **previsão de fechamento vencida**.
* Ao criar uma oportunidade com contato não cadastrado, a tela avisa para cadastrar o contato primeiro, em vez de mostrar um erro genérico.

**📢 Campanhas, Comunicados e Envio em Massa**

* **Quem respondeu:** envio em massa e campanha mostram quem respondeu em até 7 dias, com a taxa de resposta, a aba **"Respondidas"**, o botão para abrir o atendimento e colunas novas no CSV e no PDF.
* O **relatório do envio em massa** mostra por número se a mensagem foi entregue, lida ou não entregue, com o motivo informado pela Meta, também nas planilhas exportadas.
* **Comunicados com filtro de Kanban** carregam só a etapa escolhida, e o aviso diz o que ainda carrega.
* **Template agendado** com botões e sem variável volta a ser enviado, e não sai mais sem variáveis quando o canal reinicia.

**📈 Relatórios**

* O relatório de **Atendimentos por Parâmetros** não derruba mais o servidor em períodos grandes: filtro Receptivo/Ativo mais rápido, aviso acima de 20 mil atendimentos e tabela com 100 linhas por vez.

**📣 Anúncios**

* Contatos que chegam por anúncio **nas demais conexões** entram no relatório de Conversões e ganham o selo e a etiqueta automática. A mídia mostra o cartão **"Veio do anúncio"**. Nessas conexões não há envio do evento à Meta.

**📱 Canais Oficiais Meta (WABA / Instagram / Messenger)**

* **Juntar mensagens para pagar menos:** o WhatsApp oficial pode juntar numa só as mensagens seguidas de robôs e atendentes, com o balão de botões e a legenda da mídia do fluxo aparecendo inteiros no painel.
* O canal do WhatsApp oficial **não desconecta mais quando a Meta limita as consultas** da conta (erro 80008), e a tela avisa "Consultas pausadas" com o horário em que libera.
* **Canal desconectado** registra as mensagens dos clientes sem robôs e avisa na tela. Nova opção em **Configurações Gerais** para escolher se canais WABA, Instagram e Messenger desconectados continuam gravando as mensagens (ligada por padrão).
* O Diagnosticar e as ações da Meta respeitam a pausa do limite, e **templates inválidos** são recusados com o motivo.
* **Webhook da empresa** passa a avisar o status de cada mensagem enviada pelo WhatsApp oficial (enviada, entregue, lida, falhou com o motivo) e a trazer o texto do botão ou da opção de lista clicada.
* Novo botão **"Enviar convite do WebChat"** no atendimento do WhatsApp oficial, com texto personalizável: o cliente continua a conversa no chat do site como o mesmo contato. No Dialog360 e no Gupshup, o link do convite deixa de chegar como texto cru.
* **Figurinhas** acima do limite do WhatsApp oficial são reduzidas automaticamente no envio pelo WABA, 360Dialog e Gupshup. A galeria fica intacta e, se nem reduzida couber, o motivo aparece na mensagem.
* **Ligação pelo WhatsApp oficial** avisa quando o número usa outro sistema de ligação (SIP, como o WaVoIP) ou quando falta microfone no computador, e pede confirmação antes de mexer no SIP do número.
* **API externa:** template de utilidade enviado pela rota de marketing não dá mais erro.
* Mensagens de **contas diferentes recebidas juntas** chegam cada uma à empresa certa, e mensagens recebidas durante um reinício rápido do servidor são reentregues em vez de perdidas.
* **Instagram pelo Login Unificado da Meta**, sem Página do Facebook, com aviso de vencimento do acesso e reconexão pelo mesmo app (em fase final de revisão).
* **Conexão do Facebook com App próprio** e Config ID de "token do usuário" funciona em produção. Na primeira vez a tela da Meta aparece duas vezes; depois abre direto.
* A **reconexão do Instagram pelo Facebook** atualiza o canal existente e avisa quando o webhook precisa ser revalidado.
* **Messenger:** imagens, áudios, vídeos e documentos enviados pelo atendimento voltam a chegar ao cliente, com a legenda logo em seguida e aviso na mensagem quando o envio falha.
* Fotos, áudios e vídeos recebidos pelo **Instagram e Messenger** não se sobrescrevem mais entre conversas. As mensagens antigas afetadas mostram "Mídia indisponível" em vez da mídia de outro cliente.
* A **automação do Instagram** não quebra mais quando a permissão muda com a tela aberta, e a falha ao conectar o Instagram pelo aplicativo próprio registra o motivo informado pela Meta.

**📞 WebChat, WebPhone, Chat interno e App**

* **WebChat:** o atendente grava e envia áudio direto no atendimento, com dica de como o visitante recebe.
* **WebChat:** mensagens automáticas (fluxo, IA, despedida, avaliação) deixam de contar como atendimento do atendente na Produtividade Diária, valendo para as mensagens novas.
* **WebPhone:** ligações feitas pelo atendente tocam o "chamando" e os avisos da operadora antes de atenderem, com toque de reserva quando o PABX não manda áudio.
* **WebPhone:** o painel arrastado volta no mesmo lugar depois de recarregar e não sai da tela, e os botões da chamada em curso e da transferência cabem inteiros na janela.
* **Chat interno no Android:** a barra de escrever não fica mais atrás dos botões do aparelho nem corta o texto, e o envio de imagem funciona (ou avisa para escolher de novo em "Abrir arquivos").
* **App:** menus que abriam perto do rodapé (como "Apagar" na última mensagem) abrem sempre na área tocável da tela.

**📅 Google (Agenda e Avaliações)**

* **Agenda Google:** ao conectar a conta, a tela atualiza sozinha (sem F5), e a janela de autorização não pede mais login quando o painel é aberto por outro domínio da instalação.
* **Avaliações no Google:** quando uma das contas não responde, as fichas das outras aparecem normalmente e a tela avisa qual leitura falhou.
* Corrigido o erro **"Host mismatch"** ao conectar canais quando o servidor de autorização principal está indisponível.

**✉️ E-mail e outros canais**

* O **canal de e-mail** aceita servidor IMAP/SMTP em rede interna (VPN/WireGuard) liberado pelo administrador do servidor. O Testar IMAP explica por que um endereço foi recusado (no `.env` do backend, numa linha própria: `EMAIL_HOST_ALLOWLIST=10.0.4.19`).
* **UAzapi:** receber várias fotos de uma vez não mostra mais o aviso "Mídia não suportada". As fotos continuam chegando normalmente.

**⚙️ Superadmin**

* **Juntar uma empresa dentro de outra** na tela de Empresas: prévia dos conflitos, confirmação, acompanhamento e resultado, com canais sem QR novo e links antigos funcionando.
* **Termos do revendedor com variáveis:** dados da empresa, do licenciado e do sistema preenchidos no texto, pré-visualização por empresa e consulta do texto que cada empresa aceitou.

**🔧 Sistema e Infra**

* O **instalador aceita o Ubuntu 26.04 LTS**, com o Google Chrome instalado do jeito que o 26.04 exige, a versão do nginx de novo escondida e a opção Fail2ban do menu de segurança voltando a funcionar.
* **Armazenamento em nuvem (S3/R2):** áudios recebidos pelo WhatsApp oficial, Instagram e Messenger não deixam mais cópia no servidor, abrir a Galeria não traz mais as imagens da nuvem de volta para o servidor, e a migração para o S3 mostra à parte o que fica no servidor de propósito.

## Versões anteriores

### v4.0.7

**🚀 UPDATE OFICIAL (HOMOLOG) | 24/10/2026**

Nova versão Homolog (v4.0.7.0), cumulativa de todas as correções publicadas desde a v4.0.6.0.

**Ajustes automáticos nesta atualização:** as respostas recentes a stories do Instagram que chegaram só com a etiqueta são recuperadas com o texto do cliente; cadastros duplicados do mesmo cliente no WhatsApp oficial (só identificador + telefone) são unidos, com opção de reverter; e canais marcados com armazenamento SQLite passam a usar o SQLite de verdade, com migração automática e sem novo QR.

**📝 Formulários (novo)**

* **Formulários públicos que abrem atendimento:** página por link, QR code ou embutida no site, e também pela API. Cada envio cria ou completa o contato e abre o atendimento no canal escolhido (WhatsApp, WhatsApp oficial ou e-mail), com as respostas num cartão só para a equipe.
* Destino por fila, fluxo ou Agente de IA, **regras por resposta** (fila e etiquetas por opção), oportunidade no funil, confirmação ao cliente e aba **Respostas** com filtro e exportação. Veja Formulários.

**🧩 Aplicativos da Empresa**

* **Sistemas próprios no menu do painel:** cada empresa coloca seus sistemas no menu, abrindo dentro da tela ou em nova aba, e escolhe quem vê cada um. O provedor pode oferecer aplicativos para todas as empresas ou por plano.
* Os aplicativos abrem **direto do contato e do atendimento**, com os dados do cliente no endereço e identificação assinada de quem abriu. Usuário restrito e modo apresentação recebem só códigos, e cada abertura fica registrada na **Auditoria**.

**🌎 Região da Empresa**

* **País, moeda e idioma por empresa:** mensagens automáticas ao cliente no idioma escolhido, valores no formato do país e telefone estrangeiro reconhecido.

**💬 Atendimento e Tickets**

* **Atendimentos fixados** acompanham o usuário em todos os aparelhos (navegador, app e celular): o que é fixado em um aparece no outro em até 30 s, sem apagar os fixados do outro aparelho.
* **Transferências registradas no chat** com quem transferiu, origem, destino e hora, inclusive as automáticas e as feitas pela API. O registro não conta como resposta ao cliente e não aparece para o contato.
* A opção **"Listar atendimentos pela última mensagem"** passa a valer na tela: a lista segue o mesmo tempo mostrado no card, e o **"Inverter ordem"** do menu Ações mostra quando está ligado.
* **Mensagens rápidas ao iniciar conversa** (Nova Conversa, conversa avulsa e Funil, inclusive no e-mail), com as variáveis do cliente trocadas no envio e aviso quando algum dado vai sair vazio.
* Mensagem rápida do tipo **Template** abre o envio de template já selecionado para preencher as variáveis, também com a janela de 24h fechada. Antes chegava ao cliente só como texto.
* Mensagem rápida de **Botões ou Lista** envia também os anexos, antes dos botões, e trocar de mensagem rápida não leva mais o anexo da anterior.
* **Encaminhar mídia** leva a legenda certa em todos os canais (no Instagram e no Messenger ela chega logo depois). Vídeo, documento e figurinha que não chegavam passam a sair, e canais que não recebem o encaminhamento avisam em vez de deixar a mensagem parada.
* **Prévia de link** nas conversas só aparece ao clicar em **"Ver prévia"**.
* Quando o WhatsApp **não entrega uma mensagem ou mídia** que o cliente enviou, o atendimento mostra o aviso para pedir o reenvio e o motivo fica registrado no log, em vez de a mensagem sumir sem rastro.
* **Mensagens editadas** no WhatsApp (pelo contato ou pelo celular do número) voltam a aparecer editadas no atendimento, sem reabrir conversa encerrada e sem mexer nas não lidas.
* Imagens, GIFs e mídias de template e de notas voltam a ocupar só a largura da própria mídia no chat.

**📣 Anúncios (Click-to-WhatsApp, Instagram e Messenger)**

* Contato que chega por **anúncio** mostra o anúncio na 1ª mensagem (título, imagem e ID para copiar), ganha o selo **"Anúncio"** na lista e no atendimento (também no WhatsApp oficial), pode receber uma etiqueta automática e aparece no relatório de **Conversões**.
* Conversas iniciadas por anúncio mostram até quando os templates saem **sem custo** (janela grátis da Meta de até 7 dias), com interruptor em Configurações. O texto livre continua limitado a 24h.

**✅ Tarefas**

* **Tarefas no atendimento** com prazo com hora, lembrete de 10, 30 ou 60 min, aviso na tela e por push ao responsável, e número de atrasadas e de hoje no sino e no menu.
* Corrigido: a tarefa "para o dia" deixa de aparecer atrasada às 21h da véspera.

**🔔 Notificações**

* **Novo botão de som** ao lado do sino: cada usuário escolhe som ligado, grupos sem som ou tudo sem som, no painel e no push do celular. Com o som da empresa desligado, o iPhone também fica em silêncio.
* O aviso **"Notificar equipe"** e o **"Avisar a equipe"** do Agente de IA mostram nome e mensagem do cliente só para quem consegue abrir o atendimento; os demais recebem só o texto do aviso.

**🧠 Agente de IA e Copiloto**

* **Ferramentas de servidores MCP** (n8n, Zapier, Make e outros) aprovadas pela empresa, com aviso quando o servidor muda e nota interna quando a ferramenta altera dados. A senha das ferramentas externas não aparece mais na tela.
* **Base de conhecimento compartilhada** entre agentes, novo agente **"só base de conhecimento"** e criação de um agente ou de uma equipe completa a partir de **modelos prontos**, em poucos cliques.
* Novo campo **"Atraso na resposta":** o agente espera um tempo sorteado antes de responder, com "digitando..." no WhatsApp, e descarta a resposta se um atendente assumir a conversa.
* Novo botão **"Desligar agente de IA"** no atendimento (menu ⋯ e aba Integrações): a IA para de responder aquele cliente na hora, com nota na conversa, sem marcar o cliente como respondido.
* O agente **para com o "Bloquear chatbot"**, pode ser pausado e retomado em cada atendimento, e avisa e encerra (ou transfere) sozinho quando o cliente para de responder.
* **Etiquetas e etapa do funil** aplicadas depois de cada mensagem do cliente, inclusive quando transfere ou encerra, sem atrasar a resposta e com interruptor por agente na aba Ações.
* O campo **"Quando transferir"** aceita até 1.000 caracteres, com caixa maior e contador, e o texto inteiro passa a ser considerado pela IA.
* **Arquivos:** o agente confirma que lê PDF, Word, Excel e CSV, lê o arquivo com legenda ou nome em maiúsculas, avisa o cliente quando o PDF é escaneado e, no WebChat, volta a receber os arquivos enviados.
* Agente com **endereço próprio** (DeepSeek e outros) lê imagens e transcreve áudios pelo próprio provedor, e a resposta em voz que falha passa a sair em texto.
* **Todas as IAs** (Claude, Gemini, Grok, DeepSeek, Qwen, LM Studio, Ollama e o assistente da OpenAI) entendem o clique em botão ou lista e sabem qual mensagem o cliente respondeu. No WhatsApp oficial, na 360dialog e na Gupshup o clique chega às IAs, sem ser tratado como arquivo.
* O raciocínio interno que alguns modelos escrevem antes da resposta (bloco "think") não aparece mais para o cliente. No **Copiloto** com modelos que raciocinam (Qwen, DeepSeek R1 e outros), a resposta deixa de sumir quando o raciocínio estoura o limite.
* **Resposta em áudio da IA** volta a chegar ao cliente no Instagram e no Messenger, sem chegar em dobro e sem trocar o áudio entre clientes. No Mercado Livre a resposta sai em texto.
* O agente volta a responder **áudio, foto e documento** no fluxo do WhatsApp oficial, e o encerramento automático deixa de mandar despedida que a Meta recusaria fora da janela de 24 horas.
* Canal com Agente de IA e ChatGPT ligado para todos os atendimentos não entra mais no laço de erro de chave: o card do canal mostra o agente vinculado e avisa quando falta a API Key do ChatGPT.
* **IA da plataforma:** modelos sem preço no serviço (como Open WebUI e Ollama) podem ser vendidos com o preço que você digitar, cada bloqueio explica o motivo e o teste de conexão avisa quando o serviço não informa o consumo.

**🤖 Chatbot e Chatflow**

* As configurações do fluxo avisam que a **distribuição do fluxo não vale** quando a conversa passa por um Agente de IA, e mostram onde ligar a distribuição na fila.
* Corrigido: nó com vários caminhos por **Regex** reconhece todos eles, não só o primeiro da lista.

**📊 Kanban e Funil**

* **Oportunidades** abrem o atendimento direto pelo card. O quadro mostra um funil por vez, com seletor no topo, e clicar no card abre uma ficha lateral com dados, conversa, linha do tempo e Ganho/Perdido.
* **Funil estilo Kommo** conferido com atendente, usuário restrito e perfil sem permissão de criar atendimento: cada um vê só o que pode, e o link direto de atendimento avisa quando não há acesso.
* A **exportação de oportunidades** sai com uma oportunidade por linha (quebras da descrição viram " | ") e abre já separada em colunas no Excel em português.
* Funil, kanban e tarefas **no celular** voltam a rolar com muitos cards. Para mover um card, toque e segure por um instante e arraste.

**⭐ Avaliações**

* **Avaliação no Google:** pedido de avaliação depois da nota, link `{{linkAvaliacaoGoogle}}`, ação do funil ao marcar como Ganha e aba **Google** com avaliações, respostas e alerta de prazo. O Aviso de Privacidade foi atualizado com o Perfil da Empresa no Google.
* Botão **Exportar** em Excel e CSV com os filtros da tela, filtro por agente, busca que filtra de verdade e download pelo app no celular (exige atualizar o app).
* A nota do cliente em atendimento já resolvido não notifica mais o atendente, e a privacidade das avaliações passa a proteger de verdade log, relatórios e média por atendente.

**🖼️ Galeria e Catálogo**

* **Galeria com pastas:** crie pastas, mova arquivos (um a um ou em lote), exclua vários de uma vez e filtre por pasta na galeria, no seletor de arquivos e no "Da galeria" do atendimento, que agora avisa que dá para enviar vários de uma vez.
* **Catálogo de produtos:** a lista e o seletor do atendimento ganharam "Carregar mais", e nenhum produto some depois do 20º.

**👥 Contatos e Etiquetas**

* **Importação inteligente:** nova dica na etapa de colunas explica que o contato existente é achado pelo telefone, que célula vazia com "Sempre atualizar" apaga o dado e que o campo personalizado precisa ter o mesmo nome do contato.
* Etiquetas e API avisam **nome repetido** ou texto longo demais.

**📢 Campanhas e Disparo em Massa**

* **Disparo em massa com texto e arquivo** entrega os dois ao mesmo contato quando a verificação de conversa em outros canais está ligada. Antes só o texto chegava.
* **Campanha com o canal fora do ar** espera o canal sem perder contatos e pausa sozinha com aviso.
* **Mensagem de aniversário** com imagem, vídeo ou áudio aparece como mídia no atendimento em todos os canais, sem bolhas repetidas, e volta a ser enviada pelo Telegram, Mercado Livre, Instagram e Messenger.

**📱 Canais Oficiais Meta (WABA / Instagram / Messenger)**

* **Aba Custos da API oficial** desconta as 1.000 respostas grátis por número, não cobra o que foi digitado no celular nem o histórico importado e mostra o custo certo de cada tipo de mensagem.
* **Erros de envio** do WhatsApp oficial explicam o que fazer (número do canal não encontrado ou número não registrado). O aviso de PIN pendente cobre número que ficou fora da Cloud API, e a tela de verificação mostra o ID certo do número com orientações para não travar o pedido de código.
* A mensagem de um cliente não cai mais no cadastro de **outro contato** que tinha o identificador dele, e a resposta sai para o número certo. Editar o número ou mesclar contatos não carrega mais esse vínculo.
* Mensagens do WhatsApp oficial não se perdem mais com **horário de atendimento** invertido ou vazio.
* **Respostas a stories do Instagram** mostram o texto que o cliente escreveu, com a indicação "Respondeu ao seu story" e o link do story, e chatbot, IA e automações passam a receber esse texto.
* **Comentários do Instagram:** responda direto no atendimento, em público ou no Direct, e as respostas da própria conta não abrem mais atendimento em nome da empresa.
* **Comentários do Instagram e do Facebook** podem ser liberados para supervisor e atendente no cadastro do usuário, para ver, responder e comentar. Apagar, publicar e editar posts continua com o administrador.
* A automação e os Comentários do Instagram carregam **todas as publicações** (botão "Carregar mais") e mostram a capa dos vídeos. As listagens de Instagram e Facebook não deixam mais usar o token do canal fora delas.
* **Instagram e Messenger:** mensagens que chegam juntas não se perdem mais, o comentário em live aciona a automação, conversas de outro app aparecem sem o robô responder, cliques repetidos não disparam o fluxo de novo e o atendimento novo mostra o texto certo na lista.
* Instagram: responder um contato que voltou a escrever depois do atendimento encerrado não falha mais por "conversa com outro aplicativo".

**📅 Agendamento e Horários**

* **Agendamento público em canal oficial** (WABA, Gupshup, Dialog360): aviso de serviço sem template, pausa ao trocar o canal, confirmação em texto para quem conversou nas últimas 24h e template próprio para o check-in.
* Corrigido: turno de atendimento que passa da meia-noite volta a funcionar.

**📞 Chamadas de Voz, WebChat, Telegram e Chat interno**

* **WebPhone SIP** volta sozinho quando a conexão cai (aba minimizada, internet oscilando), mantém a conexão ativa com ajuste por usuário na Config SIP e avisa a chamada recebida com a aba escondida.
* **Link de convite do WebChat:** o cliente que vem do WhatsApp abre o link e continua a conversa no WebChat como o mesmo contato, e o visitante do WebChat deixa de receber dados internos do canal.
* **WebChat:** links enviados pelo atendente aparecem clicáveis para o visitante (link direto e widget novo), o texto aparece exatamente como foi escrito, e os widgets já instalados nos sites ficaram protegidos contra código injetado nas mensagens.
* **Convite do Telegram por link ou QR:** o cliente toca em Iniciar e o Telegram dele fica ligado ao cadastro certo, com os textos do bot editáveis por canal. Contatos juntados passam a receber Instagram, Messenger e Telegram sem perder o nome e a foto do WhatsApp.
* **Chat privado:** pesquisa por palavras nas conversas e nas equipes, com atalho que leva direto à mensagem. Cada pessoa só lê e cita as conversas e equipes de que participa.
* **Chat privado:** ícone próprio no topo com contador azul, lista de conversas com "Marcar como lida" e aviso que só some quando a mensagem é lida, inclusive com arquivo ou áudio.
* **Chat privado:** a confirmação de leitura (✓✓) aparece na hora, mensagens com a conversa aberta já ficam lidas, edição, exclusão e reação atualizam sozinhas, e "marcar tudo como lido" passa a valer só para quem clicou.

**📈 Dashboard**

* **TPR e TTE** passam a contar atendimentos com chatbot, fluxo e IA, com o TPR começando quando a automação entrega a conversa ao atendente. Fora do horário, a contagem começa no clique em Atender.

**⚙️ Superadmin, Planos e Pagamentos**

* **Troca de plano** cobra a diferença proporcional, o teste grátis vale com Stripe e Asaas, a configuração de pagamento sobrevive às atualizações do Docker e a área de pagamentos aparece para qualquer gateway.
* **Migração de empresa** mantém datas, ordem, citações e o número antigo dos atendimentos (com busca e selo), chega com canais desativados sem envio automático e ganhou o botão **"Reparar histórico"** para as empresas já migradas.

**🔧 Sistema e Infra**

* **Chat interno com armazenamento S3/R2** volta a encaminhar e baixar imagens (baixa na mesma aba, com o nome do arquivo). Galeria, respostas rápidas, catálogo, chat de suporte e PDF da conversa passam a funcionar com bucket sem CORS.
* A prévia de link e o download do painel ficaram protegidos contra acesso a endereços internos.

### v4.0.6

**🚀 UPDATE OFICIAL (HOMOLOG) | 29/09/2026**

Nova versão Homolog (v4.0.6.0), cumulativa de todas as correções publicadas desde a v4.0.5.0.

**👤 Página do Contato e Relacionamento**

* **Página própria do contato,** aberta pelo atendimento, pela lista de contatos ou pelo funil, com o resumo do cliente (atendimentos, cliente desde, vendas com estrelas, oportunidades, etiquetas e carteira).
* **Timeline** com todo o histórico do contato em ordem, e a aba **Relacionamento**, onde a equipe registra ligações, propostas e visitas com anexos e vincula tarefas.
* **4 relatórios novos:** ações por tipo, tarefas e funil por atendente, e ações até a venda. Também é possível escolher por quanto tempo o histórico fica guardado.

**💬 Atendimento e Tickets**

* A guia **Chatbots** do atendimento agora se chama **Automações** e mostra também as conversas com Agente de IA e integrações de IA ligadas, com um seletor para filtrar por tipo.
* **Ações em massa** ficaram bem mais rápidas e pararam de deixar o sistema lento para os outros atendentes. Encerrar vários atendimentos agora pede confirmação, com "não enviar despedida" já marcado.
* Criar atendimento pela tela ou pela API no mesmo instante em que chega mensagem do contato não gera mais dois atendimentos abertos para a mesma pessoa.
* Mensagens enviadas pela API e ações vindas de webhooks e do WebChat aparecem como **"Sistema"**, e não mais com o nome do administrador, do dono do atendimento ou de um usuário de outra empresa.
* Corrigido: atendimento encaminhado pelo chatbot **fora do horário** agora sai do robô, sem "Você está aí?" nem encerramento automático durante a noite.
* A tela de Atendimentos não trava mais quando a última mensagem é um texto longo com acentos, como transcrições de áudio.
* O **contador de mensagens não lidas** passa a ser calculado direto no atendimento, em todos os canais, contando certo em mensagens simultâneas e ao reabrir a conversa.
* A tecla **Esc** deixa de fechar a conversa aberta.

**🔔 Notificações**

* **Notificações no celular** voltam sozinhas depois de atualizar o app ou trocar de usuário no mesmo aparelho, e quem sai do sistema para de receber avisos naquele aparelho.
* O **sininho** deixa de mostrar atendimentos que já foram assumidos por outro atendente. Com a opção "não ver atendimentos atribuídos a outros" ligada, o atendente comum não consegue mais abrir o atendimento do colega nem pelo link direto.

**🧠 Agente de IA e Copiloto**

* **Novas ferramentas do Agente de IA** (aba Ferramentas): etiquetar o contato, mover no funil, anotar na ficha os dados que o cliente informa, registrar oportunidade, anotar no atendimento, avisar a equipe, encerrar o atendimento gravando o motivo, devolver a conversa para um fluxo automático, manter o cliente com o mesmo atendente por um tempo, consultar e reservar horário na agenda e programar uma mensagem para depois.
* O agente **aprende com arquivos JSON e Markdown**, passa a conversa para outro agente que já responde na mesma mensagem e pode consultar um especialista antes de responder.
* Botões **Mapa**, que mostra num desenho o que foi configurado, e **Duplicar**, que copia o agente junto com a base de conhecimento.
* O **WebChat** passa a acionar o agente vinculado ao canal e deixa de mostrar notas internas ao visitante.
* **Agente sem crédito na conta** transfere o atendimento na hora com uma nota explicando o motivo, e toda falha do provedor de IA passa a aparecer no log do servidor.
* **Gemini:** copiloto e bots voltam a funcionar com os modelos atuais do Google. A lista sugere só modelos ativos e o botão Testar deixou de acusar falha falsa em modelos que raciocinam.
* Na tela **IA da plataforma**, o "Testar conexão" explica o motivo da falha (conta sem crédito, modelo padrão não escolhido, chave recusada e outros).
* A **reescrita de mensagens com IA** respeita o idioma escolhido em Bots e IA, e a correção de ortografia mantém o idioma do texto digitado.

**🤖 Chatbot e Chatflow**

* O **número para teste** e a chave **Ativo** são salvos ao criar um fluxo, e duplicar um fluxo mantém número de teste, público-alvo, prioridade, horário e o estado ativo/inativo do original.

**📊 Kanban e Funil**

* O **calendário do funil** mostra todas as oportunidades de cada mês pela previsão de fechamento, até 5000 por mês, e avisa quando o mês passa desse limite.
* O **Dashboard do Funil** filtra por mês e período, e o gestor escolhe se as vendas contam pela data de criação ou pela data de fechamento.
* Ao **excluir uma etapa do funil**, o sistema avisa quando ela não pode sair e explica o motivo (oportunidades ganhas ou perdidas que não aparecem no quadro, ou ações do funil desativadas), em vez de dizer que salvou e a etapa voltar ao atualizar a página.

**👥 Contatos e Etiquetas**

* **Endereço completo** no contato, com CEP que preenche sozinho e filtro por bairro, cidade e UF na lista, no envio em massa e nas campanhas.
* Pedidos do **WooCommerce** e da **Nuvemshop** passam a atualizar endereço, CPF e aniversário do cliente.
* **Filtrar e exportar por várias etiquetas** ao mesmo tempo, escolhendo se o contato precisa ter todas ou qualquer uma. A planilha e os relatórios mostram todas as etiquetas de cada contato, e o relatório por carteira ganhou filtro e coluna de etiquetas.
* Supervisores voltam a ver os contatos das carteiras dos colegas ao filtrar por carteira em Contatos, Kanban, aniversariantes e exportação.
* Contatos não perdem mais foto e aniversário sozinhos.

**📢 Campanhas e Disparo em Massa**

* A tela de campanha explica que cada contato recebe só uma das 3 mensagens, sorteada, e avisa na hora qual delas falta preencher, sem deixar a campanha dar erro ao criar.
* **Disparo em massa de template** volta a funcionar para atendentes: o atendimento é criado no nome de quem dispara, vai para a fila ou usuário escolhido e não fica mais perdido quando o envio falha.

**📲 SMS**

* **SMS em massa em segundo plano,** com progresso na tela, registro no Relatório, cancelamento, retomada automática depois de reinício e proteção contra envio em dobro.
* **Comtele** volta a funcionar com as chaves do painel novo, com escolha da rota de envio, e o envio em massa mostra quantos SMS saíram e o motivo das falhas.

**✉️ E-mail Marketing**

* **Editor visual por blocos** para modelos, envios em massa e campanhas, com prévia no computador e no celular e imagens que aparecem direto na caixa do destinatário.

**📱 Canais Oficiais Meta (WABA / Instagram / Messenger)**

* **Canal WABA sem forma de pagamento ou bloqueado pela Meta** agora avisa quem administra os canais (faixa, card, selo e motivo no tique), com atalho para o WhatsApp Manager e o botão **"Já resolvi"**, que confere a situação na Meta.
* **Chamadas no WABA:** quem liga pela primeira vez recebe a mensagem de ligação não permitida e ganha atendimento com a janela de 24h aberta, contando como atendimento receptivo.
* **Instagram só com mensagens diretas:** o canal pode ficar só com DMs, os comentários deixam de abrir atendimento, e as automações de comentário continuam respondendo.
* **Automação do Instagram por comentário:** a imagem da DM é enviada assim que o contato responde, e a tela explica a regra da Meta e exige o texto de abertura.
* No Instagram, Messenger, 360dialog e Telegram, as respostas dos bots de IA e as mensagens automáticas (avaliação, despedida, fila, aniversário, fluxo) passam a aparecer sempre no histórico do atendimento.
* A **palavra-gatilho do Instagram e do Messenger** respeita o público do fluxo, não tira mais o atendimento das mãos do atendente e desliga o Agente de IA ao entrar no fluxo.

**📅 Agendamento**

* A tela de **Agendamentos** mostra todos os agendamentos com paginação, e a busca encontra qualquer agendamento, não só os da primeira página.
* A **agenda do Google** avisa na tela quando a conexão com a conta Google expira, em vez de mostrar a agenda vazia sem explicação, e para de repetir evento na segunda busca.

**📞 Chamadas de Voz, WebChat e Chat interno**

* O **WebPhone** ganhou o campo **"Domínio SIP"** na configuração do usuário e passa a funcionar com provedores que conectam por um SBC e identificam o ramal com outro domínio.
* WebChat e chamadas de voz passam a conectar de forma estável em instalações com múltiplos processos.
* **Chat privado:** as mensagens mantêm a ordem certa ao recarregar a tela mesmo quando os computadores estão com horários diferentes, e a hora mostrada passa a ser a do servidor.
* O **Rocket.Chat embutido** volta a abrir e entrar sozinho nos servidores Rocket.Chat 8, mostra o motivo real de cada erro, testa a configuração inteira em um clique e nunca entrega a um atendente a conta de outra pessoa.

**⚙️ Superadmin, Revendedores e Usuários**

* **Termos próprios do revendedor** (Superadmin → Customizar): publique seus termos, exija o aceite dos administradores das empresas clientes, com bloqueio até aceitarem, e consulte o registro de cada aceite (data, versão, IP e navegador).
* Nova tela **"Banco de dados"** no painel do superadmin, para consultar os dados e corrigir um registro por vez sem abrir o banco para fora, com segredos protegidos, senha ao abrir e registro permanente de tudo o que for executado.
* A tela de **Usuários** mostra quando cada pessoa fez o último login, com ordenação por essa coluna.
* A **exclusão de usuário** voltou a funcionar mesmo para quem já fez disparos em massa; quando algum vínculo impedir a remoção, a tela explica o motivo.
* Ao bater o **limite de usuários ou de conexões**, a tela diz exatamente isso, em vez de "Erro ao criar".

**🔧 Sistema e Infra**

* **Servidor mais leve e estável:** menos leitura de disco e travamentos na verificação de segurança, boot sem pico de memória, chat interno sem acúmulo de conexões e menos quedas de conexão com o banco.
* O **download de mídias grandes** no WhatsApp deixa de travar o servidor e de consumir CPU por minutos.
* As telas de **Configurações** passam a ser protegidas também no servidor.

---

### v4.0.5

**🚀 UPDATE OFICIAL (HOMOLOG) | 09/09/2026**

Correção cumulativa da versão Homolog atual (v4.0.5.0).

**Faça um BACKUP / SNAPSHOT antes de aplicar esta correção.**

Esta versão corrige o roteamento de mensagens do WhatsApp Oficial quando o mesmo cliente tem dois cadastros (BSUID) e ajusta o cadastro de contatos em vários canais — faça o backup antes de atualizar.

**Ajustes automáticos nesta atualização:** fluxos de chatbot afetados pelo inchaço da Tabela de Horários com mídias são limpos automaticamente, e a ação **"Bloquear Chatbot"** passa a valer também nos fluxos já existentes.

**💬 Atendimento e Tickets**

* **Colar (Ctrl+V) imagem** copiada direto da conversa ou de qualquer página do navegador — antes só a imagem de print de tela ou de arquivo era anexada.
* **Encerrar em massa por período:** no painel de atendimentos, é possível encerrar de uma vez todos os atendimentos do período filtrado, sem enviar mensagem de despedida aos contatos.
* **Ações em massa com tela de progresso:** contagem de tickets processados, execução que segue até o fim mesmo se algum falhar, e resumo de quantos deram certo e quantos falharam.
* Mensagens que o WhatsApp não conseguiu entregar deixam de aparecer como "tipo de mensagem não suportado" e passam a avisar que a mensagem está indisponível, com orientação de pedir o reenvio ao cliente — no idioma do painel.
* **Mais segurança e confiabilidade:** a API externa limita dados internos do canal, mensagens recebidas em rajada no WhatsApp Oficial não se perdem mais, conversas duplicadas por mensagens simultâneas deixam de acontecer, e a transferência de canal avisa quando o contato já tem atendimento aberto no destino.
* A **fila padrão do canal** volta a ser aplicada no WhatsApp Oficial (Meta) quando o canal também tem chatbot, e nos canais de e-mail (IMAP/POP3/Gmail) a fila e o atendente padrão passam a ser aplicados.
* No **celular**, a tela de atendimento não corta mais a lateral ao digitar, e as imagens recebidas ficam corretamente dentro do balão da conversa.
* Adicionar nota ou editar dados de um atendimento na aba **Fechados** não faz mais o atendimento sumir da lista nem fechar a conversa.
* Corrigido: o cabeçalho da janela **"Espiar atendimento"** estourava os botões Encerrar/Atender quando o contato tinha nome longo (comum no canal de e-mail).

**🔔 Notificações e Sininho**

* **Pushs:** as notificações e mensagens do sistema deixaram de usar símbolos decorativos, mantendo intacto o texto e o nome escritos pelo cliente.

**📞 Chamadas de Voz (WebPhone e SIP)**

* **Toque de chamada personalizado:** basta colocar um arquivo `ringtone.wav` na pasta pública do sistema; sem arquivo, o toque continua exatamente como era.
* Chamada em andamento não é mais derrubada quando outra chega.
* Corrigido o **botão SIP** do contato, que mostrava "Chamando..." sem completar a ligação — agora ele disca de verdade pelo WebPhone, já com o número preenchido, e avisa na tela quando a chamada não pode ser iniciada.
* **Chamadas de voz do Dialog360 e do Gupshup:** planejamento concluído, liberação em etapa seguinte.

**🧠 Copiloto e Agente de IA**

* **Copiloto:** "Copiar texto", "Pergunte ao ChatGPT" e "Traduzir" voltaram a aparecer nas mensagens recebidas por WhatsApp Oficial, Instagram, Messenger, Dialog360 e Gupshup.
* Resumos, análises de sentimento e insights de IA agora saem no **idioma escolhido por cada atendente** na tela.
* **Agente de IA:** corrigida a perda de memória entre mensagens (o agente voltou a considerar a conversa inteira); a transferência só é anunciada ao cliente depois de acontecer de verdade; e o agente ganhou **ferramentas externas** para consultar dados nas suas automações antes de responder.
* O **assistente de IA do fluxo de atendimento** entende a intenção do cliente e age sozinho — transfere para a equipe ou o atendente certo, sem exigir que o cliente digite palavras exatas.

**📊 Kanban e Funil**

* **Envio de mensagem pelos cards do funil** volta a funcionar para atendentes e permite escolher se o atendimento nasce em nome do atendente ou fica aguardando na fila.
* Corrigido: alerta indevido de "canal excluído" nas ações do funil quando a ação usava canal de template (WhatsApp Oficial e BSPs) ou um canal apenas desconectado.

**🤖 Chatbot e Chatflow**

* **Filtros de público do chatbot** passam a valer de verdade em todos os canais: contato fora do público não recebe mais o robô (nem pelo fluxo padrão da conexão), atendimentos presos num robô mudo vão direto para a equipe, etiquetas com espaço extra deixam de quebrar o filtro, e os motivos de silêncio do robô aparecem no log.
* Corrigido: **etiqueta definida por automação** durante o fluxo do bot não some mais do atendimento quando o bot envia a mensagem seguinte (canal WhatsApp API Oficial).
* Corrigido: a ação **"Bloquear Chatbot"** do construtor de fluxos não marcava o contato como bloqueado ao passar pela etapa — agora o bloqueio é aplicado corretamente, inclusive em fluxos já existentes.
* Corrigido: **inchaço do fluxo** ao usar Tabela de Horários com mídias — o salvamento reenviava cópias internas dos passos (com vídeos embutidos), estourando o limite e travando o editor; fluxos afetados são limpos automaticamente na atualização.

**📢 Campanhas e Disparo em Massa**

* Ao **editar uma campanha**, o arquivo de mídia já anexado aparece na tela, com opção de remover ou substituir — antes o campo voltava vazio e dava a impressão de que a mídia tinha se perdido (ela sempre foi enviada normalmente).
* O **template escolhido e os valores das variáveis** aparecem preenchidos ao reabrir a campanha, sem precisar recarregar a tela.
* Confirmações de envio ficaram mais leves no banco de dados: contas que não usam campanhas deixam de fazer verificações desnecessárias a cada mensagem.

**💳 Cobrança (Pix, Boleto e Link)**

* **Templates de pagamento pelo painel:** podem ser criados direto pelo painel, e os dados do Pix, boleto ou link deixaram de ser recusados por formato — o sistema avisa, mas quem decide o que cobrar é você.
* **Templates de cobrança:** o texto do botão de pagamento já vem pronto e não pode mais ser alterado por engano; o envio avisa o que está faltando — a ficha de pagamento ou o código de um botão — em vez de mostrar um erro genérico.
* **Permissão por empresa:** dá para liberar que atendentes comuns enviem cobranças por Pix, link ou boleto — e quem não tem permissão vê o aviso antes de preencher a cobrança, em vez de descobrir só ao tentar enviar.

**📱 Canais Oficiais Meta (WABA / Instagram / Messenger)**

* **Cliente com dois cadastros (BSUID):** a mensagem do WhatsApp Oficial deixa de se perder quando o mesmo cliente está cadastrado duas vezes — a conversa passa a cair no cadastro correto, e um relatório aponta os cadastros duplicados para união.
* **Cliente sem número (nome de usuário):** quem fala pelo WhatsApp Oficial usando nome de usuário é atendido normalmente — o atendente consegue responder, o cadastro salva sem exigir telefone, e há um botão para pedir o número ao cliente pelo caminho oficial do WhatsApp.
* **Criação de templates:** o campo de cabeçalho mostra o limite de caracteres e um contador, e o gerador por IA respeita os limites automaticamente.
* **Formulários do WhatsApp (Flows):** as respostas aparecem preenchidas no histórico e dão sequência ao chatbot também nas conexões 360dialog e Gupshup; a lista de conversas e os relatórios mostram o que o cliente respondeu em vez de texto técnico; campanhas passam a enviar botões de formulário e catálogo; e o envio de formulários aceita seleção por nome com cabeçalho de imagem, vídeo ou documento.
* **Modo Coexistência:** botões e listas enviados no atendimento aparecem na tela já como o cliente recebe (menu numerado), o atendente vê um aviso antes de enviar, e o canal ganhou a opção **"Botões e listas pela API oficial"** para entregá-los como botões de verdade.

**👥 Grupos**

* **Link de convite dos grupos** é entregue pela API, com aviso do motivo quando não for possível gerá-lo, e há um novo recurso para revogar o link atual e criar outro na hora.

**🛍️ Marketplaces e Hub (Mercado Livre)**

* **Mercado Livre:** as reclamações do comprador chegam dentro da própria conversa — com resposta pelo mesmo campo de sempre — e o atendimento aberto avisa quando o pedido muda de status; a reclamação vai direto para atendente, sem chatbot.

**🤝 WebChat / Chat do site**

* **Link direto e responsivo:** o WebChat pode ser usado por um link — ideal para aplicativos, portais e QR Codes —, com uma página de conversa pronta que abre sem precisar colar código no site (**Configurações → WebChat**).
* **Citação de mensagens:** respostas do atendente aparecem com a citação no chat do cliente (widget e link direto), com clique para pular até a mensagem original.
* **Celular:** o chat abre em tela cheia corretamente — o cabeçalho e o botão de fechar voltaram a aparecer, os botões de anexar e enviar não ficam mais escondidos atrás do balão flutuante, a tela para de deslocar ao tocar no campo de mensagem, funciona também com o celular deitado e, em telas baixas, o painel se ajusta sozinho para o cabeçalho e o botão de fechar nunca ficarem fora da tela.

**📣 Publicação em Redes Sociais (Instagram e Facebook)**

* Publicação de posts no Instagram e no Facebook voltou a funcionar em contas com armazenamento em nuvem — a imagem passa a ser enviada ao armazenamento antes da publicação, valendo também para posts agendados, rascunhos e mídias de resposta rápida.

**🔗 API e Integrações Externas**

* **Responder qualquer conversa pelo número do atendimento (ticket):** texto e arquivos em WhatsApp, Instagram, Messenger, Telegram, Webchat, E-mail, Hub e Mercado Livre pelo mesmo endpoint, com reabertura opcional do atendimento fechado.
* O **canal de e-mail** avisa por webhook quando uma nova mensagem chega.
* **Criar empresa pela API com plano:** os limites e recursos do plano são aplicados na hora, e um plano inexistente é recusado sem criar nada.
* **Descarteirizar contato pela API:** enviar a lista de carteiras vazia remove todas, e carteiras inválidas ou de outra empresa são recusadas com aviso claro em vez de erro genérico.
* **Documentação da API no painel** revisada de ponta a ponta, com correção dos campos e exemplos de rotas que não batiam com o que a API realmente aceita — a tela de APIs e o Postman foram atualizados.

**👥 Contatos e Importação**

* **Cadastro por vCard** passou a tolerar falha na busca da foto de perfil, como já acontece no cadastro pelo menu: o contato é salvo mesmo quando o canal não consegue devolver a imagem.
* Corrigido: a **consulta de diagnóstico de contatos sem telefone** — o canal do atendimento é lido do próprio atendimento, não do cadastro do contato.

**📈 Relatórios, Dashboard e Avaliações**

* **Relatório de oportunidades em CSV** agora traz nome, telefone e e-mail do contato (além dos nomes de funil, etapa e responsável), com o telefone preservado por inteiro ao abrir na planilha.
* **Atendimentos de grupo fora dos tempos médios:** nova opção nas configurações da empresa permite tirar as conversas de grupo dos tempos médios dos relatórios, sem que elas sumam das contagens.
* **Avaliações:** as estrelas acompanham a pontuação máxima configurada em toda parte (configuração, listagem, filtro e histórico do atendimento) — escalas menores que 5 não mostram mais estrelas sobrando, a nota 0 ficou filtrável, e a mensagem padrão de reenvio cita a escala correta.

**📅 Agendamento e Aniversários**

* **Google Agenda por página:** escolha qual agenda do Google cada página de agendamento usa, marque uma agenda padrão para o resto do sistema, e compromissos de agendas secundárias passam a bloquear horários corretamente.
* Cada página de agendamento e cada profissional aponta para a agenda e o calendário certos do Google; compromissos já marcados deixam de ser oferecidos como horário livre; e cancelar ou remarcar pelo painel também atualiza o Google.
* **Lista de consultas paginada,** com filtros de situação, período e busca, e calendário que carrega as consultas do mês exibido — antes a tela parava nos 100 primeiros registros e os meses futuros apareciam vazios.
* **Google Agenda resiliente a rede:** em vez de erro, o sistema repete a consulta sozinho e, se a listagem de agendas falhar, continua mostrando os compromissos da agenda principal.
* **A agenda voltou a abrir para atendentes** e passou a ter permissão própria — ligar ou desligar o Kanban não afeta mais a agenda, e cada item desativado no painel bloqueia só a sua própria tela.
* **Mensagem agendada disparada** deixa um aviso na conversa marcando a hora do envio e o trecho do texto, para a resposta do cliente fazer sentido na ordem — com interruptor por empresa em **Configurações → Geral**.

**⚙️ Superadmin, Planos e Pagamentos**

* **Limites por tipo de canal** passam a valer para WhatsApp Oficial via login, Instagram, Facebook e canais Hub; as telas de empresas e planos mostram uma linha por tipo real; empresas presas na lista padrão antiga ganham os canais oficiais e marketplaces; e a janela de login do Facebook, Instagram e WhatsApp Oficial passa a dizer o motivo real da recusa.
* Corrigido: o **aviso de teste grátis no menu** mostrava sempre 31 dias e ignorava a duração configurada da empresa — agora exibe os dias reais, a data de encerramento e avisa quando o prazo passa a ser a primeira cobrança.
* Corrigido: rótulos e avisos com texto técnico na **tela de edição de canal do superadmin**, agora traduzidos em todos os idiomas.

**🔐 Perfis, Permissões e Menus**

* **Restrições de menu da plataforma** valem para todos os perfis de usuário da empresa — itens desativados somem do menu e da busca e ficam bloqueados por link direto, sem exceções por tipo de conta.
* **Menu Funil por usuário:** pode ser liberado ou ocultado por usuário, e a tela de usuários do superadmin ganhou o mesmo formato de permissões de menu das demais telas.
* **Tela de perfis de acesso:** corrigida a falha que quebrava a janela de permissões ao abrir, e a permissão de **cobranças** passou a ser marcável no perfil personalizado.

**✉️ E-mail e E-mail Marketing**

* **Novo módulo de E-mail Marketing:** crie modelos de e-mail com editor visual e variáveis, dispare campanhas e envios em massa pelos seus canais de e-mail (Gmail e SMTP/IMAP), com link de descadastramento automático, lista de bloqueio e ações automáticas quando o contato responde.

**🎨 Interface, Navegação e Configurações**

* **Ícone no card de compartilhamento:** ao compartilhar o link do sistema no WhatsApp e em outras redes, a imagem do card é sempre o ícone personalizado da instalação, mesmo em instalações que enviaram o ícone há mais tempo.
* **Tela de boas-vindas:** depois de fechada uma vez, fica marcada como lida na conta do usuário e não aparece mais, nem ao trocar de navegador, aparelho ou limpar o cache.

**🔧 Sistema, Armazenamento e Infra**

* **Backup por empresa** começa na hora e avisa na tela enquanto roda — acabou o falso "erro ao iniciar" em backups grandes, que na verdade terminavam normalmente.
* **Limpeza de arquivos antigos:** a exclusão automática agora libera espaço em disco, e o envio para o armazenamento externo avisa antes o que será apagado do servidor.
* **Cloudflare R2:** a URL pública deixou de aparecer como opcional — agora é destacada como obrigatória, com explicação no próprio campo, e as mensagens de erro ao salvar dizem exatamente o que falta corrigir.

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

**🛍️ Marketplaces e Hub (Mercado Livre, OLX, LinkedIn, YouTube)**

* Respostas pelos canais **Mercado Livre, OLX, LinkedIn e YouTube** funcionam de ponta a ponta, e envios que falham passam a mostrar erro claro no chat em vez de constar como entregues.
* **Mercado Livre:** o ticket mostra o nome do comprador e o anúncio/produto da conversa (título, imagem e link), sem precisar abrir o Mercado Livre.

**🔗 API e Integrações Externas**

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

* Corrigido: mensagens agendadas com template exibem as variáveis preenchidas na tela de Agendamentos e no chat (o envio ao contato já estava correto).
* Corrigido o horário exibido nas consultas da agenda: a data/hora agora aparece igual na lista, no calendário e na tela de edição (a servidor em nuvem deve estar no timezone `America/Sao_Paulo`).
* Na lista de aniversários, ordenar por qualquer coluna considera todos os contatos, e não apenas os da página aberta.

**⚙️ Superadmin, Planos e Pagamentos**

* **Alterar as funcionalidades de um plano vale na hora** para os clientes que já estão nele — antes só valia para novas contratações.
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
* **PDF com impressão automática** (comum em faturas/2ª via) não abre mais o diálogo de imprimir sozinho — o comando é neutralizado na visualização e a pré-visualização carrega somente após um clique, mantendo o download do arquivo original intacto.
* **Notificações:** popup nativo do navegador para ticket novo em pendentes e opção de limitar notificação de chatbot (Configurações Gerais).
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

* **Projeção de custos de mensagens WABA** na configuração Meta.
* Limites da WABA aplicados ao tamanho dos inputs (botões, listas e templates) e correção do erro de "credenciais incompletas" ao criar template (exigia F5).
* Correções WABA/Meta: canal duplicado no re-onboarding, resolução número→canal prioriza a linha CONNECTED, envios com erro marcados e logados, app WABA próprio + OAuth Instagram, OAuth Facebook + Instagram em conjunto e login com Facebook preso em "Carregando SDK…".
* Assinatura com `*asterisco*` suprimida em canais não-WhatsApp.
* **Dialog360:** sanitização de payload e log de debug para coexistência via `DIALOG360_RAW_DUMP` (.env do backend). **Gupshup e Dialog360:** base64 no payload do n8n (canal).

#### 🔗 API e Integrações Externas

* Correções: `/getMessagebyId` + `mediaUrl`; envio base64 com caption de mídia.
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

### Histórico das versões antigas (antes da v4.0)

Nas páginas seguintes você encontra o histórico completo das versões anteriores.

[AnteriorAtualizações e Status do Prismabot](/central-do-assinante/atualizacoes-e-status-do-z-pro)[PróximoValidade das versões](/central-do-assinante/atualizacoes-e-status-do-z-pro/changelog-4.0.x-ultima-versao/validade-das-versoes)

Atualizado há 10 dias

Isto foi útil?