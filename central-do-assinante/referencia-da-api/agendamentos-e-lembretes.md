# 📅 Agendamentos E Lembretes

### AppointmentCreate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/appointment/create

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

titlestringOpcional

descriptionstringOpcional

contactIdstringOpcional

contactNamestringOpcional

contactPhonestringOpcional

whatsappIdstringOpcional

startAtstringOpcional

endAtstringOpcional

statusstringOpcional

notesstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/appointment/create

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### AppointmentDelete

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/appointment/delete/{id}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

idstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/appointment/delete/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### AppointmentList

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/appointment/list

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

statusstringOpcional

pending | confirmed | cancelled | completed

Example: `pending`

startFromnumberOpcional

Filtrar agendamentos a partir desta data (ISO 8601)

Example: `2026-04-01T00:00:00.000Z`

startTonumberOpcional

Filtrar agendamentos até esta data (ISO 8601)

Example: `2026-04-30T23:59:59.000Z`

searchstringOpcional

Busca por título ou nome do contato

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/appointment/list

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### AppointmentShow

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/appointment/show/{id}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

idstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/appointment/show/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### AppointmentUpdate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/appointment/update/{id}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

idstringObrigatório

Corpo

application/json

application/json

titlestringOpcional

descriptionstringOpcional

contactIdstringOpcional

contactNamestringOpcional

contactPhonestringOpcional

whatsappIdstringOpcional

startAtstringOpcional

endAtstringOpcional

statusstringOpcional

notesstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/appointment/update/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ScheduleReminderCreate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/scheduleReminder/create

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

descriptionstringOpcional

hoursBeforeEventnumberOpcional

messageTypestringOpcional

messageContentstringOpcional

whatsappIdstringOpcional

activebooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/scheduleReminder/create

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ScheduleReminderDelete

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/scheduleReminder/delete/{id}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

idstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/scheduleReminder/delete/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ScheduleReminderList

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/scheduleReminder/list

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/scheduleReminder/list

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ScheduleReminderToggle

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/scheduleReminder/toggle/{id}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

idstringObrigatório

Corpo

application/json

application/json

objectOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/scheduleReminder/toggle/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ScheduleReminderUpdate

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/scheduleReminder/update/{id}

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

idstringObrigatório

Corpo

application/json

application/json

namestringOpcional

descriptionstringOpcional

hoursBeforeEventnumberOpcional

messageTypestringOpcional

messageContentstringOpcional

whatsappIdstringOpcional

activebooleanOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/scheduleReminder/update/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response



Atualizado há 8 dias

Isto foi útil?