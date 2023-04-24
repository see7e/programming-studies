---
title: Create Users PSQL
tags: studies
use: Documentation
languages: SQL
dependences: PostgreSQL
---

## Como criar restrições de acesso de usuários a esquemas de banco de dados em postgresql
</br>

No PostgreSQL, é possível criar restrições de acesso de usuários a esquemas de banco de dados usando as permissões do sistema de autenticação e autorização do PostgreSQL. Existem dois tipos principais de permissões no PostgreSQL:

Permissões de objeto (objetos do banco de dados, como tabelas, esquemas, etc.)
Permissões de esquema (esquemas do banco de dados)
Para criar restrições de acesso de usuários a esquemas de banco de dados, você pode seguir estes passos:

Conceder acesso ao esquema para o usuário que precisa ter acesso:
> `sql`
```sql
GRANT USAGE ON SCHEMA schema_name TO user_name;
```

Revogar permissões de acesso ao esquema para os usuários que não precisam ter acesso:
> `sql`
```sql
REVOKE USAGE ON SCHEMA schema_name FROM user_name;
```

Verificar as permissões de acesso ao esquema:
> `sql`
```sql
\dn schema_name
```

Isso exibirá as permissões de acesso para o esquema especificado. Você pode ver quem tem acesso ao esquema e qual tipo de acesso foi concedido (por exemplo, USAGE, CREATE, etc.).

É importante lembrar que as permissões de acesso podem ser concedidas ou revogadas em diferentes níveis, incluindo esquemas, tabelas, funções e outros objetos do banco de dados. Por isso, é importante revisar todas as permissões concedidas para garantir a segurança do banco de dados.
</br> </br>

***
# Dentro do Linux (servidor)

## Como fazer a ligação a um banco de dados em postgres num servidor linux, usando como serviço de autenticação o LDAP para buscar na Active Directory as informações de usuários e senhas?

</br>

Para fazer a ligação a um banco de dados PostgreSQL em um servidor Linux usando o LDAP como serviço de autenticação, você precisa seguir os seguintes passos:

1.  Instale os pacotes necessários para autenticação LDAP no servidor Linux usando o gerenciador de pacotes do seu sistema operacional. Para Ubuntu/Debian, por exemplo, você pode usar o comando:

>`shell`
```sh
sudo apt-get install libpam-ldapd libnss-ldapd ldap-utils
```

2.  Configure o arquivo /etc/ldap.conf ou /etc/openldap/ldap.conf com as informações do seu servidor LDAP, incluindo o endereço do servidor, o nome do diretório, a base de busca e as credenciais de autenticação.

3.  Configure o arquivo /etc/nsswitch.conf para permitir que o sistema use o LDAP para procurar informações de usuários e grupos. Adicione ou modifique a linha "passwd" e "group" para incluir "ldap" no final.

>`makefile`
```makefile
passwd: compat ldap
group: compat ldap
```

4.  Configure o arquivo /etc/pam.d/postgresql para permitir que o PostgreSQL use o LDAP para autenticação. Adicione as seguintes linhas ao arquivo:

>`shell`
```sh
auth sufficient pam_ldap.so
account sufficient pam_ldap.so
```

5.  Reinicie o serviço do PostgreSQL para que as alterações no arquivo de configuração do PAM tenham efeito.

>`shell`
```sh
sudo systemctl restart postgresql
```
6.  Verifique se a autenticação está funcionando corretamente, tentando se conectar ao banco de dados com um usuário existente no LDAP. Por exemplo:

> `php`
```php
psql -h <endereço_do_servidor> -U <usuário_LDAP> -d <nome_do_banco>
```

Se tudo estiver configurado corretamente, você deverá conseguir se conectar ao banco de dados usando as credenciais do usuário LDAP.
</br>

## Como buscar dentro da active directory esses usuários para construir o banco de dados, fornecendo o devido acesso a certos group roles?

</br>

Para buscar usuários na Active Directory e conceder acesso a determinados grupos de funções (group roles) no PostgreSQL, você precisará seguir os seguintes passos:

