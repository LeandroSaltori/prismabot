# Envio em Massa

{% hint style="warning" %}
**Disponível para o perfil: Administrador, Supervisor e Usuário**
{% endhint %}

A página de **Envio em Massa** é a ferramenta do sistema Prismabot projetada para disparos imediatos de mensagens para grandes listas de contatos. Diferente do módulo de [Campanhas](https://www.google.com/url?sa=E\&q=link-para-campanhas), que é focado em agendamentos programados e calendários, o **Envio em Massa** executa o processamento da fila assim que o comando é disparado, sendo ideal para comunicados urgentes, alertas e notificações rápidas via WhatsApp (Oficial e Não Oficial), Voz (WaVoIP) e SMS.

### Qual aba usar?

| Aba               | Quando usar                                                                            |
| ----------------- | -------------------------------------------------------------------------------------- |
| Template          | Disparo de templates WABA aprovados pela Meta para uma lista de contatos               |
| Template Variável | Mesmo que Template, mas com variáveis dinâmicas individuais por contato via CSV        |
| Texto             | Mensagem de texto livre via conexão não oficial (QR Code), sem necessidade de template |
| Texto Variável    | Texto livre com variáveis dinâmicas por contato via CSV, via conexão não oficial       |
| WaVoIP            | Chamadas de voz em massa via WhatsApp com envio de arquivo de áudio                    |
| SMS               | Disparo de SMS em massa via provedores configurados no sistema                         |
| Relatório         | Histórico e acompanhamento de todos os disparos realizados                             |

{% hint style="info" %}
**API Oficial (WABA) ou não oficial?** As abas **Template** e **Template Variável** exigem conexão via API Oficial. As abas **Texto**, **Texto Variável** e **WaVoIP** utilizam conexões não oficiais (QR Code). O SMS usa provedores independentes.
{% endhint %}

***

#### Como acessar a página

1. No menu lateral, clique em Comunicação e Marketing;
2. Selecione a aba Envio em Massa.

<figure><img src="/files/FY9aiVcfgD13jUiDxU2a" alt="" width="276"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/rmv2GdsfdRiZ5IJE4iEj" alt=""><figcaption></figcaption></figure>

## Conceitos Fundamentais de Configuração

Antes de realizar os disparos, entenda as regras de funcionamento globais deste módulo:

**1. Intervalo Fixo vs. Aleatório (Delay)**

Para proteger a saúde do seu número (especialmente em APIs não oficiais), o sistema permite configurar o tempo de espera entre as mensagens:

* **Min (s) e Max (s):** Ao definir um valor mínimo e máximo (ex: 15 e 45 segundos), o Prismabot escolherá um tempo aleatório dentro dessa faixa para cada mensagem enviada. Isso evita padrões robóticos que facilitam o banimento.

**2. Formatação de Listas (CSV)**

Para envios que utilizam planilhas, o arquivo deve seguir o padrão: número,variável1,variável2...

* **Exemplo:** 5511999999999,Ricardo,Vencimento Amanhã
* **Regra:** Não utilize espaços, parênteses ou traços nos números. O código do país (55 para Brasil) é obrigatório.

**3. Gestão de Tickets no Envio**

* **Fechar ticket:** Se ativado, o sistema enviará a mensagem e encerrará o ticket do cliente imediatamente.
* **Atribuir fila/usuário:** Define para onde o ticket deve ir caso o cliente responda ao disparo em massa.

### Tutorial envio em massa

{% embed url="<https://www.loom.com/share/77639de581024127bf94f8ad4d118fee>" %}

#### Passo a passo de uso

**1. Disparo via API Oficial (WABA)**

Este método é o mais seguro e requer um Template HSM aprovado.

1. Na aba de API Oficial, defina o Tempo de Disparo.
2. Suba sua lista de números ou cole-os manualmente (Formato: `55DD9XXXXXXXX`).
3. Escolha o Template aprovado na lista suspensa.
4. Clique em Enviar.

{% hint style="info" %}
Dica de Importação: Use um arquivo CSV com apenas uma coluna contendo os números. O sistema processará a lista automaticamente.
{% endhint %}

{% hint style="warning" %}
Templates: Na API Oficial, se o seu template tiver variáveis (ex: `Olá, {{1}}`), certifique-se de que sua lista de importação está preparada para preencher esses campos.
{% endhint %}

**2. Disparo via APIs Não Oficiais (QR Code)**

Utilizado para envios mais flexíveis, sem necessidade de templates.

1. Selecione a Conexão (WhatsApp conectado via QR Code) que realizará o disparo.
2. Escolha o destino: Manual, Contatos, Grupos, Etiqueta ou Kanban.
3. Se for Grupos, insira os IDs dos grupos (obtidos no menu Gestão de Grupos).
4. Digite sua mensagem e, se desejar, anexe uma Mídia.
5. Clique em Enviar.

***

#### Detalhamento: Como obter IDs de Grupos

Para disparar em massa para grupos, você deve primeiro capturar os IDs:

1. Vá em Grupos > Gestão de Grupos em Massa.
2. Selecione a conexão de WhatsApp e clique em Listar ID dos Grupos.
3. Copie os IDs ou exporte a planilha para usar no disparador.

***

#### Avisos e precauções

{% hint style="danger" %}
Risco de Banimento (API Não Oficial): Ao usar conexões não oficiais, evite tempos de disparo muito curtos (como 0 a 1 segundo) para listas grandes. Isso pode sinalizar comportamento de bot ao WhatsApp e resultar no banimento do chip.
{% endhint %}

{% hint style="info" %}
Sempre utilize o formato internacional: `DDI + DDD + Número` (Ex: `5511999999999`).
{% endhint %}

### Tutorial envio em massa para grupos

{% embed url="<https://www.loom.com/share/f3e8380bb17742a4b9a5896998fcd6e0>" %}

#### Passo a passo de uso

**Passo 1: Extrair os IDs dos Grupos**

1. No menu Gestão de Grupos, selecione a Conexão desejada.
2. Clique no botão "Listar ID dos Grupos".
3. Com a lista exibida, você pode copiar os IDs manualmente ou clicar em "Exportar CSV".

{% hint style="info" %}
Para o disparo, o sistema aceita apenas os IDs. Se copiar manualmente, remova os nomes dos grupos. Se usar o CSV, exclua a coluna de nomes e mantenha apenas a coluna dos IDs.
{% endhint %}

**Passo 2: Configurar o Disparo**

1. Navegue até o menu Comunicação e Marketing > Disparo em Massa.
2. Selecione novamente a Conexão de WhatsApp que fará o envio.
3. Defina o Tempo de Disparo (Ex: entre 1 e 5 segundos).

**Passo 3: Inserir Destinatários e Mensagem**

1. Cole os IDs dos grupos no campo de contatos ou faça o upload do arquivo CSV formatado apenas com os IDs.
2. Digite o texto da sua campanha no campo de mensagem.
3. Clique em Enviar.

**Passo 4: Conferir o Envio**

Para validar se as mensagens foram entregues:

1. Vá até a tela de Atendimentos.
2. Clique na aba Grupos.
3. Verifique as mensagens enviadas (elas aparecerão inicialmente como pendentes e depois serão entregues aos grupos selecionados).

***

#### Avisos e precauções

{% hint style="warning" %}
Formatação de IDs: O disparador não reconhece nomes de grupos. Certifique-se de que o campo de destinatários contém apenas os códigos técnicos (IDs) separados por vírgula.

Intervalo de Segurança: Ao disparar para muitos grupos, utilize tempos de intervalo maiores (acima de 3 segundos) para garantir a estabilidade da conexão do WhatsApp.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/comunicacao-e-marketing/envio-em-massa.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
