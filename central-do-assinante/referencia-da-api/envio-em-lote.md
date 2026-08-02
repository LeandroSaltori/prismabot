# 📤 Envio Em Lote

### BulkDispatchIncrementProgress

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/bulkDispatch/incrementProgress/{dispatchId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

dispatchIdstringObrigatório

Corpo

application/json

application/json

successbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/bulkDispatch/incrementProgress/{dispatchId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### BulkDispatchList

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/bulkDispatch/list

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

get/v2/api/external/{ApiID}/bulkDispatch/list

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### BulkDispatchShow

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/bulkDispatch/show/{dispatchId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

dispatchIdstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/bulkDispatch/show/{dispatchId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### BulkDispatchUpdate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/bulkDispatch/update/{dispatchId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

dispatchIdstringObrigatório

Corpo

application/json

application/json

statusstringOpcional

cancellationReasonstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/bulkDispatch/update/{dispatchId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### BulkFastMessage

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/bulkFastMessage

v2 crossChannelTicketCheck: quando a flag 'Verificar conversa em outros canais' do tenant esta ligada, destinatarios com ticket aberto ou pendente (em qualquer canal) NAO recebem o disparo. A resposta inclui skipped (contagem) e skippedNumbers (lista). Para ignorar a checagem nesta chamada, envie "skipActiveTicketCheck": false no body.

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

whatsappIdstringOpcional

whatsappTypestringOpcional

arrayNumbersstring[]Opcional

messagestringOpcional

minnumberOpcional

maxnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/bulkFastMessage

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### BulkIndividual

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/bulkIndividual

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

whatsappIdstringOpcional

numberstringOpcional

messagestringOpcional

externalKeystringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/bulkIndividual

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### BulkSendMessage

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/bulkSendMessage

v2 crossChannelTicketCheck: quando a flag 'Verificar conversa em outros canais' do tenant esta ligada, destinatarios com ticket aberto ou pendente (em qualquer canal) NAO recebem o disparo. A resposta inclui skipped (contagem) e skippedNumbers (lista). Para ignorar a checagem nesta chamada, envie "skipActiveTicketCheck": false no body.

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

whatsappIdstringOpcional

arrayNumbersstring[]Opcional

messagestringOpcional

minnumberOpcional

maxnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/bulkSendMessage

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### BulkSendMessageWithVariable

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/bulkSendMessageWithVariable

v2 crossChannelTicketCheck: quando a flag 'Verificar conversa em outros canais' do tenant esta ligada, o destinatario com ticket aberto ou pendente (em qualquer canal) NAO recebe o disparo. A resposta inclui skipped (contagem) e skippedNumbers (lista). Para ignorar a checagem nesta chamada, envie "skipActiveTicketCheck": false no body.

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

whatsappIdstringOpcional

messagestringOpcional

dataInputstringOpcional

minnumberOpcional

maxnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/bulkSendMessageWithVariable

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response



 8 dias
