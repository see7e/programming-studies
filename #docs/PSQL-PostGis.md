structured query language
---
# commandos
- `ctrl + L`	limpa a tela
# tables
col x row
## relational db
shared info btw tabs
## gui
- pgadmin

## create db
- todo comando começa com `\`
- `CREATE DATABESE dbname;`
- `\l`	mostra todas as dbs no pc
- `~ pqsql -h localhost -p 5432 -U username dbname`	cria uma nova db
- `\c dbname`	conecta com uma db existente
- `dbname=#`	db atual

## delete DB
`DROP DATABESE dbname;`

## create tables
`CREATE TABLE table_name (
	column_name + data_type + constraints
)`

- sem constraints ex. </br>
`CREATE TABLE person (
	id int,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender VARCHAR(6),
	date_of_birth DATE );`

- `VARCHAR` representa texto
- [Data Types](https://www.postgresql.org/docs/current/datatype.html)
- `\d`	describle tables existentes
- `\d dbname` descreve a table selecionada
- `\i /path/to/file.sql` abre o arquivo de SQL (que pode conter já a criação do db ou não)
- com constraints ex.</br>
`CREATE TABLE person (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	gender VARCHAR(6) NOT NULL,
	date_of_birth DATE NOT NULL );`

`PRIMARY KEY` representa a chave para cada elemento da tabela</br>
`BIGSERIAL` é um (8bit) numero autoincrementavel

## delete table
`DROP TABLE table_name`

## insert records in tables
`INSERT INTO person (
	first_name,
	last_name,
	gender,
	date_of_birth)
VALUES(‘Anne’, ‘Smith’, ‘FEMALE’, DATE ‘1988-01-09’);`

## select from
`SELECT * FROM dbname;` seleciona todos os itens (colunas) da tabela</br>
`SELECT coluna FROM dbname;`

## order by
- crescente
`SELECT * FROM dbname ORDER BY col_name ACS;` por defaut vem `ACS`, assim, opcicional
- decrescente
`SELECT * FROM dbname ORDER BY col_name DESC;`</br>
Pode ser definida mais de uma ordenação `col1, col2, col3, ...`

## distinct 
`SELECT DISTINCT col1 FROM dbname;` seleciona os elementos distintos</br>
Pode ser definida ordenação `... ORDER BY col1;`

## WHERE / AND-OR
`SELECT * FROM dbname WHERE col1 = ‘a’;` atua como um filtro de busca. Podem ser aplicados mais de um requisito usando `AND`/`OR` como agrupamento
`SELECT * FROM dbname WHERE col1 = ‘a’ AND col2=’b’;`

## operadores de comparação
Podem ser aplicados comparações aritmetricas, `SELECT 1=1;` retorna (t/f):

|?column?|
|------------|
|t|
|(1 row)|

## limit / offset / fetch
`SELECT * FROM dbname LIMIT y;` seleciona os ‘y’ primeiros elementos, mas pode ser definido um afastamento a partir do primeiro elemento `SELECT * FROM dbname OFFSET x LIMT y;`
A sintaxe original do sql usa o FETCH: `SELECT * FROM dbname FETCH FIRST z ROW ONLY;`

## in
Filtra a db atraves de um array de valores `SELECT * FROM dbname WHERE col1 IN (elem1, elem2,...);`

## between
`SELECT * FROM dbname WHERE col1 BETWEEN x AND y;` seleciona a partir de um interval de dados

## like / ilike
ex. </br>
`SELECT * FROM person WHERE email LIKE ‘%.com’;` seleciona emails terminados em “.com”</br>
`%` representa qualquer caracter seguido ou antecedido pot etc. Pode ser usado `_` para representar quantidade de caracters.
Importante que o filtro `LIKE` é case sensitive, o `ILIKE` não

## group by
Agrupa as informações de acordo com grupos existentes ou no, podem ser usadas funções</br>
ex.</br>
`SELECT col1, COUNT(*) FROM dbname GROUP BY col1;`

## group by having
`SELECT col1, COUNT() FROM dbname HAVONG COUNT() <condicional> x;`</br>
Seleciona elementos que possuam contagem que atendam à condicional (aggregate functions) aritimetrica

## min / max / med
`SELECT  MAX(col1) FROM dbname;` seleciona valor max da coluna </br>
`SELECT  MIN(col1) FROM dbname;`</br>
`SELECT  AVG(col1) FROM dbname;` retorna média, pode ser formatado com `ROUND(AVG(col1))</br>
ex.</br>
`SELECT make, model, MIN(price) FROM car GROUP BY make, model;`

## soma
`SELECT SUM(col1) FROM dbname;`

## operadores aritimetricos
`+ - * / ^ ! %` </br>
round – pode ser definida a quantidade de casas decimais *ex
.*</br>
`SELECT id, make, model, price, ROUND(price *.10,) FROM car;`

|id|make|model|price|round|
|-|-|-|-|-|
|1|GMC|Acadia|17662.69|1766.26|
|...|...|...|...|...|

## alias
Quando uma função cria uma coluna dentro da query, o cabeçalho vai ser o nome da função</br>
`SELECT id, make, model, price, ROUND(price *.10,) AS nome_da_coluna FROM car;`

|id|make|model|price|nome_da_coluna|
|-|-|-|-|-|
|...|...|...|...|...|