1.  Configurar o LDAP no PostgreSQL:
Primeiro, é necessário configurar o PostgreSQL para usar o LDAP como serviço de autenticação, seguindo os passos descritos na resposta anterior.

2.  Criar um grupo de funções (group role) no PostgreSQL:

Você pode criar um grupo de funções no PostgreSQL usando o comando CREATE ROLE, que permite criar grupos de usuários com permissões específicas.

Por exemplo, para criar um grupo de funções chamado "usuarios_ativos" com permissão para ler e gravar em uma tabela específica no banco de dados, você pode executar o seguinte comando:

> `sql`
```sql
CREATE ROLE usuarios_ativos WITH LOGIN PASSWORD 'senha' IN ROLE base_de_dados;
GRANT USAGE, SELECT, INSERT, UPDATE ON tabela TO usuarios_ativos;
```

3.  Sincronizar usuários e grupos da Active Directory:

Para sincronizar os usuários e grupos da Active Directory com o PostgreSQL, você pode usar uma ferramenta de sincronização, como o LDAP2DB.

Essa ferramenta permite sincronizar os usuários e grupos da Active Directory com o PostgreSQL, criando automaticamente as contas de usuário e os grupos de funções no PostgreSQL com base nas informações da Active Directory.

4.  Conceder permissões de acesso aos usuários:
Depois que os usuários e grupos forem sincronizados, você poderá conceder permissões de acesso a tabelas específicas no banco de dados para cada grupo de funções.

Por exemplo, para conceder permissões de leitura e gravação na tabela "tabela" para o grupo de funções "usuarios_ativos", execute o seguinte comando:

> `sql`
```sql
GRANT USAGE, SELECT, INSERT, UPDATE ON tabela TO usuarios_ativos;
```
Dessa forma, os usuários da Active Directory que estiverem no grupo "usuarios_ativos" poderão ler e gravar na tabela "tabela" no PostgreSQL.

5.  Verificar o acesso dos usuários:
Para verificar se os usuários da Active Directory estão tendo acesso aos dados no PostgreSQL conforme o esperado, você pode fazer login com as credenciais do usuário e testar as permissões concedidas.

Por exemplo, se um usuário da Active Directory com credenciais válidas tentar ler ou gravar na tabela "tabela", o PostgreSQL deve permitir o acesso se as permissões de acesso foram concedidas corretamente.
</br>

## Configurar o serviço LDAP2DB dentro do servidor Linux
</br>

Para configurar o serviço LDAP2DB dentro do servidor Linux, você precisará seguir os seguintes passos:

1. Instalar o LDAP2DB:
Você pode instalar o LDAP2DB usando o gerenciador de pacotes do seu sistema operacional. Para Ubuntu/Debian, você pode usar o comando:

>`sh`
```sh
sudo apt-get install ldap2db
```
2.  Configurar o arquivo de configuração do LDAP2DB:
O arquivo de configuração do LDAP2DB é geralmente localizado em /etc/ldap2db.conf. Você precisará configurar as seguintes opções no arquivo de configuração:

- `ldap_uri`: O endereço do servidor LDAP.
- `ldap_search_base`: A base de pesquisa LDAP para encontrar usuários e grupos.
- `ldap_bind_dn`: O DN de autenticação LDAP para se conectar ao servidor.
- `ldap_bind_pw`: A senha para autenticar no servidor LDAP.
- `pg_host`: O endereço do servidor PostgreSQL.
- `pg_port`: A porta do servidor PostgreSQL.
- `pg_dbname`: O nome do banco de dados PostgreSQL.
- `pg_user`: O usuário com permissões suficientes no PostgreSQL.
- `pg_password`: A senha do usuário PostgreSQL.

Um exemplo de arquivo de configuração seria:

>`shell`
```sh
ldap_uri: ldap://localhost:389
ldap_search_base: ou=People,dc=example,dc=com
ldap_bind_dn: cn=admin,dc=example,dc=com
ldap_bind_pw: senha
pg_host: localhost
pg_port: 5432
pg_dbname: base_de_dados
pg_user: postgres
pg_password: senha
```

