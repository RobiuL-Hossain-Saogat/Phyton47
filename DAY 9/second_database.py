import sqlite3

connect_dbfile=sqlite3.connect("information.db")
cursor=connect_dbfile.cursor()

# create table
create_table="CREATE TABLE IF NOT EXISTS data(Name TEXT, FatherName TEXT, MotherName TEXT, Age INTEGER, Class TEXT, Section TEXT, Roll INTEGER)"
cursor.execute(create_table)

#insert data
cursor.execute("INSERT INTO data VALUES('ROBIUL HOSSAIN', 'MD. YOUSUP', 'PARVIN AKTER', '20', 'B.Sc(HONOURS)', 'B', '51')")
cursor.execute("INSERT INTO data VALUES('SIAM UDDIN', 'KAMAL HOSSEN', 'RUKEYA BEGUM', '19', 'TWELVE', 'D', '94')")
cursor.execute("INSERT INTO data VALUES('SAJJAD HOSSEN', 'ABSAR AHMED', 'TANJINA AKTER', '18', 'ELEVEN', 'F', '98')")
cursor.execute("INSERT INTO data VALUES('SHAHRIAR NAFEES', 'MOHAMMED KARIM', 'SAJIDA AKTER', '14', 'EIGHT', 'A', '37')")
cursor.execute("INSERT INTO data VALUES('RAFIT HASAN', 'MD. JAMAL', 'REHANA BEGUM', '17', 'TEN', 'A', '34')")

connect_dbfile.commit()