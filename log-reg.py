import tkinter as tk
import mysql.connector
from tkinter import *
import time as T


def GettingData():
        hostn = HostName.get()
        usern = Username.get()
        datab = DataBase.get()
        passw = Password.get()
        LoginToDb(hostn,usern,datab,passw)
        


def LoginToDb(hostn,usern,datab,passw):

        global db
        if passw:
                db = mysql.connector.connect(host = hostn,
                                             user = usern,
                                             password = passw,
                                             db =datab)
         
        else:
                db = mysql.connector.connect(host = hostn,
                                             user = usern,
                                             db =datab)

        if db.is_connected():
                print("Yes")
                MainBox(hostn,usern,datab)
                
                
        else:
                print("Connection Failed, Please Retry")

def FetchingAllData():

    # A Table in the database
    cursor = db.cursor()
    query = "select * from students"
     
    try:
        cursor.execute(query)
        myresult = cursor.fetchall()
         
        # Printing the result of the
        # query
        print("RoLL ||NAME||  AN || MARKS")
        for x in myresult:
          
            a = list(x)
            T.sleep(0.5)
            print(a)
        print("Query Executed successfully")
         
    except:
        db.rollback()
        print("Error occurred")


def RegFunc():
        
        DbBox = tk.Tk()
        DbBox.geometry("300x300")
        DbBox.title("DAV || DB CONNECTOR")

        global Username , Password , DataBase , HostName
        l = Label(DbBox, text = "ENTER YOUR DATABASE INFROMATION")
        #l.place(x=60,y=6)

        HostRow = tk.Label(DbBox, text ="HostName\t--> ", ).grid(row = 0)
        HostName = tk.Entry(DbBox, width = 30)
        HostName.grid(row=0, column=1)
         
        DbRow = tk.Label(DbBox, text ="DataBase\t--> ", ).grid(row = 1)
        DataBase = tk.Entry(DbBox, width = 30)
        DataBase.grid(row=1, column=1)
        
        UserRow = tk.Label(DbBox, text ="Username\t--> ", ).grid(row = 2)
        Username = tk.Entry(DbBox, width = 30)
        Username.grid(row=2, column=1)

        PassRow = tk.Label(DbBox, text ="Password\t--> ", ).grid(row = 3)
        Password = tk.Entry(DbBox, width = 30)
        Password.grid(row=3, column=1)
       
        
        submitbtn = tk.Button(DbBox, text ="Submit",
                              bg ='green', command = GettingData)
        submitbtn.place(x = 150, y = 200, width = 55)

        DbBox.mainloop()

def MainBox(hostn,usern,datab):
        
        MBox = tk.Tk()
        MBox.geometry("300x300")
        MBox.title(f"DAV || CONTROL PANEL OF database a")

        l = Label(MBox, text = "Connection was succesfully made into the database !!").pack()
        l0 = Label(MBox, text = f"DATABASE NAME --> {datab}").pack()
        l1 = Label(MBox, text = f"HOST NAME     --> {hostn}").pack()
        l2 = Label(MBox, text = f"PASSWORD      --> *******").pack()
        l3 = Label(MBox, text = f"User Name     --> {usern}").pack()
   
        l = Label(MBox, text = "DATABASE CONTROLLER").pack()
        
        submitbtn = tk.Button(MBox, text ="Fetch All Info",
                              bg ='green', command = FetchingAllData)
        submitbtn.place(x = 150, y = 200, width = 100)

        MBox.mainloop()
 
RegFunc()

