from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1510x600+0+0")
        self.root.title('employee management system')


        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_adress=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        





        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)
    

        img_logo=Image.open('images/gg.png')
        img_logo=img_logo.resize((50,50,),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        #1st image

        img1=Image.open('images/kk.png')
        img1=img1.resize((540,160,),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        #2nd image
        img_2=Image.open('images/pp.png')
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)


         #3nd image
        img_3=Image.open('images/qq.png')
        img_3=img_3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)

        #Mainframe
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)

        #upper frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=560)

        #Labels and entry fields
        lbl_dep=Label(upper_frame,text='Department',font=('times arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('times arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager','Salesman','Supervisor')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #name
        lbl_Name=Label(upper_frame,font=("arial",12,"bold"),text="Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #lbl designation
        lbl_Designition=Label(upper_frame,font=("arial",12,"bold"),text="Designition:",bg="white")
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=22,font=("arial",11,"bold"))
        txt_Designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #email
        lbl_email=Label(upper_frame,font=("arial",12,"bold"),text="Email:",bg="white")
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        #adress
        lbl_adress=Label(upper_frame,font=("arial",12,"bold"),text="Adress:",bg="white")
        lbl_adress.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        txt_adress=ttk.Entry(upper_frame,textvariable=self.var_adress,width=22,font=("arial",11,"bold"))
        txt_adress.grid(row=2,column=1,padx=2,pady=7)

        #married
        lbl_married_status=Label(upper_frame,font=("arial",12,"bold"),text="Married status:",bg="white")
        lbl_married_status.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_married['value']=("married","unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        #dob
        lbl_dob=Label(upper_frame,font=("arial",12,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        #doj
        lbl_doj=Label(upper_frame,font=("arial",12,"bold"),text="DOJ:",bg="white")
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

        #id proof
        com_txt_proof=ttk.Combobox(upper_frame,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_proof['value']=("select ID Proof","PAN CARD","AADHAR CARD","DRIVING LIECENSCE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        
        #gender
        lbl_gender=Label(upper_frame,font=("arial",12,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        #phone
        lbl_phone=Label(upper_frame,font=("arial",12,"bold"),text="PhoneNo:",bg="white")
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)
        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        #country
        lbl_country=Label(upper_frame,font=("arial",12,"bold"),text="Country:",bg="white")
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)
        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=("arial",11,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        #ctc
        lbl_ctc=Label(upper_frame,font=("arial",12,"bold"),text="Salary(ctc):",bg="white")
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)
        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("arial",11,"bold"))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

         #mask
        img_mask=Image.open('images/oo.png')
        img_mask=img_mask.resize((210,210),Image.ANTIALIAS)
        self.photomask=ImageTk.PhotoImage(img_mask)

        self.img_mask=Label(upper_frame,image=self.photomask)
        self.img_mask.place(x=1000,y=0,width=220,height=220)


        #button frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1150,y=20,width=170,height=210)


        btn_add=Button(button_frame,text="Save",command=self.add_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)


        btn_update=Button(button_frame,text="Update",command=self.update_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)










        #down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

        #search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1470,height=60)
        search_by=Label(search_frame,font=("arial",11,"bold"),text="search by:",fg="white",bg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("select an option","phone","id proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="search",command=self.search_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(search_frame,text="show all",command=self.fetch_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_ShowAll.grid(row=0,column=4,padx=5)

        stayhome=Label(search_frame,text="Wear a Mask",font=("times new roman",30,"bold"),fg="red",bg="white")
        stayhome.place(x=780,width=600,height=30)

        img_logo_mask=Image.open(r"images\aa.png")
        img_logo_mask=img_logo_mask.resize((50,50),Image.ANTIALIAS)
        self.photoimg_logo_mask=ImageTk.PhotoImage(img_logo_mask)

        self.logo=Label(search_frame,image=self.photoimg_logo_mask)
        self.logo.place(x=900,y=0,width=50,height=30)

        #employee table
        #tableframe
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","adress","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=TOP,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text="Name")
        self.employee_table.heading('degi',text="Designition")
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('adress',text='adress')
        self.employee_table.heading('married',text='married status')
        self.employee_table.heading('dob',text='Dob')
        self.employee_table.heading('doj',text='Doj')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text='ID proof')
        self.employee_table.heading('gender',text='gender')
        self.employee_table.heading('phone',text='phone')
        self.employee_table.heading('country',text='country')
        self.employee_table.heading('salary',text='salary')

        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=150)
        self.employee_table.column("name",width=150)
        self.employee_table.column("degi",width=150)
        self.employee_table.column("email",width=150)
        self.employee_table.column("adress",width=150)
        self.employee_table.column("married",width=150)
        self.employee_table.column("dob",width=150)
        self.employee_table.column("doj",width=150)
        self.employee_table.column("idproofcomb",width=150)
        self.employee_table.column("idproof",width=150)
        self.employee_table.column("gender",width=150)
        self.employee_table.column("phone",width=150)
        self.employee_table.column("country",width=150)
        self.employee_table.column("salary",width=300)


        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #function declaration

    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='second')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                                 self.var_dep.get(),
                                                                                                                 self.var_name.get(),
                                                                                                                 self.var_designition.get(),
                                                                                                                 self.var_email.get(),
                                                                                                                 self.var_adress.get(),
                                                                                                                 self.var_married.get(),
                                                                                                                 self.var_dob.get(),
                                                                                                                 self.var_doj.get(),
                                                                                                                 self.var_idproofcomb.get(),
                                                                                                                 self.var_idproof.get(),
                                                                                                                 self.var_gender.get(),
                                                                                                                 self.var_phone.get(),
                                                                                                                 self.var_country.get(),
                                                                                                                 self.var_salary.get(),
        
        


                                
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Sucess','Employee has been added!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)    

    #fetch Data
    def fetch_data(self):  
        conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='second')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee2')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_adress.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are Required')
        else:
            try: 
                update=messagebox.askyesno('Update','Are you sure update this employeedata' )
                if update>0:
                  conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='second')
                  my_cursor=conn.cursor()
                  my_cursor.execute('update employee2 set Department=%s,Name=%s,Designition=%s,Email=%s,Adress=%s,Married_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',(
                      


                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                        self.var_designition.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_adress.get(),
                                                                                                                                                                                                                        self.var_married.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_doj.get(),
                                                                                                                                                                                                                        self.var_idproofcomb.get(),
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_country.get(),
                                                                                                                                                                                                                        self.var_salary.get(),
                                                                                                                                                                                                                        self.var_idproof.get()   
                                                                                                                                                                                                                                              
                
                                                                                                                                                                                                                        ))                                                                                                                                                                                                                            
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('sucess','Employee sucessfully updated',parent=self.root)    
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    #delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error',"All fields are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this employee',parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='second')
                    my_cursor=conn.cursor()
                    sql='delete from employee2 where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee sucessfully deleted',parent=self.root)    
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)  

    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_adress.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='second')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee2 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)  




      


    

        



        


        




if  __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

        