# 🎫 Tickets

### AddTag

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/addTag

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

tagIdnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/addTag

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### AddTagContact

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/addTagContact

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

tagIdnumberOpcional

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/addTagContact

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### RemoveTagContact

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/removeTagContact

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

tagIdsnumber[]Opcional

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/removeTagContact

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CreateNotes

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/createNotes

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

notesstringOpcional

ticketIdnumberOpcional

userIdnumberOpcional

idFrontstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/createNotes

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CreateTicketWebmail

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/createTicket

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

emailstringOpcional

channelIdnumberOpcional

externalKeystringOpcional

userIdnumberOpcional

statusstringOpcional

namestringOpcional

firstNamestringOpcional

lastNamestringOpcional

validateNumberbooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/createTicket

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListNotes

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/listNotes

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

ticketIdintegerOpcional

ID do ticket

Example: `1262`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/listNotes

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### RemoveTag

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/removeTag

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

tagIdnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/removeTag

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SendPresence

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/sendPresence

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

statestringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/sendPresence

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SetQueue

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/updatequeue

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

queueIdnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/updatequeue

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SetTag

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/updatetag

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

tagnumberOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/updatetag

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### SetTicketInfo

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/updateticketinfo

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

userIdnumberOpcional

statusstringOpcional

queueIdstring · anulávelOpcional

typebotStatusbooleanOpcional

chatgptStatusbooleanOpcional

dialogflowStatusbooleanOpcional

difyStatusbooleanOpcional

n8nStatusbooleanOpcional

chatFlowIdstring · anulávelOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/updateticketinfo

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ShowAllMessages

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/showAllMessages

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

ticketstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/showAllMessages

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ShowAllTicketInformation

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/showallticket

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

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/showallticket

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ShowTicketInformation

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/showticket

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

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/showticket

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ShowTicketInformationChatBot

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/showticketchatbot

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

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/showticketchatbot

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UpdateNote

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/updateNote

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

noteIdnumberOpcional

notesstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/updateNote

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UpdateTicketChannel

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/updateTicketChannel

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

whatsappIdnumberOpcional

channelstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/updateTicketChannel

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response



Atualizado há 9 dias

Isto foi útil?