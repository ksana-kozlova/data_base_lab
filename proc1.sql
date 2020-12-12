CREATE OR REPLACE FUNCTION public.create_database(
	)
    RETURNS void
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE 
    
AS $BODY$
BEGIN
        IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'lab') THEN
            PERFORM dblink_exec(
                'dbname=postgres user=postgres password=123',
                'create database lab with owner postgres'
          );
        END IF;
    END;
$BODY$;
