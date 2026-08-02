Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Referência da API](/central-do-assinante/referencia-da-api)

# 📂 Galeria

### GalleryDelete

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/gallery/delete/{id}

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

post/v2/api/external/{ApiID}/gallery/delete/{id}

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### GalleryList

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/gallery/list

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Parâmetros de rota

ApiIDstringObrigatório

Parâmetros de consulta

pageNumberintegerOpcionalExample: `1`

fileTypestringOpcionalExample: `image`

Respostas

200

Successful response

application/json

get/v2/api/external/{ApiID}/gallery/list

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### GalleryUpload

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/v2/api/external/{ApiID}/gallery/upload

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

descriptionstringOpcional

Respostas

200

Successful response

application/json

post/v2/api/external/{ApiID}/gallery/upload

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

[Anterior📤 Envio Em Lote](/central-do-assinante/referencia-da-api/envio-em-lote)[Próximo👥 Grupos Whats App](/central-do-assinante/referencia-da-api/grupos-whats-app)

Atualizado há 8 dias

Isto foi útil?