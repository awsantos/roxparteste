use [Rox-test];


CREATE TABLE Person (
                BusinessEntityID INT IDENTITY NOT NULL,
                PersonType CHAR(4) NOT NULL,
                NameStyle INT DEFAULT 0 NOT NULL,
                FirstName CHAR NOT NULL,
                MiddleName CHAR,
                LastName VARCHAR NOT NULL,
                Suffix CHAR(4),
                EmailPromotion INT DEFAULT 0 NOT NULL,
                AdditionalContactInfo VARCHAR,
                Demographics VARCHAR,
                rowguid VARCHAR NOT NULL,
                ModifiedDate DATETIME NOT NULL,
                CONSTRAINT BusinessEntityID PRIMARY KEY (BusinessEntityID)
);