# Conexão com Passkey — APIs não oficiais

Em 30/06/2025, o WhatsApp ativou uma nova camada de segurança que exige uma **Chave de Acesso (Passkey)** durante o processo de vinculação de novos dispositivos. Isso quebrou o fluxo tradicional de leitura de QR Code utilizado pelas bibliotecas não oficiais — o problema **não é específico do Prismabot** e afeta todo o ecossistema de APIs não oficiais.

---

### Status de compatibilidade por biblioteca

Biblioteca

Status

**Baileys**

✅ Compatível — já disponível no Prismabot

**WhatsMeow**

✅ Compatível — já disponível no Prismabot

**UAZAPI**

✅ Compatível — disponível via Hotfix

**Z-API**

🟡 Conector próprio — sem suporte nativo no momento

**wwebjs**

🟠 Aguardando atualização da biblioteca oficial

**Evolution API**

🟠 Aguardando atualização da biblioteca base

Se a sua sessão já está conectada e funcionando, **não desconecte nem recrie a sessão** sem necessidade até que sua biblioteca esteja homologada.

---

### Solução: extensão Passkey Linker

A Prisma Telecom desenvolveu e disponibiliza gratuitamente a extensão **Passkey Linker** para o Google Chrome. Ela autentica via WhatsApp Web e exporta automaticamente as credenciais para o Prismabot — reproduzindo o fluxo tradicional de QR Code de forma transparente para o usuário final.

Milhares de APIs Foram Impactadas pela Nova Atualização do WhatsApp

---

### Passo a passo para usuários Prismabot

#### Passo 1 — Instale a extensão Passkey Linker

Acesse a Chrome Web Store e instale a versão mais recente da extensão:

[![Logo](../../.gitbook/assets/image_39c3bf69.png)Passkey Linker - Chrome Web Storechromewebstore.google.com](https://chromewebstore.google.com/detail/passkey-linker/hehoacnepmncbjckgnfekfcgdijpigaj)

Passkey Linker — Chrome Web Store

**Versão mínima recomendada: 3.6.0.** Se você já utilizava a extensão, verifique se ela foi atualizada para essa versão na Chrome Web Store antes de prosseguir.

#### Passo 2 — Autentique no WhatsApp Web

Abra o [WhatsApp Web](https://web.whatsapp.com/) no Chrome e faça o login normalmente com o celular:

1. Leia o QR Code com o aplicativo do WhatsApp
2. Se o WhatsApp solicitar a verificação de Passkey, complete o processo de autenticação exigido (Google Authenticator, chave de segurança ou chave salva no Chrome)
3. Aguarde o WhatsApp Web carregar completamente

#### Passo 3 — Conecte o canal no Prismabot

1. No painel, acesse **Administração → Canais**
2. Clique em **Adicionar canal** e selecione o tipo **Baileys** ou **WhatsMeow**
3. Dê um nome ao canal e salve
4. Na tela de conexão do canal, clique no botão **WhatsApp Web**

O Prismabot detectará automaticamente a sessão autenticada do WhatsApp Web e importará as credenciais. Basta confirmar a conexão.

Processo concluído. A partir da versão 3.6.0 **não é mais necessário clicar em "Extrair Sessão"** — a integração com o Prismabot é automática.

---

### Usando a extensão com outros sistemas (não Prismabot)

A extensão Passkey Linker é Prismabot e pode ser usada com qualquer sistema compatível com Baileys ou WhatsMeow.

1. Instale a extensão conforme o Passo 1
2. Abra o WhatsApp Web e autentique normalmente (com Passkey, se exigido)
3. Clique no ícone da extensão na barra do Chrome
4. Clique em **Extrair sessão** e copie as credenciais exibidas
5. Cole-as no backend ou sistema que você utiliza para autenticação

**Revendedores Prismabot:** a extensão é gratuita e Prismabot — pode ser indicada livremente aos seus clientes.

---

### Perguntas frequentes

**Minha sessão já está conectada. Preciso fazer algo?** Não. O Passkey Linker é necessário apenas para conectar **novas** sessões. Sessões existentes e ativas não são afetadas — não as desconecte sem necessidade.

**A extensão funciona com wwebjs ou Evolution?** Ainda não. Essas bibliotecas aguardam atualização dos seus respectivos mantenedores. Assim que estiver disponível, publicaremos um Hotfix do Prismabot com a compatibilidade.

**A extensão tem custo?** Não. É gratuita e disponibilizada pela Prisma Telecom para toda a comunidade.



 29 dias
