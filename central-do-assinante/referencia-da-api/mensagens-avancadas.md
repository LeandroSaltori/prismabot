Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Referência da API](/central-do-assinante/referencia-da-api)

# 📨 Mensagens Avançadas

### SearchMessages

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/searchMessages

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

ticketIdstringOpcionalExample: `{{ticketId}}`

searchParamstringOpcionalExample: `olá`

pageintegerOpcionalExample: `1`

limitintegerOpcionalExample: `20`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/searchMessages

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendLocation

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendLocation

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

numberstringOpcional

latitudenumberOpcional

longitudenumberOpcional

namestringOpcional

addressstringOpcional

ticketIdstring · anulávelOpcional

externalKeystringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendLocation

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendVcard

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendVcard

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

numberstringOpcional

contactobject[]Opcional

Mostrar propriedades

ticketIdstring · anulávelOpcional

externalKeystringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendVcard

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

[Anterior📨 Mensagens](/central-do-assinante/referencia-da-api/mensagens)[Próximo👥 Mensagens Em Grupo](/central-do-assinante/referencia-da-api/mensagens-em-grupo)

Atualizado há 8 dias

Isto foi útil?