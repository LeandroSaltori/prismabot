Copiar

Nesta página

1. [Avançado - Recursos técnicos](/avancado-recursos-tecnicos)

# Banco de dados - Como acessar

Esta documentação orienta o usuário sobre como se conectar ao banco de dados PostgreSQL do Prismabot. Esse acesso é importante para momentos em que você precise visualizar, manipular, exportar, baixar ou importar dados diretamente nas tabelas do sistema (como mensagens, contatos, etc.).

#### 🛠️ Ferramenta Necessária

Para realizar este procedimento, utilizaremos o software **PGAdmin**.

* **O que é:** Um programa gratuito e com interface gráfica para gerenciamento de bancos de dados PostgreSQL.
* **Onde encontrar:** Baixe e instale gratuitamente na sua máquina local (consulte o link oficial de download do PGAdmin).

---

### Passo a Passo para Conexão

#### Passo 1: Localizar as Credenciais de Acesso

Antes de abrir o PGAdmin, você precisará do Usuário (*Username*) e da Senha (*Password*) do seu banco de dados. Você pode encontrar essas informações de duas formas:

1. **Sumário de Instalação:** Os dados são entregues no resumo gerado no final da instalação do sistema Prismabot.
2. **Arquivo .env:** Caso não tenha salvo o sumário, acesse o servidor (VPS) onde o Prismabot está hospedado, navegue até a pasta do **back-end** e abra o arquivo `.env`. Lá constarão o `username` e o `password` do banco de dados.

#### Passo 2: Configurar o Servidor no PGAdmin

Com o PGAdmin instalado e aberto em seu computador, siga os passos abaixo para criar a conexão:

1. Na tela inicial do PGAdmin, clique com o **botão direito** sobre a opção de servidores.
2. Selecione **Registrar > Servidor** (Register > Server).
3. Na aba **Geral (General)**:

   * **Nome:** Dê um nome de sua preferência para identificar a conexão (Exemplo: `Prismabot` ou `Prismabot - Produção`).
4. Na aba **Conexão (Connection)**:

   * **Endereço/Host:** Insira o **IP da sua VPS** (Atenção: utilize `localhost` apenas se o sistema estiver rodando fisicamente no seu próprio computador).
   * **Username (Nome de usuário):** Insira o usuário localizado no Passo 1.
   * **Password (Senha):** Insira a senha localizada no Passo 1.
5. Salve as configurações. O PGAdmin se conectará automaticamente ao servidor.

#### Passo 3: Navegando pelas Tabelas do Prismabot

Com a conexão estabelecida com sucesso:

1. Expanda a conexão recém-criada no menu lateral.
2. Localize a opção **Bancos de Dados (Databases)** e abra o banco correspondente à sua instalação (nas instalações atuais, procure pelo banco com nome `Zepro` ou equivalente; em versões muito antigas, o nome era `izing`).
3. Para encontrar as informações do sistema, navegue pelo seguinte caminho:

   * **Esquemas (Schemas)** > **Tabelas (Tables)**.

✅ **Pronto!** Agora você tem acesso a todas as tabelas da solução Prismabot (como a tabela de mensagens, por exemplo). Através dessa interface, você pode visualizar e manipular todas as informações conforme a necessidade da sua operação.

### Vídeo aula no portar do assinante:

[https://portal.zdg.com.br/270021-sistema-prismabot/5179470-acessando-o-banco-de-dados](https://portal.zdg.com.br/270021-sistema-prismabot/5179470-acessando-o-banco-de-dados )

[AnteriorWavoip - Ligações pelo WhatsApp](/ferramentas-adicionais-e-integracoes/wavoip-ligacoes-pelo-whatsapp)[PróximoComo diagnosticar o erro "servidor temporariamente off-line"](/avancado-recursos-tecnicos/como-diagnosticar-o-erro-servidor-temporariamente-off-line)

Atualizado há 4 meses

Isto foi útil?