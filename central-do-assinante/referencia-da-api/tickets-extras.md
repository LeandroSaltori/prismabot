# 🎫 Tickets Extras

### EndTicketPause

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/ticket/pause/end/{ticketId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

ticketIdstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/ticket/pause/end/{ticketId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListTicketEvaluations

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/listTicketEvaluations

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

pageintegerOpcionalExample: `1`

limitintegerOpcionalExample: `20`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/listTicketEvaluations

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendEvaluation

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendEvaluation

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Corpo

application/json

application/json

ticketIdnumberOpcional

bodystringOpcional

externalKeystringOpcional

forcebooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendEvaluation

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListTicketPauseLogs

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/ticket/pause/logs/{ticketId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

ticketIdstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/ticket/pause/logs/{ticketId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ShowTicketById

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/showTicketById

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Corpo

application/json

application/json

ticketIdstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/showTicketById

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### StartTicketPause

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/ticket/pause/start/{ticketId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

ticketIdstringObrigatório

Corpo

application/json

application/json

pauseReasonstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/ticket/pause/start/{ticketId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### TicketShareCreate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/ticket/share

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Corpo

application/json

application/json

ticketIdstringOpcional

inviteUrlstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/ticket/share

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### TicketShareShow

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/ticket/share/{ticketId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

ticketIdstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/ticket/share/{ticketId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response



Atualizado há 8 dias

Isto foi útil?