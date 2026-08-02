Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Referência da API](/central-do-assinante/referencia-da-api)

# 📋 Templates WABA

### SendTemplateWaba

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/template

A resposta retorna o ticketId do atendimento criado ou reutilizado. Exemplo: { "success": true, "data": { "message": "Message sent successfully", "ticketId": 123 } }

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

isClosedbooleanOpcional

templateDataobjectOpcional

Mostrar propriedades

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/template

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendTemplateWabaBody

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/templateBody

A resposta retorna o ticketId do atendimento criado ou reutilizado. Exemplo: { "success": true, "data": { "message": "Message sent successfully", "ticketId": 123 } }

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

isClosedbooleanOpcional

templateDataobjectOpcional

Mostrar propriedades

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/templateBody

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendTemplateWabaMarketing

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/templateMarketingBody

A resposta retorna o ticketId do atendimento criado ou reutilizado. Exemplo: { "success": true, "data": { "message": "Message sent successfully", "ticketId": 123 } }

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

isClosedbooleanOpcional

templateDataobjectOpcional

Mostrar propriedades

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/templateMarketingBody

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

[Anterior💼 Oportunidades](/central-do-assinante/referencia-da-api/oportunidades)[Próximo🏢 Tenant API](/central-do-assinante/referencia-da-api/tenant-api)

Atualizado há 9 dias

Isto foi útil?