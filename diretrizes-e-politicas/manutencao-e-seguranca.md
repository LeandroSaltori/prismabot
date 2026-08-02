# Manutenção e Segurança

Ações obrigatórias após a instalação: alterar credenciais padrão, configurar firewall, criar rotina de backups e manter o servidor atualizado.

O Prismabot é um software **em nuvem**: A Prisma Telecom gerencia toda a infraestrutura e entrega o Prismabot pronto para uso em nuvem. Isso significa que a segurança e a manutenção do ambiente são de sua responsabilidade após a instalação.

Esta página reúne as ações que você precisa executar para manter sua instância segura e atualizada.

---

### Instalação

Antes de colocar o sistema em operação, certifique-se de que o servidor atende aos requisitos mínimos de hardware e software:

[Pré-requisitos de instalação e utilização](pre-requisitos-de-instalacao-e-utilizacao.md)

Para instalar o sistema, siga o guia de instalação:

[2. Processo de instalação do Prismabot](../primeiro-acesso/primeiro-acesso-ao-sistema.md)

---

### Atualizações

Manter o Prismabot atualizado é **responsabilidade do assinante** e é fundamental para garantir segurança, estabilidade e acesso aos novos recursos.

Para executar uma atualização, siga o procedimento padrão:

[Procedimento Padrão de Atualização](../central-do-assinante/atualizacoes-e-status-do-prismabot/procedimento-padrao-de-atualizacao.md)

Para acompanhar o que mudou em cada versão, consulte o changelog:

[Changelog (4.0.x última versão)](../central-do-assinante/atualizacoes-e-status-do-prismabot/changelog-4.0.x-ultima-versao.md)

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

Terminal da servidor

Não colocar o sistema em produção sem alterar essas credenciais. Instâncias com valores padrão são vulneráveis a acessos não autorizados.

---

#### Firewall

Mantenha um firewall ativo na servidor. As únicas portas que precisam estar abertas para o funcionamento do Prismabot são:

Porta

Protocolo

Uso

`22`

TCP

Acesso SSH à servidor

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

O suporte técnico da Prisma Telecom **não cobre** configuração, gestão ou segurança do servidor. Consulte o escopo completo em [Política de Suporte Técnico](politica-de-suporte-tecnico.md).

---

### Backups

A criação e a gestão de rotinas de backup são de **inteira responsabilidade do assinante**. A Prisma Telecom não tem acesso ao banco de dados instalado na nuvem e não realiza backups remotos.

Configure uma rotina de backup automático que cubra:

* Banco de dados PostgreSQL
* Arquivos de mídia armazenados pelo sistema
* Arquivo `.env` de configuração

Sem backup, a perda de dados por falha de hardware ou erro operacional é irreversível. Considere replicar os backups para um storage externo à servidor.

---

### Responsabilidades e documentos relacionados

Para entender o que é responsabilidade da Prisma Telecom e o que é responsabilidade do assinante em detalhe:

* [Termos e Condições de Uso e Licenciamento](https://prismatelecomservicos.com/ rel=) — cláusulas 8 (obrigações e responsabilidades) e 10 (privacidade e proteção de dados)
* [Política de Suporte Técnico](politica-de-suporte-tecnico.md) — o que está e o que não está incluso no suporte
* [Aviso de Privacidade](aviso-de-privacidade.md) — como os dados são tratados no modelo em nuvem



Atualizado há 1 mês

Isto foi útil?