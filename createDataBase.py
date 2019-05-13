from dataLayer import DataBaseHandle

DataBaseHandle.execute(
'''CREATE TABLE IF NOT EXISTS COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
                        );''')