3.  Executar o comando ldap2db:

Depois de configurar o arquivo de configuração, você pode executar o comando ldap2db para sincronizar os usuários e grupos da Active Directory com o PostgreSQL:

>`shell`
```sh
sudo ldap2db -c /etc/ldap2db.conf
```

Este comando irá criar automaticamente as contas de usuário e os grupos de funções no PostgreSQL com base nas informações da Active Directory.

4.  Verificar a sincronização:

Você pode verificar a sincronização dos usuários e grupos da Active Directory com o PostgreSQL executando consultas SQL no PostgreSQL para verificar se os usuários e grupos foram criados com sucesso.

Por exemplo, para verificar se o grupo de funções "usuarios_ativos" foi criado, execute o seguinte comando SQL no PostgreSQL:

>`sql`
```sql
SELECT * FROM pg_roles WHERE rolname='usuarios_ativos';
```
Se a consulta retornar um registro, isso indica que o grupo de funções foi criado com sucesso.

Dessa forma, você pode configurar o serviço LDAP2DB no servidor Linux para sincronizar os usuários e grupos da Active Directory com o PostgreSQL.
</br> </br>

***
# Dentro do Windows

## Há alguma forma de criar usuários em sequência, com essas definições através da Active Directory do windows?
</br>

Sim, é possível criar usuários em sequência com essas definições através da Active Directory do Windows usando um script ou ferramenta de automação.

Uma opção é usar o PowerShell, que é uma ferramenta de linha de comando e script do Windows. Com o PowerShell, você pode criar scripts para criar usuários em sequência e definir permissões e outros atributos de conta.

Aqui está um exemplo básico de script do PowerShell para criar usuários em sequência:

> `powershell`
```Ps
$users = Get-Content C:\users.txt
$OU = "OU=Users,OU=MyCompany,DC=mydomain,DC=com"

foreach ($user in $users) {
    $password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
    New-ADUser -Name $user -AccountPassword $password -Enabled $True -Path $OU -PasswordNeverExpires $True
}
```

Nesse exemplo, o script lê os nomes dos usuários de um arquivo de texto e cria cada usuário em sequência usando o cmdlet New-ADUser do PowerShell. O script define a senha do usuário como "P@ssw0rd", habilita a conta de usuário, define a pasta do usuário no Active Directory e configura a senha para nunca expirar.

Você precisará adaptar esse script para suas necessidades específicas, incluindo os atributos de conta que deseja definir e o caminho da unidade organizacional (OU) em que deseja criar os usuários.

Além do PowerShell, existem outras ferramentas de automação que podem ser usadas para criar usuários em sequência na Active Directory, como o script VBScript e outras ferramentas de automação de terceiros.
</br> </br>

## Como conectar esse processo com o postgresql?
</br>

Para conectar o processo de criação de usuários na Active Directory com o PostgreSQL, você pode usar a autenticação do Windows no PostgreSQL. Com a autenticação do Windows, você pode configurar o PostgreSQL para permitir que os usuários se conectem usando suas contas do Windows, em vez de usar uma conta de usuário e senha do PostgreSQL.

Para fazer isso, siga estes passos:

1.  Configure o PostgreSQL para usar a autenticação do Windows. Isso envolve editar o arquivo pg_hba.conf do PostgreSQL para permitir conexões usando a autenticação do Windows. Por exemplo, você pode adicionar a seguinte linha ao arquivo pg_hba.conf para permitir conexões de todos os usuários autenticados do Windows:

> `.conf`
```Ps
host    all         all         0.0.0.0/0         sspi    map=postgres
```
Essa linha permite que qualquer usuário autenticado do Windows se conecte a qualquer banco de dados usando a autenticação do Windows.

