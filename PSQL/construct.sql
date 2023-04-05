-- SCHEMA: projeto_nome

-- DROP SCHEMA IF EXISTS projeto_nome ;

CREATE SCHEMA IF NOT EXISTS projeto_nome
    AUTHORIZATION chicago;

COMMENT ON SCHEMA projeto_nome
    IS 'Projeto da #localização#, gerido por #gestor#';

-- GROUP ROLE (cannot login)
CREATE ROLE group_role WITH
	NOLOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;
GRANT CONNECT ON DATABASE db_name TO group_role;
GRANT USAGE ON SCHEMA projet_nome_schema TO group_role;
GRANT SELECT ON ALL TABLES IN SCHEMA projet_nome_schema TO group_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA projet_nome_schema
GRANT SELECT ON TABLES TO group_role;

-- Read-only role
CREATE ROLE app_readonly;
GRANT CONNECT ON DATABASE db_name TO app_readonly;
GRANT USAGE ON SCHEMA projet_nome_schema TO app_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA projet_nome_schema TO app_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA projet_nome_schema GRANT SELECT ON TABLES TO app_readonly;

-- Read/write role
CREATE ROLE readwrite;
GRANT CONNECT ON DATABASE db_name TO readwrite;
GRANT USAGE, CREATE ON SCHEMA projet_nome_schema TO readwrite;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA projet_nome_schema TO readwrite;
ALTER DEFAULT PRIVILEGES IN SCHEMA projet_nome_schema GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO readwrite;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA projet_nome_schema TO readwrite;
ALTER DEFAULT PRIVILEGES IN SCHEMA projet_nome_schema GRANT USAGE ON SEQUENCES TO readwrite;


-- USER (can login)
/*
-- Users creation
CREATE USER appreporting_userl WITH PASSWORD 'some_password' ;
CREATE USER WITH PASSWORD 'some_password' ;
CREATE USER app_userl WITH PASSWORD 'some_password' ;
CREATE USER app_user2 WITH PASSWORD 'some_password' ;
*/
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
