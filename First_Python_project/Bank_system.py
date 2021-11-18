import PIL.Image
from PIL import ImageTk
from tkinter import *
from tkinter import messagebox
import webbrowser
import mysql.connector
import re
import http.client as httplib

def checkInternetHttplib(url="www.google.com", timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception as e:
        return False
###data base
conn=checkInternetHttplib()
if conn:
    conn=checkInternetHttplib()
    db = mysql.connector.connect(
        host="sql4.freemysqlhosting.net",
        user='sql4450506',
        passwd='Jxdd9IvQxp',
        database="sql4450506"

    )
    mycursor = db.cursor()



    # main window
    window = Tk()
    window.config(bg="#262626")
    W = window.winfo_screenwidth()
    H = window.winfo_screenheight()
    window.resizable(0, 0)
    window.geometry(f"{W}x{H}+{0}+{0}")
    window.title("Banking system")
    ###Email pattern
    pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$"
    pattern2 = "^(?=.{8,20}$)(?![0-9_.-@])[a-zA-Z._]"
    # getting height and width



    ###IMGs
    def img_def(src):
        x = PIL.Image.open(src)
        x = ImageTk.PhotoImage(x)
        return x


    Loginpage = img_def("login.png")
    FB = img_def("Face.png")
    IG = img_def("Ig.jpg")
    TW = img_def("Tw.png")
    op = img_def("open.png")
    closee = img_def("close.png")
    signup = img_def("login.png")
    person = img_def("pics.png")
    login_button = img_def("login_button.png")
    signup_button = img_def("sign_button.png")
    withdraw=img_def("withdraw.png")
    temp=img_def("temp.png")
    withdraw_button=img_def("withdraw_button.png")
    send_button=img_def("Send_button.png")
    set=img_def("set.png")
    apply=img_def("Apply.jpg")
    ###post login page
    ###main login page
    def post_login():
                loginsuc = Toplevel(window)
                loginsuc.title("Personal Page")
                loginsuc.geometry(f"{W}x{H}")

                ###funcs
                # toggle button



                def toggle_login():
                    login_toggle = Frame(loginsuc, width=W // 4, height=H, bg="#12C4C0")
                    login_toggle.place(x=0, y=0)
                    ###withdraw page
                    ###settings
                    def update_info():
                        toggle = Frame(loginsuc,width=W, height=H, bg="#262626")
                        toggle.place(x=0, y=0)
                        ##func
                        def check():
                            mycursor.execute(f'select * from test where username="{loginuser}"')
                            sql_info=mycursor.fetchone()
                            sql_username = sql_info[0]
                            sql_paswd = sql_info[1]
                            sql_email = sql_info[2]




                            email=temp_email.get().strip()
                            username=temp_user.get().strip()
                            passwd=temp_passwd.get().strip()
                            new_passwd=tem_newpasswd.get().strip()
                            change_e=False
                            change_u=False
                            change_p=False
                            passwd_stat=False
                            ###
                            suc_e=False
                            suc_p=False
                            suc_u=False
                            #checking
                            if email=="":
                                messagebox.showwarning("Wrong Info", 'Email required')
                            elif email==e:
                                pass
                            else:
                                change_e = True

                            if username == "":
                                messagebox.showwarning("Wrong Info", 'Username required')

                            elif username == userx:
                                pass
                            else:
                                change_u = True
                            if passwd=="":
                                messagebox.showwarning("Wrong Info", "Password required")
                            elif passwd==sql_paswd:
                                passwd_stat=True
                            else:
                                messagebox.showwarning("Wrong Info", "Wrong password")
                            if new_passwd!="":
                                change_p=True

                            elif new_passwd=="":
                                suc_p=True
                            ###changing
                            def change_email():
                                mycursor.execute(f"update test set email='{email}' where username='{fill_username}'")
                                db.commit()
                            def change_passwd():
                                mycursor.execute(f"update test set password='{new_passwd}' where username='{fill_username}'")
                                db.commit()
                            def finish():
                                messagebox.showinfo("showinfo", "Information Updated successfully. \n You need to re-login")
                                loginsuc.destroy()
                                window.deiconify()
                                Login()

                            if passwd_stat:
                                if change_e and change_p:
                                    if 6 <= len(new_passwd) <= 20:
                                        if (re.search(pattern, email)):
                                            change_email()
                                            change_passwd()
                                            finish()
                                        else:
                                            messagebox.showwarning("Wrong Info", 'Enter valid email')

                                    else:
                                        messagebox.showwarning("Wrong Info", "Password length should be between 6 and 20")
                                elif change_e==True and change_p==False:
                                    if (re.search(pattern, email)):
                                        change_email()
                                        finish()
                                    else:
                                        messagebox.showwarning("Wrong Info", 'Enter valid email')

                                elif change_e==False and change_p==True:
                                    if 6<=len(new_passwd)<=20:
                                        change_passwd()
                                        finish()
                                    else:
                                        messagebox.showwarning("Wrong Info", "Password length should be between 6 and 20")

                        ###sql
                        current_user = loginuser
                        mycursor.execute(f'select * from test where username="{current_user}"')

                        info=mycursor.fetchone()
                        fill_username = info[0]
                        fillemail=info[2]



                        ### vars
                        temp_email=StringVar()
                        temp_user=StringVar()
                        temp_passwd=StringVar()
                        tem_newpasswd=StringVar()
                        ###Main withdraw window

                        Label(toggle,image=set).place(x=0,y=0)
                        Button(toggle, image=op, bg="#262626", command=toggle_login, compound=LEFT,
                               activebackground='#262626',
                               borderwidth=0).place(x=3, y=3)
                        ###
                        Label(toggle,text="Account settings",bg='#94BCF9',font=("Roboto",20)).place(x=930,y=150)
                        ###
                        Label(toggle, text="Email", bg='#94BCF9', font=("Roboto", 20)).place(x=650, y=250)
                        email=Entry(toggle, width=23, border=0, textvariable=temp_email, bg='#94BCF9',font=("calibri", 15))
                        e=f"{fillemail[0]}*******@"
                        email.insert(0,e)
                        email.place(x=650, y=300)
                        Frame(toggle, width=230, height=2, bg="black").place(x=650, y=328)
                        ###
                        Label(toggle, text="UserName", bg='#94BCF9', font=("Roboto", 20)).place(x=650, y=370)
                        user=Entry(toggle, width=23, border=0, textvariable=temp_user, font=("calibri", 15))
                        userx=fill_username
                        user.insert(0,userx)
                        user.config(state=DISABLED, bg='#94BCF9')
                        user.place(x=650, y=420)
                        Frame(toggle, width=230, height=2, bg="black").place(x=650, y=448)
                        ####
                        Label(toggle, text="Password", bg='#94BCF9', font=("Roboto", 20)).place(x=650, y=500)
                        psswd=Entry(toggle, width=23, border=0, textvariable=temp_passwd, bg='#94BCF9',show="*", font=("calibri", 15))
                        psswd.place(x=650, y=550)
                        Frame(toggle, width=230, height=2, bg="black").place(x=650, y=578)
                        ###
                        Label(toggle, text="New Password", bg='#94BCF9', font=("Roboto", 20)).place(x=950, y=500)
                        psswd = Entry(toggle, width=23, border=0, textvariable=tem_newpasswd, bg='#94BCF9', font=("calibri", 15),show="*")
                        psswd.insert(0, "")
                        psswd.place(x=950, y=550)
                        Frame(toggle, width=230, height=2, bg="black").place(x=950, y=578)
                        Button(toggle,image=apply,command=check,border=0,bg='#94BCF9',activebackground='#94BCF9').place(x=690,y=630)



                    ###withdraw
                    def Withdraw():
                        toggle = Frame(loginsuc,width=W, height=H, bg="#262626")
                        toggle.place(x=0, y=0)
                        ##func
                        def accountchecking():

                            try:
                                withdraw_amount = temp_withdraw.get()
                                mycursor.execute(f'select * from test where username="{loginuser}"')
                                accbalance = mycursor.fetchone()[3]
                                if withdraw_amount <= accbalance:
                                    accbalance -= withdraw_amount
                                    messagebox.showinfo("showinfo", "Done!!")
                                    mycursor.execute(
                                        f"UPDATE test SET balance = '{accbalance}' WHERE username='{loginuser}'")
                                    db.commit()
                                else:
                                    messagebox.showwarning("Wrong Info", "The account balance can't handel the payment")
                            except:
                                messagebox.showwarning("Wrong Info", "Please Enter Integer Number")



                        ###Variable
                        temp_withdraw=IntVar()
                        ###Main withdraw window
                        Button(toggle, image=op, bg="#262626", command=toggle_login, compound=LEFT,
                               activebackground='#262626',
                               borderwidth=0).place(x=0, y=0)
                        label=Label(toggle,image=temp,bg="#262626").place(x=770,y=300)
                        Label(toggle,image=withdraw,bg="#C4C4C4").place(x=910,y=320)
                        Label(toggle,text="Enter The amount",bg="#C4C4C4",fg="#262626",font=("Roboto",20)).place(x=850,y=450)
                        Entry(toggle,width=23,border=0,textvariable=temp_withdraw,bg="#C4C4C4",font=("calibri",15)).place(x=850,y=500)
                        Frame(toggle,width=230,height=2,bg="black").place(x=850,y=528)

                        Button(toggle,image=withdraw_button,bg="#C4C4C4",border=0,activebackground="#C4C4C4",command=accountchecking).place(x=900,y=550)

                    ##moeny transfer page
                    def transfer_money():
                        def transfer_check():


                            ###
                            try:
                                amount=temp_amount.get()
                                transfer_to=temp_transed.get()
                                if amount=="" or transfer_to=="":
                                    messagebox.showwarning("Wrong Info", "All fields are required")
                                else:
                                    mycursor.execute(f"SELECT * from test where username='{transfer_to}'")
                                    data = mycursor.fetchall()
                                    rcount = mycursor.rowcount
                                    if rcount == 1 and transfer_to!=loginuser:
                                        mycursor.execute(f"select * from test where username='{loginuser}'")
                                        user_balance = mycursor.fetchone()[3]
                                        mycursor.execute(f"select * from test where username='{transfer_to}'")
                                        second_balance = mycursor.fetchone()[3]
                                        if user_balance >= amount:
                                            new_user_balance = user_balance - amount
                                            mycursor.execute(
                                                f"update test set balance={new_user_balance} where username='{loginuser}'")
                                            db.commit()
                                            sec_new_balance = second_balance + amount
                                            mycursor.execute(
                                                f"update test set balance={sec_new_balance} where username='{transfer_to}'")
                                            db.commit()
                                            messagebox.showinfo("showinfo", "Done!!")

                                        else:

                                            messagebox.showwarning("Wrong Info", "The account balance cant handel the payment")




                                    else:

                                        messagebox.showwarning("Wrong Info", "The account u want to transfer doesn't exist")
                            except:
                                messagebox.showwarning("Wrong Info", "Please Integer Number")











                        toggle = Frame(loginsuc, width=W, height=H, bg="#262626")
                        toggle.place(x=0, y=0)


                        ###variable

                        temp_amount=IntVar()
                        temp_transed=StringVar()
                        ###Main transfer window
                        Button(toggle, image=op, bg="#262626", command=toggle_login, compound=LEFT,
                               activebackground='#262626',
                               borderwidth=0).place(x=0, y=0)
                        Label(toggle, image=temp, bg="#262626").place(x=770, y=300)
                        #amount
                        Label(toggle, image=withdraw, bg="#C4C4C4").place(x=910, y=320)
                        #amount entry
                        Label(toggle, text="Enter The amount", bg="#C4C4C4", fg="#262626", font=("Roboto", 20)).place(x=850,y=450)
                        Entry(toggle, width=23, border=0, textvariable=temp_amount, bg="#C4C4C4",
                              font=("calibri", 15)).place(x=850, y=500)
                        Frame(toggle, width=230, height=2, bg="black").place(x=850, y=528)
                        #account entry
                        Label(toggle, text="Enter account Username", bg="#C4C4C4", fg="#262626", font=("Roboto", 20)).place(x=825,y=560)
                        Entry(toggle, width=23, border=0, textvariable=temp_transed, bg="#C4C4C4",font=("calibri", 15)).place(x=850, y=610)
                        Frame(toggle, width=230, height=2, bg="black").place(x=850, y=638)


                        Button(toggle, image=send_button, bg="#C4C4C4", border=0, activebackground="#C4C4C4",
                               command=transfer_check).place(x=900, y=680)

                    def logout():
                        loginsuc.destroy()
                        window.deiconify()
                        Login()


                    def destroy():
                        login_toggle.destroy()

                    Button(login_toggle, image=closee, bg="#12C4C0", command=destroy, compound=LEFT,
                           activebackground='#12C4C0', borderwidth=0).place(x=0, y=0)

                    # toggle buttons
                    Button(login_toggle, text="Home Page",
                           width=45,
                           height=1,
                           fg='white',
                           border=0,
                           bg='black',
                           font=('calibri', 14),
                           activebackground='#0f9d9a',
                           command=None, anchor=CENTER).place(x=5, y=80)
                    Button(login_toggle, text="Withdraw",
                           width=45,
                           height=1,
                           fg='white',
                           border=0,
                           bg='black',
                           font=('calibri', 14),
                           activebackground='#0f9d9a',
                           command=Withdraw, anchor=CENTER).place(x=5, y=120)
                    Button(login_toggle, text="Transfer Money",
                           width=45,
                           height=1,
                           fg='white',
                           border=0,
                           bg='black',
                           font=('calibri', 14),
                           activebackground='#0f9d9a',
                           command=transfer_money, anchor=CENTER).place(x=5, y=160)
                    Button(login_toggle, text="Account settings",
                           width=45,
                           height=1,
                           fg='white',
                           border=0,
                           bg='black',
                           font=('calibri', 14),
                           activebackground='#0f9d9a',
                           command=update_info, anchor=CENTER).place(x=5, y=200)
                    Button(login_toggle, text="LOGOUT",
                           width=45,
                           height=1,
                           fg='white',
                           border=0,
                           bg='black',
                           font=('calibri', 14),
                           activebackground='#0f9d9a',
                           command=logout, anchor=CENTER).place(x=5, y=240)

                    # social
                    Button(login_toggle, image=IG, bg="#262626", command=instagram, compound=LEFT,
                           activebackground='#FF00EC', borderwidth=0).place(x=10, y=900)
                    Button(login_toggle, image=FB, bg="#262626", command=facebook, compound=LEFT,
                           activebackground='#1178F2', borderwidth=0).place(x=200, y=900)
                    Button(login_toggle, image=TW, bg="#262626", command=twitch, compound=LEFT,
                           activebackground='#7C00AF', borderwidth=0).place(x=400, y=900)


                ###main
                Label(loginsuc, width=W, height=H, bg="#262626").place(x=0, y=0)
                Button(loginsuc, image=op, bg="#262626", command=toggle_login, compound=LEFT,
                       activebackground='#262626',
                       borderwidth=0).place(x=0, y=0)

                mainloop()




    ### button funcs

    def login_buttonn():

        ####
        global loginuser
        loginuser = login_user.get()
        loginpasswd = login_passwd.get()
        if loginpasswd == "" or loginuser == "":
            messagebox.showwarning("Wrong Info", "All fields required *")

        else:
            mycursor.execute(f'SELECT * FROM test where username ="{loginuser}"')
            data = mycursor.fetchall()
            rcount = mycursor.rowcount
            if rcount == 0:
                messagebox.showwarning("Wrong Info", "Account Doesn't exist *")
            else:
                ####checking the user and the password
                mycursor.execute(
                    f'SELECT * FROM test where username ="{loginuser}" and password="{loginpasswd}"')
                data = mycursor.fetchall()
                rcount = mycursor.rowcount
                if rcount > 0:
                    found = True

                else:
                    messagebox.showwarning("Wrong Info", "Wrong password *")
                    found = False
                if found:
                    # disable main window
                    window.withdraw()
                    post_login()

    def regButt():
        reguser = reg_user.get()
        regpassowrd = reg_password.get()
        regemail = reg_email.get()
        try:
            regbalance = reg_balance.get()
            if reguser == "" or regpassowrd == "" or regemail == "" or regbalance == "":
                messagebox.showwarning("Wrong Info", "All fields required *")
            else:
                if (re.search(pattern, regemail)):
                    if (re.search(pattern2, reguser)):
                        if 6 <= len(regpassowrd) <= 20:

                            mycursor.execute(f'SELECT * FROM test where username ="{reguser}"')
                            data = mycursor.fetchall()
                            rcount = mycursor.rowcount
                            if rcount > 0:
                                messagebox.showwarning("Wrong Info", "The account already exist *")
                            else:
                                mycursor.execute(
                                    'insert into test (username,password,email,balance) values (%s,%s,%s,%s)',
                                    (reguser, regpassowrd, regemail, regbalance))
                                db.commit()
                                messagebox.showinfo("showinfo", "Done!!")
                        else:
                            messagebox.showwarning("Wrong Info", "Password length should be between 6 and 20*")
                    else:
                        messagebox.showwarning("Wrong Info", "Username length should be at least 8 letters. \n **Username can contain  '_ / . ' but no at the beginning \n or the end of it")
                else:
                    messagebox.showwarning("Wrong Info", "Enter a valid email *")
        except:
            messagebox.showwarning("Wrong Info", "Please Enter Integer Value")



    ###funcs

    def instagram():
        webbrowser.open('https://www.instagram.com/hassankhaled002/')


    def facebook():
        webbrowser.open('https://www.facebook.com/hassadaja84')


    def twitch():
        webbrowser.open('https://www.twitch.tv/moonhassan')

    def Login():
        def bttn(x, y, text, cmd, bcolor='#7898CC', fcolor='#94BBF9'):
            Button(window, text=text,
                   width=150,
                   height=2,
                   fg='#262626',
                   border=0,
                   bg="#94BBF9",
                   font=('calibri', 12),
                   activebackground=bcolor,
                   command=cmd).place(x=x, y=y)


        reg_toggle = Frame(window, width=W, height=H, bg="#262626")
        reg_toggle.place(x=0, y=45)
        bttn(0, 0, 'Login', Login)
        bttn(1000, 0, 'Register', Reg)

        reg_toggle = Frame(window, width=W, height=H, bg="#262626")
        reg_toggle.place(x=0, y=45)
        label = Label(window, image=Loginpage, bg="#262626")
        label.place(x=0, y=45)
        panel = Label(window, image=person, width=150, height=150, border=0)
        panel.place(x=925, y=270)
        # login vars
        global login_user
        global login_passwd
        login_user = StringVar()
        login_passwd = StringVar()
        # user name entry
        Label(window, width=40, text="U S E R N A M E", bg='#94BCF9', fg="#262626", font=('Roboto', 18)).place(x=720, y=470)
        Entry(window, width=23, font=('Roboto'), textvariable=login_user, border=0, bg='#94BCF9').place(x=830, y=530)
        Frame(window, width=393, height=2, bg='black').place(x=830, y=562)
        # password entry
        Label(window, width=41, text="P A S S W O R D", bg='#94BCF9', fg="#262626", font=('Roboto', 18)).place(x=705, y=600)
        Entry(window, width=23, font=('Roboto'), textvariable=login_passwd, border=0, bg='#94BCF9', show='*').place(x=830,
                                                                                                                    y=660)
        Frame(window, width=393, height=2, bg='black').place(x=830, y=692)
        # login button
        Button(window, image=login_button, bg="#94BBF9", command=login_buttonn, compound=LEFT, borderwidth=0,
               activebackground='#94BBF9').place(x=900, y=730)


    def Reg():
        def bttn(x, y, text, cmd, bcolor='#7898CC', fcolor='#94BBF9'):
            Button(window, text=text,
                   width=150,
                   height=2,
                   fg='#262626',
                   border=0,
                   bg="#94BBF9",
                   font=('calibri', 12  ),
                   activebackground=bcolor,
                   command=cmd).place(x=x, y=y)

        reg_toggle = Frame(window, width=W, height=H, bg="#262626")
        reg_toggle.place(x=0, y=45)
        bttn(0, 0, 'Login', Login)
        bttn(1000, 0, 'Register', Reg)

        f2 = Frame(window, width=W, height=H, bg="#262626")
        f2.place(x=0, y=45)
        label = Label(window, image=signup, bg="#262626")
        label.place(x=0, y=45)
        panel = Label(window, image=person, width=150, height=150, border=0)
        panel.place(x=925, y=170)
        ###reg_vars
        global reg_user
        global reg_password
        global reg_email
        global reg_balance
        reg_user = StringVar()
        reg_password = StringVar()
        reg_email = StringVar()
        reg_balance = IntVar()
        # username entry
        Label(window, width=40, text="U S E R N A M E", bg='#94BCF9', fg="#262626", font=('Roboto', 18)).place(x=720,
                                                                                                               y=370)
        Entry(window, width=23, font=('Roboto'), textvariable=reg_user, border=0, bg='#94BCF9').place(x=830, y=430)
        Frame(window, width=393, height=2, bg='black').place(x=830, y=462)
        # password entry
        Label(window, width=41, text="P A S S W O R D", bg='#94BCF9', fg="#262626", font=('Roboto', 18)).place(x=705,
                                                                                                               y=500)
        Entry(window, width=23, font=('Roboto'), textvariable=reg_password, border=0, bg='#94BCF9', show='*').place(x=830,
                                                                                                                    y=560)
        Frame(window, width=393, height=2, bg='black').place(x=830, y=592)
        # email
        Label(window, width=41, text="E M A I L", bg='#94BCF9', fg="#262626", font=('Roboto', 18)).place(x=705,
                                                                                                         y=630)
        Entry(window, width=23, font=('Roboto'), textvariable=reg_email, border=0, bg='#94BCF9').place(x=830, y=690)
        Frame(window, width=393, height=2, bg='black').place(x=830, y=722)
        # age

        Label(window, width=41, text="B A L A N C E", bg='#94BCF9', fg="#262626", font=('Roboto', 18)).place(x=705,y=760)
        Entry(window, width=23, font=('Roboto'), textvariable=reg_balance, border=0, bg='#94BCF9').place(x=830, y=820)
        Frame(window, width=393, height=2, bg='black').place(x=830, y=852)
        # signUp button
        Button(window, image=signup_button, bg="#94BBF9", command=regButt, compound=LEFT, borderwidth=0,
               activebackground='#94BBF9').place(x=900, y=900)


    def toggle_win():
        global f1
        f1 = Frame(window, width=W // 4, height=H, bg="black")
        f1.place(x=0, y=46)

        def dele():
            f1.destroy()

        Button(f1, image=closee, bg="#262626", command=dele, compound=LEFT, borderwidth=0).place(x=4, y=0)
        Button(f1, image=IG, bg="#262626", command=instagram, compound=LEFT, borderwidth=0).place(x=10, y=900)
        Button(f1, image=FB, bg="#262626", command=facebook, compound=LEFT, borderwidth=0).place(x=200, y=900)
        Button(f1, image=TW, bg="#262626", command=twitch, compound=LEFT, borderwidth=0).place(x=400, y=900)




    ###
    Login()





    window.mainloop()
else:
    messagebox.showwarning("Wrong Info", "Check your internet connection")


