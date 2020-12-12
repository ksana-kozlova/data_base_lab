-- FUNCTION: public.create_tables()

-- DROP FUNCTION public.create_tables();

CREATE TABLE IF NOT EXISTS sub_lines(line_id numeric(1) PRIMARY KEY,
					  title text NOT NULL,
					  tr_amount int NOT NULL DEFAULT 0);


CREATE TABLE IF NOT EXISTS drivers(driver_id numeric(3) PRIMARY KEY,
					 second_name text NOT NULL,
					 age int NOT NULL,
					 experience int NOT NULL);

CREATE TABLE IF NOT EXISTS trains(train_id numeric(3) PRIMARY KEY,
				   title text NOT NULL,
				   line_id numeric(1) NOT NULL,
					driver_id numeric(3) NOT NULL,
				   FOREIGN KEY (line_id) REFERENCES sub_lines (line_id)
					 ON DELETE CASCADE
					 ON UPDATE CASCADE,
				   FOREIGN KEY (driver_id) REFERENCES drivers (driver_id)
					 ON DELETE CASCADE
					 ON UPDATE CASCADE
				   );

CREATE OR REPLACE FUNCTION show_drivers() 
RETURNS TABLE(driver_id numeric(3), second_name text, age integer, experience integer) 
AS $$
BEGIN
	SELECT * FROM drivers;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION show_trains() 
RETURNS TABLE(train_id numeric(3),
			  title text,
		   	  line_id numeric(1),
			  driver_id numeric(3)) 
AS $$
BEGIN
	SELECT * FROM trains;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION show_lines() 
RETURNS TABLE(line_id numeric(1),
			  title text,
			  tr_amount int) 
AS $$
BEGIN
	SELECT * FROM sub_lines;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION add_driver(_id numeric(3), _name text, _age integer, _exp integer) 
RETURNS void 
AS $$
BEGIN
	INSERT INTO driver VALUES(_id, _name, _age, _exp);
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION add_train(_id numeric(3), _title text, _line numeric(1), _driver numeric(3)) 
RETURNS void 
AS $$
BEGIN
	INSERT INTO trains VALUES(_id, _title, _line, _driver);
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION add_line(_id numeric(1), _title text, _trains integer) 
RETURNS void 
AS $$
BEGIN
	INSERT INTO sub_lines VALUES(_id, _title, _trains);
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION find_drivers(_sname text) 
RETURNS TABLE(driver_id numeric(3),
			  second_name text,
			  age integer,
			  experience integer) 
AS $$
BEGIN
	SELECT driver_id, second_name, age, experience
	FROM drivers
	WHERE driver.second_name = _sname;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION find_trains(_title text) 
RETURNS TABLE(train_id numeric(3),
			  title text,
		   	  line_id numeric(1),
			  driver_id numeric(3)) 
AS $$
BEGIN
	SELECT train_id, title, l.title ,d.second_name
	FROM trains tr
	LEFT JOIN sub_lines l
		ON tr.line_id = l.line_id
	LEFT JOIN drivers d
		ON tr.driver_id = d.driver_id
	WHERE tr.title = _title;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION find_lines(_title text) 
RETURNS TABLE(line_id numeric(1),
			  title text,
			  tr_amount int) 
AS $$
BEGIN
	SELECT line_id, title, tr_amount
	FROM sub_lines
	WHERE title = _title;
END;
$$ LANGUAGE 'plpgsql';


select * from sub_lines;
