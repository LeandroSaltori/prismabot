# Detalhes do contato

O painel de **Detalhes do Contato** é o núcleo de CRM (Gestão de Relacionamento com o Cliente) dentro da tela de atendimento do Prismabot. Localizado na lateral direita, ele fornece ao atendente uma visão 360º do cliente, permitindo desde a edição de dados básicos até o acionamento de integrações complexas de IA, gestão de vendas e ferramentas de utilidade técnica.

#### Como acessar a página

Caminho clicando no Menu **Atendimento**, na aba **Atendimentos**, selecione um ticket e clique no ícone **"i" (Informações)** no canto superior direito da conversa.

***

#### Você verá a seguinte tela:

O painel é organizado em cinco abas estratégicas: **Perfil, Atend., Gestão, Integr. e Util.**

<figure><img src="/files/vleej9PxlQ84rTGls3mH" alt="" width="355"><figcaption></figcaption></figure>

***

#### Explicação dos campos por aba

**1. Aba Perfil**

Focada na identificação e segmentação do cliente.

* **Dados Básicos:** Foto, Nome, Telefone e Data de Aniversário.
* [**Botão Editar Contato**](/ferramentas-do-atendimento/atendimento/contatos.md)**:** Permite alterar as informações cadastrais.
* **Menu Telefonia:** Atalhos para realizar chamadas via [WaVoIP](/configuracao-administrador/gestao-comercial/analises-e-registros/wavoip.md), enviar SMS, usar VAPI ou consultar logs de voz.

<figure><img src="/files/DJKRkQBaRDH5nEiSYSRS" alt="" width="148"><figcaption></figcaption></figure>

* [**Etiquetas**](/configuracao-administrador/gestao-comercial/operacao-gestao-comercial/etiquetas.md) **e Carteiras:** Local para adicionar tags de identificação e definir qual atendente ou equipe é "dono" do contato.
* **Comunicação e Favoritos:** Opções para marcar mensagens como lidas/não lidas e acessar mensagens favoritadas.

**2. Aba Atend. (Atendimento)**

Ferramentas de suporte e histórico imediato.

* [**Protocolo:** ](/configuracao-administrador/gestao-comercial/analises-e-registros/protocolos.md)Gera e envia o número de protocolo ao cliente.
* [**Avaliação**](/configuracao-administrador/gestao-comercial/analises-e-registros/avaliacoes.md)**:** Dispara a pesquisa de satisfação manualmente.
* **Análise de Sentimento:** Ferramenta de IA que identifica se o interlocutor está Neutro, Positivo ou Negativo.
* [**Notas Internas**](/configuracao-administrador/gestao-comercial/operacao-gestao-comercial/notas.md)**:** Campo de texto para anotações que apenas a equipe interna visualiza.

<figure><img src="/files/tG5nW9hg3CpEujnrjNjk" alt="" width="353"><figcaption></figcaption></figure>

**3. Aba Gestão**

Controle do fluxo comercial e do ciclo de vida do ticket.

* **Ações do Ticket:** Atalhos para Resolver, Retornar à fila, Pausar ou Transferir (atendente, canal ou chatbot).
* [**Funil**](/ferramentas-do-atendimento/gestao/funil-de-vendas.md) **e** [**Kanban:**](/ferramentas-do-atendimento/gestao/kanban-de-atendimento.md) Define em qual estágio do processo de vendas ou atendimento o cliente se encontra.
* **Valor Negociado:** Campo para registro financeiro da oportunidade.
* **Bloqueios:** Chaves para bloquear o contato ou impedir que o chatbot responda a este número.

<figure><img src="/files/vUOrE0xmSjPiIuUgSEFV" alt="" width="353"><figcaption></figcaption></figure>

**4. Aba Integr. (Integrações)**

Permite ligar ou desligar provedores de IA e automações externas para este atendimento específico.

* **Toggles:** Ativa/Desativa DialogFlow, ChatGPT, N8N, Dify, Grok, Gemini, Claude, Deepseek, entre outros.
* *Nota:* Apenas as integrações previamente configuradas no Menu Configurações aparecerão aqui.

<figure><img src="/files/gQtXghoDVJdOtbTPPR2b" alt="" width="353"><figcaption></figcaption></figure>

**5. Aba Util. (Utilidades)**

Ferramentas de manutenção e conformidade de dados.

* **Extrair conversa:** Gera um arquivo PDF completo com o histórico de mensagens e dados do ticket.
* **Atualizar LID:** Sincroniza o identificador técnico do contato.
* **Sanitizar contato:** Remove dados sensíveis (número, e-mail, CPF) do registro para fins de LGPD.

<figure><img src="/files/mYklO7H2zsRlfFGG2GDT" alt="" width="353"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/ferramentas-do-atendimento/atendimento/tela-de-atendimento/detalhes-do-contato.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
