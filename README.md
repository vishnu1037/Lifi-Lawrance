# Lifi-Lawrance
Assignment submission for LIFI lawrence

This is a project code to read data from Text file in format
 |H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active
 |D|Alex|123457|20101012|20121013|MVD|Paul|SA|USA|06031987|A
 ..........................................................
Store it in a dataase.

Once main.py is ran the data maintained in var.txt is read using pandas and
we will then make entries in database tables
1)Customer_data - It will have all entries of var.txt
2)Talble_India - entries specific to india
3)Table_USA - ""
4)Table_NewYorkCity(since in given doc test data has country NYC apart from USA)-""
5)Table_Australia - ""
6)Tale_Philippines - ""

Database used:
Host: sql6.freesqldatabase.com
Database name: sql6431701
Database user: sql6431701
Database password: hcK3UBCeSg
Port number: 3306
Follow this link http://www.phpmyadmin.co and use the database details above to see the database.
