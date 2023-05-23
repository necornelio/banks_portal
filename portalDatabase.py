import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="banks_portal",
                 user='root',
                 password='********'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)

            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)


    def getAllAccounts(self):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            query = "select * from accounts"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def getAllTransactions(self):
        ''' Complete the method to execute
                query to get all transactions'''
        pass

    def deposit(self, accountID, amount):
        ''' Complete the method that calls store procedure
                    and return the results'''
        pass


    def withdraw(self, accountID, amount):
        ''' Complete the method that calls store procedure
                    and return the results'''
        pass

    def addAccount(self, ownerName, owner_ssn, balance, status):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            query = "INSERT INTO accounts(ownerName, owner_ssn, balance, status) values (%s, %s, %s, %s)", ("Natalie Cornelio", 12312312, 120000.00, "active")
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
        
      
                             
                                
    def accountTransactions(self, accountID):
        ''' Complete the method to call
                    procedure accountTransaction return results'''
        pass

    def deleteAccount(self, AccountID):
        ''' Complete the method to delete account
                and all transactions related to account'''
        pass
