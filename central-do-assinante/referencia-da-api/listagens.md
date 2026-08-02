# 📊 Listagens

### GetAllSessionApis

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/getAllSessionApis

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/getAllSessionApis

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListChannels

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/listChannels

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/listChannels

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListContacts

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/listContacts

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

pageNumberintegerOpcional

Número da página

Example: `1`

searchParamstringOpcional

Parâmetro de busca (opcional)

walletIdstringOpcional

ID da wallet (opcional)

tagIdstringOpcional

ID da tag (opcional)

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/listContacts

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListOpportunities

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/listOpportunities

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

pageintegerOpcional

Número da página

Example: `1`

limitintegerOpcional

Limite de resultados por página

Example: `40`

statusstringOpcional

Status da oportunidade (opcional)

pipelineIdstringOpcional

ID do pipeline (opcional)

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/listOpportunities

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListQueues

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/listQueues

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/listQueues

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListSessions

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/listSessions

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/listSessions

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListTags

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/listTags

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

isActivebooleanOpcional

Filtrar por tags ativas (true/false)

Example: `true`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/listTags

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListTickets

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/listTickets

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

pageNumberintegerOpcional

Número da página

Example: `1`

statusstringOpcional

Status do ticket (open, pending, closed)

Example: `open`

searchParamstringOpcional

Parâmetro de busca (opcional)

queuesIdsstringOpcional

IDs das filas (opcional)

whatsappIdsstringOpcional

IDs dos canais (opcional)

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/listTickets

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response



Atualizado há 8 dias

Isto foi útil?