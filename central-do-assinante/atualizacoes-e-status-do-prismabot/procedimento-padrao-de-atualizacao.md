Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Atualizações e Status do Prismabot](/central-do-assinante/atualizacoes-e-status-do-prismabot)

# Procedimento Padrão de Atualização

Como atualizar o Prismabot: atualização automática via script ou manual via terminal. Diferença entre versão Homolog e Hotfix e quando usar cada uma.

Manter o Prismabot atualizado garante segurança, estabilidade e acesso às novas funcionalidades. Este guia cobre os dois métodos disponíveis: atualização automática (recomendada para a maioria) e atualização manual (para ambientes com customizações).

Antes de iniciar, leia as notas da nova versão no Changelog para verificar se há **Breaking Changes** ou ações manuais necessárias.

[Changelog (4.0.x última versão)](/central-do-assinante/atualizacoes-e-status-do-prismabot/changelog-4.0.x-ultima-versao)

---

### Versões disponíveis para download

O Prismabot é distribuído em duas versões:

Versão

Para quem

Quando usar

**Homolog**

Operação padrão

Versão estável, recomendada para a maioria das instalações. Passou pela homologação antes do lançamento

**Hotfix**

Quem precisa de correções recentes

Contém correções e melhorias lançadas nos últimos dias. Mais recente que a Homolog, mas com ciclo de testes mais curto

Os pacotes de download estão disponíveis na área de membros:

[**Portal do assinante → Módulo de Instalação**](https://prismatelecomservicos.com/)

O pacote de instalação/atualização (`prismabot_passaporte_shell`) é de uso exclusivo do assinante. É proibido compartilhá-lo em grupos ou com terceiros.

---

### Passo 1 — Backup (obrigatório antes de qualquer atualização)

**Faça um snapshot do servidor antes de continuar.**

Acesse o painel do seu provedor de servidor em nuvem e crie um snapshot completo do servidor. Essa é a única garantia de reverter o sistema ao estado anterior em caso de falha durante a atualização. Não prossiga sem um backup recente.

---

### Método 1 — Atualização automática via terminal

Recomendado para a maioria das instalações. Um script cuida de todo o processo automaticamente.

O vídeo completo desta aula está disponível no [portal do assinante](https://prismatelecomservicos.com/).

#### Pré-requisitos

1. Faça o download do pacote da versão desejada (Homolog ou Hotfix) na área de membros
2. Descompacte o arquivo `.zip` no seu computador

#### Passo 2 — Upload e substituição dos arquivos

1. Conecte-se ao servidor via **SFTP** (usando Bitvise ou outro cliente)
2. Envie a pasta `prismabot_passaporte_shell` descompactada para o diretório `/root` do servidor
3. **Substitua completamente** a pasta antiga e todos os seus arquivos

#### Passo 3 — Execute o atualizador via SSH

Conecte-se ao servidor via SSH e execute os comandos em ordem:

No menu interativo que aparecer, pressione `2` + `Enter` para selecionar **"Atualizar instância primária"**.

O script executará o processo completo de atualização. Ao final, o terminal confirmará a conclusão e o sistema estará na versão mais recente.

---

### Método 2 — Atualização manual via terminal

Para usuários com instalações customizadas ou que realizaram a instalação com parâmetros diferentes do auto-instalador padrão.

**Faça o snapshot antes de iniciar** (ver Passo 1). A atualização manual envolve substituição de arquivos e alterações no banco de dados — sem backup, não há como reverter em caso de erro.

O vídeo completo desta aula está disponível no [portal do assinante](https://prismatelecomservicos.com/).

#### Passo 2 — Acesso e preparação do ambiente

Acesse o servidor via SSH com o usuário da aplicação (geralmente `deployzdg`) e navegue até o diretório raiz da instalação do Prismabot.

#### Passo 3 — Upload e substituição do frontend

1. Faça upload do pacote de atualização (`update.zip`) para a raiz da instalação
2. Renomeie a pasta do frontend atual para preservar o backup local:

1. Extraia o novo pacote:

#### Passo 4 — Configuração do novo frontend (Next.js)

1. Acesse o novo diretório do frontend
2. Identifique a porta de execução no arquivo `server.js`
3. Crie o arquivo de variáveis de ambiente:

1. Edite `.env.local` e configure a URL da API, a porta identificada e demais variáveis necessárias

#### Passo 5 — Build do frontend

O `npm run build` exige processamento intenso. Verifique se a servidor em nuvem tem RAM e swap adequados — memória insuficiente pode interromper o build por travamento.

#### Passo 6 — Atualização dos serviços no PM2

1. Identifique e remova o processo do frontend antigo (Vue):

1. Inicie o novo frontend conforme as diretrizes da nova versão
2. Salve as configurações:

#### Passo 7 — Atualização do backend e banco de dados

1. Acesse o diretório do backend
2. Instale as dependências:

1. Execute as migrações e seeders do banco de dados:

1. Reinicie o backend:

#### Passo 8 — Validação e limpeza

1. Acesse o painel pelo navegador e verifique:

   * A nova interface carregou corretamente
   * Os canais estão respondendo
2. Após confirmar o pleno funcionamento, remova os arquivos temporários:

[AnteriorValidade das versões](/central-do-assinante/atualizacoes-e-status-do-prismabot/changelog-4.0.x-ultima-versao/validade-das-versoes)[PróximoConexão com Passkey — APIs não oficiais](/central-do-assinante/atualizacoes-e-status-do-prismabot/conexao-com-passkey-apis-nao-oficiais)

Atualizado há 1 mês

Isto foi útil?