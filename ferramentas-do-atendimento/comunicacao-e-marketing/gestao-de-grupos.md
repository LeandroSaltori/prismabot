# Gestão de grupos

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

A página de Grupos centraliza todas as ferramentas de gestão de grupos de WhatsApp: criação em massa, manipulação de configurações, gerenciamento de participantes e automações de entrada e saída.

### Como acessar

Acesse **Comunicação e Marketing → Grupos**.

<figure><img src="/files/qGXBOoJnsl4tFUsq8Thx" alt="" width="226"><figcaption></figcaption></figure>

### Você verá a seguinte tela

<figure><img src="/files/5FegagYpLEUugplNrG4Q" alt=""><figcaption></figcaption></figure>

***

### Massa Grupos

Crie grupos em massa e liste participantes de múltiplos grupos de uma vez.

#### Criando grupos em massa

1. Clique em **+ Criar grupos em massa**

<figure><img src="/files/ttlCCYHaekOts5VQ6iOh" alt="" width="288"><figcaption></figcaption></figure>

2. Selecione a **Conexão** WhatsApp que será administradora dos grupos
3. Preencha os campos do formulário:

| Campo                      | Descrição                                                                          |
| -------------------------- | ---------------------------------------------------------------------------------- |
| **Conexão**                | Canal que realizará a criação — o número correspondente entrará como Administrador |
| **Nome do Grupo**          | Nome base que será atribuído aos grupos criados                                    |
| **Número do Participante** | Primeiro participante adicionado — recomendado que seja um funcionário da empresa  |
| **Quantidade de Grupos**   | Quantidade de grupos a serem criados com essa configuração                         |

4. Opcionalmente, ative **Definir Contato** para selecionar participantes já cadastrados na plataforma
5. Clique em **Salvar** e aguarde a criação automática de todos os grupos

{% hint style="info" %}
Use nomes descritivos nos grupos para facilitar a identificação posterior. Verifique também se a conta tem permissão para criar grupos antes de executar em massa.
{% endhint %}

#### Listando IDs e participantes

1. Selecione a **Conexão** desejada — o campo **Grupos** será desbloqueado automaticamente
2. Escolha o grupo que deseja consultar
3. Use os botões conforme a necessidade:

| Botão                     | O que faz                                                       |
| ------------------------- | --------------------------------------------------------------- |
| **Listar IDs dos Grupos** | Exibe os identificadores técnicos de todos os grupos da conexão |
| **Listar Participantes**  | Lista os números de todos os membros do grupo selecionado       |
| **Exportar para XLS**     | Exporta a listagem atual para uma planilha                      |
| **Limpar**                | Limpa os campos e resultados exibidos                           |

{% hint style="info" %}
Os IDs dos grupos são necessários para usar o disparo em massa para grupos. Consulte Envio em Massa — Texto para mais detalhes.
{% endhint %}

***

### Massa Grupos 2

Modifique título, descrição, imagem e permissões de múltiplos grupos em massa.

<figure><img src="/files/V9vKxOeSP98x80o6DHHE" alt=""><figcaption></figcaption></figure>

#### Modificando grupos

1. Selecione a **Conexão** e o **Grupo** que deseja modificar
2. Ative as opções de modificação desejadas:

| Opção                       | O que modifica                                                |
| --------------------------- | ------------------------------------------------------------- |
| **Alterar Título**          | Abre campo para definir o novo nome do grupo                  |
| **Alterar Descrição**       | Abre campo para definir a nova descrição                      |
| **Alterar Imagem (URL)**    | Abre campo para colar a URL da nova imagem do grupo           |
| **Alterar Imagem (Upload)** | Abre botão para fazer upload de uma imagem do seu dispositivo |
| **Somente Admins**          | Restringe o envio de mensagens apenas a administradores       |

3. Clique em **Alterar** e aguarde a conclusão das alterações

{% hint style="info" %}
Teste a modificação em um grupo antes de aplicar em massa para verificar o resultado. A imagem deve ter dimensões adequadas para melhor visualização nos dispositivos dos participantes.
{% endhint %}

***

### Massa Usuários

Gerencie usuários em grupos em massa: adicione, remova ou promova administradores.

<figure><img src="/files/FDnOrqOZy7dtgetQBKhT" alt=""><figcaption></figcaption></figure>

#### Configurando a ação

1. Selecione a **Conexão** e o **Grupo** alvo da ação
2. Escolha a ação desejada:

| Ação                        | O que faz                                               |
| --------------------------- | ------------------------------------------------------- |
| **Promover a Admin**        | Promove os números informados a Administrador do grupo  |
| **Rebaixar de Admin**       | Remove a função de Administrador dos números informados |
| **Adicionar Participantes** | Adiciona os números informados ao grupo                 |
| **Remover Participantes**   | Remove os números informados do grupo                   |

3. Informe os números manualmente ou importe uma lista via **CSV**
4. Opcionalmente, use **Selecionar Contato** para buscar contatos já cadastrados na plataforma
5. Clique em **Alterar**

