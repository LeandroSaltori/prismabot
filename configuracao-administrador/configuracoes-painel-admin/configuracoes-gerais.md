# Configurações Gerais

## Configurações Gerais

{% hint style="warning" %}
**Disponível para o perfil:** Administrador
{% endhint %}

A página de **Configurações Gerais** é o centro de controle mestre do sistema Prismabot. Nela, o administrador define as regras globais que regem a visibilidade dos atendimentos, o comportamento dos bots, a organização da lista de chats e comandos técnicos de manutenção. Estas configurações permitem personalizar a experiência da plataforma de acordo com o volume de demanda e a estrutura hierárquica da empresa.

#### Como acessar a página

Clique no Menu **Configurações**, selecione a aba **Gerais** e clique no subitem **Geral**.

<figure><img src="/files/HbG2CoF67K6OP6wBj6Qp" alt=""><figcaption></figcaption></figure>

***

## Explicação dos campos

#### Detalhamento das Configurações

Abaixo estão listadas todas as opções disponíveis, divididas por blocos operacionais:

**1. Tickets e Visibilidade**

Controla as permissões de acesso e o que cada usuário pode visualizar na tela de atendimentos.

* [**Não visualizar Tickets já atribuídos a outros usuários:** ](/configuracao-administrador/configuracoes-painel-admin/configuracoes-gerais/visibilidade-de-tickets-para-usuarios-atendentes.md)Restringe a visão de usuários comuns apenas aos seus próprios atendimentos e tickets pendentes.
* **Não visualizar Tickets no ChatBot:** Oculta tickets que ainda estão em interação exclusiva com o [ChatFlow](broken://pages/wY1o2jf1H5pRdslBfSrJ).
* **Forçar atendimento via Carteira:** Prioriza o redirecionamento de novos tickets para o dono da Carteira de Clientes.
* **Visualizar Tickets sem Usuário ou Fila Atribuído:** Permite que usuários comuns vejam tickets que entraram no sistema sem destino definido.
* **Remover privilégios de visualização do supervisor:** Quando ativo, iguala a visão do Supervisor à de um Usuário comum.
* [**Habilitar perfis personalizados:**](/configuracao-administrador/administracao-painel-admin/usuarios/perfis-de-acesso.md) Libera a funcionalidade de criar Perfis de Acesso customizáveis.
* **Privacidade do** [**Funil**](/ferramentas-do-atendimento/gestao/funil-de-vendas.md)**:** Restringe a visualização de cards no Kanban apenas ao responsável por cada oportunidade.
* **Usar Envio Rápido de Mensagens:** Desabilita o intervalo de segurança entre envios (cadenciamento).

**2. Bot e Chatbot**

Define as regras de interação automatizada e comportamento de mídias sociais.

* **Fluxo ativo para o Bot de atendimento:** Seleciona o [ChatFlow](broken://pages/wY1o2jf1H5pRdslBfSrJ) padrão global.
* **Ignorar Mensagens de Grupo:** O sistema não abre tickets para interações em grupos de WhatsApp.
* **Ignorar Stories do Instagram:** Impede a abertura de tickets por menções ou reações em Stories.
* **Mostrar Grupos para todos os usuários:** Define se a aba de grupos é pública ou restrita por fila.
* **Mostrar Fechados para todos os usuários:** Permite que usuários comuns consultem o histórico de tickets encerrados.
* **Mensagem para chamadas no Whatsapp:** Habilita o aviso automático para tentativas de ligação de voz/vídeo.
* **Mensagem ao receber ligação:** Campo para personalizar o texto de aviso de chamadas desabilitadas.
* **Habilitar guia de atendimento de Chatbots:** Adiciona uma visão lateral exclusiva para monitorar bots.

<figure><img src="/files/MqXydGLd7n0Q5vyWqeGJ" alt="" width="360"><figcaption></figcaption></figure>

* **Fixar conexões no topo do atendimento:** Fixa os ícones dos Canais no topo da barra lateral de chats.

<figure><img src="/files/meR8qOOxTmRpzOALW0Bc" alt="" width="360"><figcaption></figcaption></figure>

* **Forçar usuário atual ao mudar status do atendimento pendente:** Mantém o vínculo do atendente ao mover o ticket de "Aberto" para "Pendente".

**3. Organização e Distribuição**

Configurações técnicas de exibição e roteamento de dados.

* **Mostrar histórico de mensagens:** Define a visibilidade de mensagens de atendimentos anteriores do contato.
* [**Tipo de Listagem de Mensagens:**](/configuracao-administrador/configuracoes-painel-admin/configuracoes-gerais/tipo-de-listagem-de-mensagens.md) Escolha entre Histórico por Fila ou outras lógicas de exibição.
* **Provedor de Videochamada:** Define entre Jitsi ou Google Meet para reuniões no chat.
* **Roteamento de chamadas WABA:** Define para quais agentes o sistema notifica ligações em Canais Oficiais.
* **Listar atendimentos pela última mensagem:** Ordena a fila pelo horário da interação mais recente.
* **Inverter ordem da lista de atendimentos:** Exibe os tickets do mais antigo ao mais novo no topo.
* **Validar Contato:** Executa validação de número no cadastro para contas WABA.
* **Ativar escuta da API do Hub Notificame:** Integração específica para recepção de mensagens via API Hub.
* **Ativar Filtro de tickets no socket:** Otimiza a performance em alto volume, filtrando notificações no servidor.
* **Desativar integrações externas quando carteirização estiver ativa:** Desliga bots (IA/Typebot) se o contato tiver dono de carteira.
* **Liberar contatos carteirizados para todos os atendentes:** Permite busca global de contatos mesmo que tenham dono definido.
* **Permitir somente admin excluir contatos:** Restringe a exclusão de cadastros apenas ao perfil Administrador.
* **Esconder pagamentos de usuários comuns (LGPD):** Oculta abas de faturas e dados financeiros de atendentes.
* **Receptivo apenas por fila:** Atendentes recebem tickets baseados apenas em suas filas vinculadas.
* **Comentários do YouTube criam tickets:** Transforma comentários em vídeos em atendimentos no painel.
* **Habilitar espera no processamento de mensagens com integrações externas:** O sistema aguarda a resposta da IA antes de processar novas entradas do cliente.
* [**Transbordo de Mensagens:**](/configuracao-administrador/configuracoes-painel-admin/configuracoes-gerais/transbordo-de-mensagem-processo-de-selecao.md) Move tickets de usuários offline para outros disponíveis.
* **Habilitar envio de mensagem Waba fora da janela:** Permite tentativa de envio após disparos de templates (sem garantia de entrega).
* **Não atualizar nome ao receber mensagens:** Impede que o sistema mude o nome do contato salvo para o nome do perfil do WhatsApp do cliente.
* **Modo BSUID estrito (WABA 2026):** Parâmetro técnico para usernames privados na API Oficial.
* **Forçar admin no atendimento:** Tickets pendentes sem destino são atribuídos automaticamente ao Admin.
* **Desabilitar marcação LID (UAZAPI):** Configuração técnica exclusiva para integração UAZAPI.

**4. Atendimento e Recursos**

Controle de ferramentas do chat e regras de inatividade (Timeouts).

* **Desabilitar controle de assinatura:** Torna a assinatura do atendente obrigatória em todas as respostas.
* **Controle de Features:** Gerencia permissões de "Espiar" e "Fechamento Forçado".
* **Forçar definição de demanda no fechamento:** Obriga o uso de Motivos de Fechamento.
* **Permitir pausar atendimento:** Habilita o botão de pausa na barra de ferramentas do atendente.
* **Despausar quando o cliente responder:** Quando ativado, o atendimento pausado é retomado automaticamente ao receber uma mensagem do cliente e volta a ser pausado após a resposta do operador.
* [**Carência pós-atendimento:** ](/configuracao-administrador/configuracoes-painel-admin/configuracoes-gerais/carencia-pos-atendimento.md)Se o cliente responder dentro do período configurado após o encerramento, o atendimento reabre automaticamente para o colaborador que o atendeu, sem passar pelo chatbot.
* **Janela de roteamento de agendadas:** Quando uma mensagem agendada possui fila ou usuário configurados, a resposta do contato dentro do período definido é direcionada diretamente ao destino, sem passar pelo chatbot. Defina 0 para desativar.
* **Ficar offline ao fechar a aba:** Quando ativado, fechar a última aba do sistema marca o usuário como offline automaticamente, sem necessidade de fazer logout.
* **Reabrir toma posse do atendimento:** Ao reativar um ticket fechado, o usuário torna-se o novo responsável.
* **Contador nas tabs superiores:** Exibe números de tickets em cada aba (Privados/Grupos).
* **Usar Plugin de Áudio:** Ativa o motor de áudio em versão beta.
* **Usar Módulo de Áudio com Ondas:** Exibe visualização gráfica de ondas sonoras nas mensagens de voz.
* **Persistir Download de Mídias (Baileys):** Realiza múltiplas tentativas de download de arquivos em canais não oficiais.
* **Usar horários de atendimento do usuário:** Aplica a jornada individual do colaborador para definir sua disponibilidade.
* **Web Push para Chat Interno:** Envia notificações push exclusivas para o Chat Privado.
* **Limitar Push ao Destinatário:** Notifica apenas o dono do ticket, independente do perfil.
* **Notificações sonoras:** Habilita alertas de áudio para novas interações.
* **Resolver atendimento sem interação automaticamente:** Ativa o encerramento por inatividade.
* **Escolha uma opção de tempo:** Define o período para o encerramento automático (Preset ou Personalizado).
* **Digite o tempo em minutos:** Campo numérico para definir o timeout (ex: 5 minutos).
* **Mensagem de encerramento:** Texto automático enviado ao fechar o ticket por inatividade.
* **Ativar posição na fila para todos os canais:** Notifica o cliente sobre sua posição numérica na espera.
* **Filtrar atendimentos antigos:** Oculta conversas sem atividade de acordo com o prazo configurado.
* **Máximo de tentativas da mensagem de horário:** Limita quantas vezes o aviso de ausência é enviado por ticket.
* **Campos de Quantidade:** Ajusta o limite de busca de tickets e mensagens na tela (Otimização).

**5. Ações do Sistema**

Comandos manuais de sincronização e correção de dados.

* **Enviar mensagens paradas:** Processa mensagens que ficaram retidas na fila de envio.
* **Resolver Mensagens:** Limpa e remove mensagens que apresentam erros persistentes.
* **Validar Todos os Contatos:** Verifica e atualiza a validade de todos os números na base.
* **Atualizar Data das Mensagens:** Sincroniza o horário original de mensagens importadas.
* **Atualizar Data dos Tickets:** Sincroniza a data do atendimento com a mensagem mais recente.
* **Scan de Contatos sem Lid:** Busca técnica para identificadores em canais específicos.
* **Consolidar duplicatas LID:** Mescla cadastros repetidos baseando-se no ID técnico e número.

***

#### Avisos e precauções

{% hint style="danger" %}
**Atenção:** A função **"Consolidar duplicatas LID"** é uma operação destrutiva e irreversível. Realize um backup completo do seu banco de dados antes de executá-la.
{% endhint %}

{% hint style="warning" %}
Após realizar qualquer alteração nesta página, é obrigatório clicar no botão **Salvar** no topo superior direito para que as novas regras entrem em vigor.
{% endhint %}

***


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/configuracoes-painel-admin/configuracoes-gerais.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
