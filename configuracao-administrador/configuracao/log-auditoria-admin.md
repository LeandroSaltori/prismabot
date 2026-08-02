# Log auditoria (admin)

{% hint style="warning" %}
**Disponível para o perfil:** Administrador
{% endhint %}

A página de **Log de Auditoria** é a central de transparência e segurança do sistema Prismabot. Nela, o administrador pode rastrear detalhadamente cada interação realizada na plataforma, identificando quem executou cada ação, em qual momento, de qual local e qual recurso foi afetado.

#### Principais funções

* **Rastreabilidade Total:** Monitoramento de criações, edições e exclusões de dados.
* **Segurança e Conformidade:** Registro de endereços IP e histórico de acessos dos usuários.
* **Filtragem Avançada:** Localização de eventos específicos por usuário, período ou tipo de entidade.
* **Inspeção Técnica:** Visualização do corpo técnico das requisições realizadas ao sistema.
* **Exportação de Dados:** Geração de arquivos para auditorias externas.

#### Caso de uso

Se um Ticket importante for encerrado indevidamente, o administrador pode acessar o Log de Auditoria, filtrar pela entidade "tickets" e pelo método "PUT" (atualização). O log revelará exatamente qual Usuário realizou a alteração, o horário exato e o endereço IP utilizado, permitindo a correção do processo interno.

#### Como acessar a página

No menu lateral, clique no Menu **Configuração** e selecione a aba **Log de Auditoria**.

<figure><img src="/files/pjrTaT9jlmKp8QNOHOBC" alt="" width="277"><figcaption></figcaption></figure>

#### Você verá a seguinte tela:

<figure><img src="/files/EDXOGOaOphaROjrx0RHm" alt=""><figcaption></figcaption></figure>

**Explicação dos campos e ícones**

* **Filtros Superiores:**
  * **Ação:** Filtra pelo tipo de operação (ex: Todas as ações, Criar, Atualizar, Deletar).
  * **Entidade:** Permite buscar por um recurso específico (ex: tickets, users, Canais).
  * **Usuário:** Filtra as ações realizadas por um colaborador específico.
  * **Data Inicial/Final:** Define o intervalo de tempo da consulta.
  * **Botão Filtrar:** Aplica os filtros selecionados à lista.
  * **Ícone de Download:** Exporta os logs filtrados para um arquivo CSV.
* **Colunas da Tabela:**
  * **Ação (Badge):** Descrição amigável da operação (ex: Atualizar, Criar).
  * **Método:** Indica o método técnico HTTP (ex: POST para criar, PUT para atualizar, DELETE para excluir).
  * **Caminho:** Exibe a rota do sistema onde a ação ocorreu.
  * **Status:** Código de resposta do sistema (ex: 200 indica sucesso).
  * **IP:** Endereço de rede do dispositivo que realizou a ação.
  * **Ícone Ver Detalhes (Olho):** Abre um modal com os dados técnicos completos (Payload) da requisição.

***

#### Consultando e Interpretando os Logs

**Como realizar uma consulta**

Para buscar um evento, utilize os filtros de **Usuário** ou **Entidade**. Caso esteja procurando por uma alteração em um contato específico, digite o nome do recurso no campo **Entidade** e defina o **Período** desejado. Clique em **Filtrar** para atualizar a listagem.

**Como interpretar os registros**

* **Ações CREATE (POST):** Indicam que novos dados foram inseridos no sistema.
* **Ações UPDATE (PUT):** Indicam modificações em cadastros ou configurações existentes.
* **Ações DELETE (DELETE):** Indicam que uma informação foi removida permanentemente.
* **Identificação de Suspeitas:** Verifique regularmente se o **IP** registrado condiz com a localização habitual do colaborador e se o **Status** apresenta muitos erros (códigos diferentes de 200).

**Como exportar logs para arquivamento**

Para manter a conformidade e possuir cópias de segurança fora do sistema:

1. Aplique os filtros necessários para o período desejado (ex: último mês).
2. Clique no ícone de **Download** (Exportar CSV) ao lado do botão de filtro.
3. O arquivo será gerado com todo o histórico filtrado para análise em planilhas externas.

***

#### Detalhamento: Visualização de Dados (Ícone do Olho)

Ao clicar no ícone de visualização, o administrador tem acesso ao "corpo" da ação. Isso é útil para verificar exatamente qual informação foi alterada (por exemplo, qual era o valor antigo e qual passou a ser o novo valor de um campo).

<figure><img src="/files/SQ6qIvcfhxlD8QTAF9ga" alt="" width="375"><figcaption></figcaption></figure>

#### Avisos e precauções

{% hint style="warning" %}
**Uso Administrativo:** Esta página contém informações sensíveis de navegação e operação. O acesso deve ser restrito apenas a perfis de alta confiança na organização.
{% endhint %}

{% hint style="info" %}
Os logs de auditoria são gerados automaticamente e não podem ser editados ou excluídos, garantindo a integridade da informação para fins de fiscalização.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://prismatelecomservicos.com/configuracao-administrador/configuracao/log-auditoria-admin.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
