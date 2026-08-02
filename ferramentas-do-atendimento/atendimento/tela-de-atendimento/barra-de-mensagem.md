# Barra de Mensagem

A **Barra de Mensagem** é a ferramenta central de interação na tela de atendimento do Prismabot. Localizada no rodapé da conversa, ela reúne recursos que vão desde o envio de textos simples até automações avançadas com Inteligência Artificial e elementos interativos exclusivos para canais oficiais.

#### Como acessar a funcionalidade

A barra de mensagem está permanentemente disponível na parte inferior de qualquer ticket aberto na aba Atendimentos.

<figure><img src="/files/suPrL6eV7OZi3ZsB2DcW" alt=""><figcaption></figcaption></figure>

***

#### Explicação dos Campos e Ícones

Abaixo, detalhamos cada recurso e como utilizá-lo. Note que a disponibilidade de alguns ícones varia conforme o tipo de conexão utilizada.

**1. Avisos de Canal e Janela (WABA)**

Localizados logo acima da barra de escrita, esses alertas informam sobre as regras da Meta para a API Oficial:

* **Faixa Azul:** Lembrete para utilizar Templates caso queira iniciar uma conversa fora da janela de 24h.
* **Faixa Verde:** Indica que a janela de conversação está aberta e exibe o tempo restante para resposta livre.

<figure><img src="/files/c1rPGF3tZNLOWtyoUmxG" alt=""><figcaption></figcaption></figure>

**2. Emoji (Ícone Sorriso)**

Abre o seletor de emojis padrão

<figure><img src="/files/HCV3zM7C54RTvBJGeUvP" alt="" width="356"><figcaption></figcaption></figure>

**3. Anexo (Ícone Clipe)**

Permite o envio de diversos formatos de arquivos.

* **Opções:** Imagem, Vídeo, Documento, Múltiplos arquivos, Localização, Contato (vCard) e Figurinhas.
* **Como usar:** Clique no ícone, escolha o tipo de mídia e selecione o arquivo em seu dispositivo.
*

```
<figure><img src="/files/XA1I8w6S5pVqHJRG3zGM" alt="" width="154"><figcaption></figcaption></figure>
```

**4. Mensagens Rápidas (Ícone Balão)**

Acesso aos templates de texto pré-configurados para agilizar o suporte.

* **Como usar:** Clique no ícone para abrir a lista ou digite `/` diretamente no campo de texto seguido do atalho.
* **Configuração:** Você pode criar novos atalhos na página de Mensagens Rápidas.

<figure><img src="/files/6YbCzDXOd0b5l5IiB0Xy" alt="" width="375"><figcaption></figcaption></figure>

**5. Opções Extras (Três Pontinhos)**

<figure><img src="/files/oqMhxW7njEHsjAm7VFey" alt="" width="164"><figcaption></figcaption></figure>

Este menu agrupa ferramentas avançadas. Os recursos são divididos entre universais e exclusivos:

**Recursos Universais (Disponíveis em todas as conexões):**

* **Multi-encaminhar:** Seleciona mensagens para enviar a outros contatos.
* **Criar nota:** Abre um modal para adicionar uma anotação interna no ticket.

<figure><img src="/files/QoXJDLBuGNq9xHUdmO2q" alt="" width="332"><figcaption></figcaption></figure>

* **Reescrever com IA:** Abre opções para alterar o estilo do texto (Profissional, Simpático, Marketing ou Ortografia).

<figure><img src="/files/jjdBDaPjoJUOVhb2Qcw6" alt="" width="153"><figcaption></figcaption></figure>

* **Resumir conversa com IA:** Gera um apanhado dos pontos principais do chat.

<figure><img src="/files/ujF7S8TViTgODWQZk4bU" alt="" width="332"><figcaption></figcaption></figure>

* **Copiloto:** Interface de IA que analisa o sentimento do cliente e sugere respostas prontas.

<figure><img src="/files/YYPkbUPQMqY11SoDLi42" alt="" width="375"><figcaption></figcaption></figure>

**Recursos Exclusivos (Apenas para API Oficial WABA):**

* **WABA:** Envio de Templates, Botões, Listas, CTA (Links) e Solicitação de Localização.
*

```
<figure><img src="/files/zbJfPwWQ523kFLU7mq4U" alt="" width="328"><figcaption></figcaption></figure>
```

* **Catálogo:** Envio de Produto Único, Multi-Produto ou o Catálogo completo do Facebook.

**6. Assinatura (Chave Assinado)**

Define se o nome do atendente será enviado acima da mensagem.

* **Como usar:** Ative a chave azul para que a mensagem saia como: *"Atendente \[Nome]: Sua mensagem aqui"*.

<figure><img src="/files/h1TpDADMJjxXOlN18rtb" alt=""><figcaption></figcaption></figure>

**7. Escrita e Áudio**

* **Campo de Texto:** Local onde a mensagem é redigida. Suporta atalhos de teclado.
* **Microfone:** Permite gravar mensagens de voz.
* **Como usar:** Clique no microfone para iniciar a gravação.

***

#### Avisos e precauções

{% hint style="warning" %}
**Variação por API:** As funções de envio de **Botões**, **Listas** e **Catálogo** via chat direto funcionam exclusivamente para conexões via **API Oficial (WABA)**. Em conexões não oficiais (QR Code), esses recursos podem não aparecer ou não ser entregues corretamente.
{% endhint %}

{% hint style="info" %}
A **Reescrita com IA** exige que haja algum texto digitado no campo antes de ser acionada para que o sistema tenha uma base de processamento.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/atendimento/tela-de-atendimento/barra-de-mensagem.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
