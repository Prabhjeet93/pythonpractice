import pyodbc

#Demonstrate successful connection to SQL Server and AdventureWorks test database.
#Demonstrate that dataset (data) can be retrieved from various tables in database – Full record set.  Using a FOR loop.  Use record sorting.


# storing the below databse details in conn variable
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'     # Driver to run the sql query is mentioned
                          'Server=PRABH\SQLEXPRESS02;'    # Server name of SQL is mentioned
                          'Database=AdventureworksLT2019;'   # Database to run the sql query is mentioned
                          'Trusted_Connection=yes;')   # connection is trusted and made the value as yes or no.


cursor = conn.cursor()  # defined a variaable cursor with the help of Cursor method , it will store the values in the cursor variable

# execute a SQL query , in this query fetching the whole data of Product category table whose parent product category ID is 2 and 3
# and sorting by name in descending order
#Data will be fetched for these columns - [ProductCategoryID], [ParentProductCategoryID], [Name], [rowguid], [ModifiedDate]
cursor.execute('SELECT * FROM [SalesLT].[ProductCategory] where ParentProductCategoryID IN (2,3) ORDER BY Name DESC')
print("Print data whose parent product category ID is 2 and 3 and sorted by Names")     # print command for the message
for i in cursor:      # for loop to iterate the output of the query
    print(i)          # print output one by one with the help of cursor


# execute a SQL query, In this query fetching the productModel ID, Product Name and Row GUID from Product model and ProductModelProductDescription table with the help of Join operator.
# Here trying to fetch data from multiple table
cursor.execute('SELECT prod_model.ProductModelID Product_Model_ID, prod_model.Name name, prod_model_desc.[rowguid] roww_guid FROM [AdventureWorksLT2019].[SalesLT].[ProductModel] prod_model JOIN [AdventureWorksLT2019].[SalesLT].[ProductModelProductDescription] prod_model_desc ON (prod_model.ProductModelID = prod_model_desc.ProductModelID);')
print("Fetching data from two tables - Product model and Product Model Product Description using JOIN clause")
for j in cursor:  # for loop to iterate the output of the query
    print(j)      # print output one by one with the help of cursor
