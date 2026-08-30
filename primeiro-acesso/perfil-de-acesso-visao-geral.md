Copiar

Nesta página

1. [Primeiro Acesso](/primeiro-acesso)

# Perfil de Acesso: Visão Geral

O Prismabot organiza o acesso em duas camadas: o **Superadmin**, dono da instalação, e, dentro de cada empresa (tenant), quatro **perfis de usuário** — Administrador, Supervisor, Atendente e Perfil Personalizado. Este artigo explica o que cada perfil vê e pode fazer, como configurar isso na criação/edição de um usuário, e reúne as regras de visibilidade atualizadas (permissões e segurança).

Cada seção abaixo linka para a página de referência com o passo a passo completo — use este artigo como ponto de partida, não como substituto das páginas detalhadas.

---

### As duas camadas da plataforma

**Superadmin** — dono da instalação. Gerencia licença, tenants, planos e configurações globais que afetam todos os clientes da instância. Veja [Visão geral Superadmin](/configuracao-superadmin/visao-geral-super-admin). Não é o foco deste artigo — os perfis abaixo existem **dentro** de cada tenant.

**Dentro do tenant** — os quatro perfis geridos em **Administração → Usuários**. Veja [Visão geral Admin](/configuracao-administrador/visao-geral-admin) e [Usuários](/configuracao-administrador/administracao-painel-admin/usuarios).

---

### Os 4 perfis dentro do tenant

#### 1. Administrador

Acesso total e irrestrito a todos os atendimentos, menus e configurações. É o único perfil que pode conectar/excluir canais, gerenciar a assinatura e alterar API/Webhooks. Com a v4.0.4.0, nada muda no uso normal do Administrador — ele continua vendo tudo.

#### 2. Supervisor

* **Sem restrições configuradas:** vê todos os atendimentos, como o Administrador.
* **Com "Visualização por Departamento" ativada + filas atribuídas:** vê apenas as filas dele, mais os próprios atendimentos, convites e grupos.
* **Com "Visualização por Departamento" ativada mas sem filas atribuídas:** continua sem restrição.
* **Com canais restritos:** vê apenas os canais atribuídos a ele.
* **Novidade 4.0.4.0:** o próprio supervisor não pode mais alterar sua "Visualização por Departamento" — só um Administrador faz essa mudança, editando o cadastro dele.
* Existe também um interruptor global que rebaixa **todos** os supervisores ao comportamento de atendente comum — veja "Remover privilégios de visualização do supervisor" em Configurações Gerais.

#### 3. Atendente

* **Com filas atribuídas:** vê as filas dele, mais atendimentos próprios, convites, carteira e grupos.
* **Sem filas atribuídas:** continua vendo os atendimentos não atribuídos a ninguém.
* **Sem canais restritos:** vê todos os canais.
* **Com canais restritos:** vê apenas os canais atribuídos a ele.
* Um atendimento que já é dele continua acessível mesmo se o canal correspondente for excluído depois.
* Independente de fila/canal, existe também a opção **Usuário Restrito**, voltada à privacidade dos dados do contato (LGPD) — é um eixo separado, veja Restrição de Acesso a Contatos.

#### 4. Perfil Personalizado

Templates de permissão granular, reutilizáveis entre vários usuários. Veja o passo a passo completo de criação em Perfis de Acesso.

**Novidades para Perfil Personalizado:**

* Agora **entra no roteamento automático** — antes, um perfil personalizado era invisível para o bot e para a distribuição de fila e nunca recebia atendimento automático. Se você modelou um perfil de supervisão que não deveria atender diretamente, revise as permissões dele.
* Passaram a **exigir marcação explícita de permissão** para continuar funcionando:

  Ação

  Permissão que precisa estar marcada

  Criar, editar e excluir canal (inclusive o Login com Facebook)

  Gerenciar sessões

  Salvar qualquer configuração da empresa

  Configurações gerais

  Salvar horário de atendimento e feriados

  Gerenciar horários

  Marcar todos como não lidos

  Atribuir atendimentos
* Com **acesso total** marcado, o perfil mantém visão completa; sem acesso total, segue as mesmas regras de fila e canal do Atendente/Supervisor descritas acima.
* A página **Agenda** passou a depender da capability própria do plano (`agenda`), e não mais da capability do Funil (`funnelKanban`). Um plano que tem Funil mas não tem Agenda passa a bloquear a Agenda — antes ela "entrava de carona".

---

### Regras que valem para todos os perfis

