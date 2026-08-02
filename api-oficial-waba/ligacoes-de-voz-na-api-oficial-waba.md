Copiar

Nesta página

1. [API Oficial WABA](/api-oficial-waba)

# Ligações de voz na API Oficial (WABA)

A API Oficial do WhatsApp (WABA) permite **receber e fazer ligações de voz** dentro do próprio WhatsApp do cliente, tudo pelo painel do Prismabot. Este artigo mostra como habilitar o recebimento de chamadas, como solicitar a permissão necessária para originar ligações e como configurar o roteamento das chamadas entre os atendentes.

**Pré-requisitos:**

* Um canal já conectado e ativo na API Oficial (WABA), recebendo e enviando mensagens.
* A permissão de chamadas (`calls`) aprovada para o seu App na Meta.

**Conectado pelo App nativo da ZDG (OAuth)?** A permissão de chamadas (`calls`) já vem **aprovada** no nosso App. Não é preciso configurar webhook nem solicitar aprovação — basta ativar as chamadas no painel (Etapa 1) e usar. Por isso o processo é mais simples nesse caminho.

**Usa App próprio (Tech Provider)?** A permissão `calls` precisa ser aprovada pela Meta no processo de Análise do App (App Review) do seu próprio aplicativo.

---

### Como funciona

* **Receber ligações:** basta ativar as chamadas WebRTC no canal. Uma vez ativo, as chamadas recebidas passam a tocar para os usuários conforme a regra de roteamento definida.
* **Fazer ligações:** é diferente do recebimento. Antes de ligar para um contato, é preciso **solicitar uma permissão de chamada** e o contato precisa **aceitar**. Só depois de autorizada a permissão é possível originar a ligação.

**Janela de permissão para ligar:** após o contato autorizar, a permissão de chamada fica válida por **72 horas (padrão)**. Passado esse período, é necessário solicitar a permissão novamente para voltar a ligar para o contato.

---

### Etapa 1: Ativar o recebimento de chamadas (WebRTC)

1. Acesse **Configurações > Integrações > Meta > WhatsApp**.
2. Selecione o canal WABA que você conectou. As especificações do canal serão exibidas.
3. Verifique o telefone para confirmar que está tudo certo.
4. Localize a opção de chamadas e clique em **ativar as chamadas WebRTC**.

Pronto — o canal passa a receber (e a poder enviar) chamadas de voz.

Para **receber** chamadas não é necessário aprovar nenhuma permissão: basta deixar as chamadas ativadas. Por padrão, a chamada recebida toca para **todos os usuários logados**, e qualquer um deles pode atender ou recusar. Para direcionar as chamadas, use a Etapa 3 (Roteamento).

---

### Etapa 2: Fazer uma ligação (permissão de chamada)

Para originar uma ligação, primeiro é preciso obter a autorização do contato:

1. Abra o atendimento e acesse os **detalhes do contato**.
2. No menu **Telefonia**, selecione a opção **WABA**.
3. Envie a **solicitação de permissão de chamada** ao contato.
4. O contato recebe no WhatsApp a mensagem **"Permitir ligações"** e precisa autorizar.
5. Com a **permissão autorizada**, clique em **Ligar** para iniciar a chamada de voz.

**Sem permissão de chamada aprovada** você não conseguirá ligar — o sistema exibe o aviso e bloqueia a chamada. Sempre solicite e aguarde o aceite do contato antes de tentar originar a ligação.

---

### Etapa 3: Roteamento de chamadas WABA

Por padrão, as chamadas recebidas tocam para todos os usuários logados. Para definir **quais atendentes** recebem cada chamada, configure o roteamento:

1. Acesse **Configurações** e localize o **Roteamento de chamadas WABA**.
2. Escolha a regra de distribuição desejada.

Regra de roteamento

Comportamento

Tocar para todos os atendentes

A chamada toca para todos; o **primeiro que atender** assume a ligação. É a opção mais comum.

Apenas o atendente do ticket

Toca somente para o atendente que está com o ticket daquele contato.

Rodízio na fila

Segue a fila do canal, distribuindo as chamadas conforme as regras de gestão daquela fila.

Fallback escalonado

Toca para um usuário por vez, na ordem da fila, escalando para o próximo se não houver atendimento.

**Tempo de espera por usuário:** define por quanto tempo a chamada toca para cada usuário antes de passar para o próximo (no rodízio/fallback escalonado). O valor é em **segundos**. Ex.: com 5 segundos, a chamada toca 5s para o usuário 1; se ele não atender, passa para o usuário 2 por mais 5s, e assim por diante até alguém atender.

Se a sua operação é dividida por **departamentos ou filas**, combine o roteamento de chamadas com a configuração de filas e balanceamento de atendimentos para direcionar cada tipo de chamada ao destino correto.

---

### Resumo das Funcionalidades

Funcionalidade

Onde acessar

Ativar recebimento de chamadas (WebRTC)

**Configurações > Integrações > Meta > WhatsApp** > canal WABA

Solicitar permissão de chamada

**Detalhes do contato > Telefonia > WABA**

Fazer uma ligação

**Detalhes do contato > Telefonia > WABA > Ligar**

Configurar roteamento das chamadas

**Configurações > Roteamento de chamadas WABA**

---

### Encerramento

Com as chamadas ativadas, seu canal WABA passa a receber e fazer ligações de voz diretamente pelo Prismabot, sem ferramentas externas — e o roteamento garante que cada chamada chegue ao atendente certo.

---

### Possíveis Erros e Soluções

#### "Sem permissão de chamada aprovada" ao tentar ligar

**Causa:** o contato ainda não autorizou a permissão de chamada, ou a janela de permissão expirou. **Solução:** envie (ou reenvie) a solicitação de permissão em **Detalhes do contato > Telefonia > WABA** e aguarde o aceite do contato. Lembre-se de que a permissão vale por 72 horas (padrão).

#### As chamadas não tocam para os atendentes

**Causa:** chamadas WebRTC não ativadas nas configurações do número WABA conectado ao Prismabot, ou roteamento direcionando para usuários que não estão logados. **Solução:** confirme a ativação em **Configurações > Integrações > Meta > WhatsApp** e revise a regra em **Roteamento de chamadas WABA**.

[AnteriorComo aprovar seu App da Meta](/api-oficial-waba/whatsapp-oficial-cadastro-incorporado-e-coexistencia-com-app-proprio/como-aprovar-seu-app-da-meta)[PróximoExemplo de fluxo no N8N + API Prismabot + WABA](/api-oficial-waba/exemplo-de-fluxo-no-n8n-+-api-prismabot-+-waba)

Atualizado há 1 mês

Isto foi útil?