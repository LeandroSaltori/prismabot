# Como conectar um canal (sessão/número)

No menu lateral do seu painel, clique em ADMINISTRAÇÃO, aba ***Canais***.

<figure><img src="/files/sOZmcbEwKK1shBE5VuK2" alt="" width="279"><figcaption></figcaption></figure>

Você verá a seguinte tela:

<figure><img src="/files/Sj7c1UpLMa3ou3rQxoZU" alt=""><figcaption></figcaption></figure>

Aqui é onde você fará a conexão com os números oficiais da sua empresa, para realizar os atendimentos.

## Nova conexão <a href="#nova-conexao" id="nova-conexao"></a>

Clique em ***Adicionar Canal*** no canto superior da tela.

<figure><img src="/files/4e2lMFULhTZzhGmW4z9N" alt="" width="143"><figcaption></figcaption></figure>

Assim que selecionar esse botão, um pop up se abrirá para que você preencha as informações. Veja o exemplo:

<figure><img src="/files/ScoijExgoFPZ825D5tur" alt="" width="375"><figcaption></figcaption></figure>

### 1. Escolha do Tipo de Canal

Ao clicar em **"Adicionar Canal"**, a primeira etapa é selecionar a tecnologia de conexão. Cada tipo possui características específicas de estabilidade e recursos.

Para detalhes técnicos e passo a passo de conexão (QR Code ou Token) de cada tipo, consulte as documentações específicas:

[**WhatsApp Oficial (OAuth)**](/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/whatsapp-oficial-oauth-app-zpro-com-coexistencia.md)

[**Instagram Direct** e **Facebook Messenger**](/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/instagram-e-facebook-messenger-via-oauth-login.md)

[**Waba: WhatsApp Oficial - Cloud API**](/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/whatsapp-oficial-via-api-cloud-waba.md)

Para essa documentação vamos passar o tutorial para conectar APIs não oficiais

<figure><img src="/files/jiwXZbOCQU6N1Irel1Er" alt="" width="375"><figcaption></figcaption></figure>

### 2. Preencha dos dados&#x20;

#### Código de pareamento

<figure><img src="/files/qxtAzyZieKZAK7cqzUck" alt="" width="375"><figcaption></figcaption></figure>

<mark style="color:$primary;">Apenas para o canal tipo</mark> <mark style="color:$primary;"></mark><mark style="color:$primary;">**BAILEYS, WebJS e Meow**</mark>

Opção caso não seja possível ler o QR Code

#### Nome

<figure><img src="/files/SwmPzvMHLKrtj57YPce7" alt="" width="375"><figcaption></figcaption></figure>

Insira um nome para identificar esse canal.

* **Canal padrão:** Define se este será o canal principal para envios automáticos do sistema.

#### Atribuições

<figure><img src="/files/ZljkY5kZ223TJPiECpqL" alt="" width="375"><figcaption></figcaption></figure>

Em ***ChatFlow*** você pode escolher o ***Fluxo (BOT)*** que usará como padrão para o atendimento desse número. Voce pode atribuir apenas um fluxo para cada número/conexão.

Em ***Fila*** você pode escolher uma ***Fila*** que usará como padrão para o atendimento desse número.

Em ***Usuário*** você pode escolher uma ***Usuário*** que usará como padrão para o atendimento desse número.

*Essa função você só consegue habilitar depois de criar o canal*

#### Importar mensagem do Aparelho

<mark style="color:$primary;">Apenas para o canal tipo</mark> <mark style="color:$primary;"></mark><mark style="color:$primary;">**BAILEYS (QR CODE)**</mark>

<figure><img src="/files/rb6NuLOcZaoeh3bSPWxD" alt="" width="375"><figcaption></figcaption></figure>

### [Wavoip](/ferramentas-adicionais-e-integracoes/wavoip-ligacoes-pelo-whatsapp.md)

<figure><img src="/files/5SkJkduWgUvCau6vmcIa" alt="" width="375"><figcaption></figcaption></figure>

Ativação da ligação por meio de Chamadas VoIP

Documentação completa: [Wavoip - Ligações pelo WhatsApp](/ferramentas-adicionais-e-integracoes/wavoip-ligacoes-pelo-whatsapp.md)

#### Mensagem de Despedida do Atendimento

<figure><img src="/files/4Ra5Sv9L9CNk5hy4ZUbp" alt="" width="375"><figcaption></figcaption></figure>

Mensagem enviada assim que finaliza um atendimento nesse botão:

<figure><img src="/files/6MRgLRV09ublWmWXGdAw" alt="" width="272"><figcaption></figcaption></figure>

#### Integrações com IAs

Para integrar as inteligencias artificiais com o canal que está sendo criado é preciso adicionar as informações específicas de cada IA. Verificar os campos necessários em cada aba abaixo.

{% hint style="warning" %}
É necessário ativar a integração do seu Prismabot com a IA desejada dentro do Painel do Admin - Configurações gerais para que seja possível ativar dentro do Canal criado

[Bots e IA](/configuracao-administrador/configuracoes-painel-admin/bots-e-ia.md)
{% endhint %}

<figure><img src="/files/l15TGgvtOnxxTBrdVIb2" alt=""><figcaption></figcaption></figure>

Assim que habilitar a integração com Bots IA, ela aparecerá na criação do canal para colocar as informações:

<figure><img src="/files/fXLQnQcpKsEYXecYtMVV" alt="" width="375"><figcaption></figcaption></figure>

### Webhook do canal

