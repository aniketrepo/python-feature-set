
/* DDL script for creating the Library Management System Schema */
CREATE database db_lms;
 
/* Create a table to store the library users. This should work with a Python program to add the users data */
CREATE TABLE LIBRARY_USER(
    BORROWER_ID SERIAL PRIMARY KEY,
    UERNAME VARCHAR(50) NOT NULL,
    EMAIL VARCHAR(100) UNIQUE NOT NULL,
    PASSWORD VARCHAR(100) NOT NULL,
    REGESTRATION_DATE DATE NOT NULL DEFAULT CURRENT_DATE,
    LAST_LOGIN TIMESTAMP);
/* User_Management.py */

/* Create a table to store the library books. This should work with a Python program to add the books data */
CREATE TABLE BOOK(
	BOOK_ID SERIAL PRIMARY KEY,
    TITLE VARCHAR(255) NOT NULL,
    AUTHOR VARCHAR(100) NOT NULL,
	AVAILABLE BOOLEAN NOT NULL DEFAULT TRUE);
/* Book_Management.py */

/* Create a table to store the book checkout. This should work with a Python program to checkout the books */
CREATE TABLE BOOK_CHECKOUT (BOOK_ID FOREIGN KEY BOOK.ID, BORROWER_ID FOREIGN KEY )LIBRARY_USER.ID, CHECKOUT_TIME TIME
/* Book_Checkout.py */