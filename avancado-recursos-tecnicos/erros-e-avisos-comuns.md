Copiar

Nesta página

1. [Avançado - Recursos técnicos](/avancado-recursos-tecnicos)

# Erros e Avisos Comuns

### Avisos do painel

#### "CANAIS PRECISAM DE ATENÇÃO"

**O que significa:** alguns canais estão com conexão próxima de expirar. O canal ainda pode estar funcionando, mas o sistema identificou que a sessão precisará de renovação em breve.

**Como resolver:**

1. Acesse **Configurações → Sessões** e atualize a sessão do canal indicado
2. Verifique se o canal está conectado e sem alertas internos
3. Confirme que o envio e recebimento continuam funcionando normalmente

Após atualizar a sessão em [Configurações → Sessões](/configuracao-administrador/configuracoes-painel-admin/sessoes), o aviso deve desaparecer. Se persistir, verifique se o token/sessão está válido ou se é necessário reconectar o canal.

---

### Erros de login e acesso ao sistema

#### "Servidor temporariamente offline"

**Onde aparece:** na tela de login, após digitar usuário e senha.

**O que significa:** o frontend está abrindo, mas não consegue se comunicar com o backend. O problema não é nas credenciais — é na infraestrutura.

**Causas mais comuns:**

* Backend parado ou reiniciando com erro
* Porta do backend não está respondendo
* Configuração do Nginx apontando para porta errada
* Subdomínio do backend com erro de SSL
* Variável do frontend apontando para URL incorreta do backend
* Banco de dados ou Redis indisponível
* Erro de build após instalação ou atualização

**Como diagnosticar:** acesse a servidor em nuvem e execute:

O `pm2 status` e o `pm2 logs zpro-backend` geralmente já mostram a causa principal. Envie o retorno ao suporte se o problema persistir.

---

#### "Recuperação de licença: A licença ficou inválida durante a operação"

**Onde aparece:** na tela de login, ao tentar entrar com o superadmin.

**O que significa:** a licença expirou ou ficou inválida. O sistema entra automaticamente em **modo de recuperação**, onde somente o superadmin consegue alterar a chave de licença.

**Como resolver:**

1. Acesse com o **superadmin**
2. Insira a **nova chave de licença** (se renovou) ou a **chave atual** (se ainda válida) para revalidar
3. Se já renovou a licença mas o erro persiste, pode ser que a licença tenha ficado inválida por mais de 6 horas — nesse caso, **reinicie o backend** na servidor em nuvem:

Se o sistema ficar mais de **6 horas** com a licença inválida, ele bloqueia o acesso. Nesse caso, além de inserir a chave válida, é necessário reiniciar o backend. Somente o **superadmin** pode alterar a chave de licença nesse estado.

#### Esta empresa está inativa. Entre em contato com o administrador

* **Situação:** Tenta logar pelo superadmin e o aviso aparece
* **Causa:** Ocorre quando é inativado o **Tenant 1** via banco ou rotina externa
* **Solução:** Acessar o banco de dados e ativar na **tabela TENANT** o **Tenant 1**

---

### Erros de envio de mensagens

#### "Aguarde alguns instantes..."

**Onde aparece:** ao tentar enviar uma mensagem por um canal que utiliza a lib Baileys.

**O que significa:** comportamento associado à lib Baileys. Pode ocorrer apenas em conexões específicas e tende a ser intermitente.

**Como resolver (em ordem de prioridade):**

1. Atualize o **Prismabot para a versão HOTFIX** mais recente
2. Atualize o **aplicativo do WhatsApp** no celular vinculado ao canal
3. Atualize o **Android** do aparelho

Essas três ações resolvem o problema em cerca de 90% dos casos.

**Alternativas adicionais:**

* Recriar o canal afetado
* Migrar o canal para o **Baileys v7**: acesse **Canais → Editar canal → Baileys → selecionar v7**

O Baileys v7 está disponível a partir da versão **4.0.0.8** do Prismabot.

Se o problema persistir após todas as tentativas acima, considere migrar o canal para **wwebjs** ou **wuzapi** — essas libs não apresentam relato desse comportamento.

---

#### META: Not supported type

**Onde aparece:** no processamento de mensagens recebidas via canal WABA (API Oficial).

**O que significa:** A meta gera esse aviso e não é possível saber ao certo qual a causa, pode ser por tipo de mensagem ou arquivo que o sistema ainda não suporta.

