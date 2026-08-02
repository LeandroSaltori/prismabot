Copiar

Nesta página

1. [Avançado - Recursos técnicos](/avancado-recursos-tecnicos)

# Como liberar espaço em disco na VPS do Prismabot

Quando a VPS está com o disco cheio (ou perto disso), o sistema pode ficar lento, travar o login ou até derrubar o backend. Este guia mostra como diagnosticar o que está ocupando espaço e como liberá-lo com segurança, cobrindo tanto a limpeza pelo terminal quanto pelo painel administrativo do Prismabot.

**Pré-requisitos:**

* Acesso root/sudo à VPS via SSH (para os comandos de terminal).
* Acesso **Super Admin** no painel (para a limpeza de dados por tenant).
* Recomendado: um snapshot/backup da VPS antes de rodar comandos de remoção.

### Vídeo tutorial

---

### Como funciona

Espaço em disco ocupado no Prismabot normalmente vem de três frentes: **mídias acumuladas** por tenant (pasta `public` do backend), **pastas de backup** deixadas por atualizações, e **logs do sistema** (PM2, journal, npm). As duas primeiras costumam ser as maiores — vale sempre começar por elas.

Antes de rodar qualquer comando de remoção (`rm -rf`), confirme o caminho completo. Um comando errado pode apagar pastas em uso — sempre prefira digitar o caminho exato em vez de um curinga solto (ex.: `frontend.*`).

---

### Etapa 1: Diagnóstico geral do disco

No terminal da VPS, os dois comandos essenciais são:

Se alguma partição estiver perto de 100% em "Use%", é hora de investigar o que está ocupando esse espaço.

---

### Etapa 2: Encontrar os maiores arquivos e pastas

Para listar as maiores pastas dentro do diretório da instalação, ordenadas da maior para a menor:

Para listar os maiores arquivos individuais em toda a VPS (top 20):

Se algum volume externo (ex.: um HD separado usado só para backup) aparecer nessa lista, normalmente não faz parte do disco principal do sistema e pode ser desconsiderado da análise.

No caso do Prismabot, o maior consumo costuma estar na **pasta** `public` **do backend**, onde ficam as mídias recebidas/enviadas por todos os tenants. É possível ver o consumo por tenant (pela pasta correspondente ao ID) para identificar qual cliente está usando mais espaço.

---

### Etapa 3: Limpar mídias por tenant (painel Super Admin)

Em vez de mexer direto nos arquivos pelo terminal, o painel permite sanitizar os dados de um tenant específico:

1. Acesse **Superadmin → Tenants e Licenciamento → Tenants**.
2. Localize o tenant identificado na Etapa 2 e clique no menu de **três pontos** ao lado dele.
3. Use **Calcular tamanho dos dados** para confirmar o quanto aquele tenant está ocupando.
4. Use **Limpeza por filtro** para remover mensagens/mídias antigas — é possível filtrar por:

   * Apenas por **tempo** (ex.: tudo com mais de 60 dias).
   * Apenas por **tamanho** (ex.: tudo acima de 200 MB).
   * Ou pelos dois critérios combinados.
5. Para remover todas as mídias já armazenadas daquele tenant, use **Apagar arquivos da empresa**.

**Importante:** confirme o tenant certo antes de aplicar a limpeza — a ação remove dados permanentemente e não pode ser desfeita.

---

### Etapa 4: Limpar pastas de backup deixadas por atualizações

Toda atualização feita pelo autoinstalador cria uma pasta de backup (padrão de nome `frontend.bak.<timestamp>` / `backend.bak.<timestamp>`) como segurança — se a atualização falhar, o autoinstalador consegue reverter para essa cópia. Depois de confirmar que uma atualização funcionou, essas pastas só ocupam espaço e podem ser removidas.

**Nunca** use um curinga solto como `rm -rf frontend.*` — isso pode remover também a pasta `frontend` em produção. Sempre digite (ou copie) o nome completo da pasta de backup.

Se você tem uma **instalação secundária** (multi-servidor), confira também lá — as pastas de backup são geradas a cada atualização em cada instalação.

---

### Etapa 5: Limpar logs do sistema

**Logs do PM2** (processos do Prismabot):

**Cache do npm:**

**Logs do sistema (journal):**

Os logs ajudam a diagnosticar problemas caso algo dê errado depois — evite apagá-los por completo. Uma rotina de limpeza semanal (reduzindo para um tamanho como 500 MB) é suficiente para manter o disco sob controle sem perder o histórico recente.

---

### Alternativa definitiva: Storage externo (S3)

Se o disco enche recorrentemente por causa de mídias, a solução definitiva é mover o armazenamento para um provedor externo (AWS, Cloudflare R2, Wasabi, MinIO), em vez de ficar sanitizando manualmente. Veja o guia completo: Storage S3.

Se tiver dúvidas de como configurar seu tipo específico de storage, abra um chamado no suporte com os detalhes do que já tentou — a equipe orienta o restante.

---

### Resumo das Funcionalidades

Funcionalidade

Onde acessar

Diagnóstico geral de disco

Terminal SSH — `df -h`

Maiores arquivos/pastas

Terminal SSH — `du`

Limpar mídias de um tenant

Superadmin → Tenants → menu de três pontos → Limpeza por filtro / Apagar arquivos da empresa

Limpar pastas de backup pós-atualização

Terminal SSH — pasta da instalação (`frontend.bak.*` / `backend.bak.*`)

Limpar logs do PM2

Terminal SSH — `pm2 flush`

Limpar logs do sistema (journal)

Terminal SSH — `journalctl --vacuum-size`

Solução definitiva para mídias

Superadmin → Sistema → Storage S3

---

### Encerramento

Com o disco liberado, o servidor volta a operar normalmente — sem risco de travar o recebimento de mídias grandes ou interromper o backup noturno. Repetir esse checklist periodicamente (ou migrar para Storage S3) evita que o problema volte a se acumular.

---

### Possíveis Erros e Soluções

#### O disco voltou a encher pouco tempo depois da limpeza

**Causa:** o que ocupa o disco é mídia acumulada em uso ativo, não backup ou log. **Solução:** migre o armazenamento para Storage S3 em vez de sanitizar manualmente com frequência.

#### Apaguei a pasta errada por engano com um curinga (`rm -rf frontend.*`)

**Causa:** curinga solto pegou também a pasta em produção, não só a de backup. **Solução:** restaure a partir do backup/snapshot da VPS — por isso a recomendação de snapshot antes de qualquer remoção em massa.

#### `df -h` mostra espaço livre, mas o sistema ainda acusa disco cheio

**Causa:** esgotamento de **inodes**, não de espaço em bytes. **Solução:** rode `df -i` para confirmar e localize diretórios com excesso de arquivos pequenos (ex.: muitos arquivos de sessão/cache).

[AnteriorErro de Autenticação no app Whatsapp Oauth](/avancado-recursos-tecnicos/erro-de-autenticacao-no-app-whatsapp-oauth)[PróximoCustomização do Frontend](/avancado-recursos-tecnicos/customizacao-do-frontend)

Atualizado há 15 dias

Isto foi útil?