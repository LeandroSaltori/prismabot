Copiar

Nesta página

# WEBRTC\_TURN\_SETUP

Este guia configura um servidor **TURN** com **coturn** para chamadas de áudio/vídeo do **chat privado**. O tráfego de mídia pode ser retransmitido pelo TURN quando a conexão direta (STUN) não funciona — por exemplo, usuários em redes/ISPs diferentes ou CGNAT.

Os frontends (Vue e Next) obtêm a lista de servidores ICE em `GET /chat-privado/webrtc/ice-servers`, que lê as variáveis abaixo do **backend**.

---

## Variáveis no `.env` do backend

Adicione (ou edite) estas chaves no arquivo `.env` **do backend** (não no frontend):

Variável

Obrigatória

Descrição

`WEBRTC_TURN_URLS`

Não\*

Uma ou mais URLs TURN, separadas por vírgula. Ex.: `turn:turn.seudominio.com:3478` ou `turn:203.0.113.10:3478`

`WEBRTC_TURN_USERNAME`

Não\*

Usuário configurado no coturn (`user=...` antes dos dois pontos)

`WEBRTC_TURN_CREDENTIAL`

Não\*

Senha configurada no coturn (depois dos dois pontos em `user=usuario:senha`)

\* **As três devem existir juntas** para o TURN ser incluído na resposta da API. Se alguma faltar, o backend continua respondendo só com **STUN** públicos (sem relay).

Opcional:

Variável

Descrição

`WEBRTC_ICE_SERVERS_JSON`

JSON com array extra de objetos no formato `RTCIceServer` (mesclado após os STUN padrão). Use só se souber o que está fazendo.

### Exemplos de `.env` (backend)

**Só TURN em UDP/TCP 3478 (sem TLS):**

Copiar

```
WEBRTC_TURN_URLS=turn:turn.exemplo.com.br:3478
WEBRTC_TURN_USERNAME=prismabot_turn
WEBRTC_TURN_CREDENTIAL=uma_senha_longa_e_aleatoria
```

**TURN + TURNS (TLS na 5349), se o coturn estiver com certificado:**

**Importante:** use o **mesmo** usuário e senha no coturn (`user=prismabot_turn:uma_senha_longa_e_aleatoria`) e reinicie o processo Node (PM2/systemd) após alterar o `.env`.

---

## 1. Instalar coturn no Ubuntu

Ativar o serviço:

---

## 2. Configurar `/etc/turnserver.conf`

Edite o arquivo (ex.: `sudo nano /etc/turnserver.conf`) e ajuste ao seu ambiente.

### Exemplo mínimo (credenciais estáticas — alinhado ao `.env` acima)

Substitua:

* `SEU_IP_PUBLICO` — IP público da VPS (ou par `IP_PUBLICO/IP_INTERNO` se a VM estiver atrás de 1:1 NAT).
* `exemplo.com.br` — domínio ou nome lógico (campo `realm`).
* `prismabot_turn` e `uma_senha_longa_e_aleatoria` — **iguais** a `WEBRTC_TURN_USERNAME` e `WEBRTC_TURN_CREDENTIAL`.

Se a VPS não tiver IP público direto na interface (NAT do provedor):

### TLS (`turns:` na porta 5349)

1

### Obtenha certificado

Obtenha certificado (ex.: Let’s Encrypt).

2

### No mesmo arquivo

3

### No `.env`

Inclua `turns:turn.exemplo.com.br:5349` em `WEBRTC_TURN_URLS` (como no exemplo acima).

Reinicie o coturn:

---

## 3. Firewall (UFW na VPS)

No painel da nuvem (security group / firewall), abra as **mesmas** portas.

---

## 4. DNS (recomendado)

Aponte um registro **A** (ou AAAA) para o subdomínio usado no TURN, ex.:

* `turn.exemplo.com.br` → IP público da VPS

Use esse nome em `WEBRTC_TURN_URLS` em vez do IP, se possível (facilita certificado TLS e mudanças de IP).

---

## 5. Verificação rápida

* Página [Trickle ICE](https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/): adicione um servidor TURN com o mesmo host, porta, usuário e senha do coturn e confira se aparecem candidatos **relay**.
* Nos logs do coturn (`journalctl -u coturn -f`) devem aparecer alocações quando houver chamada usando relay.

---

## 6. Reiniciar o backend

Após editar o `.env` do backend:

---

## Referência no código

* Montagem da lista ICE: `backend/src/utils/webrtcIceServersPrismabot.ts`
* Rota HTTP: `GET /chat-privado/webrtc/ice-servers` (autenticada)
* Frontends consomem essa rota e montam o `RTCPeerConnection`

---

## Segurança

* Use senha forte e exclusiva para o usuário TURN.
* Em produção, prefira **TLS** (`turns:`) quando possível.
* Credenciais ficam **somente** no servidor (backend `.env`); não coloque senha TURN em variáveis `NEXT_PUBLIC_*` no frontend.

Para credenciais **temporárias** por usuário (shared secret / REST do coturn), seria necessário estender o backend — este guia cobre o modo **usuário/senha estático**, que já é suportado pelas variáveis `WEBRTC_TURN_*`.

[AnteriorTemplate (WABA) não chega ao destinatário](/avancado-recursos-tecnicos/erros-e-avisos-comuns/template-waba-nao-chega-ao-destinatario)

Isto foi útil?