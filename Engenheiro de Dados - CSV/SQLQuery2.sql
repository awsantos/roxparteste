
CREATE TABLE SpecialOfferProduct (
	            SpecialOfferID INT NOT NULL,
                ProductID INT NOT NULL,
                rowguid VARCHAR(MAX) NOT NULL,
                ModifiedDate DATETIME NOT NULL,
                CONSTRAINT New_Table_pkSpecialOfferID PRIMARY KEY (ProductID, SpecialOfferID)
)

CREATE TABLE SalesOrderDetail (
                SalesOrderDetailID INT  NOT NULL,
                ProductID INT NOT NULL,
                SpecialOfferID INT DEFAULT 1 NOT NULL,
                SalesOrderID INT NOT NULL,
                CarrierTrackingNumber VARCHAR(MAX),
                OrderQty INT NOT NULL,
                UnitPrice NUMERIC(4) NOT NULL,
                UnitPriceDiscount NUMERIC(4) DEFAULT 0 NOT NULL,
                LineTotal REAL NOT NULL,
                rowguid VARCHAR(MAX) NOT NULL,
                ModifiedDate DATETIME NOT NULL,
                CONSTRAINT SalesOrderDetailID PRIMARY KEY (SalesOrderDetailID)
)

CREATE TABLE Product (
                ProductID INT NOT NULL,
                SpecialOfferID INT NOT NULL,
                Name VARCHAR(MAX) NOT NULL,
                ProductNumber VARCHAR(MAX) NOT NULL,
                MakeFlag INT DEFAULT 0 NOT NULL,
                FinishedGoodsFlag INT NOT NULL,
                Color VARCHAR(MAX),
                SafetyStockLevel INT NOT NULL,
                ReorderPoint INT NOT NULL,
                StandardCost NUMERIC(4) DEFAULT 0 NOT NULL,
                ListPrice NUMERIC(3) DEFAULT 0 NOT NULL,
                Size VARCHAR(MAX),
                SizeUnitMeasureCode VARCHAR(MAX),
                WeightUnitMeasureCode VARCHAR(MAX),
                Weight NUMERIC(2),
                Style VARCHAR(MAX),
                DaysToManufacture INT DEFAULT 0 NOT NULL,
                ProductLine VARCHAR(MAX),
                Class VARCHAR(MAX),
                ProductSubcategoryID VARCHAR(MAX),
                ProductModelID VARCHAR(MAX),
                SellStartDate DATETIME NOT NULL,
                SellEndDate DATETIME,
                rowguid VARCHAR(MAX) NOT NULL,
                DiscontinuedDate DATETIME,
                ModifiedDate DATETIME NOT NULL,
                CONSTRAINT ProductID PRIMARY KEY (ProductID, SpecialOfferID)
)

CREATE TABLE Person (
                BusinessEntityID INT  NOT NULL,
                PersonType VARCHAR(MAX) NOT NULL,
                NameStyle INT DEFAULT 0 NOT NULL,
                Title VARCHAR(MAX),
                FirstName VARCHAR(MAX) NOT NULL,
                MiddleName VARCHAR(MAX),
                LastName VARCHAR(MAX) NOT NULL,
                Suffix VARCHAR(MAX),
                EmailPromotion INT DEFAULT 0 NOT NULL,
                AdditionalContactInfo VARCHAR(MAX),
                Demographics NVARCHAR,
                rowguid VARCHAR(MAX) NOT NULL,
                ModifiedDate DATETIME NOT NULL,
                CONSTRAINT BusinessEntityID PRIMARY KEY (BusinessEntityID)
)

CREATE TABLE Customer (
                CustomerID INT NOT NULL,
                PersonID INT,
                StoreID INT,
                TerritoryID INT NOT NULL,
                AccountNumber VARCHAR(MAX) NOT NULL,
                rowguid VARCHAR(MAX) NOT NULL,
                ModifiedDate DATETIME NOT NULL,
                CONSTRAINT CustomerID PRIMARY KEY (CustomerID)
)

CREATE TABLE SalesOrderHeader (
                SalesOrderID INT NOT NULL,
                CustomerID INT NOT NULL,
                RevisionNumber INT NOT NULL,
                OrderDate DATETIME NOT NULL,
                DueDate DATETIME NOT NULL,
                Status INT NOT NULL,
                ShipDate DATETIME NOT NULL,
                OnlineOrderFlag INT DEFAULT 0 NOT NULL,
                SalesOrderNumber VARCHAR(MAX) NOT NULL,
                PurchaseOrderNumber VARCHAR(MAX),
                AccountNumber VARCHAR(MAX) NOT NULL,
                SalesPersonID INT,
                TerritoryID INT NOT NULL,
                BillToAddressID INT NOT NULL,
                ShipToAddressID INT NOT NULL,
                ShipMethodID INT DEFAULT 5 NOT NULL,
                CreditCardID INT NOT NULL,
                CreditCardApprovalCode VARCHAR(MAX),
                CurrencyRateID VARCHAR(MAX),
                SubTotal NUMERIC(4) DEFAULT 0 NOT NULL,
                TaxAmt NUMERIC(4) DEFAULT 0 NOT NULL,
                Freight NUMERIC(4) DEFAULT 0 NOT NULL,
                TotalDue NUMERIC(4) DEFAULT 0 NOT NULL,
                Comment VARCHAR(MAX),
                rowguid VARCHAR(MAX) NOT NULL,
                ModifiedDate DATETIME NOT NULL,
                CONSTRAINT SalesOrderID PRIMARY KEY (SalesOrderID)
)

ALTER TABLE Product ADD CONSTRAINT SpecialOfferProduct_Product_fk
FOREIGN KEY (ProductID, SpecialOfferID)
REFERENCES SpecialOfferProduct (ProductID, SpecialOfferID)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE SalesOrderDetail ADD CONSTRAINT SpecialOfferProduct_SalesOrderDetail_fk
FOREIGN KEY (ProductID, SpecialOfferID)
REFERENCES SpecialOfferProduct (ProductID, SpecialOfferID)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE SalesOrderHeader ADD CONSTRAINT SalesOrderDetail_SalesOrderHeader_fk
FOREIGN KEY (SalesOrderID)
REFERENCES SalesOrderDetail (SalesOrderDetailID)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE Customer ADD CONSTRAINT Person_Customer_fk
FOREIGN KEY (CustomerID)
REFERENCES Person (BusinessEntityID)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE SalesOrderHeader ADD CONSTRAINT Customer_SalesOrderHeader_fk
FOREIGN KEY (CustomerID)
REFERENCES Customer (CustomerID)
ON DELETE NO ACTION
ON UPDATE NO ACTION