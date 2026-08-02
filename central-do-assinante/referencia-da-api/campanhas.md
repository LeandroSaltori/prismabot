# 📣 Campanhas

### CampaignCancel

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/cancel/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/cancel/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignContactsAdd

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/contacts/add/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Corpoobject[]

application/json

application/json

namestringOpcional

numberstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/contacts/add/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignContactsList

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/contacts/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/campaign/contacts/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignContactsRemove

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/contacts/remove/{campaignId}/{contactId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

contactIdstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/contacts/remove/{campaignId}/{contactId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignContactsRemoveAll

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/contacts/removeAll/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/contacts/removeAll/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignCreate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/create

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

startstringOpcional

message1stringOpcional

message2stringOpcional

message3stringOpcional

sessionIdstringOpcional

delaystringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/create

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignDelete

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/delete/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/delete/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignDuplicate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/duplicate/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/duplicate/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignList

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/list

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

pageintegerOpcionalExample: `1`

limitintegerOpcionalExample: `10`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/campaign/list

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignPause

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/pause/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/pause/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignReport

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/report/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/campaign/report/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignResume

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/resume/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/resume/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignSkip

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/skip/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/skip/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignStart

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/start/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/start/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CampaignUpdate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/campaign/update/{campaignId}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

campaignIdstringObrigatório

Corpo

application/json

application/json

namestringOpcional

startstringOpcional

message1stringOpcional

message2stringOpcional

message3stringOpcional

sessionIdstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/campaign/update/{campaignId}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response



Atualizado há 8 dias

Isto foi útil?