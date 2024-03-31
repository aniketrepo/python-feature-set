### `POWER(X,Y);` - Calculates X to the power Y
```
use carshowroom;
select * POWER(2,5);	### calculates 2 to the power 5
```

### `ROUND(N,D);` - Rounds off number N to D number of decimal places
```
use carshowroom;
select * ROUND(1912.564, 1);	### Rounds off 1912.564 to 1 decimal place
select ROUND(12/100*Price, 1) 'GST' from inventory;	
```

### `MOD(A,B);` - Divides number A by B and returns the remainder
```
use carshowroom;
select MOD(15,2);	### Divides 15 by 2 and returns the remainder
```

### `UCASE('string');` or UPPER('string'); - Converts string into uppercase
```
use carshowroom;
select UCASE('example');
select UPPER('example');
select UPPER(CustName), UPPER(Email) from customer;
```

### `LOWER('string'); or LCASE('string');` - Converts string into lowercase
```
use carshowroom
select LOWER('example');
select LCASE('example');
select LOWER(CustName), LOWER(Email) from customer;
```

### `MID('string', pos, n); or SUBSTRING('string', pos, n); or SUBSTR('string', pos, n);` - Returns a substring of size 'n' starting from the specified position 'pos' of the 'string'
```
use carshowroom
select MID('example', 2, 3);
select SUBSTRING('example', 2, 3);
select SUBSTR('example', 2, 3);
```

### `LENGTH('string');` - Returns the number of specified characters in the given string
```
use carshowroom
select LENGTH('example');
select LENGTH(Email) from customer;
```

### `LEFT('string', n);` - Returns 'n' number of characters from the left side of the given string
```
use carshowroom
select LEFT('example', 2);
select LEFT(Email, instr(Email, '@')-1) from customer;
```

### `RIGHT('string', n);` - Returns 'n' number of characters from the right side of the given string
```
use carshowroom
select RIGHT('example', 2);
```

### `INSTR('string', 'substring');` - Returns the position of the first occurence of the substring in the string
```
use carshowroom
select INSTR('example', 'pl');
select INSTR(Email, '@') from customer;
```

### `LTRIM('string');` - Returns the string after removing the leading white space characters 
```
use carshowroom
select LTRIM('    example');
```

### `RTRIM('string');` - Returns the string after removing the trailing white space characters
```
use carshowroom
select RTRIM('example    ');
```

### `TRIM('string');` - Returns the string after removing the leading and the trailing white space characters
```
use carshowroom
select TRIM('	example		');
select TRIM('.com' from Email) from customer;
```

### `NOW();` - It returns the current system date and time
```
use carshowroom;
select NOW();
```

### `DATE();` - It returns the date part from the date/time expression
```
use carshowroom;
select DATE(NOW());
```

### `MONTH(date);` - It returns the month in numeric form of the date
```
use carshowroom;
select MONTH('2005-09-16');
select MONTH(DOJ) from employee;
```

### `MONTHNAME(date);` - It returns the month name from the specified date
```
use carshowroom;
select MONTHNAME('2005-09-16');
```

### `YEAR(date);` - It returns the year from the date
```
use carshowroom;
select YEAR('2005-09-16');
```

### `DAY(date);` - It returns the day part from the date
```
use carshowroom;
select DAY('2005-09-16');
```

### `DAYNAME(date);` - It returns the name of the day from the date
```
use carshowroom;
select DAYNAME('2005-09-16');
select DAYNAME(DOJ) from employee;
```

### `MAX(column);` - Returns the largest value from the specified column
```
use carshowroom;
select MAX(Price) from inventory;
```

### `MIN(column);` - Returns the smallest value from the specified column
```
use carshowroom;
select MIN(Price) from inventory;
```

### `AVG(column);` - Returns the average of the values in the specified column
```
use carshowroom;
select AVG(Price) from inventory;
```

### `SUM(column);` - Returns the sum of the values in the specified column
```
use carshowroom;
select SUM(Price) from inventory;
```

### `COUNT(column);` - Returns the number of values in a column IGNORING THE NULL VALUES
```
use carshowroom;
select COUNT(Price) from inventory;
```

### `COUNT(*);` - Returns the number of records IN A TABLE
```
use carshowroom;
select COUNT(*);
```

### GROUP BY- 
* It groups the rows together that contain the same values in a specified column
```
use CARSHOWROOM;
select CustID, count(*) 'Number of Cars' from sale group by CustID;		### to display the number of cars purchased by each customer from the sale table
select CustID, count(*) from sale group by CustID having count(*)>1;  	### to display the customer id and the number of cars purchased if the customer purchased more than 1 car from the table sale
select PaymentMode, count(PaymentMode) from sale group by PaymentMode order by PaymentMode;		### to display the number of people in each category of payment mode from the table sale
select PaymentMode, count(PaymentMode) from sale group by PaymentMode having count(*)>1 order by PaymentMode; 	### to display the payment mode and the number of payments made using that mode more than once
```

### UNION-
* It is used to combine the selected rows of two tables at a time. If some rows are same in both the tables, then it will print them only once.
```
use school;
select * from dance union select * from music;	### to apply union between two tables dance and music
```

### INTERSECT- 
* t is used to obtain the common tuples from two tables
```
use school;
select * from dance intersect select * from music;	### to apply an intersect between two tables dance and music
```

### MINUS-
* It is used to obtain the tuples/rows which are in the first table and not in the second
```
use school;
select * from dance minus select * from music;
```

### Cartesian Product-
* It is a result of combining every row from one table with every row from another table
```
use school;
select * from dance, music;	### to apply cartesian product between two tables dance and music
```

### JOIN-
* It is an operation which is used to combine rows from two or more tables based on one or more common fields between them
```
use school;