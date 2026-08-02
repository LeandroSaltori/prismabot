Copiar

Nesta página

1. [Configuração Superadmin](/configuracao-superadmin)
2. [Tenants e Licença](/configuracao-superadmin/tenants-e-licenca)

# Artigo: Usando o Prismabot para Vários Clientes

Esta página é um guia completo para entender como o modelo Prismabot do Prismabot funciona em cenários com múltiplos clientes. O objetivo é esclarecer a relação entre sua licença, as instalações, a personalização de marca e as regras de uso da plataforma.

**A Dúvida Mais Comum:** "Posso configurar uma marca, logo e cores diferentes para cada um dos meus clientes?"

A resposta curta é: **uma instalação = uma marca**. Para ter marcas diferentes para clientes diferentes, você precisará de instalações separadas. Abaixo, detalhamos os dois modelos de operação possíveis.

---

### **Entendendo os Conceitos-Chave da Sua Licença**

Sua licença Prismabot está atrelada a alguns conceitos fundamentais que definem como você pode estruturar seu negócio:

* **Uma Licença Anual:** Governa o seu direito de uso do software Prismabot.
* **Um Domínio Principal:** Sua licença está associada a um domínio principal (ex: suaagencia.com). Todas as suas instalações devem operar em subdomínios deste domínio principal.
* **Múltiplas Instalações (servidor):** Sua única licença permite que você instale o Prismabot em múltiplos servidores (servidor), desde que as regras de propriedade da infraestrutura sejam seguidas.
* **Múltiplos Clientes (Tenants):** O Prismabot foi projetado para o modelo SaaS, permitindo que você crie contas de clientes (tenants) isoladas.
* **Uma Marca (Prismabot) por Instalação:** A personalização de marca (logo, cores, nome) é definida no nível do Super Admin e se aplica a **toda aquela instalação** e a todos os tenants dentro dela.

---

#### **Cenário 1: O Modelo Centralizado (Uma Instalação, Vários Clientes, Uma Marca)**

Este é o modelo de operação mais comum e direto.

* **Como Funciona:** Você tem **uma única instalação** do Prismabot em um único servidor (servidor). Dentro desta instalação, você cria múltiplos tenants, um para cada cliente seu.
* **Personalização:** Você configura o Prismabot com a **sua própria marca** no painel Super Admin. Todos os seus clientes acessarão a plataforma através de um subdomínio seu (ex: app.suaagencia.com) e verão a sua marca.

**Vantagens:**

* **Gestão Simplificada:** Você gerencia, atualiza e mantém um único servidor.
* **Custo de Infraestrutura Menor:** O custo se limita a um único servidor (que pode precisar de upgrade conforme o número de clientes cresce).

**Limitação:**

* Você não pode personalizar a marca para cada cliente individualmente. Todos verão a mesma marca (a sua).

---

#### **Cenário 2: O Modelo Distribuído (Várias Instalações, Vários Clientes, Várias Marcas)**

Este modelo oferece a máxima flexibilidade de personalização e é a solução para quem precisa oferecer a plataforma com a marca de cada cliente.

* **Como Funciona:** Você realiza **múltiplas instalações** do Prismabot, cada uma em um **servidor (servidor) separado**. Cada instalação será dedicada a um único cliente.

Você (o assinante) deve ser o proprietário ou o responsável direto pela infraestrutura (servidor) onde cada instalação está rodando

* **Personalização:** Como cada instalação tem seu próprio painel Super Admin, você pode configurar o Prismabot de **cada instalação com a marca específica daquele cliente**.

**Exemplo:**

* **Instalação 1 (servidor 1):** Para o Cliente A. Acessível em clientea.suaagencia.com. Marca, logo e cores do Cliente A.
* **Instalação 2 (servidor 2):** Para o Cliente B. Acessível em clienteb.suaagencia.com. Marca, logo e cores do Cliente B.

**Vantagens:**

* **Personalização Total:** Cada cliente tem uma experiência 100% Prismabot com sua própria marca.
* **Isolamento de Infraestrutura:** Cada cliente opera em um ambiente completamente isolado, o que pode ser um requisito de segurança para alguns.

**Pontos a Considerar:**

* **Custo de Infraestrutura Maior:** Cada instalação requer seu próprio servidor, multiplicando os custos.
* **Gestão Mais Complexa:** Você será responsável por manter e atualizar múltiplas instalações.

---

#### **A Regra de Ouro: Licenciamento e Propriedade da Infraestrutura**

A flexibilidade de múltiplas instalações está diretamente ligada aos nossos Termos de Uso, especificamente à cláusula de sublicenciamento.

**Aviso sobre Sublicenciamento e Propriedade**

Sua licença Prismabot **pode ser usada em múltiplas instalações sem custo adicional**, contanto que duas condições sejam atendidas:

1. Todas as instalações operem sob subdomínios do **mesmo domínio principal** associado à sua licença.
2. **Você (o assinante) deve ser o proprietário ou o responsável direto pela infraestrutura (servidor)** onde cada instalação está rodando.

Não é permitido "revender" ou "transferir" a licença do software de forma avulsa. O que você vende é o **acesso a um serviço** que roda em uma infraestrutura gerenciada por você.

Para detalhes completos, consulte a seção 9 dos nossos Termos de Uso.
[**→ Ler os Termos e Condições de Uso**](/diretrizes-e-politicas/termos-e-condicoes-gerais-de-uso-e-licenciamento)

---

[AnteriorComo configurar a integração de Planos com o Stripe](/configuracao-superadmin/tenants-e-licenca/planos/como-configurar-a-integracao-de-planos-com-o-stripe)[PróximoConfigurações Superadmin](/configuracao-superadmin/configuracoes)

Atualizado há 4 meses

Isto foi útil?