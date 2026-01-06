# MySQL SQL Statements

Reference for MySQL 8.0 SQL statement syntax.

## Data Definition Statements (DDL)

### CREATE Statements
```sql
CREATE DATABASE [IF NOT EXISTS] db_name
    [CHARACTER SET charset_name]
    [COLLATE collation_name];

CREATE TABLE [IF NOT EXISTS] tbl_name (
    col_name data_type [NOT NULL | NULL] [DEFAULT value]
        [AUTO_INCREMENT] [PRIMARY KEY] [COMMENT 'string'],
    ...
    [PRIMARY KEY (col_name, ...)],
    [INDEX idx_name (col_name, ...)],
    [FOREIGN KEY (col_name) REFERENCES tbl_name (col_name)]
) [ENGINE=InnoDB] [DEFAULT CHARSET=utf8mb4];

CREATE INDEX idx_name ON tbl_name (col_name [ASC | DESC], ...);

CREATE VIEW view_name AS select_statement;

CREATE PROCEDURE proc_name ([param_list])
BEGIN
    -- statements
END;

CREATE FUNCTION func_name ([param_list]) RETURNS type
BEGIN
    -- statements
    RETURN value;
END;

CREATE TRIGGER trigger_name
    {BEFORE | AFTER} {INSERT | UPDATE | DELETE}
    ON tbl_name FOR EACH ROW
BEGIN
    -- statements
END;

CREATE EVENT event_name
    ON SCHEDULE {AT timestamp | EVERY interval}
    DO statement;
```

### ALTER Statements
```sql
ALTER DATABASE db_name
    [CHARACTER SET charset_name]
    [COLLATE collation_name];

ALTER TABLE tbl_name
    ADD [COLUMN] col_name data_type [FIRST | AFTER col_name],
    ADD INDEX idx_name (col_name),
    ADD PRIMARY KEY (col_name),
    ADD FOREIGN KEY (col_name) REFERENCES tbl (col),
    DROP [COLUMN] col_name,
    DROP INDEX idx_name,
    DROP PRIMARY KEY,
    DROP FOREIGN KEY fk_symbol,
    MODIFY [COLUMN] col_name data_type,
    CHANGE [COLUMN] old_name new_name data_type,
    RENAME TO new_tbl_name,
    ENGINE = engine_name,
    AUTO_INCREMENT = value;
```

### DROP Statements
```sql
DROP DATABASE [IF EXISTS] db_name;
DROP TABLE [IF EXISTS] tbl_name [, tbl_name] ...;
DROP INDEX idx_name ON tbl_name;
DROP VIEW [IF EXISTS] view_name;
DROP PROCEDURE [IF EXISTS] proc_name;
DROP FUNCTION [IF EXISTS] func_name;
DROP TRIGGER [IF EXISTS] trigger_name;
DROP EVENT [IF EXISTS] event_name;
```

### Other DDL
```sql
TRUNCATE [TABLE] tbl_name;
RENAME TABLE tbl_name TO new_tbl_name [, tbl_name2 TO new_name2] ...;
```

## Data Manipulation Statements (DML)

### SELECT
```sql
SELECT [ALL | DISTINCT]
    select_expr [, select_expr] ...
    [FROM table_references]
    [WHERE where_condition]
    [GROUP BY {col_name | expr} [ASC | DESC], ...]
    [HAVING where_condition]
    [ORDER BY {col_name | expr} [ASC | DESC], ...]
    [LIMIT {[offset,] row_count | row_count OFFSET offset}]
    [FOR UPDATE | FOR SHARE];

-- Common Table Expressions (CTE)
WITH cte_name [(col_name, ...)] AS (
    SELECT ...
)
SELECT * FROM cte_name;

-- Recursive CTE
WITH RECURSIVE cte_name AS (
    SELECT ...  -- anchor
    UNION ALL
    SELECT ... FROM cte_name WHERE ...  -- recursive
)
SELECT * FROM cte_name;
```

### JOIN Types
```sql
SELECT * FROM t1
    INNER JOIN t2 ON t1.id = t2.id
    LEFT [OUTER] JOIN t3 ON t2.id = t3.id
    RIGHT [OUTER] JOIN t4 ON t3.id = t4.id
    CROSS JOIN t5
    NATURAL JOIN t6;
```

### INSERT
```sql
INSERT [INTO] tbl_name [(col_name, ...)]
    VALUES (value, ...), (value, ...), ...;

INSERT [INTO] tbl_name [(col_name, ...)]
    SELECT ...;

INSERT [INTO] tbl_name [(col_name, ...)]
    VALUES (value, ...)
    ON DUPLICATE KEY UPDATE col_name = value, ...;

REPLACE [INTO] tbl_name [(col_name, ...)]
    VALUES (value, ...);
```

### UPDATE
```sql
UPDATE tbl_name
    SET col_name = value [, col_name = value] ...
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count];

-- Multi-table UPDATE
UPDATE t1, t2
    SET t1.col = value, t2.col = value
    WHERE t1.id = t2.id;
```