* **Notificações seguem exatamente as mesmas permissões da tela de Atendimentos** — o usuário só é avisado de conversas que ele realmente pode abrir.
* **Reforço de segurança no servidor:** um atendimento fora do alcance do usuário não pode mais ser aberto nem respondido por link direto — a restrição deixou de valer só na interface.
* **Conversas com o robô** ficam ocultas apenas enquanto estão em atendimento pelo chatbot. Depois que o robô encaminha para uma fila, elas voltam a aparecer para quem tem acesso àquela fila.
* **Carteira:** o dono da carteira volta a visualizar e a ser avisado dos atendimentos do seu contato, mesmo que o atendimento não esteja na fila dele.
* Alterações de permissão em um usuário levam **até 30 segundos** para valer.

Para a tabela completa de combinações (padrão × "não visualizar atribuídos" × "visualizar sem dono/fila" etc.), veja Visibilidade de Tickets para usuários (atendentes).

---

### Como limitar o que um usuário vê ao criar (ou editar) o cadastro

Em **Administração → Usuários → + Novo Usuário** (ou editando um usuário existente), os campos abaixo controlam o que ele vê e pode fazer:

Campo

O que controla

**Perfil\***

Administrador, Supervisor, Atendente ou Personalizado. Não é possível criar um usuário com perfil superior ao seu próprio (regra nova da 4.0.4.0).

**Usuário Restrito**

Blindagem de dados sensíveis do contato (nome parcial, foto borrada, campos ocultos) — ver Restrição de Acesso a Contatos.

**Bloquear WaVoIP**

Impede chamadas pela plataforma. Aparece na edição de Supervisor e Atendente.

**Visualização por Departamento**

Só aparece para o perfil Supervisor — restringe a visão dele às próprias filas.

**Permissões de Menu**

Checklist dos módulos visíveis no menu lateral. **O conjunto de opções oferecido muda conforme o Perfil selecionado** — um Atendente recebe uma lista mais enxuta (módulos operacionais como Envio em Massa, Grupos, Chat Privado, Kanban, Tarefas, Campanhas e Contatos), enquanto Supervisor e Administrador recebem a lista completa, incluindo Relatórios, Painel de Atendimentos, Filas, Equipes, Sessões, Chatbot e demais módulos de configuração.

**Config SIP**

Ramal e credenciais de telefonia IP (opcional, colapsado).

**Horário de Atendimento**

Define, dia a dia, os turnos em que o usuário fica disponível para novos atendimentos.

---

### Depois de criar: vinculando canais e filas

Na listagem de **Usuários**, dois ícones por linha controlam o escopo do usuário:

* **Ícone Canais (celular):** abre o modal **Conexões de [usuário]**, com os canais agrupados por **Meta (Oficial)** e **Outros**. Marque só os canais que esse usuário deve acessar — sem nenhum marcado, ele vê todos os canais.
* **Ícone Gerenciar Filas (vínculo):** abre o modal **Filas de [usuário]**, com a lista de filas cadastradas (mesmas cores definidas em Filas).

**Novidade 4.0.4.0:** essas restrições agora são reforçadas também no **servidor** — não é mais só uma questão de esconder na interface. Tentar abrir, por link direto, um atendimento de um canal ou fila fora do que foi marcado aqui passa a ser bloqueado.

---

### Editando o próprio cadastro

A partir da 4.0.4.0, editar o **próprio** usuário ficou mais restrito:

* Um usuário sem permissão de gestão não pode mais alterar as próprias filas, canais, horário de atendimento, e-mail ou senha.
* **Ninguém altera o próprio Perfil ou as próprias Permissões**, nem mesmo o Administrador — o campo aparece bloqueado com o aviso *"Você não pode alterar o próprio perfil nem as próprias permissões. Peça a outro administrador."*
* Criar um novo usuário passou a exigir permissão de gestão, e não é mais possível criar um perfil superior ao próprio.
* A API deixou de criar contas de nível plataforma — continua criando normalmente Administrador, Supervisor, Atendente e Perfil Personalizado.

---

### Configurações Gerais relacionadas

Estas opções, em [**Configurações → Gerais → Geral**](/configuracao-administrador/configuracoes-painel-admin/configuracoes-gerais), mudam o comportamento de visibilidade para todos os perfis de uma vez. Veja o detalhamento de cada uma em Configurações Gerais:

* **Não visualizar Tickets já atribuídos a outros usuários**
* **Não visualizar Tickets no ChatBot**
* **Forçar atendimento via Carteira**
* **Visualizar Tickets sem Usuário ou Fila Atribuído**
* **Remover privilégios de visualização do supervisor**
* **Habilitar perfis personalizados** — pré-requisito para usar Perfil Personalizado
* **Privacidade do Funil**
* **Receptivo apenas por fila**
* **Permitir somente admin excluir contatos**
* **Ativar Filtro de tickets no socket**

---

[AnteriorPrimeiro Acesso ao Sistema](/primeiro-acesso/primeiro-acesso-ao-sistema)[PróximoVisão geral Superadmin](/configuracao-superadmin/visao-geral-super-admin)

Atualizado há 9 dias

Isto foi útil?