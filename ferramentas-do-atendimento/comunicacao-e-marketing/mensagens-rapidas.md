# Mensagens Rápidas

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

Mensagens Rápidas são atalhos de texto, arquivo ou áudio que os atendentes podem acionar diretamente no chat durante um atendimento. Evitam retrabalho em respostas frequentes e garantem padronização na comunicação da equipe.

{% hint style="info" %}
Para aprender a usar mensagens rápidas durante o atendimento, acesse [Barra de Mensagem](https://prismatelecomservicos.com/ferramentas-do-atendimento/atendimento/tela-de-atendimento/barra-de-mensagem).
{% endhint %}

### Como acessar

Acesse **Comunicação e Marketing → Mensagens Rápidas**.

<figure><img src="/files/ZH1YO9sN4KBRC9MLBu7K" alt="" width="225"><figcaption></figcaption></figure>

### Você verá a seguinte tela

A listagem exibe todas as mensagens cadastradas com as colunas: **Atalho**, **Mensagem**, **Tipo**, **Anexo**, **Voz**, **Visibilidade** e **User ID**.

<figure><img src="/files/EsQCjACQd5U31HYDUAgI" alt=""><figcaption></figcaption></figure>

### Criando uma mensagem rápida

Clique em **+ Nova Mensagem** para abrir o formulário de criação.

Preencha os campos comuns a todos os tipos:

| Campo                | Descrição                                                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Atalho**           | Palavra-chave precedida de `/` para localizar a mensagem no chat (ex: `/saudacao`)                                                                  |
| **Mensagem**         | Texto que será enviado ao acionar o atalho. Use o menu **Variáveis** para inserir dados dinâmicos como `{{name}}`, `{{greeting}}` ou `{{protocol}}` |
| **Anexo**            | Adicione até 5 arquivos ou grave um áudio diretamente pelo sistema                                                                                  |
| **Mensagem de Voz**  | Ative para que o atalho envie o áudio anexado como mensagem de voz                                                                                  |
| **Mensagem pública** | Ative para tornar a mensagem visível para todos os usuários — desativado, fica visível apenas para você                                             |

Em seguida, escolha o **Tipo de mensagem** conforme o canal e o formato desejado:

***

#### Texto

Use para mensagens simples de texto, com ou sem anexo. Compatível com todos os canais.

Não há campos adicionais — basta escrever a mensagem no campo **Mensagem** e salvar.

<figure><img src="/files/2zVenPNMWP6SqrRgLrCN" alt="" width="375"><figcaption></figcaption></figure>

***

#### Botões

Use para enviar uma mensagem com opções clicáveis de resposta rápida. Disponível para conexões **Baileys, UAZAPI e WABA**.

| Campo                  | Descrição                                                           |
| ---------------------- | ------------------------------------------------------------------- |
| **Título (cabeçalho)** | Texto exibido acima da mensagem — opcional                          |
| **Rodapé**             | Texto exibido abaixo da mensagem — opcional                         |
| **Botão 1, 2...**      | Texto de cada botão de resposta (máximo de 20 caracteres por botão) |

Clique em **+ Adicionar botão** para incluir mais opções de resposta.

{% hint style="info" %}
Use Botões quando quiser guiar o contato para escolhas simples, como "Sim / Não" ou "Falar com atendente / Ver preços".
{% endhint %}

<figure><img src="/files/Z6ozd1NI5DzYCSPFLs2j" alt="" width="375"><figcaption></figcaption></figure>

***

#### Lista

Use para enviar um menu com seções e itens organizados que o contato pode selecionar. Disponível para conexões **Baileys, UAZAPI e WABA**.

| Campo              | Descrição                                                             |
| ------------------ | --------------------------------------------------------------------- |
| **Cabeçalho**      | Título da lista — opcional                                            |
| **Texto do botão** | Texto do botão que abre a lista (ex: "Ver opções") — obrigatório      |
| **Rodapé**         | Texto complementar abaixo da lista — opcional                         |
| **Seção**          | Agrupamento de itens dentro da lista (ex: "Departamentos")            |
| **Item**           | Opção dentro de uma seção — cada item tem título e descrição opcional |

Clique em **+ Adicionar item** para incluir mais opções dentro de uma seção e em **+ Adicionar seção** para criar novos grupos de opções.

{% hint style="info" %}
Use Listas quando tiver muitas opções para oferecer ao contato — é mais organizado do que vários botões. Ideal para menus de departamentos, produtos ou serviços.
{% endhint %}

<figure><img src="/files/iFfWBhq3S79F6snZrvh3" alt="" width="375"><figcaption></figcaption></figure>

***

#### Template WABA

Use para acionar um template aprovado pela Meta diretamente como mensagem rápida. Disponível **apenas para canais WABA**.

| Campo                | Descrição                                                         |
| -------------------- | ----------------------------------------------------------------- |
| **Nome do template** | Nome exato do template cadastrado na Meta (ex: `welcome_message`) |
| **Idioma**           | Código do idioma do template (ex: `pt_BR`)                        |

{% hint style="warning" %}
O template precisa estar aprovado pela Meta antes de ser usado. O nome e o idioma devem corresponder exatamente ao cadastrado no Gerenciador de Negócios da Meta.
{% endhint %}

<figure><img src="/files/SqXdnKVB32FKiU3xAi8i" alt="" width="375"><figcaption></figcaption></figure>

***

### Gerenciando mensagens existentes

* Use a **barra de busca** para localizar uma mensagem pelo atalho ou conteúdo
* Clique no ícone de **lápis** para editar uma mensagem
* Clique no ícone de **lixeira** para excluir
* Clique em **Atualizar** para recarregar a listagem

### Boas práticas

* Use atalhos curtos e intuitivos para que toda a equipe memorize com facilidade (ex: `/oi`, `/preco`, `/horario`)
* Mensagens públicas ficam disponíveis para todo o time de atendimento — crie as respostas padrão da empresa como públicas
* Use variáveis como `{{name}}` e `{{greeting}}` para personalizar mensagens sem precisar editar o texto a cada envio

{% hint style="info" %}
Veja todas as variáveis disponíveis em Configurações → CRM → Variáveis.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/comunicacao-e-marketing/mensagens-rapidas.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
