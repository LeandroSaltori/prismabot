# Pré-requisitos de instalação e utilização

Especificações mínimas de servidor, sistema operacional (Ubuntu), RAM, vCPU, domínio e navegador para instalar e usar o Prismabot.

### Requisitos do Servidor (servidor)

A servidor onde o sistema será instalado deve atender às seguintes especificações mínimas:

Recurso

Requisito mínimo

**Memória RAM**

16 GB ou mais

**Processador**

4 vCPUs ou mais (arquitetura AMD ou Intel x86-64)

**Armazenamento**

SSD ou NVMe a partir de 200 GB

**Latência**

50 ms ou menos

**Sistema operacional**

Ubuntu 24.04 LTS — instalação limpa, sem painel

O pleno funcionamento do sistema está condicionado ao atendimento dessas especificações. Ambientes subdimensionados ou fora das especificações não recebem diagnóstico de performance pelo suporte técnico.

Recomendamos datacenter brasileiro para garantir baixa latência e melhor experiência para os usuários.

#### Provedores de servidor recomendados

**Brasil:**

* [Hostinger]
* [HostGator](https://www.hostgator.com.br/servidor-servidor)

**Internacional (avalie a latência antes de contratar):**

* [Hetzner](https://www.hetzner.com/)
* [DigitalOcean](https://www.digitalocean.com/)
* [AWS](https://aws.amazon.com/)
* [OVHcloud](https://www.ovhcloud.com/pt/)

#### Registro de domínio

O Prismabot utiliza dois subdomínios (front-end e back-end) apontados para o IP da servidor. Para registrar um domínio `.com.br`, acesse [registro.br](https://registro.br/).

---

### Escalabilidade e projeção de consumo de recursos

O Prismabot não possui limite de canais ou usuários na licença — a capacidade de escalar depende diretamente dos recursos do servidor.

#### Consumo médio de memória RAM

Tipo de canal / conexão

Consumo médio por canal

Canais WABA / Hub

até 100 MB

Canais Baileys / Evolution / Meow

até 250 MB

Canais wwebjs

até 1 GB

**Por usuário logado (atendente)**

100 a 150 MB

Esses valores são uma projeção média e podem variar conforme a intensidade de uso. Monitore o consumo do servidor à medida que a operação cresce — alta utilização de RAM/CPU indica que é hora de fazer upgrade no plano de servidor.

---

### Requisitos da máquina do usuário (atendente)

Para acessar o painel do Prismabot, a máquina de cada atendente deve atender aos requisitos abaixo:

* **Memória RAM:** 8 GB ou mais
* **Processador:** Intel i5 ou equivalente
* **Conexão:** internet rápida e estável
* **Navegador e sistema operacional:** mantenha ambos atualizados para garantir segurança e compatibilidade

---

### Versões suportadas da API WhatsApp

* API WhatsApp Business Account v19.0 ou superior
* WhatsApp Web até a versão v2.24xx.x

---

### Manutenção e segurança do servidor

A gestão, segurança e manutenção do servidor são de responsabilidade do assinante. Veja as ações obrigatórias após a instalação:

[Manutenção e Segurança](manutencao-e-seguranca.md)



 25 dias
