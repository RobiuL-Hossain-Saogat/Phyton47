import sqlite3

class Mydatabase:
    def __init__(self,mydb):
        self.conn=sqlite3.connect(mydb)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS mydatabase(Id INTEGER PRIMARY KEY, MobileNumber INTEGER, Amount INTEGER, Pin INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM mydatabase ")
        pack=self.cur.fetchall()
        return pack

    def insert(self,MobileNumber,Amount,Pin):
        self.cur.execute("INSERT INTO mydatabase VALUES(NULL,?,?,?)",(MobileNumber,Amount,Pin))
        self.conn.commit()

    def __init__(self,mydb):
        self.conn=sqlite3.connect(mydb)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS mydatabase1(Id INTEGER PRIMARY KEY, MeterNumber INTEGER, Amount INTEGER, MobileNumber, Refereence text, Pin INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM mydatabase1 ")
        pack=self.cur.fetchall()
        return pack
    
    def insert(self,MeterNumber,Amount,MobileNumber,Reference,Pin):
        self.cur.execute("INSERT INTO mydatabase1 VALUES(NULL,?,?,?,?,?)",(MeterNumber,Amount,MobileNumber,Reference,Pin))
        self.conn.commit()

    def __init__(self,mydb):
        self.conn=sqlite3.connect(mydb)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS mydatabase2(Id INTEGER PRIMARY KEY, MerchantNumber INTEGER, Amount INTEGER, Refereence text, Pin INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM mydatabase2 ")
        pack=self.cur.fetchall()
        return pack
    
    def insert(self,MerchantNumber,Amount,Reference,Pin):
        self.cur.execute("INSERT INTO mydatabase2 VALUES(NULL,?,?,?,?)",(MerchantNumber,Amount,Reference,Pin))
        self.conn.commit()

