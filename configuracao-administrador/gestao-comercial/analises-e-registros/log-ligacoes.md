# Log Ligações

{% hint style="warning" %}
**Disponível para o perfil:** Administrador e Supervisor
{% endhint %}

A página de **Log de Ligações** é o registro histórico de toda a atividade de voz realizada através das integrações de telefonia do sistema Prismabot (como o WaVoIP). Nela, o gestor pode auditar chamadas recebidas e efetuadas, monitorar a duração dos contatos e avaliar a produtividade da equipe de atendimento por voz.

#### Principais funções

* **Auditoria de Chamadas:** Registro detalhado de números de origem e destino.
* **Controle de Produtividade:** Visualização do tempo de duração de cada ligação.
* **Rastreabilidade por Agente:** Identificação de qual Usuário realizou ou atendeu a chamada.
* **Exportação Gerencial:** Geração de relatórios em formato CSV para análises externas.

#### Caso de uso

Um supervisor de atendimento precisa verificar o volume de chamadas não atendidas no dia anterior. Ele acessa a página de **Log de Ligações**, filtra o status por "Falhou" ou "Perdida" e identifica quais números de clientes não foram contatados. Com essas informações, ele delega à equipe uma lista de retorno prioritária, garantindo que nenhum lead ou cliente fique sem retorno.

#### Como acessar a página

No menu lateral esquerdo, clique no Menu **Gestão Comercial** e selecione a aba **Log Ligações**.

<figure><img src="/files/CGsXULnIVvOcLQO4yFJJ" alt="" width="249"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/jgO5yXih3aLQXcEodh6H" alt=""><figcaption></figcaption></figure>

**Explicação dos campos e ícones**

* **Painel de Filtros:**
  * **Data Início / Data Fim:** Delimita o período do histórico.
  * **Status:** Filtra chamadas por estado (ex: Encerrada, Chamando, Falhou).
  * **Agente:** Filtra as ligações vinculadas a um Usuário específico.
  * **Número Origem / Destino:** Localiza chamadas envolvendo um telefone específico.
* **Colunas da Tabela:**
  * **ID:** Identificador numérico da ligação no sistema.
  * **Usuário:** Nome do atendente responsável.
  * **Origem:** Número que iniciou a chamada.
  * **Destino:** Número que recebeu a chamada.
  * **Status (Badge):** Situação final da ligação (ex: Encerrada, em laranja para Chamando).
  * **Duração:** Tempo total de conversação.
  * **Data:** Dia e horário exato do registro.
* **Botão Exportar CSV:** Baixa a lista filtrada para uma planilha Excel.
* **Ícone Lixeira (Ações):** Permite excluir um registro individual de log.

***

#### Passo a passo de uso

**Consultar o Histórico**

1. Defina o intervalo de datas nos campos **Data Início** e **Data Fim**.
2. Se desejar analisar um colaborador específico, selecione o nome dele no campo **Agente**.
3. Clique no botão **Buscar**. A tabela será atualizada com os registros correspondentes.

**Exportar Dados para Relatórios**

1. Aplique os filtros desejados para segmentar os dados que você precisa.
2. Clique no botão **Exportar CSV** localizado no canto superior direito.
3. O arquivo será gerado automaticamente com todas as colunas da tabela para análise externa.

***


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/gestao-comercial/analises-e-registros/log-ligacoes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
