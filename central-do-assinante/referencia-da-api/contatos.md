Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Referência da API](/central-do-assinante/referencia-da-api)

# 👤 Contatos

### BlockContact

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/blockContact

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

contactIdnumberOpcional

blockedbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/blockContact

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CreateContact

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/createContact

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

numberstringOpcional

emailstringOpcional

cpfstringOpcional

firstNamestringOpcional

lastNamestringOpcional

businessNamestringOpcional

birthdayDatestringOpcional

externalKeystringOpcional

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/createContact

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### GetContactExtraInfo

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/getContactExtraInfo

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

contactIdintegerOpcional

ID do contato

Example: `1`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/getContactExtraInfo

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SearchContacts

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/contacts/search

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

searchParamstringOpcional

pagenumberOpcional

limitnumberOpcional

tagIdnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/contacts/search

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ShowContact

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/showcontact

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

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/showcontact

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UpdateContact

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/updateContact

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

numberstringOpcional

emailstringOpcional

cpfstringOpcional

firstNamestringOpcional

lastNamestringOpcional

businessNamestringOpcional

birthdayDatestringOpcional

kanbannumberOpcional

externalKeystringOpcional

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/updateContact

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UpdateContactExtraInfo

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/updateContactExtraInfo

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

contactIdnumberOpcional

extraInfoobject[]Opcional

Mostrar propriedades

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/updateContactExtraInfo

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UpdateContactKanban

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/updateContactKanban

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

contactIdnumberOpcional

kanbannumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/updateContactKanban

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UpdateContactWallet

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/updateContactWallet

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

contactIdnumberOpcional

walletIdnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/updateContactWallet

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### MergeContacts

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/mergecontacts

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

pairsobject[]Opcional

Mostrar propriedades

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/mergecontacts

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### FindDuplicateContacts

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/findduplicatecontacts

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

limitnumberOpcional

matchKindsstring[]Opcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/findduplicatecontacts

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UnmergeContacts

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/unmergecontacts

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

duplicateIdsnumber[]Opcional

mergeLogIdsstring[]Opcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/unmergecontacts

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

[Anterior🔌 Canais E Sessões](/central-do-assinante/referencia-da-api/canais-e-sessoes)[Próximo🏗️ CRM Pipeline](/central-do-assinante/referencia-da-api/crm-pipeline)

Atualizado há 8 dias

Isto foi útil?