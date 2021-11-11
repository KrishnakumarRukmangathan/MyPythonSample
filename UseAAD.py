import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'mysqlserver619.database.windows.net' 
database = 'mySampleDatabase' 
#username = 'azureuser' 
username = 'krirukm@microsoft.com' 
#password = 'India123@' 
authentication='ActiveDirectoryInteractive'
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';Authentication='+ authentication)
cursor = cnxn.cursor()

#Sample select query
#cursor.execute("SELECT @@version;") 
#cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
cursor.execute("SELECT * FROM [SalesLT].[Product];") 
row = cursor.fetchone() 
while row: 
    print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]) + " " + str(row[6]) + " " + str(row[7]))
    row = cursor.fetchone()


    
