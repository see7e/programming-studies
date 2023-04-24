---
title: PSQL PostGis
tags: studies
use: Documentation
languages: SQL
dependences: PostgreSQL
---

> structured query language
# Commandos
- `ctrl + L`	limpa a tela
# Tables
col x row
## Relational db
shared info btw tabs
## GUI
- pgadmin

## Create db
- todo comando começa com `\`
- `CREATE DATABESE dbname;`
- `\l`	mostra todas as dbs no pc
- `~ pqsql -h localhost -p 5432 -U username dbname`	cria uma nova db
- `\c dbname`	conecta com uma db existente
- `dbname=#`	db atual

## Delete DB
`DROP DATABESE dbname;`

## Create tables
```SQL
CREATE TABLE table_name (
	column_name + data_type + constraints
)
```

- sem constraints *ex.* </br>
```SQL
CREATE TABLE person (
	id int,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender VARCHAR(6),
	date_of_birth DATE );
```

- `VARCHAR` representa texto
- [Data Types](https://www.postgresql.org/docs/current/datatype.html)
- `\d`	describle tables existentes
- `\d dbname` descreve a table selecionada
- `\i /path/to/file.sql` abre o arquivo de SQL (_que pode conter já a criação do db ou não_)
- com constraints *ex.*</br>
```SQL
CREATE TABLE person (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	gender VARCHAR(6) NOT NULL,
	date_of_birth DATE NOT NULL );
```

`PRIMARY KEY` representa a chave para cada elemento da tabela</br>
`BIGSERIAL` é um (_8bit_) numero autoincrementavel

## Delete table
`DROP TABLE table_name`

## Insert records in 
```SQL
INSERT INTO person (
	first_name,
	last_name,
	gender,
	date_of_birth)
VALUES(‘Anne’, ‘Smith’, ‘FEMALE’, DATE ‘1988-01-09’);
```

## Select from
`SELECT * FROM dbname;` seleciona todos os itens (colunas) da tabela</br>
`SELECT coluna FROM dbname;`

## Order by
- crescente
`SELECT * FROM dbname ORDER BY col_name ACS;` por defaut vem `ACS`, assim, opcicional;
- decrescente
`SELECT * FROM dbname ORDER BY col_name DESC;`</br>

Pode ser definida mais de uma ordenação `col1, col2, col3, ...`

## Distinct 
`SELECT DISTINCT col1 FROM dbname;` seleciona os elementos distintos.</br>
Pode ser definida ordenação `... ORDER BY col1;`

## WHERE / AND-OR
`SELECT * FROM dbname WHERE col1 = ‘a’;` atua como um filtro de busca. Podem ser aplicados mais de um requisito usando `AND`/`OR` como agrupamento
`SELECT * FROM dbname WHERE col1 = ‘a’ AND col2=’b’;`

## Operadores de comparação
Podem ser aplicados comparações aritmetricas, `SELECT 1=1;` retorna (_t/f_):

|?column?|
|------------|
|t|
|(1 row)|

## Limit / offset / fetch
`SELECT * FROM dbname LIMIT y;` seleciona os ‘y’ primeiros elementos, mas pode ser definido um afastamento a partir do primeiro elemento `SELECT * FROM dbname OFFSET x LIMT y;`
A sintaxe original do sql usa o FETCH: `SELECT * FROM dbname FETCH FIRST z ROW ONLY;`

## In
Filtra a db atraves de um array de valores `SELECT * FROM dbname WHERE col1 IN (elem1, elem2,...);`.

## Between
`SELECT * FROM dbname WHERE col1 BETWEEN x AND y;` seleciona a partir de um interval de dados.

## Like / ilike
*ex.* </br>
`SELECT * FROM person WHERE email LIKE ‘%.com’;` seleciona emails terminados em “.com”.</br>

`%` representa qualquer caracter seguido ou antecedido pot etc. Pode ser usado `_` para representar quantidade de caracters. Importante que o filtro `LIKE` é case sensitive, o `ILIKE` não.

## Group by
Agrupa as informações de acordo com grupos existentes ou no, podem ser usadas funções.</br>

*ex.*</br>
`SELECT col1, COUNT(*) FROM dbname GROUP BY col1;`

## Group by having
`SELECT col1, COUNT() FROM dbname HAVONG COUNT() <condicional> x;`</br>
Seleciona elementos que possuam contagem que atendam à condicional (aggregate functions) aritimétrica.

## Min / max / med
`SELECT  MAX(col1) FROM dbname;` seleciona valor max da coluna </br>
`SELECT  MIN(col1) FROM dbname;`</br>
`SELECT  AVG(col1) FROM dbname;` retorna média, pode ser formatado com `ROUND(AVG(col1)).</br>

*ex.*</br>
`SELECT make, model, MIN(price) FROM car GROUP BY make, model;`

## Soma
`SELECT SUM(col1) FROM dbname;`

## Operadores aritimetricos
`+ - * / ^ ! %` </br>

round – pode ser definida a quantidade de casas decimais *ex
.*</br>

`SELECT id, make, model, price, ROUND(price *.10,) FROM car;`

|id|make|model|price|round|
|-|-|-|-|-|
|1|GMC|Acadia|17662.69|1766.26|
|...|...|...|...|...|

## Alias
Quando uma função cria uma coluna dentro da query, o cabeçalho vai ser o nome da função.</br>

`SELECT id, make, model, price, ROUND(price *.10,) AS nome_da_coluna FROM car;`

|id|make|model|price|nome_da_coluna|
|-|-|-|-|-|
|...|...|...|...|...|

## União / COALESCE
Retorna o primeiro valor que não seja `null`. </br>

`SELECT COALESCE(null, ..., x);`

*ex.*</br>
`SELECT COALESCE(email, 'N/A') FROM person;` retorna o email(primeiro parâmetro) e caso esse seja nulo/não exista, retorna a string 'N/A'.

## NULLIF
Recebe dois argumentos e retorna o primeiro *se* o segundo não for igual ao primeiro, se for igual, retorna `null`. </br>

|query|resultado|
|-|-|
|`SELECT NULLIF (100,100);` | `null` |
|`SELECT NULLIF (1,2);` | 1 |

## Timestamps e Datas
|query|resultado|
|-|-|
|`SELECT NOW()::DATE;`|YYYY-MM-DD|
|`SELECT NOW()::TIME;`|HH:MM:SS.XXXXXX|

### Modificando datas
`SELECT NOW() - INTERVAL '1 YEAR;` | DAY(S) | MONTH(S) | YEAR(S)

## Extraindo campos / valores
`SELECT EXTRACT(YEAR FROM NOW());`

## AGE()
`AGE(NOW(), data_de_nascimento);` recebe dois parametros, geralmente o cast da hora/data atual (menos/e) a data especificada (data_de_nascimento[var]).

## PRIMARY KEYS
Chave *única* que representa um elemento dentro de um banco de dados.
`SELECT * FROM table_name LIMIT 1;` retorna a primeira chave numérica de valor 1.

### Adicionando uma Chave Primária
`ALTER TABLE table_name ADD PRIMARY KEY(col);` modifica a tablea, caso algum chave esteja repetida, os elementos incosistentes devem ser removidos `DELETE FROM table_name WHERE chame=x;` e provavelmente inserir o valor correto `INSERT INTO table_name (info);`. </br>

##  Unique CONSTRAINTS
*ex.* `ALTER TABLE person ADD CONSTRAINT unique_email_address UNIQUE (email);` irá modificar a tabela para que receba na coluna **(email)** a limitação **unique_email_address**.

Caso a tabela já tenha algum valor repetido na coluna especificada, será preciso:
1. ou remover o item (no caso a pessoa) que possui o valor duplicado
2. ou selecionar (a pessoa) e anular o campo do email

*para confirmar:* `\d person`

	> Indexes:
	> "person_pkey" PRIMARY KEY, btree (id)
	> "unique_email_address" UNIQUE CONSTRAINT, btree (email)

## Check CONSTRAINTS
Permite adicionar uma CONSTRAINT baseada numa condição booleana.
*ex.* para restringir na table person o campo *gender*, basta `ALTER TABLE person ADD CONSTRAINT gender_Caonstraint CHECK (GENDER == 'Female' OR 'Male' OR 'Other');`.

## Delete Records
Para deletar, é necessário passar por parâmetro a chave pela qual será gerada o filtro `DELETE FROM table_name WHERE key = x;`. Ou até deletar tudo `DELETE FROM table_name;`.

## Update Records

``
``
``
``
``
``
``
``
``
``
``
``