**Tipos de conteúdo que comumente geram esse erro:**

* Reações a mensagens (emoji reactions)
* Fotos ou vídeos com **Visualização única** (View Once)
* Enquetes (Polls)
* Compartilhamento de localização ao vivo
* Stickers ou GIFs
* Mensagens apagadas
* Mensagens trocadas entre contas WABA
* Arquivos em formatos não suportados

**Como tratar:** verifique se o arquivo ou tipo de mensagem está na lista de formatos suportados pelo Prismabot: [https://prismatelecomservicos.com/ class="gb-icon ml-0.5 inline size-3 links-accent:text-tint-subtle" fill="currentColor" style="overflow:visible" viewbox="0 0 384 512">](https://prismatelecomservicos.com/ rel=)

Se o tipo de conteúdo não for suportado, o comportamento esperado é que o Prismabot ignore ou registre o evento sem processar — não há ação corretiva do lado do sistema.

---

### Erros de acesso e permissão

#### ERR\_NO\_PERMISSION\_CONNECTIONS\_LIMIT

**Onde aparece:** ao tentar criar ou ativar um canal.

**O que significa:** o tenant atingiu o limite de conexões permitidas para a sua conta.

**Como resolver:** acesse o **Superadmin → Tenants** e revise o limite de conexões configurado para esse tenant. Aumente o limite se necessário.

---

#### ERR\_NO\_TICKET\_ACCESS — 403

Usuário sem permissão para acessar o ticket. Verifique fila, canal, perfil e permissões do usuário.

#### Por que ocorre o ERR\_NO\_TICKET\_ACCESS ao disparar um template WABA?

O erro indica que o usuário que realiza o disparo não possui acesso ao ticket associado ao contato. Mesmo com todos os canais liberados, o acesso ao ticket é validado individualmente.

**Causas mais comuns** — o contato já possuía um ticket aberto/pendente que foi reaproveitado, e esse ticket:

* está atribuído a outro atendente;
* está em uma fila da qual o usuário não faz parte;
* está sem atendente e sem fila, enquanto a configuração `nullTickets` do tenant está desabilitada (`disabled`).

Para identificar o motivo exato, habilite `LOGGER_WARN=true` no backend. O sistema registrará:

**O que é a configuração** `nullTickets`**?** Controla se os usuários podem acessar tickets que não possuem atendente nem fila definidos. Quando desabilitada (`disabled`), o acesso a esses tickets é bloqueado — o que também pode resultar neste erro.

---

### Erros de API

#### errors.numberInvalidFormat — API WebChat

**Onde aparece:** ao tentar enviar mensagem via API pelo canal WebChat, no campo `number`.

**O que significa:** o campo `number` espera um **número de telefone em formato internacional** (somente dígitos). Identificadores internos de sessão do WebChat (como `mphyls0-2hfb65`) não são aceitos nesse campo.

**Formato correto:**

**Outros pontos a verificar:**

* O header de autenticação deve usar `Bearer`, não outras variações:

Se o contato do WebChat **não possui telefone cadastrado**, não é possível enviar mensagem por essa rota. O campo `number` exige um telefone válido — o identificador do WebChat não substitui o número. Nesse caso, o atendimento deve seguir pelo próprio ticket do WebChat dentro do sistema.

---

## Erros de Apontamento DNS

### Erro ao gerar o certificado HTTPS

* Verifique se o apontamento foi prapagado
* Acesse a servidor em nuvem como root e execute o comando

## Erros de Banco de Dados

## Erro ao acessar Postgres

Internal server error: SequelizeConnectionError: could not open file "global/pg\_filenode.map": Permission denied

Acessar o terminal com root

Acessar o portainer, abrir console do postgres e executar o comando

### Caso o erro persista, criar uma rotina no crontab

Acessar o terminal com root

## Erros de Frontend

## Customização não são carregadas no front

Acessar a servidor em nuvem como deployzdg

Realizar as customizações

[AnteriorTypebot autohospedado](/avancado-recursos-tecnicos/integracoes-terceiras/typebot-autohospedado)[PróximoTemplate (WABA) não chega ao destinatário](/avancado-recursos-tecnicos/erros-e-avisos-comuns/template-waba-nao-chega-ao-destinatario)

Atualizado há 1 mês

Isto foi útil?