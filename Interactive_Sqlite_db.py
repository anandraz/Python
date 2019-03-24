import sqlite3

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS mytable(Id INT PRIMARY KEY NOT NULL, Name TEXT, Age REAL, Company TEXT, Salary REAL)')
    conn.commit()
    print("************************* Table is Successfully Created or Already exist. *********************************")

def insert_data():
    user_data = (int(input("Enter the id:")), input("Enter the name:"), int(input("Enter the age:")), input("Enter the company name:"),float(input("Enter the salary:")))
    c.execute("INSERT INTO mytable VALUES {}".format(user_data))
    conn.commit()

def display_data():
    c.execute("SELECT * FROM mytable")
    l = c.fetchall()
    print("***********************************************************************************************************")
    for i in range(0, len(l)):
        print(l[i])
    conn.commit()
    print("***********************************************************************************************************")

def delete_data():
    d= int(input("Enter Id:"))
    c.execute("DELETE FROM mytable WHERE Id={}".format(d))
    conn.commit()

if __name__=='__main__':
    database_name = input("Enter the database name(Without any extesion):")
    conn = sqlite3.connect(database_name + '.db')
    c = conn.cursor()
    while(1):
        op= int(input(" 1 --> Create Table\n 2 --> Display Data\n 3 --> Insert Data\n 4 --> Delete Data\n 5 --> Exit\nPlease Choose Option:"))
        if op==1:
            create_table()
        elif op==2:
            display_data()
        elif op==3:
            insert_data()
        elif op==4:
            delete_data()
        elif op==5:
            print("Thanks, Bye.")
            conn.close()
            break