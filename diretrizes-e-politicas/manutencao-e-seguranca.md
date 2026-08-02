Copiar

Nesta página

1. [Diretrizes e Políticas](/diretrizes-e-politicas)

# Manutenção e Segurança

Ações obrigatórias após a instalação: alterar credenciais padrão, configurar firewall, criar rotina de backups e manter o servidor atualizado.

O Prismabot é um software **self-hosted**: a ZDG entrega a licença e o instalador; você hospeda e opera o sistema na própria VPS. Isso significa que a segurança e a manutenção do ambiente são de sua responsabilidade após a instalação.

Esta página reúne as ações que você precisa executar para manter sua instância segura e atualizada.

---

### Instalação

Antes de colocar o sistema em operação, certifique-se de que o servidor atende aos requisitos mínimos de hardware e software:

[Pré-requisitos de instalação e utilização](/diretrizes-e-politicas/pre-requisitos-de-instalacao-e-utilizacao)

Para instalar o sistema, siga o guia de instalação:

[2. Processo de instalação do Prismabot](/primeiro-acesso/instalar-prismabot/2.-instalacao-automatica)

---

### Atualizações

Manter o Prismabot atualizado é **responsabilidade do assinante** e é fundamental para garantir segurança, estabilidade e acesso aos novos recursos.

Para executar uma atualização, siga o procedimento padrão:

[Procedimento Padrão de Atualização](/central-do-assinante/atualizacoes-e-status-do-prismabot/procedimento-padrao-de-atualizacao)

Para acompanhar o que mudou em cada versão, consulte o changelog:

[Changelog (4.0.x última versão)](/central-do-assinante/atualizacoes-e-status-do-prismabot/changelog-4.0.x-ultima-versao)

---

### Segurança da instância

#### Imediatamente após a instalação (obrigatório)

Ao instalar o Prismabot pela primeira vez, altere as credenciais padrão antes de colocar o sistema em operação:

O que alterar

Onde

**JWT\_SECRET** e **JWT\_REFRESH\_SECRET**

Arquivo `.env` do backend

**Senhas dos bancos de dados**

Configuração do PostgreSQL/Redis

**Senha do usuário de deploy** (`deployzdg`)

Terminal da VPS

Não colocar o sistema em produção sem alterar essas credenciais. Instâncias com valores padrão são vulneráveis a acessos não autorizados.

---

#### Firewall

Mantenha um firewall ativo na VPS. As únicas portas que precisam estar abertas para o funcionamento do Prismabot são:

Porta

Protocolo

Uso

`22`

TCP

Acesso SSH à VPS

`80`

TCP

HTTP (redirecionamento para HTTPS)

`443`

TCP

HTTPS (acesso ao painel)

Todas as demais portas devem permanecer **bloqueadas**.

---

#### Manutenção do servidor

Além das configurações acima, execute periodicamente:

* Atualizações de segurança do sistema operacional (Ubuntu)
* Revisão de logs de acesso SSH
* Monitoramento de uso de CPU e RAM

O suporte técnico da ZDG **não cobre** configuração, gestão ou segurança do servidor. Consulte o escopo completo em [Política de Suporte Técnico](/diretrizes-e-politicas/politica-de-suporte-tecnico).

---

### Backups

A criação e a gestão de rotinas de backup são de **inteira responsabilidade do assinante**. A ZDG não tem acesso ao banco de dados instalado na sua VPS e não realiza backups remotos.

Configure uma rotina de backup automático que cubra:

* Banco de dados PostgreSQL
* Arquivos de mídia armazenados pelo sistema
* Arquivo `.env` de configuração

Sem backup, a perda de dados por falha de hardware ou erro operacional é irreversível. Considere replicar os backups para um storage externo à VPS.

---

### Responsabilidades e documentos relacionados

Para entender o que é responsabilidade da ZDG e o que é responsabilidade do assinante em detalhe:

* [Termos e Condições de Uso e Licenciamento](https://ajuda.zdg.com.br/) — cláusulas 8 (obrigações e responsabilidades) e 10 (privacidade e proteção de dados)
* [Política de Suporte Técnico](/diretrizes-e-politicas/politica-de-suporte-tecnico) — o que está e o que não está incluso no suporte
* [Aviso de Privacidade](/diretrizes-e-politicas/aviso-de-privacidade) — como os dados são tratados no modelo self-hosted

[AnteriorAviso de Privacidade](/diretrizes-e-politicas/aviso-de-privacidade)[PróximoAPI Oficial vs API Não Oficial](/diretrizes-e-politicas/api-oficial-vs-api-nao-oficial)

Atualizado há 1 mês

Isto foi útil?