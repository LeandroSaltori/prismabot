Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Referência da API](/central-do-assinante/referencia-da-api)

# 🟩 Interativo Uaz API

### UazapiButton

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendInteractive/uazapi/button

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

textstringOpcional

choicesstring[]Opcional

footerTextstringOpcional

imageButtonstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendInteractive/uazapi/button

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UazapiList

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendInteractive/uazapi/list

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

textstringOpcional

choicesstring[]Opcional

listButtonstringOpcional

footerTextstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendInteractive/uazapi/list

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UazapiPoll

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendInteractive/uazapi/poll

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

textstringOpcional

choicesstring[]Opcional

selectableCountnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendInteractive/uazapi/poll

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UazapiCarousel

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendInteractive/uazapi/carousel

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

textstringOpcional

carouselobject[]Opcional

Mostrar propriedades

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendInteractive/uazapi/carousel

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UazapiPixButton

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendInteractive/uazapi/pixButton

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

pixTypestringOpcional

pixKeystringOpcional

pixNamestringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendInteractive/uazapi/pixButton

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UazapiLocationButton

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendInteractive/uazapi/locationButton

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

textstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendInteractive/uazapi/locationButton

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UazapiRequestPayment

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendInteractive/uazapi/requestPayment

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

amountnumberOpcional

titlestringOpcional

textstringOpcional

footerstringOpcional

itemNamestringOpcional

invoiceNumberstringOpcional

pixTypestringOpcional

pixKeystringOpcional

pixNamestringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendInteractive/uazapi/requestPayment

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

[Anterior💬 Interativo Messenger](/central-do-assinante/referencia-da-api/interativo-messenger)[Próximo🔘 Interativo Waba](/central-do-assinante/referencia-da-api/interativo-waba)

Atualizado há 8 dias

Isto foi útil?