Dispara notificações para uma URL exclusiva deste canal, em paralelo ao webhook geral do tenant

<figure><img src="/files/eUFWVJZ513DZ1K6SkhXw" alt="" width="375"><figcaption></figcaption></figure>

### Pix

Configuração padrão pré-salva para o botão PIX. Os campos são carregados automaticamente ao abrir o envio e podem ser alterados antes de enviar.

<figure><img src="/files/veoj9zdxFiaBtiTdQ0qA" alt="" width="375"><figcaption></figcaption></figure>

### Recursos do canal

<figure><img src="/files/K79WMb0qNRBdKuwmKeKC" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="/files/wFOe1Ff1LIpji1p6M9R6" alt="" width="375"><figcaption></figcaption></figure>

| **Opção**                                                               | **Descrição e Funcionamento**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Habilitar avaliação automática                                          | <p>Envio automático de pesquisa de satisfação.<br></p><p>Ao resolver um ticket, o sistema envia automaticamente a mensagem de avaliação configurada para o cliente, sem necessidade de ação manual do atendente.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Habilitar transcrição de áudio                                          | <p>Conversão de voz para texto.<br></p><p>Os áudios recebidos no chat serão processados e transcritos para texto, facilitando a leitura e a indexação do conteúdo.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Habilitar auto distribuir                                               | <p>Balanceamento de carga entre a equipa.<br></p><p>Novos tickets que chegam sem dono definido serão distribuídos automaticamente e de forma equitativa entre os atendentes que estiverem online no sistema.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Habilitar destruição de mensagem                                        | <p>Privacidade e limpeza de dados.<br></p><p>Quando uma mensagem é apagada na interface do chat (pelo utilizador ou admin), ela é removida permanentemente da base de dados do sistema, e não apenas ocultada visualmente.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Habilitar envio de mensagem para aniversariantes                        | <p>Marketing e relacionamento automático.<br></p><p>Envia automaticamente uma mensagem de felicitações (definida no campo abaixo desta opção) na data de aniversário do contacto.</p><p></p><p>• Nota: Esta função ignora as configurações de horário de atendimento, garantindo que os parabéns sejam enviados mesmo fora do expediente.</p>                                                                                                                                                                                                                                                                                                                                                                                                      |
| Ignorar Horário de Atendimento                                          | Ignora o horário de atendimento do sistema para este canal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Redistribuição Automática de Tickets                                    | Redistribui automaticamente tickets de usuários que ficarem offline por mais do que o tempo configurado.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Posição na fila                                                         | Quando um novo atendimento entra na fila como pendente, o sistema envia uma mensagem automática informando a posição do cliente e o tempo médio de espera. Herdar: segue a configuração global do tenant. Ativado: sobrescreve o global e usa a configuração deste canal. Desativado: sobrescreve o global e não envia. O gatilho dispara apenas uma vez por ticket, depois que o chatbot/flow termina. Se o ticket for atribuído a um agente automaticamente ou se um chatbot assumir, a mensagem não é enviada. Escopo da posição: contagem na mesma fila (queue) do ticket; se não houver fila, conta pelo canal. Canais suportados: WhatsApp Web, Baileys, WABA, Instagram, Messenger, Webchat, Telegram, Evolution, Z-API, UazAPI, Meow, Hub. |
| Habilitar desligamento automático das integrações externas              | <p>Transição suave de Robô para Humano.</p><p></p><p>Quando um atendente abre ou assume um ticket, o sistema desativa automaticamente as integrações de IA (ChatGPT, Typebot, Dify, N8N, DialogFlow) para aquela conversa, evitando que o robô interrompa o atendimento humano.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Habilitar espera no processamento de mensagens com integrações externas | <p>Fila de processamento para Chatbots.<br></p><p>Evita que o bot se confunda quando o cliente envia várias mensagens seguidas. O sistema processará uma mensagem de cada vez, aguardando a resposta da integração (ex: Typebot) antes de processar a frase seguinte do cliente.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Habilitar Web Push                                                      | <p>Notificações do Sistema.</p><p></p><p>Ativa o envio de notificações <em>push</em> (alertas de navegador ou PWA) para avisar os utilizadores sobre novas mensagens ou atividades no painel, mesmo quando a aba não está em primeiro plano.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Contingência                                                            | Se ativo: o canal recebe mensagens. Se inativo: permanece conectado mas não recebe mensagens.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Palavra-chave para fechamento automático                                | Ao receber esta palavra-chave o ticket será encerrado automaticamente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

Você pode habilitar uma palavra chave para fechamento automático do atendimento. Essa é uma palavra chave que ao ser recebida irá encerrar o ticket automaticamente.

### Configurações adicionais (Proxy)

<mark style="color:$primary;">Apenas para o canal tipo</mark> <mark style="color:$primary;"></mark><mark style="color:$primary;">**BAILEYS, WebJS, Meow, Evolution API, Uazapi**</mark>

<figure><img src="/files/wHKecI0FuDbv2WhkJ1kO" alt="" width="375"><figcaption></figcaption></figure>

{% content-ref url="/pages/vh9IxgE5vP6vALpCouvj" %}
[Proxy IPv4 no Proxy-Seller](/avancado-recursos-tecnicos/infraestrutura/proxy-ipv4-no-proxy-seller.md)
{% endcontent-ref %}

### Ações finais

<figure><img src="/files/OpeEXIriNYMTIL4oq0vV" alt="" width="207"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/como-conectar-um-canal-sessao-numero.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
