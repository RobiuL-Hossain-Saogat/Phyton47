import sqlite3

class Formdata:
    def __init__(self,fd):
        self.conn=sqlite3.connect(fd)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, StudentName text, Class text, Section text, RollNo INTEGER, GurdianContact INTEGER, FormFee INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM data ")
        data=self.cur.fetchall()
        return data
    
    def insert(self,StudentName,Class,Section,RollNo,GurdianContact,FormFee):
        self.cur.execute("INSERT INTO data VALUES(NULL,?,?,?,?,?,?)",(StudentName,Class,Section,RollNo,GurdianContact,FormFee))
        self.conn.commit()

    def edit(self,id,StudentName,Class,Section,RollNo,GurdianContact,FormFee):
        self.cur.execute("UPDATE data SET StudentName=?,Class=?,Section=?,RollNo=?,GurdianContact=?,FormFee=? WHERE id=?",(StudentName,Class,Section,RollNo,GurdianContact,FormFee,id))
        self.conn.commit()

    def deletedata(self,id):
        self.cur.execute("DELETE FROM data WHERE id=?",(id,))
        self.conn.commit()
