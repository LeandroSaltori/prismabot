# 📨 Mensagens

### GetMessageByMessageId

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/getMessageByMessageId

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

messageIdstringOpcional

ID da mensagem retornado pela Meta (ex: wamid.xxxxx)

Example: `wamid.xxxxx`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/getMessageByMessageId

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendMessageAPIText

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}

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

bodystringOpcional

numberstringOpcional

externalKeystringOpcional

isClosedbooleanOpcional

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendMessageAPIFileURL

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/url

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

mediaUrlstringOpcional

bodystringOpcional

numberstringOpcional

externalKeystringOpcional

isClosedbooleanOpcional

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/url

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendMessageAPITextBase64

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/base64

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

bodystringOpcional

numberstringOpcional

base64DatastringOpcional

mimeTypestringOpcional

fileNamestringOpcional

isClosedbooleanOpcional

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/base64

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendMessageAPIVoice

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/voice

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

audiostringOpcional

numberstringOpcional

externalKeystringOpcional

isClosedbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/voice

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendMessageParams

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/params/

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

bodystringOpcional

Texto da mensagem que será enviada

Example: `A%20mensagem%20desejadaa`

numberintegerOpcional

Número do WhatsApp do destinatário (formato: 5511999999999)

Example: `5515998566622`

externalKeystringOpcional

Chave única do sistema para identificação (valor gerado do seu lado para controle do envio e não pode se repetir)

Example: `ID_UNICA_DO_SISTEMA_CLIENTE_PARA_EXECUTAR_UMA_ACAO_COM_WEBHOOK`

bearertokenstringOpcional

Token de autenticação

Example: `{{BearerToken}}`

isClosedbooleanOpcional

Define se o ticket será fechado após o envio

Example: `false`

validateNumberbooleanOpcional

Validar numero (opcional, padrao true). Se false, usa o numero exatamente como enviado, sem normalizacao do 9o digito BR (recomendado p/ WABA).

Example: `true`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/params/

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response



Atualizado há 8 dias

Isto foi útil?