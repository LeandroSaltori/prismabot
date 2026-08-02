Copiar

Nesta página

1. [CENTRAL DO ASSINANTE](/central-do-assinante)
2. [Referência da API](/central-do-assinante/referencia-da-api)

# 🏢 Tenant API

### CreateApi

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/tenantCreateApi

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Corpo

application/json

application/json

namestringOpcional

sessionIdnumberOpcional

urlServiceStatusstring · anulávelOpcional

urlMessageStatusstring · anulávelOpcional

userIdnumberOpcional

authTokenstringOpcional

tenantnumberOpcional

Respostas

200

Successful response

application/json

post/tenantCreateApi

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### CreateSessionTenant

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/tenantApiCreateSession

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Corpo

application/json

application/json

tenantnumberOpcional

namestringOpcional

statusstringOpcional

typestringOpcional

Respostas

200

Successful response

application/json

post/tenantApiCreateSession

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### DeleteApi

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/tenantDeleteApi

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Corpo

application/json

application/json

sessionIdnumberOpcional

userIdnumberOpcional

tenantnumberOpcional

apiIdstringOpcional

Respostas

200

Successful response

application/json

post/tenantDeleteApi

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ListTenants

get

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/tenantApiListTenants

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Respostas

200

Successful response

application/json

get/tenantApiListTenants

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### ShowTenant

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/tenantApiShowTenant

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Corpo

application/json

application/json

idnumberOpcional

Respostas

200

Successful response

application/json

post/tenantApiShowTenant

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### StoreTenant

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/tenantApiStoreTenant

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Corpo

application/json

application/json

statusstringOpcional

namestringOpcional

maxUsersnumberOpcional

maxConnectionsnumberOpcional

acceptTermsbooleanOpcional

emailstringOpcional

passwordstringOpcional

userNamestringOpcional

profilestringOpcional

paymentGatewaystringOpcional

stripeCustomerIdstringOpcional

stripeTokenstringOpcional

Respostas

200

Successful response

application/json

post/tenantApiStoreTenant

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

### UpdateTenant

post

https://{{BaseUrl}}

https://{{BaseUrl}}undefined://{{BASE\_URL}}

/tenantApiUpdateTenant

Autorizações

bearerAuth

bearerAuth

AuthorizationstringObrigatório

Bearer authentication header of the form Bearer <token>.

Corpo

application/json

application/json

identitystringOpcional

statusstringOpcional

maxUsersnumberOpcional

maxConnectionsnumberOpcional

paymentGatewaystringOpcional

supportChatEnabledstringOpcional

menuVisibilitystring[]Opcional

allowedChannelsstring[]Opcional

channelConnectionLimitsobjectOpcional

Mostrar propriedades

oauthEnabledbooleanOpcional

oauthProxyUrlstringOpcional

instagramWebhookProxyUrlstringOpcional

instagramWebhookProxySecretstringOpcional

messengerWebhookProxyUrlstringOpcional

messengerWebhookProxySecretstringOpcional

Respostas

200

Successful response

application/json

post/tenantApiUpdateTenant

HTTP

HTTPcURLJavaScriptPython

Testar

200

Successful response

[Anterior📋 Templates WABA](/central-do-assinante/referencia-da-api/templates-waba)[Próximo🎫 Tickets](/central-do-assinante/referencia-da-api/tickets)

Atualizado há 8 dias

Isto foi útil?