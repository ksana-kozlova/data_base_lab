funcs = """
CREATE TABLE IF NOT EXISTS sub_lines(line_id numeric(1) PRIMARY KEY,
									 title text NOT NULL,
									 tr_amount int NOT NULL DEFAULT 0,
									 UNIQUE(title));

CREATE TABLE IF NOT EXISTS drivers(driver_id numeric(3) PRIMARY KEY,
								   second_name text NOT NULL,
								   age int NOT NULL,
								   experience int NOT NULL,
								   UNIQUE(second_name, age));

CREATE INDEX IF NOT EXISTS driver_name ON drivers(second_name);

CREATE TABLE IF NOT EXISTS trains(train_id numeric(3) PRIMARY KEY,
								   title text NOT NULL,
								   line_id numeric(1) NOT NULL,
									driver_id numeric(3) NOT NULL,
								   FOREIGN KEY (line_id) REFERENCES sub_lines (line_id)
									 ON DELETE CASCADE
									 ON UPDATE CASCADE,
								   FOREIGN KEY (driver_id) REFERENCES drivers (driver_id)
									 ON DELETE CASCADE
									 ON UPDATE CASCADE,
								  UNIQUE (title, line_id)								  
				   );
				   
CREATE INDEX IF NOT EXISTS train_title ON trains(title);

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
	INSERT INTO drivers VALUES(_id, _name, _age, _exp);
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

CREATE OR REPLACE FUNCTION cnt_trains()
RETURNS trigger AS
$$
DECLARE delta sub_lines.tr_amount%TYPE;
		_line trains.line_id%TYPE;
BEGIN
	IF TG_OP = 'INSERT' THEN
		delta = 1;
		_line = NEW.line_id;
	ELSIF TG_OP = 'DELETE' THEN
		delta = -1;
		_line = OLD.line_id;
	END IF;
	UPDATE sub_lines l 
	SET tr_amount = tr_amount + delta
	WHERE _line = l.line_id;
	RETURN NULL;
END;
$$ LANGUAGE plpgsql;
	
DROP TRIGGER IF EXISTS cnt_trains ON trains;

CREATE TRIGGER cnt_trains
AFTER INSERT OR DELETE ON trains
FOR EACH ROW EXECUTE PROCEDURE cnt_trains();


CREATE OR REPLACE FUNCTION delete_drivers_by_name(_sname text) 
RETURNS void
AS $$
BEGIN
	DELETE
	FROM drivers
	WHERE drivers.second_name = _sname;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION delete_trains_by_title(_title text) 
RETURNS void 
AS $$
BEGIN
	DELETE
	FROM trains tr
	WHERE tr.title = _title;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION delete_lines_by_title(_title text) 
RETURNS void 
AS $$
BEGIN
	DELETE
	FROM sub_lines
	WHERE title = _title;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION delete_driver(_sname text, _age integer) 
RETURNS void
AS $$
BEGIN
	DELETE
	FROM drivers
	WHERE drivers.second_name = _sname
	AND drivers.age = _age;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION delete_train(_title text, _line numeric(1)) 
RETURNS void 
AS $$
BEGIN
	DELETE
	FROM trains tr
	WHERE tr.title = _title
	AND tr.line_id = _line;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION clear_trains() 
RETURNS void 
AS $$
BEGIN
	DELETE
	FROM trains;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION clear_drivers() 
RETURNS void 
AS $$
BEGIN
	DELETE
	FROM drivers;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION clear_lines() 
RETURNS void 
AS $$
BEGIN
	DELETE
	FROM sub_lines;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION update_drivers(_oldname text, _oldage integer,
										 _sname text, _age integer, 
										  _exp integer) 
RETURNS void
AS $$
BEGIN
	UPDATE drivers
	SET second_name = _sname, age = _age, experience = _exp
	WHERE drivers.second_name = _oldname
	AND drivers.age = _oldage;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION update_trains(_oldtitle text, _oldline text,
										_title text,
										 _line text,
										_driver text,
										 _age integer) 
RETURNS void 
AS $$
DECLARE new_line trains.line_id%TYPE;
		new_driver trains.driver_id%TYPE;
BEGIN
	new_line = (SELECT line_id FROM sub_lines
			  WHERE sub_lines.title = _oldline);
	new_driver = (SELECT driver_id FROM drivers
				 WHERE drivers.second_name = _driver
				 AND drivers.age = _age);
	UPDATE trains
	SET title = _title, line_id = new_line, driver_id = new_driver
	WHERE trains.title = _title;
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION update_lines(_oldtitle text, _title text) 
RETURNS void
AS $$
BEGIN
	UPDATE sub_lines
	SET title = _title
	WHERE title = _oldtitle;
END;
$$ LANGUAGE 'plpgsql';

"""
