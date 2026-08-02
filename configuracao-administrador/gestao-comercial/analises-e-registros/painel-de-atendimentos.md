# Painel de Atendimentos

{% hint style="warning" %}
**Disponível para o perfil: Administrador**
{% endhint %}

O **Painel de Atendimentos** é o centro de comando para administradores do Prismabot. Diferente da tela operacional de chat, este painel oferece uma visão macro e em tempo real de todos os tickets da empresa, permitindo realizar intervenções rápidas e ações em lote para manter a fluidez da operação.

#### Principais funções

* **Monitoramento Global:** Visualização de todos os tickets abertos e pendentes divididos por colunas.
* **Ações em Massa:** Resolução ou transferência de múltiplos atendimentos simultaneamente.
* **Gestão de Contingência:** Reatribuição rápida de tickets entre usuários e filas.
* **Auditoria Visual:** Acesso rápido ao conteúdo das conversas sem necessidade de assumir o ticket.

#### Caso de uso

O administrador percebe que um atendente precisou se ausentar inesperadamente, deixando 15 tickets em aberto. Para não interromper o fluxo, acessa o **Painel de Atendimentos**, utiliza a ferramenta de **Transferir entre Usuários** e move todos os atendimentos daquele colaborador para um colega disponível, garantindo que nenhum cliente fique sem resposta.

#### Como acessar a página

Clique no Menu **Gestão Comercial** e selecione a aba **Painel Atendimentos**.

<figure><img src="/files/0fLA8Qa0rK2YUz6CDiwX" alt="" width="250"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/9E5aKiwwFIsnCaymvmvx" alt="" width="375"><figcaption></figcaption></figure>

***

#### Explicação dos Campos e Ícones

**Barra de Ferramentas Superior**

<figure><img src="/files/We159xz2MF7AnEVd1xxq" alt=""><figcaption></figcaption></figure>

Os ícones localizados no canto superior direito permitem executar ações que afetam toda a visualização ou grupos de tickets:

1. **Ícone Check (Abertos):** Resolve (encerra) todos os tickets com status "Aberto" de uma só vez. \
   ![](/files/TahO8aT044uA43MYnt7W)
2. **Ícone Check (Pendentes):** Resolve (encerra) todos os tickets com status "Pendente" de uma só vez.\
   ![](/files/dxNBuDHB0SZO5wD8hciO)
3. **Ícone Troca entre Usuários:** Abre o modal para transferir tickets de um atendente origem para um atendente destino.

<figure><img src="/files/LkMCiWqKyT3oQxYU3GPR" alt="" width="375"><figcaption></figcaption></figure>

4. **Ícone Troca entre Filas:** Abre o modal para mover tickets de uma fila específica para outra.

<figure><img src="/files/wcrtFkEVRs0INah1bgrK" alt="" width="375"><figcaption></figcaption></figure>

5. **Ícone Troca entre Canais:** Permite migrar atendimentos de uma conexão para outra (ex: mudar do WhatsApp A para o WhatsApp B).

<figure><img src="/files/kCRi2RQppGu4ImiiGAt7" alt="" width="373"><figcaption></figcaption></figure>

6. **Ícone Envelope:** Marca todos os tickets visualizados como lidos.
7. **Botão Filtros:** Permite alternar o **Tipo de Visualização** entre **Por Usuário** (focado em quem atende) ou **Por Fila** (focado nos departamentos).

<figure><img src="/files/K47db9VuaAqycRHYPbjN" alt="" width="329"><figcaption></figcaption></figure>

**Ícones dentro do Card de Chat**

<figure><img src="/files/cXY0zXFSH7Rsj54iEyYE" alt=""><figcaption></figcaption></figure>

Cada ticket individual no painel possui dois controles rápidos:

* **Ícone de Seta (Atender):** Assume o ticket para você, movendo-o para sua central de atendimentos.
* **Ícone de Olho (Espiar):** Abre o histórico da conversa em modo de leitura para supervisão, sem que o cliente saiba e sem assumir a responsabilidade pelo ticket.

***

#### Passo a passo de uso (Ações em Lote)

**1. Transferir entre Usuários**

1. Clique no ícone de transferência entre usuários na barra superior.
2. No modal, selecione o **Usuário origem** (quem está com os tickets agora).
3. Selecione o **Usuário destino** (quem passará a ser o responsável).
4. Confirme em **Transferir**.

**2. Transferir entre Filas e Lógica de Conflitos**

1. Clique no ícone de transferência entre filas.
2. Selecione a **Fila origem** e a **Fila destino**.
3. **Usuário destino (Opcional):** Se você informar um usuário específico aqui, todos os tickets serão atribuídos a ele.
4. **Tratamento de Conflitos:** Se você não informar um usuário destino, o sistema detectará automaticamente se os atendentes atuais possuem acesso à nova fila.

***

#### Avisos e precauções

{% hint style="danger" %}
**Cuidado com as Ações Globais:** As funções de "Resolver tickets abertos/pendentes" são irreversíveis e encerram centenas de conversas simultaneamente. Certifique-se de aplicar os filtros de data corretamente antes de executar.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/gestao-comercial/analises-e-registros/painel-de-atendimentos.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
