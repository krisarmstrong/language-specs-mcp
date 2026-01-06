Table of contents Exit editor modeAsk LearnAsk LearnFocus modeTable of contents[Read in English](#)AddAdd to plan[Edit](https://github.com/MicrosoftDocs/sql-docs/blob/live/docs/t-sql/functions/functions.md)

#### Share via

[Facebook](#)[x.com](#)[LinkedIn](#)[Email](#)Print

Note

 Access to this page requires authorization. You can try [signing in](#) or changing directories. 

 Access to this page requires authorization. You can try changing directories. 

# What are the SQL database functions?

Feedback Summarize this article for me 

##  In this article 

Applies to:[SQL Server](../../sql-server/sql-docs-navigation-guide?view=sql-server-ver16#applies-to)[Azure SQL Database](../../sql-server/sql-docs-navigation-guide?view=sql-server-ver16#applies-to)[Azure SQL Managed Instance](../../sql-server/sql-docs-navigation-guide?view=sql-server-ver16#applies-to)[Azure Synapse Analytics](../../sql-server/sql-docs-navigation-guide?view=sql-server-ver16#applies-to)[Analytics Platform System (PDW)](../../sql-server/sql-docs-navigation-guide?view=sql-server-ver16#applies-to)[SQL analytics endpoint in Microsoft Fabric](../../sql-server/sql-docs-navigation-guide?view=sql-server-ver16#applies-to)[Warehouse in Microsoft Fabric](../../sql-server/sql-docs-navigation-guide?view=sql-server-ver16#applies-to)[SQL database in Microsoft Fabric](../../sql-server/sql-docs-navigation-guide?view=sql-server-ver16#applies-to)

Learn about the categories of built-in functions you can use with SQL databases. You can use the built-in functions or create your own user-defined functions.

## Aggregate functions

Aggregate functions perform a calculation on a set of values and return a single value. They're allowed in the select list or the `HAVING` clause of a `SELECT` statement. You can use an aggregation in combination with the `GROUP BY` clause to calculate the aggregation on categories of rows. Use the `OVER` clause to calculate the aggregation on a specific range of value. The `OVER` clause can't follow the `GROUPING` or `GROUPING_ID` aggregations.

All aggregate functions are deterministic, which means they always return the same value when they run on the same input values. For more information, see [Deterministic and nondeterministic functions](../../relational-databases/user-defined-functions/deterministic-and-nondeterministic-functions?view=sql-server-ver16).

## Analytic functions

Analytic functions compute an aggregate value based on a group of rows. However, unlike aggregate functions, analytic functions can return multiple rows for each group. You can use analytic functions to compute moving averages, running totals, percentages, or top-N results within a group.

## Bit manipulation functions

Applies to: SQL Server 2022 (16.x) and later versions, Azure SQL Managed Instance, Azure SQL Database, SQL database in Microsoft Fabric

Bit manipulation functions allow you to process and store data more efficiently than with individual bits. For more information, see [Bit manipulation functions](bit-manipulation-functions-overview?view=sql-server-ver16).

## Ranking functions

Ranking functions return a ranking value for each row in a partition. Depending on the function that is used, some rows might receive the same value as other rows. Ranking functions are nondeterministic.

## Rowset functions

Rowset functions Return an object that can be used like table references in a SQL statement.

## Scalar functions

Operate on a single value and then return a single value. Scalar functions can be used wherever an expression is valid.

### Categories of scalar functions

Function categoryDescription[Configuration Functions](configuration-functions-transact-sql?view=sql-server-ver16)Return information about the current configuration.[Conversion Functions](conversion-functions-transact-sql?view=sql-server-ver16)Support data type casting and converting.[Cursor Functions](cursor-functions-transact-sql?view=sql-server-ver16)Return information about cursors.[Date and Time Data Types and Functions](date-and-time-data-types-and-functions-transact-sql?view=sql-server-ver16)Perform operations on a date and time input values and return string, numeric, or date and time values.[Graph Functions](graph-functions-transact-sql?view=sql-server-ver16)Perform operations to convert to and from character representations of graph node and edge IDs.[JSON Functions](json-functions-transact-sql?view=sql-server-ver16)Validate, query, or change JSON data.[Logical Functions](logical-functions-choose-transact-sql?view=sql-server-ver16)Perform logical operations.[Mathematical Functions](mathematical-functions-transact-sql?view=sql-server-ver16)Perform calculations based on input values provided as parameters to the functions, and return numeric values.[Metadata Functions](metadata-functions-transact-sql?view=sql-server-ver16)Return information about the database and database objects.[Security Functions](security-functions-transact-sql?view=sql-server-ver16)Return information about users and roles.[String Functions](string-functions-transact-sql?view=sql-server-ver16)Perform operations on a string (char or varchar) input value and return a string or numeric value.[System Functions](../../relational-databases/system-functions/system-functions-category-transact-sql?view=sql-server-ver16)Perform operations and return information about values, objects, and settings in an instance of SQL Server.[System Statistical Functions](system-statistical-functions-transact-sql?view=sql-server-ver16)Return statistical information about the system.[Text and Image Functions](text-and-image-functions-textptr-transact-sql?view=sql-server-ver16)Perform operations on text or image input values or columns, and return information about the value.

## Function determinism

SQL Server built-in functions are either deterministic or nondeterministic. Functions are deterministic when they always return the same result anytime they're called by using a specific set of input values. Functions are nondeterministic when they could return different results every time they're called, even with the same specific set of input values. For more information, see [Deterministic and nondeterministic functions](../../relational-databases/user-defined-functions/deterministic-and-nondeterministic-functions?view=sql-server-ver16)

## Function collation

Functions that take a character string input and return a character string output use the collation of the input string for the output.

Functions that take non-character inputs and return a character string use the default collation of the current database for the output.

Functions that take multiple character string inputs and return a character string use the rules of collation precedence to set the collation of the output string. For more information, see [Collation precedence](../statements/collation-precedence-transact-sql?view=sql-server-ver16).

## Limitations

For information on limitations of function types and platforms, see [CREATE FUNCTION (Transact-SQL)](../statements/create-function-transact-sql?view=sql-server-ver16).

## Related content

- [CREATE FUNCTION (Transact-SQL)](../statements/create-function-transact-sql?view=sql-server-ver16)
- [Deterministic and nondeterministic functions](../../relational-databases/user-defined-functions/deterministic-and-nondeterministic-functions?view=sql-server-ver16)

## Feedback

 Was this page helpful? 

YesNoNo

 Need help with this topic? 

 Want to try using Ask Learn to clarify or guide you through this topic? 

Ask LearnAsk Learn Suggest a fix? 

##  Additional resources 

- Last updated on  2025-11-18
