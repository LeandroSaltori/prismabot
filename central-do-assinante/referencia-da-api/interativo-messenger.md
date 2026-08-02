Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Referência da API](/central-do-assinante/referencia-da-api)

# 💬 Interativo Messenger

### Quick Reply

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{apiId}/sendInteractive/messenger/quickReply

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

apiIdstringObrigatório

Parâmetros de cabeçalho

Content-TypestringOpcionalExample: `application/json`

AuthorizationstringOpcionalExample: `Bearer {{API_TOKEN}}`

Corpo

application/json

application/json

ticketIdnumberOpcional

messagestringOpcional

quickRepliesobject[]Opcional

Mostrar propriedades

Respostas

200

Successful response

application/json

post/v2/api/external/{apiId}/sendInteractive/messenger/quickReply

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### Button Template

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{apiId}/sendInteractive/messenger/buttonTemplate

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

apiIdstringObrigatório

Parâmetros de cabeçalho

Content-TypestringOpcionalExample: `application/json`

AuthorizationstringOpcionalExample: `Bearer {{API_TOKEN}}`

Corpo

application/json

application/json

ticketIdnumberOpcional

messagestringOpcional

buttonsobject[]Opcional

Mostrar propriedades

Respostas

200

Successful response

application/json

post/v2/api/external/{apiId}/sendInteractive/messenger/buttonTemplate

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### Generic Template (cards)

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{apiId}/sendInteractive/messenger/genericTemplate

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

apiIdstringObrigatório

Parâmetros de cabeçalho

Content-TypestringOpcionalExample: `application/json`

AuthorizationstringOpcionalExample: `Bearer {{API_TOKEN}}`

Corpo

application/json

application/json

ticketIdnumberOpcional

elementsobject[]Opcional

Mostrar propriedades

Respostas

200

Successful response

application/json

post/v2/api/external/{apiId}/sendInteractive/messenger/genericTemplate

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### Media Template (image/video + botões)

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{apiId}/sendInteractive/messenger/mediaTemplate

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

apiIdstringObrigatório

Parâmetros de cabeçalho

Content-TypestringOpcionalExample: `application/json`

AuthorizationstringOpcionalExample: `Bearer {{API_TOKEN}}`

Corpo

application/json

application/json

ticketIdnumberOpcional

mediaTypestringOpcional

mediaUrlstringOpcional

buttonsobject[]Opcional

Mostrar propriedades

Respostas

200

Successful response

application/json

post/v2/api/external/{apiId}/sendInteractive/messenger/mediaTemplate

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### Receipt Template (recibo)

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{apiId}/sendInteractive/messenger/receiptTemplate

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

apiIdstringObrigatório

Parâmetros de cabeçalho

Content-TypestringOpcionalExample: `application/json`

AuthorizationstringOpcionalExample: `Bearer {{API_TOKEN}}`

Corpo

application/json

application/json

ticketIdnumberOpcional

receiptobjectOpcional

Mostrar propriedades

Respostas

200

Successful response

application/json

post/v2/api/external/{apiId}/sendInteractive/messenger/receiptTemplate

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### Message Tag (Marketing/Utility)

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{apiId}/sendInteractive/messenger/messageTag

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

apiIdstringObrigatório

Parâmetros de cabeçalho

Content-TypestringOpcionalExample: `application/json`

AuthorizationstringOpcionalExample: `Bearer {{API_TOKEN}}`

Corpo

application/json

application/json

ticketIdnumberOpcional

messagestringOpcional

tagstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{apiId}/sendInteractive/messenger/messageTag

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### Customer Feedback Template (NPS/CSAT)

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{apiId}/sendInteractive/messenger/customerFeedback

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

apiIdstringObrigatório

Parâmetros de cabeçalho

Content-TypestringOpcionalExample: `application/json`

AuthorizationstringOpcionalExample: `Bearer {{API_TOKEN}}`

Corpo

application/json

application/json

ticketIdnumberOpcional

titlestringOpcional

subtitlestringOpcional

business\_privacy\_urlstringOpcional

expires\_in\_daysnumberOpcional

feedback\_screensobject[]Opcional

Mostrar propriedades

Respostas

200

Successful response

application/json

post/v2/api/external/{apiId}/sendInteractive/messenger/customerFeedback

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### Greeting Text (get/set/delete)

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{apiId}/messenger/greeting

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

apiIdstringObrigatório

Parâmetros de cabeçalho

Content-TypestringOpcionalExample: `application/json`

AuthorizationstringOpcionalExample: `Bearer {{API_TOKEN}}`

Corpo

application/json

application/json

actionstringOpcional

greetingsobject[]Opcional

Mostrar propriedades

Respostas

200

Successful response

application/json

post/v2/api/external/{apiId}/messenger/greeting

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### Personas (list/create/delete)

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{apiId}/messenger/personas

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

apiIdstringObrigatório

Parâmetros de cabeçalho

Content-TypestringOpcionalExample: `application/json`

AuthorizationstringOpcionalExample: `Bearer {{API_TOKEN}}`

Corpo

application/json

application/json

actionstringOpcional

namestringOpcional

profilePictureUrlstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{apiId}/messenger/personas

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

[Anterior📷 Interativo Instagram](/central-do-assinante/referencia-da-api/interativo-instagram)[Próximo🟩 Interativo Uaz API](/central-do-assinante/referencia-da-api/interativo-uaz-api)

Atualizado há 8 dias

Isto foi útil?