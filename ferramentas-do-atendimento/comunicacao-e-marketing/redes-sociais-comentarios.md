# Redes Sociais - Comentários

{% hint style="warning" %}
**Disponível para o perfil:** Administrador e  usuário
{% endhint %}

As páginas de gestão de comentários permitem centralizar a interação com o público das principais redes sociais (Instagram, Facebook, TikTok e YouTube) diretamente no painel Prismabot. Através desta funcionalidade, o usuário visualiza as publicações e responde aos comentários sem a necessidade de alternar entre diferentes aplicativos ou abas.

#### Principais funções

* **Centralização de Canais:** Gestão de múltiplas redes sociais em uma única interface.
* **Visualização de Mídia:** Exibição da imagem ou vídeo da publicação selecionada para contexto.
* **Interação em Tempo Real:** Leitura e resposta de comentários de forma ágil.

#### Caso de uso

Uma empresa realiza uma campanha de lançamento no **Instagram** e no **YouTube**. O gestor de mídias sociais utiliza o Prismabot para monitorar as dúvidas dos clientes nos comentários de ambas as redes. Ao identificar uma pergunta sobre preço no Instagram, ele clica em "Responder" e envia a informação instantaneamente, garantindo um tempo de resposta reduzido e maior engajamento.

#### Como acessar a página

No menu lateral, clique no Menu **Comunicação e Marketing** e selecione a aba correspondente à rede social desejada: **Instagram**, **Facebook**, **TikTok** ou **YouTube**.

<figure><img src="/files/E84CFzzeVg7LbAdydDrL" alt="" width="267"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

*(O layout e funcionamento são idênticos para todas as redes sociais citadas)*

<figure><img src="/files/HhUJ1evRlcRZK7i3ebEa" alt=""><figcaption></figcaption></figure>

**Explicação dos campos e ícones**

* **Conexão:** Menu suspenso para selecionar a conta da rede social que está Conectada ao sistema.&#x20;

{% hint style="warning" %}
O canal precisa estar criado em [CANAIS](/configuracao-administrador/administracao-painel-admin/canais-de-comunicacao.md)
{% endhint %}

* **Botão Carregar publicações:** Realiza a busca das postagens mais recentes da conta selecionada.
* **Publicação:** Lista as postagens encontradas para que o usuário escolha qual deseja monitorar.
* **Buscar por ID da publicação:** Campo para inserir manualmente o código identificador de uma postagem específica.
* **Botão Buscar comentários:** Carrega todos os comentários vinculados à publicação selecionada.
* **Card de Visualização (Esquerda):** Exibe a mídia da postagem (imagem/vídeo) e fornece um ícone de **Link Externo** para abrir a publicação original na rede social.
* **Lista de Comentários (Direita):** Exibe o nome do usuário (@), a data/hora do comentário e o texto enviado.
* **Link Responder:** Abre o modal para digitar e enviar uma resposta ao comentário selecionado.

<figure><img src="/files/W8Js1rRZ75SKmiOEgFST" alt=""><figcaption></figcaption></figure>

***

#### Passo a passo de uso

1. **Selecionar a conta:** Escolha a conta desejada no campo **Conexão**.
2. **Localizar a postagem:** Clique em **Carregar publicações** e selecione a postagem no campo **Publicação**. Caso tenha o ID em mãos, utilize o campo de busca por ID.
3. **Carregar interações:** Clique em **Buscar comentários**. A lista de interações aparecerá no lado direito da tela.
4. **Responder ao público:** Clique em **Responder** no comentário desejado. Um modal será aberto com o campo de texto.
5. **Enviar resposta:** Digite sua mensagem e clique no botão **Responder**. A resposta será publicada automaticamente na rede social original.

<figure><img src="/files/AA8hBa6iIZSBKj0eaaVO" alt="" width="375"><figcaption></figcaption></figure>

#### Detalhamento

A integração permite responder apenas a comentários de nível primário. O sistema exibe o histórico de data e hora para auxiliar na priorização das respostas mais antigas.

#### Avisos e precauções

{% hint style="warning" %}
**Permissões de API:** Certifique-se de que sua conta de rede social possui as permissões de "Gerenciamento de Comentários" ativas nas configurações de desenvolvedor da plataforma (Meta, TikTok ou Google).
{% endhint %}

{% hint style="info" %}
Pode haver um pequeno delay (atraso) entre a publicação do comentário na rede social e a sua aparição no painel Prismabot, dependendo do tempo de resposta da API de cada plataforma.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/comunicacao-e-marketing/redes-sociais-comentarios.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