2.  Configure o mapeamento do usuário PostgreSQL para a conta do Windows. Você pode criar um mapeamento entre as contas de usuário do PostgreSQL e as contas de usuário do Windows usando o arquivo pg_ident.conf do PostgreSQL. Por exemplo, você pode adicionar uma linha como esta:

> `.conf`
```Ps
postgres        mydomain\pgadmin
```

Essa linha mapeia o usuário "postgres" do PostgreSQL para a conta "mydomain\pgadmin" do Windows.

3.  Crie um usuário do PostgreSQL para cada usuário da Active Directory que precise acessar o banco de dados. Você pode criar usuários do PostgreSQL correspondentes às contas de usuário do Windows que deseja permitir acesso ao banco de dados. Por exemplo, você pode criar um usuário do PostgreSQL com o mesmo nome de usuário que o nome da conta da Active Directory.

> `sql`
```sql
CREATE USER mydomain\pgadmin;
```
Essa linha cria um usuário do PostgreSQL chamado "mydomain\pgadmin" que corresponde à conta de usuário do Windows "mydomain\pgadmin".

4.  Conceda permissões aos usuários do PostgreSQL. Você precisará conceder as permissões necessárias aos usuários do PostgreSQL para acessar os objetos do banco de dados que precisam acessar. Por exemplo, você pode conceder permissões de leitura e gravação a uma tabela específica usando a seguinte linha:

> `sql`
```sql
GRANT SELECT, INSERT, UPDATE ON my_table TO mydomain\pgadmin;
```
Essa linha concede permissões de leitura e gravação à tabela "my_table" para o usuário do PostgreSQL "mydomain\pgadmin".

Dessa forma, você pode conectar o processo de criação de usuários na Active Directory com o PostgreSQL, permitindo que os usuários se conectem ao banco de dados usando suas contas do Windows e concedendo as permissões necessárias aos usuários do PostgreSQL para acessar os objetos do banco de dados.

</br>

---

</br>

### Sugestão de formatação

Analizar [código](construct.sql) de acordo com a demanda e a resposta acima.
</br> </br>

## Criar lista de usuários a partir de planilha Excel
</br>

> `sql`
```sql
CREATE ROLE nome_pessoa WITH
	LOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD '######';

GRANT group_role TO nome_pessoa;
```
É possível executar esse trecho de código usando os valores de "nome_pessoa" e "password" a partir de um arquivo Excel. Você precisará usar uma linguagem de programação ou uma ferramenta de automação para ler os dados do arquivo Excel e executar o código SQL no PostgreSQL.

Por exemplo, se você estiver usando Python, pode usar a biblioteca pandas para ler os dados do arquivo Excel e a biblioteca psycopg2 para se conectar ao PostgreSQL e executar o código SQL. O código Python pode ficar assim:

> `python`
```py
import pandas as pd
import psycopg2

# Leitura do arquivo Excel
df = pd.read_excel('arquivo_excel.xlsx')

# Conexão com o PostgreSQL
conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="myhost", port="myport")
cursor = conn.cursor()

# Loop para criar usuários e conceder permissões
for index, row in df.iterrows():
    nome_pessoa = row['nome_pessoa']
    password = row['password']

    # Criação do usuário
    sql_create_user = f"CREATE ROLE {nome_pessoa} WITH LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT -1 PASSWORD '{password}'"
    cursor.execute(sql_create_user)

    # Concessão de permissões
    sql_grant_permissions = f"GRANT group_role TO {nome_pessoa}"
    cursor.execute(sql_grant_permissions)

# Finalização
conn.commit()
cursor.close()
conn.close()
```

Nesse exemplo, o código Python lê os valores de "nome_pessoa" e "password" do arquivo Excel e, em seguida, executa o código SQL necessário para criar o usuário e conceder as permissões no PostgreSQL.

Lembre-se de que você precisará adaptar esse código para suas necessidades específicas, incluindo os nomes dos campos do arquivo Excel e os detalhes de conexão do PostgreSQL. Além disso, certifique-se de que o arquivo Excel esteja formatado corretamente e que os valores estejam válidos para evitar erros durante a execução do código.