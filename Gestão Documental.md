---
title: Gestão Documental
tags: studies
use: Documentation
languages: NULL
dependences: NULL
---
# 12 princípios do Manifesto Ágil

1. Nossa maior prioridade é satisfazer o cliente por meio da entrega antecipada e contínua de software valioso. ![principio1]( https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/Henrik.png)

2. Aceitar mudanças nos requisitos, mesmo no final do desenvolvimento. Os processos ágeis aproveitam a mudança para a vantagem competitiva do cliente. ![principo2]( https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/cone-of-uncertainty.png)

3. Entregue o software funcionando com frequência, de algumas semanas a alguns meses, com preferência para a escala de tempo mais curta. ![principio3]( https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/Hexagon.png)

4. Clientes e desenvolvedores devem trabalhar juntos diariamente ao longo do projeto. ![principio4]( https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/ComparingEvolutions-colorblindinclusive.png)

5. Construir projetos em torno de indivíduos motivados. Dê a eles o ambiente e o suporte de que precisam e confie neles para fazer o trabalho.

6. O método mais eficiente e eficaz de transmitir informações para e dentro de uma equipe de desenvolvimento é a conversa face a face.

7. O software funcionando é a principal medida de progresso. ![principio7]( https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/Done_1.png)

8. Processos ágeis promovem o desenvolvimento sustentável. Os patrocinadores, desenvolvedores e usuários devem ser capazes de manter um ritmo constante indefinidamente.

9. A atenção contínua à excelência técnica e ao bom design aumenta a agilidade.

10. Simplicidade – a arte de maximizar a quantidade de trabalho não feito – é essencial. ![principio10]( https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/FocusOnThis.png)

11. As melhores arquiteturas, requisitos e designs surgem de equipes auto-organizadas. ![principio11]( https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/Architecture-Image.png)

>A arquitetura do produto, que é a estrutura subjacente e a abordagem para entrega do produto, surge junto com a entrega de recursos. Aderir a esse princípio significa que a equipe não desaparece por seis meses enquanto descobre a melhor arquitetura de longo prazo. Em vez disso, os membros da equipe decidem a melhor forma de construir o produto enquanto criam o produto.

12. Em intervalos regulares, a equipe reflete sobre como se tornar mais eficaz, então ajusta seu comportamento de acordo. ![principio12]( https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/Retrospective-board.png)

## Conclusão
Revisitar o manifesto regularmente é um exercício útil para as equipes como uma camada adicional de responsabilidade. Se você está se perguntando como sua equipe pode viver melhor esses princípios ágeis, discuta isso na próxima [Sprint Retrospective](https://www.scrum.org/resources/blog/ideas-scrums-sprint-retrospective-event).

<p>Uma maneira de fazer isso é colocar os 12 princípios ágeis em um quadro branco compartilhado. Em seguida, peça aos membros do Time Scrum que façam um brainstorming sobre como incorporar melhor esses princípios em seu trabalho e interações com a organização-mãe ou partes interessadas do negócio. Em seguida, vote em uma ou duas melhorias acionáveis e implemente-as o mais rápido possível.</p>

# [Planejamento de Software e Documentação Técnica](https://www.youtube.com/watch?v=2qlcY9LkFik)

```mermaid
flowchart TD
	A(Gestão Documental)
	A --> AA(Documentação do Produto)
		
	AA --> AAA(Requerimentos do Produto)
	AAA --> AAAA(Funcionais)
	AAA --> AAAB(Não-funcionais)
	
	AA --> AAB(UX)
	AAB--> AABA(Perfil do Usuário)
	AAB--> AABB(Cenários)
	
	AA--> AAC(Arquitetura)
	
	A --> AB(Documentação do Processo)
	AB --> ABA(Roadmaps)
	ABA --> ABAA(Estratégias)
	ABA --> ABAB(Tecnologias)
	ABA --> ABAC(Releases)
	
	AB --> ABB(Métricas)
	ABB --> ABBA(Work in progress)
	ABB --> ABBB(Saúde do Processo e Gargalos)
	ABB --> ABBC(Qualidade de Código)

	AB --> ABC(Guidelines)
	ABC --> ABCA(Melhores práticas)
	ABC --> ABCB(Manuais)

	ABBA --> ABBAA(Velocidade)
	ABBA --> ABBAB(Sprint Burndowns)
	ABBA --> ABBAC(Release Burndowns)

	ABBB --> ABBBA(Ciclos)
	ABBB --> ABBBB(Fluxo Culmulativo)
	ABBB --> ABBBC(Eficiência do Fluxo)
	
	ABBC --> ABBCA(Média de código)
	ABBC --> ABBCB(Automação vs Testes manuais)
	ABBC --> ABBCC(Rotatividade de código)
	ABBC --> ABBCD(MCC)
```

1.	Documentação do produto
    1.	Requerimentos do produto
        1.	 funcionais (capacidades do usuário)
        2.	não funcionais (capacidades do produto)
    2.	UX - Experiencias dos usuários (perfil e necessidades do usuário)
    3.	[Arquitetura](https://www.youtube.com/watch?v=BrT3AO8bVQY)</br>
        1.	Interface
        2.	Logica de negocio
        3.	Database

    ![Arquitetura](src/arquit.png)
    >from [AltexSoft]( https://www.youtube.com/@AltexSoft)
    </br>

    4.	Testing plans (define os responsáveis por cada caso e os casos)
        1.	Casos (descrição de como cada feature deve ser testada)

    ![Etapas do processo](src/processo.png)
    >from [AltexSoft]( https://www.youtube.com/@AltexSoft)
    </br>

2.	Documentação do Processo
    1.	Roadmap (Gannt)
        1.	Estratégia 
        2.	Tecnologias
        3.	Releases
    2.	Métricas

    ![Métricas](src/metricas.png)
    >from [AltexSoft]( https://www.youtube.com/@AltexSoft)
    </br>

    3.	Guidelines
        1.	Melhores práticas
        2.	Manuais

---
