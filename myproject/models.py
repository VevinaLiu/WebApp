import pyodbc

# construct connection to database using network login

class con_sql():
    consql = pyodbc.connect('Driver={SQL Server};'
                      'Server=Server;'
                      'Database=Database;'
                      'Trusted_Connection=yes;')
