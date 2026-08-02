# Chat Privado

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

O **Chat Privado** é a ferramenta de comunicação interna do sistema Prismabot. Ele permite que os agentes e administradores interajam entre si em tempo real, sem a necessidade de ferramentas externas, facilitando a troca de informações, o suporte entre colegas e a coordenação de equipes.

#### Caso de uso

Um atendente está lidando com um ticket técnico complexo e precisa de auxílio do setor de engenharia. Ele utiliza o **Chat Privado**, localiza o supervisor na aba de **Usuários** e envia uma captura de tela do erro. Para agilizar a solução, ele inicia uma **Videochamada** rápida para explicar os detalhes, mantendo todo o fluxo de colaboração dentro da plataforma.

#### Como acessar a página

No menu lateral esquerdo, clique no Menu **Atendimento** e selecione a aba **Chat Privado**.

<figure><img src="/files/5k0HrwC8kBrXJ13ceqqD" alt="" width="273"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/5vKWCYGqlPFvG60zqaVc" alt=""><figcaption></figcaption></figure>

**Explicação dos campos e ícones**

**Barra Lateral (Lista de Contatos):**

* **Busca:** Campo para localizar usuários ou equipes pelo nome.
* **Abas Usuários/Equipes:** Alterna entre a visualização de contatos individuais ou grupos de departamentos.
* **Status de Presença:** Uma bolinha verde ao lado do avatar indica que o colega está **Online**.

**Barra Superior (Janela de Chat):**

* **Nome e Status:** Identificação de com quem você está conversando.
* **Ícone de Telefone:** Inicia uma chamada de áudio interna.
* **Ícone de Câmera:** Inicia uma videochamada interna.

**Barra de Envio (Rodapé):**

* **Emoji (Sorriso):** Acesso à biblioteca de ícones expressivos.
* **Anexo (Clipe):** Permite o envio de documentos e imagens do seu computador.
* **Videoconferência (Monitor):** Gera e envia um link de reunião instantânea (Jitsi Meet).
* **Microfone:** Permite gravar e enviar mensagens de áudio.

***

#### Como iniciar uma conversa interna

Para falar com um colega específico, mantenha a aba **Usuários** selecionada e clique sobre o nome desejado na lista. Caso precise falar com um departamento inteiro, mude para a aba **Equipes** e selecione o grupo. O histórico de mensagens será carregado automaticamente no painel central.

#### Como realizar chamadas de voz ou vídeo

Dentro de uma conversa aberta, utilize os ícones de **Telefone** ou **Câmera** localizados no canto superior direito.

* **Nota:** O sistema utiliza tecnologia WebRTC para chamadas diretas ou gera links de salas virtuais privativas para que os membros cliquem e entrem na conferência.

#### Como enviar arquivos e documentos

Clique no ícone de **Clipe** na barra inferior, selecione o arquivo em seu dispositivo e confirme o envio. Você também pode enviar mensagens de voz segurando o ícone do **Microfone**, facilitando a comunicação em momentos de alta demanda de Tickets.

#### Como localizar mensagens e contatos

Utilize a barra de **Busca** acima da lista de usuários para filtrar rapidamente a pessoa ou equipe com quem deseja interagir. As mensagens enviadas e recebidas ficam armazenadas, permitindo a consulta de informações compartilhadas anteriormente.

***

#### Avisos e precauções

{% hint style="info" %}
As conversas do **Chat Privado** são estritamente internas e não são visíveis para os clientes finais que estão em atendimento nos Canais externos.
{% endhint %}

### Configuração de WebRTC TURN (coturn)

Para melhorar a qualidade e a taxa de sucesso das chamadas de áudio e vídeo no chat interno, pode ser necessário configurar um servidor TURN (coturn).

📌 Esse recurso é utilizado quando a conexão direta (STUN) falha — algo comum quando os usuários estão em redes diferentes, provedores distintos ou CGNAT.

⚠️ Importante: Essa configuração NÃO faz parte da infraestrutura padrão da Prismabot. A ativação do TURN (coturn) é opicional e deve ser realizada pelo próprio cliente, conforme sua necessidade.

💡 Quando vale a pena configurar?

* Usuários em provedores diferentes
* Problemas de conexão em chamadas
* Baixa taxa de sucesso em áudio/vídeo
* Uso interno frequente de chamadas entre atendentes

🛠 A configuração envolve:

* Instalação do coturn na VPS (Ubuntu)
* Abertura de portas no firewall
* Definição das variáveis no .env do backend

🎯 Benefício: Maior estabilidade e aceitação das chamadas internas, garantindo que o áudio/vídeo funcione mesmo em cenários de rede mais restritivos.

{% file src="/files/uO0csiZW4uATZky6p6cl" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/atendimento/chat-privado.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