{% hint style="warning" %}
Números inválidos ou bloqueados retornam erro — revise a lista antes de executar. Promova apenas usuários de confiança a administrador. Aguarde a conclusão de uma ação antes de executar outra nos mesmos grupos.
{% endhint %}

***

### Ban List

Gerencie a lista de números banidos dos grupos e impeça o reingresso automático.

<figure><img src="/files/czFiwBWImrtiRySI8E9u" alt=""><figcaption></figcaption></figure>

#### Adicionando um número banido

1. Clique em **Adicionar**

<figure><img src="/files/N8Zu3Zc6jCSr99BxS5Hj" alt="" width="331"><figcaption></figcaption></figure>

1. Preencha os campos:

| Campo             | Descrição                                                        |
| ----------------- | ---------------------------------------------------------------- |
| **Número de Ban** | Número a ser banido dos disparos e grupos                        |
| **WhatsApp ID**   | Canal ao qual o banimento será aplicado                          |
| **Grupo**         | Grupo específico do banimento — deixe vazio para aplicar a todos |

3. Clique em **Salvar**

#### Gerenciando a lista

* Use a **barra de busca** para localizar rapidamente um número na lista
* Clique em **Excluir Todos** para limpar a lista completa de banidos

{% hint style="info" %}
Números na Ban List não serão adicionados a grupos nem receberão disparos realizados pela plataforma, evitando denúncias de contatos sem interesse.
{% endhint %}

***

### Word List

Gerencie palavras proibidas — o bot removerá automaticamente mensagens que contenham esses termos nos grupos monitorados.

<figure><img src="/files/WRXkfVuCARv6WHrfeZYN" alt=""><figcaption></figcaption></figure>

#### Adicionando uma palavra proibida

1. Clique em **Adicionar**
2. Preencha os campos:

| Campo                   | Descrição                                                                 |
| ----------------------- | ------------------------------------------------------------------------- |
| **Palavra (minúscula)** | Palavra a ser proibida — cadastre sempre em minúsculo                     |
| **WhatsApp ID**         | Canal ao qual a regra será aplicada                                       |
| **Grupo**               | Grupo específico — deixe vazio para aplicar a todos os grupos monitorados |

3. Clique em **Salvar**

<figure><img src="/files/LCDcGCuf3rTupVURi9oX" alt="" width="347"><figcaption></figcaption></figure>

#### Gerenciando a lista

* Use o **campo de pesquisa** para localizar rapidamente uma palavra
* Clique em **Excluir Todos** para limpar toda a lista de uma vez

***

### Saudação

Configure mensagens de boas-vindas automáticas enviadas quando alguém entra no grupo.

<figure><img src="/files/YCU68eWn0Tub1zApWN2m" alt=""><figcaption></figcaption></figure>

#### Adicionando uma saudação

1. Clique em **Adicionar**
2. Preencha os campos:

| Campo           | Descrição                                                                 |
| --------------- | ------------------------------------------------------------------------- |
| **Saudação**    | Texto da mensagem de boas-vindas                                          |
| **WhatsApp ID** | Canal ao qual a saudação será aplicada                                    |
| **Grupo**       | Grupo específico — deixe vazio para aplicar a todos os grupos monitorados |

3. Clique em **Salvar**

<figure><img src="/files/wSgBA0pva9OdHve8EXJo" alt="" width="347"><figcaption></figcaption></figure>

#### Variáveis disponíveis

Use as variáveis abaixo para personalizar a mensagem com os dados do novo membro:

| Variável   | O que insere          |
| ---------- | --------------------- |
| `{nome}`   | Nome do novo membro   |
| `{numero}` | Número do novo membro |

**Exemplo:** `Olá, {nome}! Seja bem-vindo ao grupo. 👋`

***

### Despedida

Configure mensagens de saída automáticas enviadas quando alguém sai do grupo.

<figure><img src="/files/RA2KwSBuVcC6mmKXDcpX" alt=""><figcaption></figcaption></figure>

#### Adicionando uma despedida

1. Clique em **Adicionar**
2. Preencha os campos:

| Campo           | Descrição                                                                 |
| --------------- | ------------------------------------------------------------------------- |
| **Despedida**   | Texto da mensagem de saída                                                |
| **WhatsApp ID** | Canal ao qual a despedida será aplicada                                   |
| **Grupo**       | Grupo específico — deixe vazio para aplicar a todos os grupos monitorados |

3. Clique em **Salvar**

<figure><img src="/files/kWOwtJJfGRCX0L5YGY4K" alt="" width="335"><figcaption></figcaption></figure>

#### Variáveis disponíveis

| Variável   | O que insere              |
| ---------- | ------------------------- |
| `{nome}`   | Nome do membro que saiu   |
| `{numero}` | Número do membro que saiu |

**Exemplo:** `Até logo, {nome}! Foi um prazer ter você no grupo.`


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/comunicacao-e-marketing/gestao-de-grupos.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
