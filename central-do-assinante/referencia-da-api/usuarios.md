# 👥 Usuários

### CreateUser

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/createUser

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

emailstringOpcional

passwordstringOpcional

namestringOpcional

profilestringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/createUser

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### GetUserStatus

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/getUserStatus

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

userIdintegerOpcional

ID do usuário

Example: `1`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/getUserStatus

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListUsers

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/listUsers

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

pageNumberintegerOpcional

Número da página

Example: `1`

searchParamstringOpcional

Parâmetro de busca (opcional)

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/listUsers

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UpdateUser

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/updateUser

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

userIdnumberOpcional

namestringOpcional

emailstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/updateUser

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response



 8 dias
