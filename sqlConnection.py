import pyodbc

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=xyz\SQLEXPRESS02;'
                      'Database=AdventureworksLT2019;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('SELECT * FROM [SalesLT].[ProductCategory] where ParentProductCategoryID = 1')

for i in cursor:
    print(i)

cursor.execute('SELECT * FROM [SalesLT].[ProductCategory] where ParentProductCategoryID = 2')

for i in cursor:
    print(i)

cursor.execute('SELECT prod_model.ProductModelID Product_Model_ID, prod_model.Name name, prod_model_desc.[rowguid] roww_guid FROM [AdventureWorksLT2019].[SalesLT].[ProductModel] prod_model JOIN [AdventureWorksLT2019].[SalesLT].[ProductModelProductDescription] prod_model_desc ON (prod_model.ProductModelID = prod_model_desc.ProductModelID);')
for i in cursor:
    print(i)
