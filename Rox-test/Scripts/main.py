import configparser
import pyodbc
import os
import pandas as pd

config = configparser.ConfigParser()
config.read('app.ini')

user = config['authentication']['user']
passwd = config['authentication']['password']
driver = config['cnxbase']['driver']
server = config['cnxbase']['server']
database = config['cnxbase']['database']

mpath = '.\\csvs\\'


def do_import():
    # Executa a importação dos CSVs da pasta

    # Cria conexão ODBC Sql Server
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + passwd)
    cursor = cnxn.cursor()

    # Cria lista de arquivos CSV na pasta mpath
    included_extensions = ['csv', 'CSV']
    file_names = [mpath + fn for fn in os.listdir(mpath)
                  if any(fn.endswith(ext) for ext in included_extensions)]

    # Mapeia e importa os aqrquivos para o SQL Server
    for mfile in file_names:
        mtable = mfile.split('.')
        mquery = f"delete from {mtable[2]}"
        print(f'*** Deletando Dados -->>> {mtable[2]}')
        cursor.execute(mquery)
        cursor.commit()
        mfiletl = pd.read_csv(mfile, sep=";")
        mfiletl = mfiletl.fillna('Null')
        for i, mlinha in mfiletl.iterrows():
            if mtable[2] == 'Person':
                minsert = f"insert into [dbo].[Person] " \
                          f"([BusinessEntityID] " \
                          f",[PersonType]         " \
                          f",[NameStyle]   " \
                          f",[Title]        " \
                          f",[FirstName]      " \
                          f",[MiddleName]         " \
                          f",[LastName]  " \
                          f",[Suffix]  " \
                          f",[EmailPromotion]" \
                          f",[AdditionalContactInfo]   " \
                          f",[Demographics]      " \
                          f",[rowguid]    " \
                          f",[ModifiedDate]) VALUES  " \
                          f"({mlinha['BusinessEntityID']} " \
                          f",'{mlinha['PersonType']}'" \
                          f",{mlinha['NameStyle']}" \
                          f",'{mlinha['Title']}'" \
                          f",'{mlinha['FirstName']}' " \
                          f",'{mlinha['MiddleName']}'" \
                          f",'{mlinha['LastName']}'" \
                          f",'{mlinha['Suffix']}' " \
                          f",{mlinha['EmailPromotion']}" \
                          f",'{mlinha['AdditionalContactInfo']}' " \
                          f",'{mlinha['Demographics']}'" \
                          f", '{mlinha['rowguid']}'" \
                          f",'{mlinha['ModifiedDate']}') "
                try:
                    cursor.execute(minsert)
                    cursor.commit()
                    print('OK -->> ' + minsert)
                except:
                    print('Trouble -->> ' + minsert)
            elif mtable[2] == 'Product':
                minsert = f"INSERT INTO [dbo].[Product] " \
                          f"([ProductID] " \
                          f",[SpecialOfferID] " \
                          f",[Name]  " \
                          f",[ProductNumber]  " \
                          f",[MakeFlag]  " \
                          f",[FinishedGoodsFlag]  " \
                          f",[Color]  " \
                          f",[SafetyStockLevel]  " \
                          f",[ReorderPoint]  " \
                          f",[StandardCost]  " \
                          f",[ListPrice]  " \
                          f",[Size]  " \
                          f",[SizeUnitMeasureCode]  " \
                          f",[WeightUnitMeasureCode]  " \
                          f",[Weight]  " \
                          f",[Style]  " \
                          f",[DaysToManufacture]  " \
                          f",[ProductLine]  " \
                          f",[Class]  " \
                          f",[ProductSubcategoryID]  " \
                          f",[ProductModelID]  " \
                          f",[SellStartDate]  " \
                          f",[SellEndDate]  " \
                          f",[rowguid]  " \
                          f",[DiscontinuedDate]  " \
                          f",[ModifiedDate])  VALUES" \
                          f"({mlinha['ProductID']}  " \
                          f",1  " \
                          f",'{mlinha['Name']} ' " \
                          f",'{mlinha['ProductNumber']}'  " \
                          f",{mlinha['MakeFlag']}  " \
                          f",{mlinha['FinishedGoodsFlag']}  " \
                          f",'{mlinha['Color']}'  " \
                          f",{mlinha['SafetyStockLevel']}  " \
                          f",{mlinha['ReorderPoint']}  " \
                          f",{mlinha['StandardCost'].replace(',', '.')}  " \
                          f",{mlinha['ListPrice'].replace(',', '.')}  " \
                          f",'{mlinha['Size']}'  " \
                          f",'{mlinha['SizeUnitMeasureCode']}'  " \
                          f",'{mlinha['WeightUnitMeasureCode']}'  " \
                          f",{mlinha['Weight']}  " \
                          f",'{mlinha['Style']} ' " \
                          f",{mlinha['DaysToManufacture']}  " \
                          f",'{mlinha['ProductLine']}'  " \
                          f",'{mlinha['Class']}'  " \
                          f",'{mlinha['ProductSubcategoryID']}'  " \
                          f",{mlinha['ProductModelID']}  " \
                          f",'{mlinha['SellStartDate'].replace('Null', '')}'  " \
                          f",'{mlinha['SellEndDate'].replace('Null', '')}'  " \
                          f",'{mlinha['rowguid']}'  " \
                          f",'{mlinha['DiscontinuedDate'].replace('Null', '')}'  " \
                          f",'{mlinha['ModifiedDate'].replace('Null', '')}')  "
                try:
                    cursor.execute(minsert)
                    cursor.commit()
                    print('OK -->> ' + minsert)
                except:
                    print('Trouble -->> ' + minsert)
            elif mtable[2] == 'Customer':
                minsert = f"INSERT INTO [dbo].[Customer] " \
                          f" ([CustomerID]" \
                          f",[PersonID] " \
                          f",[StoreID]" \
                          f",[TerritoryID]" \
                          f",[AccountNumber]" \
                          f",[rowguid]" \
                          f",[ModifiedDate]) VALUES     " \
                          f"({mlinha['CustomerID']}" \
                          f",{mlinha['PersonID']}" \
                          f",{mlinha['StoreID']}" \
                          f",{mlinha['TerritoryID']}" \
                          f",'{mlinha['AccountNumber']}'" \
                          f",'{mlinha['rowguid']}'" \
                          f",'{mlinha['ModifiedDate']}')"
                try:
                    cursor.execute(minsert)
                    cursor.commit()
                    print('OK -->> ' + minsert)
                except:
                    print('Trouble -->> ' + minsert)
            elif mtable[2] == 'SalesOrderDetail':
                minsert = f" INSERT INTO [dbo].[SalesOrderDetail]" \
                          f"([SalesOrderDetailID]" \
                          f" ,[ProductID]" \
                          f" ,[SpecialOfferID]" \
                          f" ,[SalesOrderID]" \
                          f" ,[CarrierTrackingNumber]" \
                          f" ,[OrderQty]" \
                          f" ,[UnitPrice]" \
                          f" ,[UnitPriceDiscount]" \
                          f" ,[LineTotal]" \
                          f" ,[rowguid]" \
                          f" ,[ModifiedDate])" \
                          f" VALUES " \
                          f"({mlinha['SalesOrderDetailID']}" \
                          f" ,{mlinha['ProductID']}" \
                          f" ,{mlinha['SpecialOfferID']}" \
                          f" ,{mlinha['SalesOrderID']}" \
                          f" ,'{mlinha['CarrierTrackingNumber']}'" \
                          f" ,{mlinha['OrderQty']}" \
                          f" ,{mlinha['UnitPrice'].replace(',', '.')}" \
                          f" ,{mlinha['UnitPriceDiscount'].replace(',', '.')}" \
                          f" ,{str(mlinha['LineTotal']).replace('.', '')}" \
                          f" ,'{mlinha['rowguid']}'" \
                          f" ,'{mlinha['ModifiedDate']}')"
                try:
                    cursor.execute(minsert)
                    cursor.commit()
                    print('OK -->> ' + minsert)
                except:
                    print('Trouble -->> ' + minsert)
            elif mtable[2] == 'SalesOrderHeader':
                minsert = f"INSERT INTO [dbo].[SalesOrderHeader]" \
                          f"([SalesOrderID]" \
                          f",[CustomerID]" \
                          f",[RevisionNumber]" \
                          f",[OrderDate]" \
                          f",[DueDate]" \
                          f",[Status]" \
                          f",[ShipDate]" \
                          f",[OnlineOrderFlag]" \
                          f",[SalesOrderNumber]" \
                          f",[PurchaseOrderNumber]" \
                          f",[AccountNumber]" \
                          f",[SalesPersonID]" \
                          f",[TerritoryID]" \
                          f",[BillToAddressID]" \
                          f",[ShipToAddressID]" \
                          f",[ShipMethodID]" \
                          f",[CreditCardID]" \
                          f",[CreditCardApprovalCode]" \
                          f",[CurrencyRateID]" \
                          f",[SubTotal]" \
                          f",[TaxAmt]" \
                          f",[Freight]" \
                          f",[TotalDue]" \
                          f",[Comment]" \
                          f",[rowguid]" \
                          f",[ModifiedDate])  VALUES " \
                          f"({mlinha['SalesOrderID']}" \
                          f",{mlinha['CustomerID']}" \
                          f",{mlinha['RevisionNumber']}" \
                          f",'{mlinha['OrderDate']}'" \
                          f",'{mlinha['DueDate']}'" \
                          f",{mlinha['Status']}" \
                          f",'{mlinha['ShipDate']}'" \
                          f",{mlinha['OnlineOrderFlag']}" \
                          f",'{mlinha['SalesOrderNumber']}'" \
                          f",'{mlinha['PurchaseOrderNumber']}'" \
                          f",'{mlinha['AccountNumber']}'" \
                          f",{mlinha['SalesPersonID']}" \
                          f",{mlinha['TerritoryID']}" \
                          f",{mlinha['BillToAddressID']}" \
                          f",{mlinha['ShipToAddressID']}" \
                          f",{mlinha['ShipMethodID']}" \
                          f",{mlinha['CreditCardID']}" \
                          f",'{mlinha['CreditCardApprovalCode']}'" \
                          f",'{mlinha['CurrencyRateID']}'" \
                          f",{mlinha['SubTotal'].replace(',', '.')}" \
                          f",{mlinha['TaxAmt'].replace(',', '.')}" \
                          f",{mlinha['Freight'].replace(',', '.')}" \
                          f",{mlinha['TotalDue'].replace(',', '.')}" \
                          f",'{mlinha['Comment']}'" \
                          f",'{mlinha['rowguid']}'" \
                          f",'{mlinha['ModifiedDate']}')"
                try:
                    cursor.execute(minsert)
                    cursor.commit()
                    print('OK -->> ' + minsert)
                except:
                    print('Trouble -->> ' + minsert)
            elif mtable[2] == 'SpecialOfferProduct':
                minsert = f" INSERT INTO [dbo].[SpecialOfferProduct]" \
                          f" ([SpecialOfferID]" \
                          f" ,[ProductID]" \
                          f" ,[rowguid]" \
                          f" ,[ModifiedDate])      VALUES " \
                          f"({mlinha['SpecialOfferID']}" \
                          f",{mlinha['ProductID']}" \
                          f",'{mlinha['rowguid']}'" \
                          f",'{mlinha['ModifiedDate']}')"
                try:
                    cursor.execute(minsert)
                    cursor.commit()
                    print('OK -->> ' + minsert)
                except:
                    print('Trouble -->> ' + minsert)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    do_import()
