Copiar

Nesta página

1. [Avançado - Recursos técnicos](/avancado-recursos-tecnicos)

# Como diagnosticar o erro "servidor temporariamente off-line"

Se o seu Prismabot parou de carregar (tela branca, erro de conexão ou "servidor offline"), na maioria dos casos dá pra identificar — e às vezes já resolver — sozinho, em menos de 5 minutos, sem esperar o suporte. Este checklist ensina a acessar o terminal do seu servidor e descobrir exatamente o que parou.

**Acabou de atualizar ou instalar o Prismabot?** Antes de sair investigando, **espere cerca de 5 minutos**. É normal o sistema ficar temporariamente fora do ar logo após uma atualização ou instalação — as dependências do servidor levam alguns minutos para inicializar por completo. Na grande maioria dos casos em que esse erro aparece logo depois de atualizar/instalar, o problema se resolve sozinho nesse intervalo, sem precisar de nenhum dos passos abaixo.

**Pré-requisitos:**

* Acesso **SSH** à nuvem (usuário e senha, ou chave — o mesmo acesso usado na instalação).
* Um terminal para conectar: PuTTY (Windows), o Terminal do Mac/Linux, ou o terminal web da sua hospedagem (ex: Hostinger).

---

### Como funciona

O Prismabot roda como um processo (`backend`) gerenciado pelo **PM2** dentro do usuário `deployzdg` da nuvem. Quando o sistema "cai", quase sempre é esse processo que parou, travou ou entrou em loop de reinício — não é preciso reinstalar nada para descobrir o motivo.

**Atenção:** os comandos abaixo apenas **consultam** o estado do servidor — nenhum deles apaga dados ou arquivos. Pode seguir o checklist com tranquilidade.

---

### Etapa 1: Acesse o terminal e o usuário do sistema

1. Conecte na nuvem via SSH (ou abra o terminal web da hospedagem).
2. Entre no usuário `deployzdg` — é obrigatório, as aplicações rodam dentro dele:

Copiar

```
sudo su deployzdg
```

---

### Etapa 2: Antes de qualquer coisa, reinicie o backend

Reiniciar resolve boa parte das instabilidades pontuais, mesmo sem uma causa clara:

Acompanhe o `pm2 log` por alguns segundos após o restart para confirmar que ele ficou `online` e parou de reiniciar sozinho.

---

### Etapa 3: Veja se o backend está de pé

Liste os processos do sistema:

Olhe a coluna **status** da linha `zpro-backend`:

O que aparece

O que significa

`online`

O backend está rodando. Se mesmo assim o sistema não abre, o problema é de rede/domínio/navegador — pule para "Possíveis Erros" abaixo.

`errored` / `stopped`

O backend caiu. Siga para a Etapa 3.

Alternando `online` → `errored` sem parar

Está em **crash-loop** (cai, tenta subir, cai de novo). Siga para a Etapa 3.

---

### Etapa 4: Descarte o motivo mais comum - Disco Cheio

Antes de olhar logs, confira o estado do disco do seu servidor.

Alguma partição perto de **100% em "Use%"**? (erro `disk_full` / `53100` no log do Postgres)

**Causa:** a servidor em nuvem ficou sem espaço em disco — quase sempre logs do PM2, cache ou mídias acumuladas.

**Solução:**

Se o espaço some de novo rápido, o problema costuma ser **mídia acumulada** — considere migrar para Storage S3 (Superadmin → Sistema → Storage S3).

---

### Etapa 5: Capture o erro exato (se ainda não resolveu)

Se o disco está ok e recriar o Redis não resolveu, veja o erro real que está derrubando o backend:

O erro que está causando a queda aparece na tela. **Copie o texto inteiro** (não só a última linha) — é essa mensagem que o suporte vai pedir se você precisar abrir um chamado.

Para sair e devolver o processo ao PM2:

**Não deixe rodando assim (**`node dist/server.js`**).** Esse modo é só para *ver* o erro na tela — ele morre se você fechar o SSH. Depois de copiar o erro, sempre devolva ao PM2 com `pm2 start zpro-backend` (ou `pm2 restart all`).

---

### Resumo do checklist

Etapa

Comando

O que verifica

1

`sudo su deployzdg`

Acesso ao usuário do sistema

2

`pm2 list`

Se o backend está `online`, `errored` ou em loop

3

`df -h` / autoinstalador → Recriar Redis

Disco cheio / Redis fora do ar

4

`node dist/server.js` (foreground)

Erro exato por trás da queda

5

`pm2 stop all && pm2 flush && pm2 start all`

Reinício limpo do backend

---

### Encerramento

Na maioria das vezes, o sistema volta já na Etapa 3 ou 5. Se depois de seguir todas as etapas o backend continuar caindo, abra um chamado de suporte técnico e **anexe o erro copiado na Etapa 4** — com ele, o time consegue diagnosticar direto, sem ida e volta pedindo mais informação.

---

### Possíveis Erros e Soluções

#### `502 Bad Gateway` no navegador + erro de CORS no console

**Causa:** o nginx está no ar mas o backend não responde — o erro de CORS que aparece junto é **consequência**, não a causa. Não aplique correção de CORS aqui: siga as Etapas 2 a 5 deste checklist para tratar o backend caído.

#### Segui todas as etapas e o backend continua caindo

**Causa:** pode ser um erro específico do código, de uma integração ou de uma atualização incompleta. **Solução:** abra um chamado de **Suporte Técnico**, anexando o texto do erro copiado na Etapa 4 e um print do `pm2 list` mostrando o status atual.

[AnteriorBanco de dados - Como acessar](/avancado-recursos-tecnicos/banco-de-dados-como-acessar)[PróximoErro de Autenticação no app Whatsapp Oauth](/avancado-recursos-tecnicos/erro-de-autenticacao-no-app-whatsapp-oauth)

Atualizado há 1 mês

Isto foi útil?