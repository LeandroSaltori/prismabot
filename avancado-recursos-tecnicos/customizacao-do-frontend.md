Copiar

Nesta página

1. [Avançado - Recursos técnicos](/avancado-recursos-tecnicos)

# Customização do Frontend

### Introdução e Avisos Importantes

O código do frontend do Prismabot é aberto e permite customizações para adequá-lo à sua marca.

**AVISO: CONHECIMENTO TÉCNICO NECESSÁRIO**

* As alterações descritas nesta documentação exigem conhecimento técnico em desenvolvimento **Vue.js** e administração de servidores Linux.
* Antes de iniciar **qualquer** procedimento, crie um **ponto de restauração (snapshot)** completo do seu servidor VPS. Alterações incorretas podem comprometer o funcionamento da sua plataforma.
* Todas as alterações devem ser feitas logado na VPS com o usuário `deployzdg`. **Não realize os procedimentos se estiver logado como** `root`.
* O Prismabot não se responsabilza com alterações no frontend e suporte para essas personalizações.

### Procedimento Obrigatório Após Alterações

Após realizar qualquer modificação nos arquivos do frontend, você **precisa** "compilar" o código para que as mudanças apareçam na sua aplicação. Siga os passos abaixo:

Copiar

```
1. navegar até a pasta do frontend pelo terminal
2. cd prismabot.io
3. cd frontend
4. export NODE_OPTIONS=--openssl-legacy-provider && npx quasar build -P -m pwa
5. pm2 restart all
6. limpar os cookies/cache do navegador
```

---

### Guia de Customização por Elemento

#### Ícones

* **Local:** `frontend/public/icons`
* **Ação:** Gere e substitua os arquivos de ícone nos tamanhos disponíveis nesta pasta.

#### Logos e Favicon

* **Local:** `frontend/public/`
* **Ação:** Substitua os seguintes arquivos pelos seus:

  + `frontend/public/prismabot.png`
  + `frontend/public/favicon.ico`

#### Vídeos e Sons

* **Local:** `frontend/src/assets`
* **Ação:** Substitua os seguintes arquivos:

  + `frontend/src/assets/110694.mp4` (Vídeo da tela de login)
  + `frontend/src/assets/sound.mp3` (Som de notificação)
  + `frontend/src/assets/sound.ogg` (Som de notificação)

#### Nomes da Aplicação

* **Ação:** Altere o nome "Prismabot" para o nome da sua marca nos seguintes arquivos e locais:

  + **Arquivo:** `frontend/quasar.conf.js`
  + **Arquivo:** `frontend/src/App.vue`
  + **Arquivo:** `frontend/src/index.template.html`

#### Cores

* **Ação:** Altere os códigos hexadecimais de cor (`#5c67f2`, etc.) nos seguintes arquivos:

  + **Arquivo:** `frontend/src/css/app.sass` (Estilos e Fontes)
  + **Arquivo:** `frontend/src/css/quasar.variables.sass` (Cores Básicas)
  + **Arquivo:** `frontend/src/pages/dashboard/Index.vue` (Cores Dashboard)
  + **Arquivo:** `frontend/src/components/EssentialLink.vue` (Borda Esquerda do Menu)
  + **Arquivo:** `frontend/src/pages/relatorios/ccListaRelatorios.vue` (Bordas dos Relatórios)
  + **Arquivos:** `frontend/src/pages/atendimento/ModalLayout.vue` e `frontend/src/layouts/ModalLayout.vue` (Borda do Modal de Atendimento)
  + **Arquivos do Construtor de Chatbot (**`frontend/src/components/ccFlowBuilder/`**):**

    - `panel.vue`: `paintStyle: { strokeWidth: 3, stroke: '#5c67f2' }`
    - `node.vue`: `border-left: 5px solid #5c67f2 !important;`
    - `mixins.js`: `stroke: '#5c67f2'` e `HoverPaintStyle: { stroke: '#5c67f2', ... }`
    - `jsplumb.js`: `EndpointStyle: { fill: "#5c67f2" }` e `PaintStyle: { ..., stroke: "#5c67f2" }`
    - `defaultFlow.js`: `paintStyle: { strokeWidth: 3, stroke: '#5c67f2' }`
    - `index.css`: Altere as variáveis CSS como `--primary-color: #5c67f2;`

---

### Precisa de Ajuda Profissional?

Como mencionado, a customização do frontend requer a ajuda de um desenvolvedor com experiência em Vue.js.

Se precisar de indicações, temos uma lista de profissionais e parceiros externos que podem te auxiliar. Para isso, por favor, abra um chamado no departamento **"Preciso de indicação de profissional para manutenção e desenvolvimento"**.

[AnteriorComo liberar espaço em disco na VPS do Prismabot](/avancado-recursos-tecnicos/como-liberar-espaco-em-disco-na-vps-do-prismabot)[PróximoIntegrando o chat GPT](/avancado-recursos-tecnicos/integrando-o-chat-gpt)

Atualizado há 5 meses

Isto foi útil?