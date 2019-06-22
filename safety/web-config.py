import mysql.connector as conn

mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="Shiki992",
  database="safety"
)
print(mydb)

def showreads():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Readings")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def showsubs():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM subarea")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def showarea():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM area")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def insertreads( Acode, Timestamp, H2S = "NULL", N2_lvl = "NULL", CO_lvl = "NULL", Cl2_lvl = "NULL", Pressure_lvl="NULL", Smoke="NULL"):
    sql = "INSERT INTO Readings (Areacode,H2S_lvl,N2_lvl,CO_lvl,Cl2_lvl,Pressure_lvl,Smoke,Timestamp) VALUES (%d, %d, %d, %d, %d, %d, %b, %s);"
    val = (Acode,H2S,N2_lvl,CO_lvl,Cl2_lvl,Pressure_lvl,Smoke,Timestamp)
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    print("\nTable after insertion:\n")
    showreads()

def viewstations():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM subarea as s,area as a where s.Areaid=a.Areaid;")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def updateitem(data,id,table="S",mode="M"):#there are 2 tables, these table modes represent the changes you want to make to tables S =subareas, A = areas
#there are 2 modes, these modes represent what you want to change. you can only change the manager or the name of the particular area.
    mycursor = mydb.cursor()
    sql="update %s SET %s=%s where %s=%s;"
    
    if table=="S":
        if mode=="M":
            val=('subarea','SAManager',data,'SAid',id)
        else: #if mode=="N":
            val=('subarea','SAName',data,'SAid',id)
    else:#if table=="A":
        if mode=="M":
            val=('area','AreaManager',data,'Areaid',id)
        else:#if mode=="N":
            val=('area','AreaName',data,'Areaid',id) 
    
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record updated.")
    print("\nTable after update:\n")
    viewstations()
updateitem("gym",13,"S","N")
#showreads()
#print("\n")
#showarea()
#print("\n")
#showsubs()
#print("\n")
#viewstations()
