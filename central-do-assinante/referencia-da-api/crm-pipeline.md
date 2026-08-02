Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Referência da API](/central-do-assinante/referencia-da-api)

# 🏗️ CRM Pipeline

### PipelineCreate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/pipeline/create

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

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/pipeline/create

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### PipelineDelete

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/pipeline/delete/{id}

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

post/v2/api/external/{ApiID}/pipeline/delete/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### PipelineList

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/pipeline/list

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

get/v2/api/external/{ApiID}/pipeline/list

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### PipelineShow

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/pipeline/show/{id}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

idstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/pipeline/show/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### PipelineUpdate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/pipeline/update/{id}

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

namestringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/pipeline/update/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### StageCreate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/stage/create

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

pipelineIdstringOpcional

ordernumberOpcional

colorstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/stage/create

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### StageDelete

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/stage/delete/{id}

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

post/v2/api/external/{ApiID}/stage/delete/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### StageList

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/stage/list

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

pipelineIdstringOpcionalExample: `{{pipelineId}}`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/stage/list

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### StageShow

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/stage/show/{id}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

idstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/stage/show/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### StageUpdate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/stage/update/{id}

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

namestringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/stage/update/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

[Anterior👤 Contatos](/central-do-assinante/referencia-da-api/contatos)[Próximo📊 Dashboard](/central-do-assinante/referencia-da-api/dashboard)

Atualizado há 8 dias

Isto foi útil?