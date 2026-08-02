Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Referência da API](/central-do-assinante/referencia-da-api)

# ✅ To Do List

### TodoCreate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/todo/create

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

namestringOpcional

descriptionstringOpcional

ownerstringOpcional

ownerIdstringOpcional

statusstringOpcional

prioritystringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/todo/create

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### TodoDelete

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/todo/delete/{id}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

idstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/todo/delete/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### TodoList

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/todo/list

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

get/v2/api/external/{ApiID}/todo/list

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### TodoLogs

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/todo/logs/{userId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

userIdstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/todo/logs/{userId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### TodoUpdate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/todo/update/{id}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

idstringObrigatório

Corpo

application/json

application/json

statusstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/todo/update/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

[Anterior🎫 Tickets Extras](/central-do-assinante/referencia-da-api/tickets-extras)[Próximo👥 Usuários](/central-do-assinante/referencia-da-api/usuarios)

Atualizado há 8 dias

Isto foi útil?