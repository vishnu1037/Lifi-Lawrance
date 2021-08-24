# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import mysql.connector
conn = mysql.connector.connect(host='sql6.freesqldatabase.com',user='sql6431701',passwd='hcK3UBCeSg',database='sql6431701')
cur = conn.cursor()
df =pd.read_csv(r"var.txt",sep='|')
for i,r in df.iterrows():
    print(r.DOB)
    s = str(r.DOB)
    p = s[-4:] + s[-6:-4]
    if len(s[:-6]) == 1:
        p += '0'+s[:-6]
    else:
        p += s[:-6]
    r.DOB = int(p)
    print(r.Country)
    try:
        cur.execute(r"INSERT INTO Customer_data (`Customer Name`, `Customer ID`, `Customer Open Date`, `Last Consulted Date`, `Vaccination Type`, `Doctor Consulted`, `State`, `Country`, `Date of Birth`, `Active Customer`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(r.Customer_Name,r.Customer_Id,r.Open_Date,r.Last_Consulted_Date,r.Vaccination_Id,r.Dr_Name,r.State,r.Country,r.DOB,r.Is_Active));
    except mysql.connector.Error as error:
        print(error);
    if r.Country == 'IND':
        try:
            cur.execute(
                r"INSERT INTO Table_India (`Customer Name`, `Customer ID`, `Customer Open Date`, `Last Consulted Date`, `Vaccination Type`, `Doctor Consulted`, `State`, `Country`, `Date of Birth`, `Active Customer`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (r.Customer_Name, r.Customer_Id, r.Open_Date, r.Last_Consulted_Date, r.Vaccination_Id, r.Dr_Name, r.State,
                r.Country, r.DOB, r.Is_Active));
        except mysql.connector.Error as error:
            print("Entry message for Table_India",error);
    elif r.Country == 'USA':
        try:
            cur.execute(
                r"INSERT INTO Table_USA (`Customer Name`, `Customer ID`, `Customer Open Date`, `Last Consulted Date`, `Vaccination Type`, `Doctor Consulted`, `State`, `Country`, `Date of Birth`, `Active Customer`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (r.Customer_Name, r.Customer_Id, r.Open_Date, r.Last_Consulted_Date, r.Vaccination_Id, r.Dr_Name, r.State,
                r.Country, r.DOB, r.Is_Active));
        except mysql.connector.Error as error:
            print("Entry message for Table_USA",error);
    elif r.Country == 'PHIL':
        try:
            cur.execute(
                r"INSERT INTO Table_Philippines (`Customer Name`, `Customer ID`, `Customer Open Date`, `Last Consulted Date`, `Vaccination Type`, `Doctor Consulted`, `State`, `Country`, `Date of Birth`, `Active Customer`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (r.Customer_Name, r.Customer_Id, r.Open_Date, r.Last_Consulted_Date, r.Vaccination_Id, r.Dr_Name, r.State,
                r.Country, r.DOB, r.Is_Active));
        except mysql.connector.Error as error:
            print("Entry message for Table_Philippines",error);
    elif r.Country == 'NYC':
        try:
            cur.execute(
                r"INSERT INTO Table_NewYorkCity (`Customer Name`, `Customer ID`, `Customer Open Date`, `Last Consulted Date`, `Vaccination Type`, `Doctor Consulted`, `State`, `Country`, `Date of Birth`, `Active Customer`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (r.Customer_Name, r.Customer_Id, r.Open_Date, r.Last_Consulted_Date, r.Vaccination_Id, r.Dr_Name, r.State,
                r.Country, r.DOB, r.Is_Active));
        except mysql.connector.Error as error:
            print("Entry message for Table_NewYorkCity",error);
    elif r.Country == 'AU':
        try:
            cur.execute(
                r"INSERT INTO Table_Australia (`Customer Name`, `Customer ID`, `Customer Open Date`, `Last Consulted Date`, `Vaccination Type`, `Doctor Consulted`, `State`, `Country`, `Date of Birth`, `Active Customer`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (r.Customer_Name, r.Customer_Id, r.Open_Date, r.Last_Consulted_Date, r.Vaccination_Id, r.Dr_Name, r.State,
                r.Country, r.DOB, r.Is_Active));
        except mysql.connector.Error as error:
            print("Entry message for Table_Australia",error);
conn.commit()
cur.close()
print(pd.read_sql_query('select * from Customer_data',conn))
print(pd.read_sql_query('select * from Table_India',conn))
print(pd.read_sql_query('select * from Table_USA',conn))
print(pd.read_sql_query('select * from Table_Philippines',conn))
print(pd.read_sql_query('select * from Table_NewYorkCity',conn))
print(pd.read_sql_query('select * from Table_Australia',conn))

