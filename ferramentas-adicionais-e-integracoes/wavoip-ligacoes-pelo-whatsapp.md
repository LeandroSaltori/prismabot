# Wavoip - Ligações pelo WhatsApp

O Prismabot possui integração nativa com o **WaVoIP**, plataforma de voz sobre IP que permite realizar e receber **ligações pelo WhatsApp** diretamente pelo painel, sem precisar de telefonia convencional.

A integração funciona com **todos os canais de WhatsApp** do Prismabot — API Oficial (WABA), Baileys, WebJS, Evolution API, Z-API e demais conexões. A interface é a mesma independentemente do tipo de canal utilizado.

**O WaVoIP é uma plataforma externa.** Para criar conta, adquirir planos ou resolver qualquer problema técnico relacionado à telefonia, acesse diretamente: [wavoip.com](https://wavoip.com/)

---

### O que é possível com a integração

* Realizar e receber **ligações de voz pelo WhatsApp** dentro do ticket de atendimento
* **Gravar todas as chamadas** e acessar as gravações pelo painel
* Acompanhar **métricas e histórico de chamadas** por horário, token e canal
* Fazer **disparo de ligações em massa** com arquivo de áudio
* Usar um **softphone integrado** (webphone) diretamente no frontend do Prismabot
* Integrar com **PBX/tronco SIP** existente na sua operação
* Conectar **múltiplos atendentes ligando pelo mesmo número** com rastreamento individual por ramal

---

### Pré-requisitos

* Conta ativa no Prismabot com pelo menos um canal de WhatsApp conectado
* Conta criada no WaVoIP ([wavoip.com](https://wavoip.com/))
* Dispositivo criado no painel do WaVoIP

A criação de conta no WaVoIP é **gratuita** e inclui dispositivos de teste para validar a integração antes de contratar um plano pago.

---

### Como conectar

A conexão com o WaVoIP é feita diretamente pelo frontend do Prismabot, sem necessidade de acessar as configurações de canal individualmente.

1. Acesse [**Gestão Comercial → WaVoIP**](../configuracao-administrador/gestao-comercial/analises-e-registros/wavoip.md) no menu lateral
2. Clique em **Conectar** ou **Adicionar dispositivo**
3. O sistema exibirá um **QR Code** — leia-o diretamente pela interface do WaVoIP
4. Informe o **hash** gerado para concluir a vinculação
5. A conexão é ativada automaticamente

Toda a configuração de telefonia — QR Code, hash, tokens e softphone — é gerenciada pelo **WaVoIP**. Em caso de dificuldade na conexão ou qualquer problema técnico relacionado às ligações, entre em contato diretamente com o suporte da WaVoIP em [wavoip.com](https://wavoip.com/).

---

### Fazer uma ligação no atendimento

Com a integração ativa, um botão de ligação aparece dentro de qualquer ticket de atendimento:

1. Abra um atendimento no Prismabot
2. No painel lateral de detalhes do ticket, clique no **ícone de telefone**
3. A chamada é iniciada imediatamente para o número do contato via WhatsApp
4. Ao finalizar, a chamada é registrada automaticamente como **nota de ligação** no histórico do chat

---

### Softphone (Webphone) integrado

O WaVoIP disponibiliza um **softphone nativo** diretamente no frontend do Prismabot, acessível pelo ícone de webphone na barra superior.

No softphone você pode:

* Gerenciar os números e tokens conectados
* Configurar preferências de ligação
* Realizar diagnóstico da conexão (verificar se o microfone, áudio e rede estão funcionando)
* Adicionar novos tokens manualmente ou vinculados a um canal específico
* Acompanhar o status das ligações em andamento

---

### [Disparo de ligações em massa](../ferramentas-do-atendimento/comunicacao-e-marketing/envio-em-massa/envio-em-massa-wavoip.md)

É possível realizar disparos em lote utilizando um arquivo de áudio pré-gravado.

1. Acesse **Envio em Massa** no menu lateral
2. Selecione a opção de **disparo de ligações**
3. Preencha os campos:

Campo

Descrição

**Token**

Token do dispositivo WaVoIP que fará os disparos

**Sessão**

Canal de WhatsApp vinculado

**Números**

Lista de telefones que receberão a ligação

**E-mail**

E-mail de notificação da campanha

**Arquivo de áudio**

Áudio que será reproduzido na ligação

1. Inicie o disparo

Ligações em massa para contatos que nunca interagiram com o número aumentam o risco de denúncias e banimento. Recomenda-se ligar apenas para contatos que já tiveram interação prévia com o número. Consulte as boas práticas anti-banimento antes de usar este recurso.

---

### [Painel de métricas (Gestão Comercial → WaVoIP)](../configuracao-administrador/gestao-comercial/analises-e-registros/wavoip.md)

Acesse **Gestão Comercial → WaVoIP** para acompanhar todas as atividades de ligação da sua operação.

#### Aba: Login e Chamadas

Autenticação com a conta WaVoIP para visualizar o histórico completo:

Campo

Descrição

**E-mail**

E-mail cadastrado no WaVoIP

**Senha**

Senha da conta WaVoIP

**Botão Autorizar e Carregar Chamadas**

Valida as credenciais e exibe o histórico

#### Aba: Por Token

Consulta rápida filtrada por dispositivo:

Campo

Descrição

**Token WaVoIP**

Selecione o token desejado

**Botão Buscar Chamadas**

Filtra e exibe o histórico do token

#### O que você verá

* **Histórico de chamadas:** data, hora, duração, direção (entrada/saída) e status
* **Horários de pico:** gráfico de distribuição das chamadas ao longo do dia
* **Gravações:** coluna com botão para ouvir cada chamada
* **Métricas por token:** volume e desempenho por dispositivo/canal

As gravações ficam disponíveis de acordo com o **plano contratado no WaVoIP**. Caso um áudio não carregue, verifique se a chamada ainda está dentro do prazo de retenção configurado no plano.

---

### Integração SIP / PBX

Se sua operação já utiliza um PBX ou tronco SIP, o WaVoIP permite integrar os números de WhatsApp a essa infraestrutura existente via protocolo SIP. Com isso, é possível receber e fazer ligações pelo WhatsApp dentro do seu sistema de telefonia atual, sem perceber diferença na interface.

Para configurar a integração SIP, entre em contato com o suporte da WaVoIP: [wavoip.com](https://wavoip.com/)

---

### Suporte e problemas

A integração WaVoIP é **100% gerenciada pelo frontend do Prismabot**, incluindo o softphone, QR Code, tokens e métricas. Como a responsabilidade técnica da telefonia é da WaVoIP, qualquer ajuste ou problema relacionado a:

* Qualidade de chamada
* Conexão do dispositivo
* Gravações
* Tokens e dispositivos
* Softphone

deve ser tratado diretamente com o suporte da WaVoIP em [**wavoip.com**](https://wavoip.com/).

---



Atualizado há 1 mês

Isto foi útil?