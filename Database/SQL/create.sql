-- To to select all the fields in a Table named "table_name"
SELECT * FROM table_name;
-- To select specific columns  from a table_name
SELECT column_name_1, column_name_2 FROM table_name;

-- To to select distinct values in a columns in a table in a db
SELECT DISTINCT column_name  FROM table_name;
-- To to return the count of values use
SELECT COUNT(DISTINCT column_name) FROM table_name;
-- To assign variable to returns
SELECT COUNT(*) AS Number_of_value FROM (SELECT DISTINCT column_name FROM table_name);
-- Setting condition on queries
SELECT * FROM table_name WHERE Country="Mexico";