Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Referência da API](/central-do-assinante/referencia-da-api)

# 🔘 Interativo Waba

### SendButtonWABA

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendButtonWABA

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

messagestringOpcional

button1stringOpcional

button2stringOpcional

button3stringOpcional

ticketIdnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendButtonWABA

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendListWABA

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendListWABA

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

headerstringOpcional

bodystringOpcional

footerstringOpcional

button\_textstringOpcional

sectionsobject[]Opcional

Mostrar propriedades

ticketIdnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendListWABA

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

[Anterior🟩 Interativo Uaz API](/central-do-assinante/referencia-da-api/interativo-uaz-api)[Próximo🏷️ Kanban / Tags / Motivos / Filas](/central-do-assinante/referencia-da-api/kanban-tags-motivos-filas)

Atualizado há 9 dias

Isto foi útil?