### DELETE
```sql
DELETE FROM tbl_name
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count];

-- Multi-table DELETE
DELETE t1, t2 FROM t1
    INNER JOIN t2 ON t1.id = t2.id
    WHERE condition;
```

### Set Operations
```sql
SELECT ... UNION [ALL | DISTINCT] SELECT ...;
SELECT ... INTERSECT [ALL | DISTINCT] SELECT ...;
SELECT ... EXCEPT [ALL | DISTINCT] SELECT ...;
```

## Transaction Statements

```sql
START TRANSACTION [READ ONLY | READ WRITE];
BEGIN [WORK];
COMMIT [WORK];
ROLLBACK [WORK];

SAVEPOINT savepoint_name;
ROLLBACK TO [SAVEPOINT] savepoint_name;
RELEASE SAVEPOINT savepoint_name;

SET autocommit = {0 | 1};
SET TRANSACTION ISOLATION LEVEL
    {READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SERIALIZABLE};
```

## Locking Statements

```sql
LOCK TABLES tbl_name {READ | WRITE} [, tbl_name {READ | WRITE}] ...;
UNLOCK TABLES;

SELECT ... FOR UPDATE [NOWAIT | SKIP LOCKED];
SELECT ... FOR SHARE [NOWAIT | SKIP LOCKED];
```

## Prepared Statements

```sql
PREPARE stmt_name FROM 'SELECT * FROM t WHERE id = ?';
SET @id = 1;
EXECUTE stmt_name USING @id;
DEALLOCATE PREPARE stmt_name;
```

## Account Management

```sql
CREATE USER 'user'@'host' IDENTIFIED BY 'password';
ALTER USER 'user'@'host' IDENTIFIED BY 'new_password';
DROP USER 'user'@'host';

GRANT privilege_type ON db.tbl TO 'user'@'host';
GRANT ALL PRIVILEGES ON db.* TO 'user'@'host';
REVOKE privilege_type ON db.tbl FROM 'user'@'host';

SHOW GRANTS FOR 'user'@'host';
FLUSH PRIVILEGES;

CREATE ROLE 'role_name';
GRANT 'role_name' TO 'user'@'host';
SET DEFAULT ROLE 'role_name' TO 'user'@'host';
```

## Table Maintenance

```sql
ANALYZE TABLE tbl_name [, tbl_name] ...;
CHECK TABLE tbl_name [, tbl_name] ...;
CHECKSUM TABLE tbl_name [, tbl_name] ...;
OPTIMIZE TABLE tbl_name [, tbl_name] ...;
REPAIR TABLE tbl_name [, tbl_name] ...;
```

## SHOW Statements

```sql
SHOW DATABASES [LIKE 'pattern'];
SHOW TABLES [FROM db_name] [LIKE 'pattern'];
SHOW COLUMNS FROM tbl_name [FROM db_name];
SHOW CREATE TABLE tbl_name;
SHOW CREATE DATABASE db_name;
SHOW INDEX FROM tbl_name;
SHOW TABLE STATUS [FROM db_name];

SHOW PROCESSLIST;
SHOW FULL PROCESSLIST;
SHOW STATUS [LIKE 'pattern'];
SHOW VARIABLES [LIKE 'pattern'];
SHOW WARNINGS;
SHOW ERRORS;
SHOW GRANTS [FOR user];
SHOW ENGINE engine_name STATUS;
SHOW ENGINES;
SHOW PLUGINS;
```

## Utility Statements

```sql
DESCRIBE tbl_name;
DESC tbl_name;
EXPLAIN [FORMAT = {TRADITIONAL | JSON | TREE}] SELECT ...;
EXPLAIN ANALYZE SELECT ...;

USE db_name;
HELP 'search_string';

SET @var_name = value;
SET SESSION var_name = value;
SET GLOBAL var_name = value;
```

## Compound Statements (Stored Programs)

```sql
-- Variables
DECLARE var_name [, var_name] ... type [DEFAULT value];
SET var_name = expr;

-- Conditionals
IF condition THEN
    statements;
ELSEIF condition THEN
    statements;
ELSE
    statements;
END IF;

CASE case_value
    WHEN when_value THEN statements;
    WHEN when_value THEN statements;
    ELSE statements;
END CASE;

-- Loops
WHILE condition DO
    statements;
END WHILE;

REPEAT
    statements;
UNTIL condition
END REPEAT;

[label:] LOOP
    statements;
    LEAVE label;
    ITERATE label;
END LOOP [label];

-- Cursors
DECLARE cursor_name CURSOR FOR select_statement;
OPEN cursor_name;
FETCH cursor_name INTO var_name [, var_name] ...;
CLOSE cursor_name;

-- Handlers
DECLARE {CONTINUE | EXIT} HANDLER FOR condition_value statement;
```

See: https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html
