# Procedimento Padrão de Atualização

Manter o Prismabot atualizado garante segurança, estabilidade e acesso às novas funcionalidades. Este guia cobre os dois métodos disponíveis: atualização automática (recomendada para a maioria) e atualização manual (para ambientes com customizações).

Antes de iniciar, leia as notas da nova versão no Changelog para verificar se há **Breaking Changes** ou ações manuais necessárias.

{% content-ref url="/pages/9DHSTWtSbsPvYR8zkUAE" %}
[Changelog (4.0.x última versão)](/central-do-assinante/atualizacoes-e-status-do-z-pro/changelog-4.0.x-ultima-versao.md)
{% endcontent-ref %}

***

### Versões disponíveis para download

O Prismabot é distribuído em duas versões:

<table><thead><tr><th width="103.5">Versão</th><th width="233.5">Para quem</th><th>Quando usar</th></tr></thead><tbody><tr><td><strong>Homolog</strong></td><td>Operação padrão</td><td>Versão estável, recomendada para a maioria das instalações. Passou pela homologação antes do lançamento</td></tr><tr><td><strong>Hotfix</strong></td><td>Quem precisa de correções recentes</td><td>Contém correções e melhorias lançadas nos últimos dias. Mais recente que a Homolog, mas com ciclo de testes mais curto</td></tr></tbody></table>

Os pacotes de download estão disponíveis na área de membros:

[**Portal do assinante → Módulo de Instalação**](https://portal.zdg.com.br/)

{% hint style="warning" %}
O pacote de instalação/atualização (`zpro_passaporte_shell`) é de uso exclusivo do assinante. É proibido compartilhá-lo em grupos ou com terceiros.
{% endhint %}

***

### Passo 1 — Backup (obrigatório antes de qualquer atualização)

{% hint style="danger" %}
**Faça um snapshot do servidor antes de continuar.**

Acesse o painel do seu provedor de VPS e crie um snapshot completo do servidor. Essa é a única garantia de reverter o sistema ao estado anterior em caso de falha durante a atualização. Não prossiga sem um backup recente.
{% endhint %}

***

### Método 1 — Atualização automática via terminal

Recomendado para a maioria das instalações. Um script cuida de todo o processo automaticamente.

{% hint style="info" %}
O vídeo completo desta aula está disponível no [portal do assinante](https://portal.zdg.com.br/270021-sistema-zpro/5179468-atualizacao-automatica-via-terminal).
{% endhint %}

#### Pré-requisitos

1. Faça o download do pacote da versão desejada (Homolog ou Hotfix) na área de membros
2. Descompacte o arquivo `.zip` no seu computador

#### Passo 2 — Upload e substituição dos arquivos

1. Conecte-se ao servidor via **SFTP** (usando Bitvise ou outro cliente)
2. Envie a pasta `zpro_passaporte_shell` descompactada para o diretório `/root` do servidor
3. **Substitua completamente** a pasta antiga e todos os seus arquivos

#### Passo 3 — Execute o atualizador via SSH

Conecte-se ao servidor via SSH e execute os comandos em ordem:

```bash
sudo chmod +x ./zpro_passaporte_shell/zpro
cd ./zpro_passaporte_shell
sudo ./zpro
```

No menu interativo que aparecer, pressione `2` + `Enter` para selecionar **"Atualizar instância primária"**.

O script executará o processo completo de atualização. Ao final, o terminal confirmará a conclusão e o sistema estará na versão mais recente.

***

### Método 2 — Atualização manual via terminal

Para usuários com instalações customizadas ou que realizaram a instalação com parâmetros diferentes do auto-instalador padrão.

{% hint style="danger" %}
**Faça o snapshot antes de iniciar** (ver Passo 1). A atualização manual envolve substituição de arquivos e alterações no banco de dados — sem backup, não há como reverter em caso de erro.
{% endhint %}

{% hint style="info" %}
O vídeo completo desta aula está disponível no [portal do assinante](https://portal.zdg.com.br/270021-sistema-zpro/5179469-atualizacao-manual-via-terminal-v4).
{% endhint %}

#### Passo 2 — Acesso e preparação do ambiente

Acesse o servidor via SSH com o usuário da aplicação (geralmente `deployzdg`) e navegue até o diretório raiz da instalação do Prismabot.

#### Passo 3 — Upload e substituição do frontend

1. Faça upload do pacote de atualização (`update.zip`) para a raiz da instalação
2. Renomeie a pasta do frontend atual para preservar o backup local:

```bash
mv frontend frontend_old
```

3. Extraia o novo pacote:

```bash
unzip update.zip
```

#### Passo 4 — Configuração do novo frontend (Next.js)

1. Acesse o novo diretório do frontend
2. Identifique a porta de execução no arquivo `server.js`
3. Crie o arquivo de variáveis de ambiente:

```bash
cp .env.example .env.local
```

4. Edite `.env.local` e configure a URL da API, a porta identificada e demais variáveis necessárias

#### Passo 5 — Build do frontend

```bash
npm install
npm run build
```

{% hint style="warning" %}
O `npm run build` exige processamento intenso. Verifique se a VPS tem RAM e swap adequados — memória insuficiente pode interromper o build por travamento.
{% endhint %}

#### Passo 6 — Atualização dos serviços no PM2

```bash
pm2 list
```

1. Identifique e remova o processo do frontend antigo (Vue):

```bash
pm2 delete [nome_ou_id_do_processo_antigo]
```

2. Inicie o novo frontend conforme as diretrizes da nova versão
3. Salve as configurações:

```bash
pm2 save
```

#### Passo 7 — Atualização do backend e banco de dados

1. Acesse o diretório do backend
2. Instale as dependências:

```bash
npm install
```

3. Execute as migrações e seeders do banco de dados:

```bash
npx sequelize db:migrate
npx sequelize db:seed:all
```

4. Reinicie o backend:

```bash
pm2 restart [nome_ou_id_do_backend]
```

#### Passo 8 — Validação e limpeza

1. Acesse o painel pelo navegador e verifique:
   * A nova interface carregou corretamente
   * Os canais estão respondendo
2. Após confirmar o pleno funcionamento, remova os arquivos temporários:

```bash
rm update.zip
rm -rf frontend_old
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/central-do-assinante/atualizacoes-e-status-do-z-pro/procedimento-padrao-de-atualizacao.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
