---
title: LTE Network Introduction
tags:
  - studies
  - programming
  - telecomunications
  - 4g_core
use: Documentation, Algorithms
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [4G LTE (Long Term Evolution)]()
- [References](#references)

</details>

---
#to_translate #to_review


# 4G LTE (Long Term Evolution)

> Servicos baseados em IP

- A maioria dos **sistemas de monitoramento** de rede baseiam-se em coletas de **SNMP** (Somple Network Management Protocol), e geracao de relatorios

Pode gerar problemas de **elevacao de CPV** nos equipamentos de rede acarretando a perda da gerencia.

Necessidade de implantacao de **elementos coletores** aumentando a possibilidade de falha e ineficiencia.

A estrutura de gerenciamento **nao permite avaliar a qualidade da rede** (QoS) e a qualidade da experiencia do usuario final (QoE).

Para avaliar a rede LTE fazendo uso de Call Detail Record (CDR), possibilitando avaliacao e2e nao onerando os elementos da rede.

---

## Arquitetura

![graph](https://www.teleco.com.br/imagens/tutoriais/tutorialltecdr_figura01.jpg)

### MME - Mobile Management Entity
É **equivalente ao Home Location Register** e ao **Visitor Location Register** na rede UTMS (?). MME **lida com a sinalizacao e controle, gestao da mobilidade e distribuicao da paginacao** das mensages para o **eNodeB** (?).
- Facilita a otimizacao das redes implementadas e **permite flexibilidade total na ampliacao da capacidade**.
- Faz a gestao do UE (?) a rede atraves da **interacao com o HSS (Home Subscription Server)** autenticando os utilizadores.
- Fornece a funcao do plano de controle para permitir a mobilidade continua entre o LTE e a rede 2G/3G. **Suporta intercepcoes legais de sinalizacao**.

### HSS / AAA - Authentication, Authorization, Accounting
Abrange funcionalidades semelhantes as do HCR com informacao especifica do utilizador e **podem ser extraidas CDR (Radius/Diameter)**.

### S-GW - Serving Gatweway
> Podem ser extraidos CDRs

- Atua como **ponto de terminacao entre a rede de acesso radio E-UTRAN e a rede core**.
- **Encaminha os pacotes para eNodeB** e realiza a compatibilizacao e o **controle dos dados do utilizador**.
- (?) Serve de ancora de mobilidade local para os **handovers** entre eNodeB ou para a passagem entre redes 3GPP.
- Informa o trafego do utilizador no caso de intercepcao legal.

### P-GW - Packet Data Network Gatweway
> Podem gerar CDRs

Serve como **ponto de entrada e de saida  do trafego de dados** do equipamento do usuario e da interface entre as redes LTE e as redes de pacotes de dados, baseados em **protocolos de iniciacao da sessao (SIP)** ou **protocolo de internet de subsistemas de multimidea (IMS)**.
- Faz a **gestao da atribuicao dos enderecos de IP** e **suporta a filtragem de pacotes para cada usuario**.
- Oferece **suporte a tarifacao**, servindo tambem de ancora para a mobiulidade entre 3GPP e nao 3GPP.

### PCRF - Policy and Charging Rules Function
Permite ou nega pedidos de multimidea.

- Cria e faz a atualizacao do contexto do **protocolo de pacote de dados (PDP)**.
- controla a **atribuicao de recursos**.
- Fornece regras de tarifacao com base no fluxo de servicos de dados para o P-GW.

# References

- [teleco.com.br](https://www.teleco.com.br/tutoriais/tutorialltecdr/pagina_1.asp)