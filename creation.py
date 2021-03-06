creat = """
CREATE EXTENSION IF NOT EXISTS dblink;
CREATE OR REPLACE FUNCTION create_database() RETURNS void
AS $$
BEGIN
        IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'subway') THEN
            PERFORM dblink_exec(
                'dbname=postgres user=postgres password=postgres',
                'create database subway with owner lab'
          );
        END IF;
    END;
$$ LANGUAGE 'plpgsql';

CREATE EXTENSION IF NOT EXISTS dblink;
CREATE OR REPLACE FUNCTION drop_database() RETURNS void
AS $$
BEGIN
		PERFORM dblink_exec(
			'dbname=postgres user=postgres password=postgres',
			'drop database if exists subway'
	  );
    END;
$$ LANGUAGE 'plpgsql';"""
