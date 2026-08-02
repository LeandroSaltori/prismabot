# E-mail (IMAP/SMTP)

A conexão via **IMAP/SMTP** permite integrar qualquer provedor de e-mail externo (Outlook, Yahoo, Hostgator, Locaweb, servidores próprios, etc.) ao painel de atendimento do Prismabot. Através desta configuração, o sistema será capaz de receber e-mails como tickets de atendimento e responder aos clientes diretamente pela interface de chat.

#### Passo 1: Informações Iniciais

Ao adicionar um novo canal, selecione o tipo **Email (IMAP/SMTP)**.

* **Nome do Canal:** Insira um nome para identificar esta conta (ex: E-mail Comercial).
* **Canal Padrão:** Defina se esta será a conta principal de envio de e-mails do sistema.

<figure><img src="/files/i18iz8y2zRxzwGqcMby1" alt="" width="375"><figcaption></figcaption></figure>

#### Passo 2: Configuração SMTP (Envio)

Esta seção configura a saída das mensagens. Os dados variam conforme o seu provedor.

* **Servidor SMTP:** O endereço do servidor de saída.
  * *Exemplos comuns:* `smtp.seudominio.com.br` ou `mail.seudominio.com.br`.
* **Porta SMTP:** Geralmente utiliza-se **587** (para conexão TLS) ou **465** (para conexão SSL).
* **Conexão Segura (SSL/TLS):** Ative este campo caso seu provedor exija uma conexão criptografada.
* **Usuário:** O endereço de e-mail completo de autenticação (ex: `atendimento@empresa.com.br`).
* **Senha / App Password:** A senha da conta de e-mail ou uma "senha de aplicativo" gerada no painel do provedor.
* **E-mail remetente (from):** O endereço que aparecerá para o cliente ao receber sua mensagem.
* **E-mail de resposta (replyTo):** O endereço que receberá as respostas caso o cliente responda ao e-mail manualmente.

<figure><img src="/files/D84ujp5tYx00svwwK6M0" alt="" width="375"><figcaption></figcaption></figure>

#### Passo 3: Configuração IMAP (Recebimento)

Esta seção configura a entrada das mensagens no sistema.

* **Detecção Automática:** Insira seu e-mail e clique em **Detectar**. O sistema tentará encontrar as configurações de host e porta automaticamente.
* **Host IMAP:** O endereço do servidor de entrada.
  * *Exemplos comuns:* `imap.seudominio.com.br` ou `mail.seudominio.com.br`.
* **Porta IMAP:** Geralmente utiliza-se **993** (com TLS/SSL ativo) ou **143** (sem segurança).
* **TLS/SSL:** Ative para garantir a segurança no recebimento.
* **Usuário IMAP:** Geralmente o mesmo e-mail do SMTP. Você pode clicar no botão **Igual ao SMTP** para preenchimento rápido.
* **Caixa (mailbox):** A pasta que o sistema deve monitorar. O padrão é **INBOX**.
* **Intervalo (segundos):** Tempo de espera entre cada verificação de novos e-mails. O recomendado é **30** segundos.

<figure><img src="/files/Ym0pLs79feUQCk6zNoW7" alt="" width="375"><figcaption></figcaption></figure>

#### Passo 4: Configurações Avançadas

* **Validar certificado TLS:** Mantenha ativo para garantir que o sistema verifique a autenticidade do servidor de e-mail.
* **Keepalive / IDLE:** Mantém a conexão com o servidor de e-mail sempre "viva", permitindo o recebimento de mensagens quase instantaneamente.
* **Assinatura (HTML):** Insira aqui o texto de assinatura que será anexado ao final de todos os e-mails enviados. Aceita formatação HTML.
  * *Exemplo:* `<p>Atenciosamente,<br/><b>Equipe de Suporte</b></p>`

<figure><img src="/files/EL5HQn5KawqvEOxVfLWo" alt="" width="375"><figcaption></figcaption></figure>

#### Passo 5: Webhook do Canal

* **Habilitar Webhook do Canal:** Se ativado, o sistema disparará notificações para uma URL específica sempre que um novo e-mail for processado por esta conta.

<figure><img src="/files/TzkMSQ8pRxyzC0O7wGwi" alt="" width="375"><figcaption></figcaption></figure>

***

#### Avisos e Observações

1. **Firewall:** Certifique-se de que o seu servidor de e-mail permite conexões externas para as portas configuradas (587, 465, 993).
2. **Senhas de Aplicativo:** Alguns provedores (como Outlook/Office 365) exigem a criação de uma "Senha de Aplicativo" caso a Autenticação de Dois Fatores (2FA) esteja ativa na conta.
3. **Limite de Anexos:** O tamanho dos arquivos enviados e recebidos via e-mail respeitará o limite imposto pelo seu provedor de e-mail (geralmente entre 10MB e 25MB).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao/e-mail-imap-smtp.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
