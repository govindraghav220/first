
import tkinter as tk
import mysql.connector as mysql
conn=mysql.connect(host="localhost",user="root",password="",database="gaurav")
root=tk.Tk()
root.geometry("450x480")
root.config(bg="lightblue")
def submit():
    em_id =e1.get()
    em_name= e2.get()
    em_email=e3.get()
    contact_no=e4.get()
    em_address=e5.get()
    em_position=e6.get()
    curr=conn.cursor()
    curr.execute("insert into employee2(em_id,em_name,em_email,contact_no,em_address,em_position)values('%s','%s','%s','%s','%s','%s')"%(em_id,em_name,em_email,contact_no,em_address,em_position))
    conn.commit()

tk.Message(root)
l=tk.Label(root,text="Create An Emoloyee Account",fg="Blue",bg="lightblue",font=("times new roman",22))
l.place(x=50,y=0)

l1=tk.Label(root,text="Em_Id: ",fg="orange",bg="lightblue",font=("Calibri",14))
l1.place(x=50,y=50)
e1=tk.Entry(root,width=20,bg="lightblue",fg="orange",font=("Calibri",15))
e1.place(x=190,y=50)

l2=tk.Label(root,text="Em_Name: ",fg="orange",bg="lightblue",font=("Calibri",14))
l2.place(x=50,y=100)
e2=tk.Entry(root,width=20,bg="lightblue",fg="orange",font=("Calibri",15))
e2.place(x=190,y=100)

l3=tk.Label(root,text="Em_Email: ",fg="orange",bg="lightblue",font=("Calibri",14))
l3.place(x=50,y=150)
e3=tk.Entry(root,width=20,bg="lightblue",fg="orange",font=("Calibri",15))
e3.place(x=190,y=150)

l4=tk.Label(root,text="Contact_no: ",fg="orange",bg="lightblue",font=("Calibri",14))
l4.place(x=50,y=200)
e4=tk.Entry(root,width=20,bg="lightblue",fg="orange",font=("Calibri",15))
e4.place(x=190,y=200)

l5=tk.Label(root,text="Emp_Address: ",fg="orange",bg="lightblue",font=("Calibri",14))
l5.place(x=50,y=250)
e5=tk.Entry(root,width=20,bg="lightblue",fg="orange",font=("Calibri",15))
e5.place(x=190,y=250)

l6=tk.Label(root,text="Emp_Position: ",fg="orange",bg="lightblue",font=("Calibri",14))
l6.place(x=50,y=370)
e6=tk.Entry(root,width=20,bg="lightblue",fg="orange",font=("Calibri",15))
e6.place(x=190,y=375)

b1=tk.Button(text="Submit Now",command=submit,fg="red",font=("Calibri",14))
b1.place(x=150,y=420)

root.mainloop()
