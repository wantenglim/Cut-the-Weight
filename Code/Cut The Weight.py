from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
import math
import random
import datetime
import time;
import os

foods = []
prices = []
calories = []
foodRedeem = []
pointRedeem = []
test = []

def register_success ():
  global screen7
  screen7 = Toplevel(screen)
  screen7.grid()
  screen7.geometry("250x120+0+0")
  screen7.resizable(False,False)
  screen7.configure(background='white')
  screen7.update_idletasks()
  width = screen7.winfo_width()
  height = screen7.winfo_height()
  x = (screen7.winfo_screenwidth() // 2) - (width // 2)
  y = (screen7.winfo_screenheight() // 2) - (height // 2)
  screen7.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen7.title ("Register Success")
  Label(screen7 , text="Register Success" ,bg="white",fg = "green" ,font = ("calibri", 11)).pack()
  Button(screen7 , text="OK" , command = delete5).pack()

def register_fail ():
  global screen8
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  re_password_entry.delete(0,END)
  screen8 = Toplevel(screen)
  screen8.grid()
  screen8.geometry("250x120+0+0")
  screen8.resizable(False,False)
  screen8.configure(background='white')
  screen8.update_idletasks()
  width = screen8.winfo_width()
  height = screen8.winfo_height()
  x = (screen8.winfo_screenwidth() // 2) - (width // 2)
  y = (screen8.winfo_screenheight() // 2) - (height // 2)
  screen8.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen8.title ("Register Fail")
  Label(screen8 , text="Register Fail" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Label(screen8 , text="").pack()
  Label(screen8 , text="Please Make Sure Password enter are the same !" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Button(screen8 , text="OK" , command = delete6).pack()

def register_fail1 ():
  global screen8
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  re_password_entry.delete(0,END)
  screen8 = Toplevel(screen)
  screen8.grid()
  screen8.geometry("250x120+0+0")
  screen8.resizable(False,False)
  screen8.configure(background='white')
  screen8.update_idletasks()
  width = screen8.winfo_width()
  height = screen8.winfo_height()
  x = (screen8.winfo_screenwidth() // 2) - (width // 2)
  y = (screen8.winfo_screenheight() // 2) - (height // 2)
  screen8.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen8.title ("Register Fail")
  Label(screen8 , text="Register Fail" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Label(screen8 , text="").pack()
  Label(screen8 , text="Please Make Sure No Empty Space Between Characters !" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Button(screen8 , text="OK" , command = delete6).pack()

def register_fail2 ():
  global screen8
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  re_password_entry.delete(0,END)
  screen8 = Toplevel(screen)
  screen8.grid()
  screen8.geometry("250x120+0+0")
  screen8.resizable(False,False)
  screen8.configure(background='white')
  screen8.update_idletasks()
  width = screen8.winfo_width()
  height = screen8.winfo_height()
  x = (screen8.winfo_screenwidth() // 2) - (width // 2)
  y = (screen8.winfo_screenheight() // 2) - (height // 2)
  screen8.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen8.title ("Register Fail")
  Label(screen8 , text="Register Fail" ,bg="white", fg = "red" ,font = ("calibri", 11)).pack()
  Label(screen8 , text="").pack()
  Label(screen8 , text="Username and Password Cannot be Empty !" ,bg="white", fg = "red" ,font = ("calibri", 11)).pack()
  Button(screen8 , text="OK" , command = delete6).pack()

def register_fail3 ():
  global screen8
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  re_password_entry.delete(0,END)
  screen8 = Toplevel(screen)
  screen8.geometry = "250X120"
  screen8.resizable(0,0)
  screen8.title ("Register Fail")
  Label(screen8 , text="Register Fail", bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Label(screen8 , text="").pack()
  Label(screen8 , text="Please Make Sure The Username and Password is more than 5 Characters" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Button(screen8 , text="OK" , command = delete6).pack()

def register_fail4 ():
  global screen8
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  re_password_entry.delete(0,END)
  screen8 = Toplevel(screen)
  screen8.geometry = "250X120"
  screen8.resizable(0,0)
  screen8.title ("Register Fail")
  Label(screen8 , text="Register Fail" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Label(screen8 , text="").pack()
  Label(screen8 , text="Please Make Sure The Password Contains at least 1 uppercase !" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Button(screen8 , text="OK" , command = delete6).pack()
  
def register_fail5 ():
  global screen8
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  re_password_entry.delete(0,END)
  screen8 = Toplevel(screen)
  screen8.grid()
  screen8.geometry("250x120+0+0")
  screen8.resizable(False,False)
  screen8.configure(background='white')
  screen8.update_idletasks()
  width = screen8.winfo_width()
  height = screen8.winfo_height()
  x = (screen8.winfo_screenwidth() // 2) - (width // 2)
  y = (screen8.winfo_screenheight() // 2) - (height // 2)
  screen8.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen8.title ("Register Fail")
  Label(screen8 , text="Register Fail" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Label(screen8 , text="").pack()
  Label(screen8 , text="Please Make Sure Password Contains  at least 1 Alphabet !" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Button(screen8 , text="OK" , command = delete6).pack()

def register_fail6 ():
  global screen8
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  re_password_entry.delete(0,END)
  screen8 = Toplevel(screen)
  screen8.grid()
  screen8.geometry("250x120+0+0")
  screen8.resizable(False,False)
  screen8.configure(background='white')
  screen8.update_idletasks()
  width = screen8.winfo_width()
  height = screen8.winfo_height()
  x = (screen8.winfo_screenwidth() // 2) - (width // 2)
  y = (screen8.winfo_screenheight() // 2) - (height // 2)
  screen8.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen8.title ("Register Fail")
  Label(screen8 , text="Register Fail" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Label(screen8 , text="").pack()
  Label(screen8 , text="Please Make Sure The Password Contains at least 1 digit !",bg="white" ,fg = "red" ,font = ("calibri", 11)).pack()
  Button(screen8 , text="OK" , command = delete6).pack()

def register_fail7 ():
  global screen8
  global screen8
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  re_password_entry.delete(0,END)
  screen8 = Toplevel(screen)
  screen8.geometry = "250X120"
  screen8.resizable(0,0)
  screen8.title ("Register Fail")
  Label(screen8 , text="Register Fail" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Label(screen8 , text="").pack()
  Label(screen8 , text="Please Make Sure The Password Contains at least 1 lowercase !" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Button(screen8 , text="OK" , command = delete6).pack()


def user_existed ():
  global screen9
  screen9 = Toplevel(screen)
  screen9.grid()
  screen9.geometry("250x120+0+0")
  screen9.resizable(False,False)
  screen9.configure(background='white')
  screen9.update_idletasks()
  width = screen9.winfo_width()
  height = screen9.winfo_height()
  x = (screen9.winfo_screenwidth() // 2) - (width // 2)
  y = (screen9.winfo_screenheight() // 2) - (height // 2)
  screen9.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen9.title ("Register Fail")
  Label(screen9 , text="Register Fail" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Label(screen9 , text="").pack()
  Label(screen9 , text="User Existed" ,bg="white",fg = "red" ,font = ("calibri", 11)).pack()
  Button(screen9 , text="OK" , command = delete7).pack()
  
  
def delete1() :
  screen.destroy()
  main_screen()
  
def delete2():
  screen3.destroy()
  screen2.destroy()
  screen.destroy()
  if __name__ == "__main__":
    root = MainMenu(None)
    root.title("Main Menu")
    root.mainloop()
 
def delete3():
  screen4.destroy()
 
def delete4():
  screen5.destroy()

def delete5() :
  screen7.destroy()
  screen1.destroy()
  
def delete6() :
  screen8.destroy()

def delete7():
  screen9.destroy()

def about():
    messagebox.showinfo("Welcome" ,"This is a Cut The Weight Vending Machine. \nTerm & Condition:\n1. Charge RM5.00 for first time member registration\n2. Free 50 points for new member\n3. Each purchase can only buy 4 items.\n4. RM 1 = 1 point")
  
  
def points() :
  global point
  global fee
  all_files = os.listdir()
  if username1+"point" in all_files :
    file = open(username1+"point", "r")
    verify=file.read().splitlines()
    point = int(verify[0])
    fee = int(verify[1])
   
def login_success():
  global screen3
  global status
  screen3 = Toplevel(screen)
  screen3.grid()
  screen3.geometry("150x100+0+0")
  screen3.resizable(False,False)
  screen3.configure(background='white')
  screen3.update_idletasks()
  width = screen3.winfo_width()
  height = screen3.winfo_height()
  x = (screen3.winfo_screenwidth() // 2) - (width // 2)
  y = (screen3.winfo_screenheight() // 2) - (height // 2)
  screen3.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen3.title("Success")
  Label(screen3, text = "Login Success" ,bg="white",fg="green").pack()
  Button(screen3, text = "OK", command =delete2 ).pack()
  status = "member"
  points()
  
 
def password_error():
  global screen4
  screen4 = Toplevel(screen)
  screen4.grid()
  screen4.geometry("150x100+0+0")
  screen4.resizable(False,False)
  screen4.configure(background='white')
  screen4.update_idletasks()
  width = screen4.winfo_width()
  height = screen4.winfo_height()
  x = (screen4.winfo_screenwidth() // 2) - (width // 2)
  y = (screen4.winfo_screenheight() // 2) - (height // 2)
  screen4.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen4.title("Login Fail")
  Label(screen4, text = "Password Error" ,bg="white",fg="red").pack()
  Button(screen4, text = "OK", command =delete3).pack()
 
def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.grid()
  screen5.geometry("150x100+0+0")
  screen5.resizable(False,False)
  screen5.configure(background='white')
  screen5.update_idletasks()
  width = screen5.winfo_width()
  height = screen5.winfo_height()
  x = (screen5.winfo_screenwidth() // 2) - (width // 2)
  y = (screen5.winfo_screenheight() // 2) - (height // 2)
  screen5.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen5.title("Success")
  Label(screen5, text = "User Not Found",bg="white",fg="red").pack()
  Button(screen5, text = "OK", command =delete4).pack()
 
   
def register_user():

  global username_info
  global point 
  username_info = username.get()
  password_info = password.get()
  point = 50
 
  file=open(username_info.lower(), "w")
  file.write(username_info.lower()+"\n")
  file.write(password_info)
  file.close()


  file1=open(username_info +"point","w")
  file1.write("{}".format(point)+"\n")
  file1.write("5")
  file1.close()


  username_entry.delete(0, END)
  password_entry.delete(0, END)
  re_password_entry.delete(0,END)
  register_success()
 
def login_verify():
  global username1
   
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
 
  all_files = os.listdir()
  if username1.lower() in all_files: 
    file = open(username1.lower(), "r")
    verify = file.read().splitlines()
    if password1 == verify[1]: 
        login_success()
    else:
        password_error()
 
  else:
        user_not_found()
   
 
def registration_check() :
  global username_check
  username_check = username.get()
  password_check = password.get()
  re_password_check = re_password.get()
  all_files = os.listdir()    
  if " " in password_check or " " in username_check:
      register_fail1()
     
  elif username_check == "" or password_check == "" :
      register_fail2()

  elif len(username_check) < 5 or len(password_check)<5 :
      register_fail3()

  elif password_check.islower() == True :
      register_fail4()

  elif password_check.isdigit() == True :
      register_fail5()

  elif password_check.isdigit() == True :
      register_fail6()

  elif password_check.isupper() == True :
      register_fail7()
  
  elif username_check.lower() not in all_files :
      password_check = password.get()
      re_password_check = re_password.get()
      if  password_check == re_password_check :
          register_user()
            
      else :
          register_fail()

  else : 
         username_entry.delete(0, END)
         password_entry.delete(0, END)
         re_password_entry.delete(0,END)
         user_existed()
                  
def register():
  global screen1  
  global username
  global password
  global re_password
  global username_entry
  global password_entry
  global re_password_entry
  screen1 = Toplevel(screen)
  screen1.geometry("250x100+0+0")
  screen1.resizable(False,False)
  screen1.configure(background='white')
  screen1.update_idletasks()
  width = screen1.winfo_width()
  height = screen1.winfo_height()
  x = (screen1.winfo_screenwidth() // 2) - (width // 2)
  y = (screen1.winfo_screenheight() // 2) - (height // 2)
  screen1.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  screen1.title("Register")  
  username = StringVar()
  password = StringVar()
  re_password = StringVar()

 
  Label(screen1, text = "Please enter details below")
  Label(screen1, text = "")
  Label(screen1, text = "Username : ",bg="white").grid(row = 0 , column = 0)
  
  username_entry = Entry(screen1, textvariable = username)
  username_entry.grid(row = 0 , column = 1)
  Label(screen1, text = "Password : ",bg="white").grid(row = 1 , column = 0)
  password_entry =  Entry(screen1, textvariable = password , show = "*")
  password_entry.grid(row = 1 , column = 1)
  Label(screen1, text = "")
  Label(screen1, text = "Re-Enter Password : ", bg="white").grid(row = 2 , column = 0)
  re_password_entry = Entry(screen1, textvariable = re_password , show = "*")
  re_password_entry.grid(row = 2 , column = 1)
  Label(screen1, text = "")
  Button(screen1, text = "Register", width = 10, height = 1, command = registration_check).grid(row = 3 , column = 0)
  Button(screen1, text = "Cancel", width = 10, height = 1, command = delete1).grid(row = 3 , column = 1)
  
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.grid()
  screen2.geometry("230x80+0+0")
  screen2.resizable(False,False)
  screen2.title("Login")
  screen2.configure(background='white')
  screen2.update_idletasks()
  width = screen2.winfo_width()
  height = screen2.winfo_height()
  x = (screen2.winfo_screenwidth() // 2) - (width // 2)
  y = (screen2.winfo_screenheight() // 2) - (height // 2)
  screen2.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  Label(screen2, text = "Please enter details below to login")
  Label(screen2, text = "")
 
  global username_verify
  global password_verify
   
  username_verify = StringVar()
  password_verify = StringVar()
 
  global username_entry1
  global password_entry1
   
  Label(screen2, text = "Username : ",bg="white").grid(row=0 , column = 0)
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.grid(row=0 ,column=1)
  Label(screen2, text = "")
  Label(screen2, text = "Password  : ",bg="white").grid(row = 1 ,column = 0)
  password_entry1 = Entry(screen2, textvariable = password_verify , show = "*")
  password_entry1.grid(row= 1 , column = 1)
  Label(screen2, text = "")
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).grid(row=3 , column = 0)
  Button(screen2, text = "Cancel", width = 10, height = 1, command = delete1).grid(row=3 , column = 1)
  
def guest() :
  global status 
  status = "guest"
  screen.destroy()
  if __name__ == "__main__":
    root = MainMenu(None)
    root.title("Main Menu")
    root.mainloop()
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("530x620+0+0")
  screen.resizable(False,False)
  screen.title("Cut The Weight")
  screen.configure(background='white')
  screen.update_idletasks()
  width = screen.winfo_width()
  height = screen.winfo_height()
  x = (screen.winfo_screenwidth() // 2) - (width // 2)
  y = (screen.winfo_screenheight() // 2) - (height // 2)
  screen.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  font_title = font.Font(family = "Helvetica", size = 64, weight = "bold")
  Label(text = "Cut \nThe Weight", font = font_title, bg = "black", fg = "white").grid(row=1,padx=35)
  Button(text = "Login", width = "14", command = login , font=("Tahoma",25)).grid(row=3,pady=15)
  Button(text = "Register", width = "14", command = register ,font=("Tahoma",25)).grid(row=5,pady=15)
  Button(text = "Guest" , width = "14" , command = guest,font=("Tahoma",25)).grid(row=7,pady=15)
  Button(text = "About",  width = "10" , command = about, font=("Tahoma",18)).grid(row=8,pady=15)
  screen.mainloop()


class MainMenu(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
    def initialize(self):
        # Set up grid for widgets
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

        # Create custom fonts
        self.font_title = font.Font(family = "Helvetica", size = 64, weight = "bold")
        self.font_button1 = font.Font(family = "Tahoma", size = 25)
        self.font_button2 = font.Font(family = "Tahoma", size = 15)

        # Create title text for main menu
        label_title = Label(self, text = "Cut\nThe Weight", bg = "black", fg = "white",font=self.font_title)
        label_title.grid(sticky=E+W, pady = 10)


        # Create buttons for the menu
        button_food = Button(text = "FOOD", bg = "red", fg = "white", font = self.font_button1, command = self.food)
        button_beverage = Button(text = "BEVERAGE", bg = "yellow", fg = "black", font = self.font_button1, command = self.beverage)
        button_setMeal = Button(text = "SET MEAL", bg = "blue", fg = "white", font = self.font_button1, command = self.setMeal)
        button_logOut = Button(text = "Log Out", font = self.font_button2, command = self.logOut)

        button_food.grid(row = 1, pady = 10)
        button_beverage.grid(row = 2, pady = 10)
        button_setMeal.grid(row = 3, pady = 10)
        button_logOut.grid(row = 4, pady = 2)
        self.centralize_window()
    
    
    def food(self):
        self.destroy()
        # Go to food windows
        FoodPage(None).title("Food Pg1")
        
    def beverage(self):
        self.destroy()
        # Go to beverage windows
        BeveragePage(None).title("Beverage Pg1")

    def setMeal(self):
        import datetime
        now = datetime.datetime.now()
        if now.hour >= 0 and now.hour < 11:
            self.destroy()
            BreakfastPage(None).title("Breakfast")
        elif now.hour >= 11 and now.hour < 18:
            self.destroy()
            LunchPage(None).title("Lunch")
        else:
            self.destroy()
            DinnerPage(None).title("Dinner")
        
    def logOut(self):
        qExit = messagebox.askyesno("Log Out","Do you want to log out and quit Cut the Weight Vending Machine?")
        if qExit > 0:
          self.destroy()
          return
        
        
# Foodpage 1       
class FoodPage(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.minsize(650, 500)
        self.maxsize(650, 500)
        self.configure(bg="white")
        border1 = Frame(self, relief=SOLID, borderwidth=3)
        border1.place(relx=0.02, rely=0.20, anchor=NW)
        border2 = Frame(self,relief = SOLID, borderwidth=3)
        border2.place(relx=0.37 , rely=0.20, anchor=NW)
        border3 = Frame(self,relief = SOLID, borderwidth=3)
        border3.place(relx=0.72, rely=0.20, anchor=NW)

        # Create custom fonts
        self.font_titleFood = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.font_label_1 = font.Font(family = "Tahoma", size = 14)
        self.font_label_2 = font.Font(family = "Tahoma", size = 12)

        # Create title text for main menu
        label_titleFood = Label(self, text = "FOOD", bg = "black", fg = "white",font=self.font_titleFood)
        label_titleFood.grid(row=0,column=2, padx = 181, pady = 10)

        # Labels (top)
        self.label_point = Label(text = "Point:", bg = "light pink", font = self.font_label_1)

        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="Back", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_finishOrder = Button(text="Finish Order", bg="firebrick1", fg="white", font = self.font_label_2, command=self.finishOrder)
        self.img_next= PhotoImage(file="Photo/Food/right_arrow.png")
        self.button_next = Button(bg="lightyellow", image = self.img_next, command=self.food2)
        
        
        # Labels & button (Using borders)-LEFT
        self.img_food_name1 = PhotoImage(file="Photo/Food/turkey_sandwich.gif")
        self.canvas_food1 = Canvas(border1, width = 150 , height = 150)
        self.layer_food1 = self.canvas_food1.create_image(20, 20,image = self.img_food_name1)
        self.label_food_name1 = Label(border1,text = "Turkey\nsandwich", font = self.font_label_2,justify = LEFT)
        self.label_food_price1 = Label(border1,text = "RM 3.50", font = self.font_label_2,justify = LEFT)
        self.button_select1 = Button(border1,text="Select", bg="yellow", fg="black", command=self.select1)

         # Labels & button (Using borders)-center
        self.img_food_name2 = PhotoImage(file="Photo/Food/avocado_tomato_salad.gif")
        self.canvas_food2 = Canvas(border2, width = 150 , height = 150)
        self.layer_food2 = self.canvas_food2.create_image(20, 20,image = self.img_food_name2)
        self.label_food_name2 = Label(border2,text = "Avocado\ntomato salad", font = self.font_label_2, justify = LEFT)
        self.label_food_price2 = Label(border2,text = "RM 4.00", font = self.font_label_2, justify = LEFT)
        self.button_select2 = Button(border2,text="Select", bg="yellow", fg="black", command=self.select2)
        
         # Labels & button (Using borders)-right
        self.img_food_name3 = PhotoImage(file="Photo/Food/tuna_salad_pita.gif")
        self.canvas_food3 = Canvas(border3, width = 150 , height = 150)
        self.layer_food3= self.canvas_food3.create_image(20, 20,image = self.img_food_name3)
        self.label_food_name3 = Label(border3,text = "Tuna\nsalad pita", font = self.font_label_2, justify = LEFT)
        self.label_food_price3 = Label(border3,text = "RM 4.50", font = self.font_label_2, justify = LEFT)
        self.button_select3 = Button(border3,text="Select", bg="yellow", fg="black", command=self.select3)

        
        # Layout widgets
        # First column
        self.label_point.grid(row = 0, column = 0,padx = 10, pady = 5, columnspan = 2,sticky = N)
        self.canvas_food1.grid(row=1, column=1, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name1.grid(row = 5, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price1.grid(row = 6, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select1.grid(row = 8, column = 1, padx = 60, pady = 5, columnspan = 10, sticky = W)

        # Second column
        self.canvas_food2.grid(row=1, column=2, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name2.grid(row = 5, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price2.grid(row = 6, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select2.grid(row = 8, column = 2, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.button_back.grid(row = 8, column = 2, padx = 8, pady = 340, columnspan = 1, sticky = SW)
        self.button_finishOrder.grid(row = 8,column = 2, padx = 5, pady = 340, columnspan = 1,sticky = S)
        self.button_next.grid(row = 8, column = 2, padx = 20, pady = 340, columnspan = 1, sticky = SE)

        # Third column
        self.button_shoppingCart.grid(row = 0, column = 3, padx = 25, pady = 5, columnspan = 2,sticky = N)
        self.canvas_food3.grid(row=1, column=3, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name3.grid(row = 5, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price3.grid(row = 6, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select3.grid(row = 8, column = 3, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.centralize_window()
        
        if status == "member":
          self.point_info = Label(text = "{}".format(point),bg="white", font = self.font_label_2, justify = LEFT)
          self.point_info.place(x=70,y=8)

    def select1(self):
        self.destroy()
        FoodSelect1(None).title("Food 1")
        
    def select2(self):
        self.destroy()
        FoodSelect2(None).title("Food 2")

    def select3(self):
        self.destroy()
        FoodSelect3(None).title("Food 3")

    def back(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def finishOrder(self):
        self.destroy()
        totalCalories(None).title("Summary of Order")

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def food2(self):
        self.destroy()
        FoodPage2(None).title("Food Pg2")


        
# Foodpage 2
class FoodPage2(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.minsize(650, 500)
        self.maxsize(650, 500)
        self.configure(bg="white")
        border1 = Frame(self, relief=SOLID, borderwidth=3)
        border1.place(relx=0.02, rely=0.20, anchor=NW)
        border2 = Frame(self,relief = SOLID, borderwidth=3)
        border2.place(relx=0.37 , rely=0.20, anchor=NW)
        border3 = Frame(self,relief = SOLID, borderwidth=3)
        border3.place(relx=0.72, rely=0.20, anchor=NW)

        # Create custom fonts
        self.font_titleFood = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.font_label_1 = font.Font(family = "Tahoma", size = 14)
        self.font_label_2 = font.Font(family = "Tahoma", size = 12)

        # Create title text for main menu
        label_titleFood = Label(self, text = "FOOD", bg = "black", fg = "white",font=self.font_titleFood)
        label_titleFood.grid(row=0,column=2, padx = 181, pady = 10)

        # Labels (top)
        self.label_point = Label(text = "Point:", bg="light pink", font = self.font_label_1)

        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_finishOrder = Button(text="Finish Order", bg="firebrick1", fg="white", font = self.font_label_2, command=self.finishOrder)
        self.img_next= PhotoImage(file="Photo/Food/right_arrow.png")
        self.button_next = Button(bg="lightyellow", image = self.img_next, command=self.food3)
        self.img_previous= PhotoImage(file="Photo/Food/left_arrow.png")
        self.button_previous = Button(bg="lightyellow", image = self.img_previous, command=self.food)
        
        
        # Labels & button (Using borders)-LEFT
        self.img_food_name4 = PhotoImage(file="Photo/Food/baked_potato.gif")
        self.canvas_food4 = Canvas(border1, width = 150 , height = 150)
        self.layer_food4 = self.canvas_food4.create_image(20, 20,image = self.img_food_name4)
        self.label_food_name4 = Label(border1,text = "4 Baked \npotato", font = self.font_label_2,justify = LEFT)
        self.label_food_price4 = Label(border1,text = "RM 3.50", font = self.font_label_2,justify = LEFT)
        self.button_select4 = Button(border1,text="Select", bg="yellow", fg="black", command=self.select4)

         # Labels & button (Using borders)-center
        self.img_food_name5 = PhotoImage(file="Photo/Food/chicken_breast_with_broccoli.gif")
        self.canvas_food5 = Canvas(border2, width = 150 , height = 150)
        self.layer_food5 = self.canvas_food5.create_image(20, 20,image = self.img_food_name5)
        self.label_food_name5 = Label(border2,text = "Chicken breast \nwith broccoli", font = self.font_label_2, justify = LEFT)
        self.label_food_price5 = Label(border2,text = "RM 5.00", font = self.font_label_2, justify = LEFT)
        self.button_select5 = Button(border2,text="Select", bg="yellow", fg="black", command=self.select5)
        
         # Labels & button (Using borders)-right
        self.img_food_name6 = PhotoImage(file="Photo/Food/oatmeal_raisin_cookies.gif")
        self.canvas_food6 = Canvas(border3, width = 150 , height = 150)
        self.layer_food6= self.canvas_food6.create_image(20, 20,image = self.img_food_name6)
        self.label_food_name6 = Label(border3,text = "3 Oatmeal \nraisin cookies", font = self.font_label_2, justify = LEFT)
        self.label_food_price6 = Label(border3,text = "RM 3.00", font = self.font_label_2, justify = LEFT)
        self.button_select6 = Button(border3,text="Select", bg="yellow", fg="black", command=self.select6)

        
        # Layout widgets
        # First column
        self.label_point.grid(row = 0, column = 0,padx = 10, pady = 5, columnspan = 2,sticky = N)
        self.canvas_food4.grid(row=1, column=1, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name4.grid(row = 5, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price4.grid(row = 6, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select4.grid(row = 8, column = 1, padx = 60, pady = 5, columnspan = 10, sticky = W)

        # Second column
        self.canvas_food5.grid(row=1, column=2, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name5.grid(row = 5, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price5.grid(row = 6, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select5.grid(row = 8, column = 2, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.button_previous.grid(row = 8, column = 2, padx = 2, pady = 340, columnspan = 1, sticky = W)
        self.button_finishOrder.grid(row = 8,column = 2, padx = 5, pady = 340, columnspan = 1,sticky = S)
        self.button_next.grid(row = 8, column = 2, padx = 20, pady = 340, columnspan = 1, sticky = SE)

        # Third column
        self.button_shoppingCart.grid(row = 0, column = 3, padx = 25, pady = 5, columnspan = 2,sticky = N)
        self.canvas_food6.grid(row=1, column=3, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name6.grid(row = 5, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price6.grid(row = 6, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select6.grid(row = 8, column = 3, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.centralize_window()
        
        if status == "member":
          self.point_info = Label(text = "{}".format(point), bg="white",font = self.font_label_2, justify = LEFT)
          self.point_info.place(x=70,y=8)

    def select4(self):
        self.destroy()
        FoodSelect4(None).title("Food 4")
        
    def select5(self):
        self.destroy()
        FoodSelect5(None).title("Food 5")

    def select6(self):
        self.destroy()
        FoodSelect6(None).title("Food 6")

    def back(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def finishOrder(self):
        self.destroy()
        totalCalories(None).title("Summary of Order")

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def food(self):
        self.destroy()
        FoodPage(None).title("Food Pg1")

    def food3(self):
        self.destroy()
        FoodPage3(None).title("Food Pg3")

# Foodpage 3       
class FoodPage3(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.minsize(650, 500)
        self.maxsize(650, 500)
        self.configure(bg="white")
        border1 = Frame(self, relief=SOLID, borderwidth=3)
        border1.place(relx=0.02, rely=0.20, anchor=NW)
        border2 = Frame(self,relief = SOLID, borderwidth=3)
        border2.place(relx=0.37 , rely=0.20, anchor=NW)
        border3 = Frame(self,relief = SOLID, borderwidth=3)
        border3.place(relx=0.72, rely=0.20, anchor=NW)

        # Create custom fonts
        self.font_titleFood = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.font_label_1 = font.Font(family = "Tahoma", size = 14)
        self.font_label_2 = font.Font(family = "Tahoma", size = 12)

        # Create title text for main menu
        label_titleFood = Label(self, text = "FOOD", bg = "black", fg = "white",font=self.font_titleFood)
        label_titleFood.grid(row=0,column=2, padx = 181, pady = 10)

        # Labels (top)
        self.label_point = Label(text = "Point:", bg="light pink", font = self.font_label_1)

        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_finishOrder = Button(text="Finish Order", bg="firebrick1", fg="white", font = self.font_label_2, command=self.finishOrder)
        self.img_previous= PhotoImage(file="Photo/Food/left_arrow.png")
        self.button_previous = Button(bg="lightyellow", image = self.img_previous, command=self.food2)
        
        # Labels & button (Using borders)-LEFT
        self.img_food_name7 = PhotoImage(file="Photo/Food/pesto_pasta.gif")
        self.canvas_food7 = Canvas(border1, width = 150 , height = 150)
        self.layer_food7 = self.canvas_food7.create_image(20, 20,image = self.img_food_name7)
        self.label_food_name7 = Label(border1,text = "Pesto \npasta", font = self.font_label_2,justify = LEFT)
        self.label_food_price7 = Label(border1,text = "RM 5.50", font = self.font_label_2,justify = LEFT)
        self.button_select7 = Button(border1,text="Select", bg="yellow", fg="black", command=self.select7)

         # Labels & button (Using borders)-center
        self.img_food_name8 = PhotoImage(file="Photo/Food/mix_fruit_salad.gif")
        self.canvas_food8 = Canvas(border2, width = 150 , height = 150)
        self.layer_food8 = self.canvas_food8.create_image(20, 20,image = self.img_food_name8)
        self.label_food_name8 = Label(border2,text = "Mix \nfruit salad", font = self.font_label_2, justify = LEFT)
        self.label_food_price8 = Label(border2,text = "RM3.50", font = self.font_label_2, justify = LEFT)
        self.button_select8 = Button(border2,text="Select", bg="yellow", fg="black", command=self.select8)
        
         # Labels & button (Using borders)-right
        self.img_food_name9 = PhotoImage(file="Photo/Food/scrambled_egg_sandwich.gif")
        self.canvas_food9 = Canvas(border3, width = 150 , height = 150)
        self.layer_food9 = self.canvas_food9.create_image(20, 20,image = self.img_food_name9)
        self.label_food_name9 = Label(border3,text = "Scrambled \negg sandwich", font = self.font_label_2, justify = LEFT)
        self.label_food_price9 = Label(border3,text = "RM 4.50", font = self.font_label_2, justify = LEFT)
        self.button_select9 = Button(border3,text="Select", bg="yellow", fg="black", command=self.select9)

        
        # Layout widgets
        # First column
        self.label_point.grid(row = 0, column = 0,padx = 10, pady = 5, columnspan = 2,sticky = N)
        self.canvas_food7.grid(row=1, column=1, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name7.grid(row = 5, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price7.grid(row = 6, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select7.grid(row = 8, column = 1, padx = 60, pady = 5, columnspan = 10, sticky = W)

        # Second column
        self.canvas_food8.grid(row=1, column=2, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name8.grid(row = 5, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price8.grid(row = 6, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select8.grid(row = 8, column = 2, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.button_previous.grid(row = 8, column = 2, padx = 2, pady = 340, columnspan = 1, sticky = W)
        self.button_finishOrder.grid(row = 8,column = 2, padx = 5, pady = 340, columnspan = 1,sticky = S)
        

        # Third column
        self.button_shoppingCart.grid(row = 0, column = 3, padx = 25, pady = 5, columnspan = 2,sticky = N)
        self.canvas_food9.grid(row=1, column=3, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name9.grid(row = 5, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price9.grid(row = 6, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select9.grid(row = 8, column = 3, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.centralize_window()

        if status == "member":
          self.point_info = Label(text = "{}".format(point), bg="white", font = self.font_label_2, justify = LEFT)
          self.point_info.place(x=70,y=8)

    def select7(self):
        self.destroy()
        FoodSelect7(None).title("Food 7")
        
    def select8(self):
        self.destroy()
        FoodSelect8(None).title("Food 8")

    def select9(self):
        self.destroy()
        FoodSelect9(None).title("Food 9")

    def finishOrder(self):
        self.destroy()
        totalCalories(None).title("Summary of Order")

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def food2(self):
        self.destroy()
        FoodPage2(None).title("Food Pg2")
        
# Beverage 1       
class BeveragePage(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.minsize(650, 500)
        self.maxsize(650, 500)
        self.configure(bg="white")
        border1 = Frame(self, relief=SOLID, borderwidth=3)
        border1.place(relx=0.02, rely=0.20, anchor=NW)
        border2 = Frame(self,relief = SOLID, borderwidth=3)
        border2.place(relx=0.37 , rely=0.20, anchor=NW)
        border3 = Frame(self,relief = SOLID, borderwidth=3)
        border3.place(relx=0.72, rely=0.20, anchor=NW)

        # Create custom fonts
        self.font_titleBeverage = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.font_label_1 = font.Font(family = "Tahoma", size = 14)
        self.font_label_2 = font.Font(family = "Tahoma", size = 12)

        # Create title text for main menu
        label_titleBeverage = Label(self, text = "BEVERAGE", bg = "black", fg = "white",font=self.font_titleBeverage)
        label_titleBeverage.grid(row=0,column=2, padx =108, pady = 10)

        # Labels (top)
        self.label_point = Label(text = "Point:", bg="light pink", font = self.font_label_1)

        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Beverage/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_finishOrder = Button(text="Finish Order", bg="firebrick1", fg="white", font = self.font_label_2, command=self.finishOrder)
        self.img_next= PhotoImage(file="Photo/Beverage/right_arrow.png")
        self.button_next = Button(bg="lightyellow", image = self.img_next, command=self.beverage2)
        
        
        
        # Labels & button (Using borders)-LEFT
        self.img_beverage_name1 = PhotoImage(file="Photo/Beverage/aloe_vera_juice.gif")
        self.canvas_beverage1 = Canvas(border1, width = 150 , height = 150)
        self.layer_beverage1 = self.canvas_beverage1.create_image(20, 20,image = self.img_beverage_name1)
        self.label_beverage_name1 = Label(border1,text = "Aloe \nVera Juice", font = self.font_label_2,justify = LEFT)
        self.label_beverage_price1 = Label(border1,text = "RM 1.80", font = self.font_label_2,justify = LEFT)
        self.button_select1 = Button(border1,text="Select", bg="yellow", fg="black", command=self.selectB1)

         # Labels & button (Using borders)-center
        self.img_beverage_name2 = PhotoImage(file="Photo/Beverage/dark_raw_hot_chocolate.gif")
        self.canvas_beverage2 = Canvas(border2, width = 150 , height = 150)
        self.layer_beverage2 = self.canvas_beverage2.create_image(20, 20,image = self.img_beverage_name2)
        self.label_beverage_name2 = Label(border2,text = "Dark Raw \nHot Chocolate", font = self.font_label_2, justify = LEFT)
        self.label_beverage_price2 = Label(border2,text = "RM 2.20", font = self.font_label_2, justify = LEFT)
        self.button_select2 = Button(border2,text="Select", bg="yellow", fg="black", command=self.selectB2)
        
         # Labels & button (Using borders)-right
        self.img_beverage_name3 = PhotoImage(file="Photo/Beverage/frozen_yogurt.gif")
        self.canvas_beverage3 = Canvas(border3, width = 150 , height = 150)
        self.layer_beverage3= self.canvas_beverage3.create_image(20, 20,image = self.img_beverage_name3)
        self.label_beverage_name3 = Label(border3,text = "Frozen \nYogurt", font = self.font_label_2, justify = LEFT)
        self.label_beverage_price3 = Label(border3,text = "RM 2.80", font = self.font_label_2, justify = LEFT)
        self.button_select3 = Button(border3,text="Select", bg="yellow", fg="black", command=self.selectB3)

        
        # Layout widgets
        # First column
        self.label_point.grid(row = 0, column = 0,padx = 10, pady = 5, columnspan = 2,sticky = N)
        self.canvas_beverage1.grid(row=1, column=1, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_beverage_name1.grid(row = 5, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_beverage_price1.grid(row = 6, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select1.grid(row = 8, column = 1, padx = 60, pady = 5, columnspan = 10, sticky = W)

        # Second column
        self.canvas_beverage2.grid(row=1, column=2, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_beverage_name2.grid(row = 5, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_beverage_price2.grid(row = 6, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select2.grid(row = 8, column = 2, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.button_back.grid(row = 8, column = 2, padx = 8, pady = 340, columnspan = 1, sticky = SW)
        self.button_finishOrder.grid(row = 8,column = 2, padx = 5, pady = 340, columnspan = 1,sticky = S)
        self.button_next.grid(row = 8, column = 2, padx = 20, pady = 340, columnspan = 1, sticky = SE)

        # Third column
        self.button_shoppingCart.grid(row = 0, column = 3, padx = 25, pady = 5, columnspan = 2,sticky = N)
        self.canvas_beverage3.grid(row=1, column=3, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_beverage_name3.grid(row = 5, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_beverage_price3.grid(row = 6, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select3.grid(row = 8, column = 3, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.centralize_window()

        if status == "member":
          self.point_info = Label(text = "{}".format(point), bg="white", font = self.font_label_2, justify = LEFT)
          self.point_info.place(x=70,y=8)

    def selectB1(self):
        self.destroy()
        BeverageSelect1(None).title("Beverage 1")
        
    def selectB2(self):
        self.destroy()
        BeverageSelect2(None).title("Beverage 2")

    def selectB3(self):
        self.destroy()
        BeverageSelect3(None).title("Beverage 3")

    def back(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def finishOrder(self):
        self.destroy()
        totalCalories(None).title("Summary of Order")

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def beverage2(self):
        self.destroy()
        BeveragePage2(None).title("Beveage Pg2")

# Beverage 2     
class BeveragePage2(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.minsize(650, 500)
        self.maxsize(650, 500)
        self.configure(bg="white")
        border1 = Frame(self, relief=SOLID, borderwidth=3)
        border1.place(relx=0.02, rely=0.20, anchor=NW)
        border2 = Frame(self,relief = SOLID, borderwidth=3)
        border2.place(relx=0.37 , rely=0.20, anchor=NW)
        border3 = Frame(self,relief = SOLID, borderwidth=3)
        border3.place(relx=0.72, rely=0.20, anchor=NW)

        # Create custom fonts
        self.font_titleBeverage = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.font_label_1 = font.Font(family = "Tahoma", size = 14)
        self.font_label_2 = font.Font(family = "Tahoma", size = 12)

        # Create title text for main menu
        label_titleBeverage = Label(self, text = "BEVERAGE", bg = "black", fg = "white",font=self.font_titleBeverage)
        label_titleBeverage.grid(row=0,column=2, padx =108, pady = 10)

        # Labels (top)
        self.label_point = Label(text = "Point:", bg="light pink", font = self.font_label_1)

        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Beverage/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_finishOrder = Button(text="Finish Order", bg="firebrick1", fg="white", font = self.font_label_2, command=self.finishOrder)
            
        # Labels & button (Using borders)-LEFT
        self.img_beverage_name4 = PhotoImage(file="Photo/Beverage/lemon_water.gif")
        self.canvas_beverage4 = Canvas(border1, width = 150 , height = 150)
        self.layer_beverage4 = self.canvas_beverage4.create_image(20, 20,image = self.img_beverage_name4)
        self.label_beverage_name4 = Label(border1,text = "Lemon \nWater", font = self.font_label_2,justify = LEFT)
        self.label_beverage_price4 = Label(border1,text = "RM 1.20", font = self.font_label_2,justify = LEFT)
        self.button_select4 = Button(border1,text="Select", bg="yellow", fg="black", command=self.selectB4)

         # Labels & button (Using borders)-center
        self.img_beverage_name5 = PhotoImage(file="Photo/Beverage/light_coffee_smoothies.gif")
        self.canvas_beverage5 = Canvas(border2, width = 150 , height = 150)
        self.layer_beverage5 = self.canvas_beverage5.create_image(20, 20,image = self.img_beverage_name5)
        self.label_beverage_name5 = Label(border2,text = "Light \nCoffee Smoothies", font = self.font_label_2, justify = LEFT)
        self.label_beverage_price5 = Label(border2,text = "RM 2.60", font = self.font_label_2, justify = LEFT)
        self.button_select5 = Button(border2,text="Select", bg="yellow", fg="black", command=self.selectB5)
        
         # Labels & button (Using borders)-right
        self.img_beverage_name6 = PhotoImage(file="Photo/Beverage/vanilla_latte.gif")
        self.canvas_beverage6 = Canvas(border3, width = 150 , height = 150)
        self.layer_beverage6 = self.canvas_beverage6.create_image(20, 20,image = self.img_beverage_name6)
        self.label_beverage_name6 = Label(border3,text = "Vanilla \nLatte", font = self.font_label_2, justify = LEFT)
        self.label_beverage_price6 = Label(border3,text = "RM 2.80", font = self.font_label_2, justify = LEFT)
        self.button_select6 = Button(border3,text="Select", bg="yellow", fg="black", command=self.selectB6)

        
        # Layout widgets
        # First column
        self.label_point.grid(row = 0, column = 0,padx = 10, pady = 5, columnspan = 2,sticky = N)
        self.canvas_beverage4.grid(row=1, column=1, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_beverage_name4.grid(row = 5, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_beverage_price4.grid(row = 6, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select4.grid(row = 8, column = 1, padx = 60, pady = 5, columnspan = 10, sticky = W)

        # Second column
        self.canvas_beverage5.grid(row=1, column=2, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_beverage_name5.grid(row = 5, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_beverage_price5.grid(row = 6, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select5.grid(row = 8, column = 2, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.button_back.grid(row = 8, column = 2, padx = 8, pady = 340, columnspan = 1, sticky = SW)
        self.button_finishOrder.grid(row = 8,column = 2, padx = 5, pady = 340, columnspan = 1,sticky = S)

        # Third column
        self.button_shoppingCart.grid(row = 0, column = 3, padx = 25, pady = 5, columnspan = 2,sticky = N)
        self.canvas_beverage6.grid(row=1, column=3, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_beverage_name6.grid(row = 5, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_beverage_price6.grid(row = 6, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select6.grid(row = 8, column = 3, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.centralize_window()

        if status == "member":
          self.point_info = Label(text = "{}".format(point), bg="white", font = self.font_label_2, justify = LEFT)
          self.point_info.place(x=70,y=8)

    def selectB4(self):
        self.destroy()
        BeverageSelect4(None).title("Beverage 4")
        
    def selectB5(self):
        self.destroy()
        BeverageSelect5(None).title("Beverage 5")

    def selectB6(self):
        self.destroy()
        BeverageSelect6(None).title("Beverage 6")

    def back(self):
        self.destroy()
        BeveragePage(None).title("Beverage Pg1")

    def finishOrder(self):
        self.destroy()
        totalCalories(None).title("Summary of Order")

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
        
# Selection 1
class FoodSelect1(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

        # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_food_name1 = PhotoImage(file="Photo/Food/turkey_sandwich.png")
        self.label_img = Label(image=self.img_food_name1)

        # Label
        self.label_food_name1 = Label(text = "Turkey sandwich", bg="white",font = self.font_label_1, justify = LEFT)
        self.label_calories1 = Label(text = "308 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_description1 = Label(text = "~ A fantastic sandwich with sliced turkey, \ntoasted whole wheat bread, fresh tomato, \nlettuce, bean sprouts, yellow mustard and light mayo.",bg="white",font = self.font_label_1, justify = CENTER)
        self.label_nutrition1 = Label(text = "Total Fat: 8.94g Cholesterol:64 mg Sodium:550mg\nPotassium:309 mg Carbohydrates:26.7g Protein:28.11g", bg="white", fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:    RM3.50",bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 105, pady = 5, rowspan = 4, sticky = W)
        self.label_food_name1.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories1.grid(row = 8, padx = 5, pady = 5)
        self.label_description1.grid(row = 9, padx = 5, pady = 5, sticky = W+E)
        self.label_nutrition1.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()
            

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        FoodPage(None).title("Food Pg1")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        #if len(foods)< 4 and foods == "Turkey sandwich"  :"
        #if "Turkey sandwich" not in foods : 
            #messagebox.showinfo("Success","Add item to cart")
            #foods.append("Turkey sandwich")
            #prices.append("RM 3.50")
            #calories.append("308 calories")
            if len(foods)< 4 and "Turkey sandwich" not in foods : 
                foods.append("Turkey sandwich")
                prices.append(float("3.50"))
                calories.append(int("308"))
                messagebox.showinfo("Success","Add item to cart")
            elif "Turkey sandwich" in foods:
                 messagebox.showerror("Sorry","Item has been added")
            else:
                messagebox.showerror("Sorry","Only 4 items can be added")
                
# Selection 2
class FoodSelect2(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_food_name2 = PhotoImage(file="Photo/Food/avocado_tomato_salad.png")
        self.label_img = Label(image=self.img_food_name2)

        # Label
        self.label_food_name2 = Label(text = "Avocado tomato salad",bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories2 = Label(text = "261 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_description2 = Label(text = "~ Classic cucumber and tomato salad just \ngot better with the addition of avocado, a light and flavorful \nlemon dressing and the freshness of cilantro",bg="white",font = self.font_label_1, justify = CENTER)
        self.label_nutrition2 = Label(text = " Total Fat:22g Saturated Fat:3g Sodium:596mg\nPotassium:886mg Carbohydrates:17g Fiber:8g Protein:3g", bg="white",fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:    RM4.00", bg="yellow",font = self.font_label_1, justify = CENTER)
        

        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 155, pady = 5, rowspan = 4, sticky = W)
        self.label_food_name2.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories2.grid(row = 8, padx = 5, pady = 5)
        self.label_description2.grid(row = 9, padx = 5, pady = 5, sticky = W+E)
        self.label_nutrition2.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()
        
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        FoodPage(None).title("Food Pg1")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Avocado tomato salad" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Avocado tomato salad")
            prices.append(float("4.00"))
            calories.append(int("261"))
        elif "Avocado tomato salad" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")
            
#Selection 3
class FoodSelect3(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_food_name3 = PhotoImage(file="Photo/Food/tuna_salad_pita.png")
        self.label_img = Label(image=self.img_food_name3)

        # Label
        self.label_food_name3 = Label(text = "Tuna salad pita", bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories3 = Label(text = "321 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_description3 = Label(text = "~ Pita bread halves are lined with \nlettuce and sliced tomatoes, and then filled with \na tasty tuna salad made with creamy mayo in this ultimate sandwich.",bg="white",font = self.font_label_1, justify = CENTER)
        self.label_nutrition3 = Label(text = "Total Fat:8g Saturated Fat:1g Cholesterol:31 mg Sodium:721 mg\nPotassium:659 mg Carbohydrates:36g Fiber:8g Protein:23g", bg="white",fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:    RM4.50", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 135, pady = 5, rowspan = 4, sticky = W)
        self.label_food_name3.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories3.grid(row = 8, padx = 5, pady = 5)
        self.label_description3.grid(row = 9, padx = 5, pady = 5, sticky = W+E)
        self.label_nutrition3.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()

        
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        FoodPage(None).title("Food Pg1")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Tuna salad pita" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Tuna salad pita")
            prices.append(float("4.50"))
            calories.append(int("321"))
        elif "Tuna salad pita" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")

#Selection 4
class FoodSelect4(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_food_name4 = PhotoImage(file="Photo/Food/baked_potato.png")
        self.label_img = Label(image=self.img_food_name4)

        # Label
        self.label_food_name4 = Label(text = "4 Baked potato", bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories4 = Label(text = "208 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_description4 = Label(text = "~ Potatoes which are baked until the skin is \ncrisp, and the insides are soft, white, and fluffy. ",bg="white", font = self.font_label_1, justify = CENTER)
        self.label_nutrition4 = Label(text = "Total Fat:3g Saturated Fat:2g Sodium:594mg Potassium:945mg\nCarbohydrates:40g Fiber:2g Protein\:4g ", bg="white", fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:    RM3.50", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 105, pady = 5, rowspan = 4, sticky = W)
        self.label_food_name4.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories4.grid(row = 8, padx = 5, pady = 5)
        self.label_description4.grid(row = 9, padx = 5, pady = 5, sticky = W+E)
        self.label_nutrition4.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()

        
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        FoodPage2(None).title("Food Pg2")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "4 Baked potato" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("4 Baked potato")
            prices.append(float("3.50"))
            calories.append(int("208"))
        elif "4 Baked potato" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")
            
# Selection 5
class FoodSelect5(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_food_name5 = PhotoImage(file="Photo/Food/chicken_breast_with_broccoli.png")
        self.label_img = Label(image=self.img_food_name5)

        # Label
        self.label_food_name5 = Label(text = "Chicken breast with broccoli", bg="white",font = self.font_label_1, justify = LEFT)
        self.label_calories5 = Label(text = "249 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_description5 = Label(text = "~ Skinless chicken breast is filled \nwith simple fresh broccoli",bg="white",font = self.font_label_1, justify = CENTER)
        self.label_nutrition5 = Label(text = "Total Fat:9g Cholesterol:73 mg Sodium:766 mg\nCarbohydrates:14.6g Fiber:1.6g Protein:27g",bg="white", fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:    RM5.00", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 145, pady = 5, rowspan = 4, sticky = W)
        self.label_food_name5.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories5.grid(row = 8, padx = 5, pady = 5)
        self.label_description5.grid(row = 9, padx = 5, pady = 5, sticky = W+E)
        self.label_nutrition5.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        FoodPage2(None).title("Food Pg2")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Chicken breast" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Chicken breast")
            prices.append(float("5.00"))
            calories.append(int("249"))
        elif "Chicken breast" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")
        
# Selection 6
class FoodSelect6(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)


        # Photo
        self.img_food_name6 = PhotoImage(file="Photo/Food/oatmeal_raisin_cookies.png")
        self.label_img = Label(image=self.img_food_name6)

        # Label
        self.label_food_name6 = Label(text = "3 Oatmeal raisin cookies", bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories6 = Label(text = "276 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_description6 = Label(text = "~ Soft and chewy oatmeal raisin Cookies \nthat are super soft, thick, and loaded \nwith oats and raisins",bg="white",font = self.font_label_1, justify = CENTER)
        self.label_nutrition6 = Label(text = "Total Fat:10.2 g Cholesterol:45 mg Sodium:225 mg\nCarbohydrates:43.8 g Protein:3.9 g",bg="white", fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:    RM3.00", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 145, pady = 5, rowspan = 4, sticky = W)
        self.label_food_name6.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories6.grid(row = 8, padx = 5, pady = 5)
        self.label_description6.grid(row = 9, padx = 5, pady = 5, sticky = W+E)
        self.label_nutrition6.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()

        
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        FoodPage2(None).title("Food Pg2")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "3 Oatmeal raisin cookies" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("3 Oatmeal raisin cookies")
            prices.append(float("3.00"))
            calories.append(int("276"))
        elif "3 Oatmeal raisin cookies" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")

# Selection 7
class FoodSelect7(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="light yellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_food_name7 = PhotoImage(file="Photo/Food/pesto_pasta.png")
        self.label_img = Label(image=self.img_food_name7)

        # Label
        self.label_food_name7 = Label(text = "Pesto pasta", bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories7 = Label(text = "238 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_description7 = Label(text = "~  Pasta with creamy \nblended bright green sauce.",bg="white",font = self.font_label_1, justify = CENTER)
        self.label_nutrition7 = Label(text = "Total Fat:5g Saturated Fat:3g Cholesterol:16mg Sodium:198mg\nPotassium:257 mg Carbohydrates:36g Protein:12g",bg="white", fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:    RM5.50", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 145, pady = 5, rowspan = 4, sticky = W)
        self.label_food_name7.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories7.grid(row = 8, padx = 5, pady = 5)
        self.label_description7.grid(row = 9, padx = 5, pady = 5, sticky = W+E)
        self.label_nutrition7.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()
        
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        FoodPage3(None).title("Food Pg3")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Pesto pasta" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Pesto pasta")
            prices.append(float("5.50"))
            calories.append(int("238"))
        elif "Pesto pasta" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")
            
# Selection 8
class FoodSelect8(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_food_name8 = PhotoImage(file="Photo/Food/mix_fruit_salad.png")
        self.label_img = Label(image=self.img_food_name8)

        # Label
        self.label_food_name8 = Label(text = "Mix fruit salad", bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories8 = Label(text = "155 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_description8 = Label(text = "~ Creamy fruit salad with strawberries, \nkiwi fruits, grapes and blueberries.",bg="white", font = self.font_label_1, justify = CENTER)
        self.label_nutrition8 = Label(text = "Total Fat:0.6 g Sodium:5 mg Potassium:451 mg\nCarbohydrates:9 g Protein:1.8 g",bg="white", fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:    RM3.50", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 145, pady = 5, rowspan = 4, sticky = W)
        self.label_food_name8.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories8.grid(row = 8, padx = 5, pady = 5)
        self.label_description8.grid(row = 9, padx = 5, pady = 5, sticky = W+E)
        self.label_nutrition8.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()
        
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        FoodPage3(None).title("Food Pg3")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Mix fruit salad" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Mix fruit salad")
            prices.append(float("3.50"))
            calories.append(int("155"))
        elif "Mix fruit salad" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")
            
# Selection 9
class FoodSelect9(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_food_name9 = PhotoImage(file="Photo/Food/scrambled_egg_sandwich.png")
        self.label_img = Label(image=self.img_food_name9)

        # Label
        self.label_food_name9 = Label(text = "Scrambled egg sandwich with cucumber",bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories9 = Label(text = "320 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_description9 = Label(text = "~ Protein packed sandwich with scrambled eggs, \ncucumber and cream cheese, makes a perfect lunch box or \npicnic lunch or even a wholesome breakfast",bg="white",font = self.font_label_1, justify = CENTER)
        self.label_nutrition9 = Label(text = "Total Fat:10g Saturated Fat:4g Cholesterol:174mg Sodium:581mg\nPotassium:355mg Fiber:7g Carbohydrates:43g Protein:14g", bg="white",fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:    RM4.50", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 205, pady = 5, rowspan = 4, sticky = W)
        self.label_food_name9.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories9.grid(row = 8, padx = 5, pady = 5)
        self.label_description9.grid(row = 9, padx = 5, pady = 5, sticky = W+E)
        self.label_nutrition9.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()
        
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        FoodPage3(None).title("Food Pg3")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Scrambled egg sandwich" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Scrambled egg sandwich")
            prices.append(float("4.50"))
            calories.append(int("320"))
        elif "Scrambled egg sandwich" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")
            
# Beverage Selection 1
class BeverageSelect1(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_beverage_name1 = PhotoImage(file="Photo/Beverage/aloe_vera_juice.png")
        self.label_img = Label(image=self.img_beverage_name1)

        # Label
        self.label_beverage_name1 = Label(text = "Aloe Vera Juice", bg="white",font = self.font_label_1, justify = LEFT)
        self.label_calories1 = Label(text = "36 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_nutrition1 = Label(text = "Total Fat:0g Sodium:19mg Carbohydrates:9g\nSugars:9g Protein:0g",bg="white",fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:    RM1.80", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 105, pady = 5, rowspan = 4, sticky = W)
        self.label_beverage_name1.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories1.grid(row = 8, padx = 5, pady = 5)
        self.label_nutrition1.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        BeveragePage(None).title("Beverage Pg1")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Aloe Vera Juice" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Aloe Vera Juice")
            prices.append(float("1.80"))
            calories.append(int("36"))
        elif "Aloe Vera Juice" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")
            
# Beverage Selection 2
class BeverageSelect2(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)


        # Photo
        self.img_beverage_name2 = PhotoImage(file="Photo/Beverage/dark_raw_hot_chocolate.png")
        self.label_img = Label(image=self.img_beverage_name2)

        # Label
        self.label_beverage_name2 = Label(text = "Dark Raw Hot Chocolate", bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories2 = Label(text = "160 calories", bg="light blue", font =self.font_label_1, justify = LEFT)
        self.label_nutrition2 = Label(text = "Total Fat:2g Saturated Fat:2g Cholesterol:0mg Sodium:170mg\nCarbohydrate:34g Fiber:0.5g Sugars:28g Protein:1g",bg="white", fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:   RM2.20", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 185, pady = 5, rowspan = 4, sticky = W)
        self.label_beverage_name2.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories2.grid(row = 8, padx = 5, pady = 5)
        self.label_nutrition2.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        BeveragePage(None).title("Beverage Pg1")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Dark Raw Hot Chocolate" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Dark Raw Hot Chocolate")
            prices.append(float("2.20"))
            calories.append(int("160"))
        elif "Dark Raw Hot Chocolate" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")

# Beverage Selection 3
class BeverageSelect3(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_beverage_name3 = PhotoImage(file="Photo/Beverage/frozen_yogurt.png")
        self.label_img = Label(image=self.img_beverage_name3)

        # Label
        self.label_beverage_name3 = Label(text = "Frozen Yogurt",bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories3 = Label(text = "159 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_nutrition3 = Label(text = "Total Fat:6.3g Saturated Fat:4g Cholesterol:23 mg Sodium:110 mg\nPotassium:271mg Carbohydrates:38g Fiber:0g Sugars:35g Protein:5.2g", bg="white", fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:   RM2.80", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 205, pady = 5, rowspan = 4, sticky = W)
        self.label_beverage_name3.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories3.grid(row = 8, padx = 5, pady = 5)
        self.label_nutrition3.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        BeveragePage(None).title("Beverage Pg1")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Frozen Yogurt" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Frozen Yogurt")
            prices.append(float("2.80"))
            calories.append(int("159"))
        elif "Frozen Yogurt" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")
            
# Beverage Selection 4
class BeverageSelect4(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_beverage_name4 = PhotoImage(file="Photo/Beverage/lemon_water.png")
        self.label_img = Label(image=self.img_beverage_name4)

        # Label
        self.label_beverage_name4 = Label(text = "Lemon Water", bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories4 = Label(text = "30 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_nutrition4 = Label(text = "Total Fat:2g Cholesterol:0mg\nCarbohydrate:5g Protein:0g",bg="white", fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:   RM1.20", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 135, pady = 5, rowspan = 4, sticky = W)
        self.label_beverage_name4.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories4.grid(row = 8, padx = 5, pady = 5)
        self.label_nutrition4.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        BeveragePage2(None).title("Beverage Pg2")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Lemon Water" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Lemon Water")
            prices.append(float("1.20"))
            calories.append(int("30"))
        elif "Lemon Water" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")
            
# Beverage Selection 5
class BeverageSelect5(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_beverage_name5 = PhotoImage(file="Photo/Beverage/light_coffee_smoothies.png")
        self.label_img = Label(image=self.img_beverage_name5)

        # Label
        self.label_beverage_name5 = Label(text = "Light Coffee Smoothies", bg="white",font = self.font_label_1, justify = LEFT)
        self.label_calories5 = Label(text = "148 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_nutrition5 = Label(text = "Total Fat:0g Saturated Fat:0g Cholesterol:0mg\nSodium:15mg Carbohydrates:41.9g \nFiber:0.7g Sugars:40.4g Protein:0.7g", bg="white",fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:   RM2.60", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 105, pady = 5, rowspan = 4, sticky = W)
        self.label_beverage_name5.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories5.grid(row = 8, padx = 5, pady = 5)
        self.label_nutrition5.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        BeveragePage2(None).title("Beverage Pg2")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Light Coffee Smoothies" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Light Coffee Smoothies")
            prices.append(float("2.60"))
            calories.append(int("148"))
        elif "Light Coffee Smoothies" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")

# Beverage Selection 6
class BeverageSelect6(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")

         # Font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )
        
        # Button(top)
        self.img_shoppingCart = PhotoImage(file="Photo/Food/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)

        # Button(Bottom)
        self.button_back = Button(text="BACK", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_mainMenu = Button(text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command=self.MainMenu)
        self.button_addCart = Button(text="Add\nto Cart", bg="orange2", fg="white", font = self.font_label_2, command=self.AddCart)

        # Photo
        self.img_beverage_name6 = PhotoImage(file="Photo/Beverage/vanilla_latte.png")
        self.label_img = Label(image=self.img_beverage_name6)

        # Label
        self.label_beverage_name6 = Label(text = "Vanilla Latte", bg="white", font = self.font_label_1, justify = LEFT)
        self.label_calories6 = Label(text = "200 calories", bg="light blue", font = self.font_label_1, justify = LEFT)
        self.label_nutrition6 = Label(text = "Total Fat:6.7g Saturated Fat:4.3g Cholesterol:27 mg\nSodium:167 mg Potassium:551mg Carbohydrates:36g\nFiber:0g Sugars:36g", bg="white", fg="blue", font = self.font_label_3, justify = CENTER)
        self.label_price = Label(text = "Price:   RM2.80", bg="yellow", font = self.font_label_1, justify = CENTER)
        
        # Layout widgets
        self.button_shoppingCart.grid(row = 1,padx = 5, pady = 5, sticky = NE)
        self.label_img.grid(row = 1, padx = 105, pady = 5, rowspan = 4, sticky = W)
        self.label_beverage_name6.grid(row = 6, padx = 5, pady = 5, sticky = W+E)
        self.label_calories6.grid(row = 8, padx = 5, pady = 5)
        self.label_nutrition6.grid(row = 10, padx = 5, pady = 5, sticky = W+E)
        self.label_price.grid(row = 12 , padx = 5, pady = 5,)
        self.button_back.grid(row = 13, padx = 20, pady = 5, columnspan = 2, sticky = E)
        self.button_mainMenu.grid(row = 13, padx = 80, pady = 5, columnspan = 2, sticky = E)
        self.button_addCart.grid(row = 13, padx = 180, pady = 5, columnspan = 2, sticky = E)
        self.centralize_window()

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")
            
    def back(self):
        self.destroy()
        BeveragePage2(None).title("Beverage Pg2")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def AddCart(self):
        if len(foods)< 4 and "Vanilla Latte" not in foods :
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Vanilla Latte")
            prices.append(float("2.80"))
            calories.append(int("200"))
        elif "Vanilla Latte" in foods:
            messagebox.showerror("Sorry","Item has been added.")
        else:
            messagebox.showerror("Sorry","Only 4 items can be added")

# Breakfast
class BreakfastPage(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
        self.minsize(760, 700)
        self.maxsize(760, 700)
        border1 = Frame(self, relief = RIDGE, borderwidth=1.3)
        border1.place(relx=0.02, rely=0.150, anchor=NW)
        border2 = Frame(self,relief=SUNKEN, borderwidth=1.3)
        border2.place(relx=0.02 , rely=0.34, anchor=NW)
        border3 = Frame(self,relief = RIDGE, borderwidth=1.3)
        border3.place(relx=0.02, rely=0.53, anchor=NW)
        border4 = Frame(self,relief = SUNKEN, borderwidth=1.4)
        border4.place(relx=0.02, rely=0.72, anchor=NW)

        # Create fonts
        self.font_titleBreakfast = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.font_label_1 = font.Font(family = "Tahoma", size = 14)
        self.font_label_2 = font.Font(family = "Tahoma", size = 12)

        # Create title text for breakfast page
        label_titleBreakfast = Label(self, text = "BREAKFAST", bg = "orange", fg = "black", font = self.font_titleBreakfast) 
        label_titleBreakfast.grid(row=0,column=1, padx = 135, pady = 10)

        # Point Label (top)
        self.label_point = Label(text = "Point:",bg = "light pink",font = self.font_label_1)
        self.label_point.grid(row = 0, column = 0, sticky = N+W, pady = 10)

        # Cart Button (top)
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)
        self.button_shoppingCart.grid(row = 0, column = 2, padx = 63, pady = 5,sticky = N+E)

        # Back / Main Menu / Finish Order Buttons (bottom)
        self.button_back = Button(text="Back", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_back.grid(row = 10, column = 0 , padx = 5, pady = 570)
        self.button_finishOrder = Button(text="Finish Order", bg="firebrick1",fg="white", font = self.font_label_2, command=self.finishOrder)
        self.button_finishOrder.grid(row = 10, column = 2 ,padx = 0, pady = 570)
        
        # Labels & button (breakfast 1) - ROW 1
        self.img_breakfast_name1 = PhotoImage(file="Photo/SetMeal/Scrambled egg sandwich with cucumber + Lemon water.gif")
        self.canvas_breakfast1 = Canvas(border1, width =290  , height = 100)
        self.layer_breakfast1 = self.canvas_breakfast1.create_image(100,50,image = self.img_breakfast_name1)
        self.label_breakfast_name1 = Label(border1,text = "Scrambled egg sandwich\nwith cucumber + Lemon water", font = self.font_label_2,justify = LEFT)
        self.label_breakfast_price1 = Label(border1,text = "RM 5.50", font = self.font_label_2,justify = RIGHT)
        self.button_choice1 = Button(border1,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice1, justify = RIGHT)

        # Labels & button (breakfast 2)- ROW 2
        self.img_breakfast_name2 = PhotoImage(file="Photo/SetMeal/Turkey sandwich + Dark raw hot chocolate.gif")
        self.canvas_breakfast2 = Canvas(border2, width = 290 , height = 100)
        self.layer_breakfast2 = self.canvas_breakfast2.create_image(100, 50,image = self.img_breakfast_name2)
        self.label_breakfast_name2 = Label(border2,text = "Turkey sandwich + Dark raw \nhot chocolate", font = self.font_label_2,justify = LEFT)
        self.label_breakfast_price2 = Label(border2,text = "RM 5.50", font = self.font_label_2,justify = RIGHT)
        self.button_choice2 = Button(border2,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice2,justify = RIGHT)

        # Labels & button (breakfast 3)- ROW 3
        self.img_breakfast_name3 = PhotoImage(file="Photo/SetMeal/English Muffin With Peanut Butter + Vanilla latte.gif")
        self.canvas_breakfast3 = Canvas(border3, width = 287 , height = 100)
        self.layer_breakfast3 = self.canvas_breakfast3.create_image(100, 50,image = self.img_breakfast_name3)
        self.label_breakfast_name3 = Label(border3,text = "English Muffin With Peanut\t\nButter + Vanilla latte", font = self.font_label_2,justify = LEFT)
        self.label_breakfast_price3 = Label(border3,text = "RM 6.00", font = self.font_label_2,justify = RIGHT)
        self.button_choice3 = Button(border3,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice3,justify = RIGHT)

        # Labels & button (breakfast 4)- ROW 4
        self.img_breakfast_name4 = PhotoImage(file="Photo/SetMeal/Mix fruit salad + Frozen yogurt + Lemon water.gif")
        self.canvas_breakfast4 = Canvas(border4, width = 286 , height = 100)
        self.layer_breakfast4 = self.canvas_breakfast4.create_image(100, 50,image = self.img_breakfast_name4)
        self.label_breakfast_name4 = Label(border4,text = "Mix fruit salad + Frozen yogurt\n + Lemon water", font = self.font_label_2,justify = LEFT)
        self.label_breakfast_price4 = Label(border4,text = "RM 7.20", font = self.font_label_2,justify = RIGHT)
        self.button_choice4 = Button(border4,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice4,justify = RIGHT)

        # Widgets Grid
        # Breakfast 1
        self.canvas_breakfast1.grid(row=4, column=0, padx = 10, pady = 10)
        self.label_breakfast_name1.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.label_breakfast_price1.grid(row = 4, column = 2, padx = 10, pady = 10)
        self.button_choice1.grid(row = 4, column = 3, padx = 5, pady = 10 )

        # Breakfast 2
        self.canvas_breakfast2.grid(row=5, column=0, padx = 10, pady = 10)
        self.label_breakfast_name2.grid(row = 5, column = 1,padx = 10, pady = 10)
        self.label_breakfast_price2.grid(row = 5, column = 2, padx = 10, pady = 10)
        self.button_choice2.grid(row = 5, column = 3, padx = 10, pady = 10)
        
        # Breakfast 3
        self.canvas_breakfast3.grid(row=6, column=0, padx = 10, pady = 10)
        self.label_breakfast_name3.grid(row = 6, column = 1, padx = 10, pady = 10)
        self.label_breakfast_price3.grid(row = 6, column = 2, padx = 10, pady = 10)
        self.button_choice3.grid(row = 6, column = 3, padx = 10, pady = 10)
        
        # Breakfast 4
        self.canvas_breakfast4.grid(row=7, column=0, padx = 10, pady = 10)
        self.label_breakfast_name4.grid(row = 7, column = 1, padx = 10, pady = 10)
        self.label_breakfast_price4.grid(row = 7, column = 2, padx = 10, pady = 10)
        self.button_choice4.grid(row = 7, column = 3, padx = 10, pady = 10)
        self.centralize_window()

        if status == "member":
          self.point_info = Label(text = "{}".format(point), bg="white", font = self.font_label_2, justify = LEFT)
          self.point_info.place(x=63,y=12)
        
    def choice1(self):
        self.destroy()
        Breakfast1(None).title("Breakfast 1")
        
    def choice2(self):
        self.destroy()
        Breakfast2(None).title("Breakfast 2")

    def choice3(self):
        self.destroy()
        Breakfast3(None).title("Breakfast 3")

    def choice4(self):
        self.destroy()
        Breakfast4(None).title("Breakfast 4")

    def back(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def finishOrder(self):
        self.destroy()
        totalCalories(None).title("Summary of Order")

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

class LunchPage(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
        self.minsize(760, 700)
        self.maxsize(760, 700)
        border1 = Frame(self, relief = RIDGE, borderwidth=1.3)
        border1.place(relx=0.02, rely=0.150, anchor=NW)
        border2 = Frame(self,relief=SUNKEN, borderwidth=1.3)
        border2.place(relx=0.02 , rely=0.34, anchor=NW)
        border3 = Frame(self,relief = RIDGE, borderwidth=1.3)
        border3.place(relx=0.02, rely=0.53, anchor=NW)
        border4 = Frame(self,relief = SUNKEN, borderwidth=1.4)
        border4.place(relx=0.02, rely=0.72, anchor=NW)

        # Create fonts
        self.font_titleLunch = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.font_label_1 = font.Font(family = "Tahoma", size = 14)
        self.font_label_2 = font.Font(family = "Tahoma", size = 12)

        # Create title text for lunch page
        label_titleLunch = Label(self, text = "LUNCH", bg = "yellow2", fg = "black", font = self.font_titleLunch) 
        label_titleLunch.grid(row=0,column=1, padx = 180, pady = 10)

        # Point Label (top)
        self.label_point = Label(text = "Point:",bg = "light pink",font = self.font_label_1)
        self.label_point.grid(row = 0, column = 0, sticky = N+W, pady = 10)

        # Cart Button (top)
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)
        self.button_shoppingCart.grid(row = 0, column = 2, padx = 63, pady = 5,sticky = N+E)

        # Back / Main Menu / Finish Order Buttons (bottom)
        self.button_back = Button(text="Back", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_back.grid(row = 10, column = 0, padx = 5 ,pady = 570)
        self.button_finishOrder = Button(text="Finish Order", bg="firebrick1",fg="white", font = self.font_label_2, command=self.finishOrder)
        self.button_finishOrder.grid(row = 10, column = 2,padx = 0, pady = 570)
        
        # Labels & button (Lunch 1)- ROW 1
        self.img_lunch_name1 = PhotoImage(file="Photo/SetMeal/Skinny Lasagna + Honey green tea.gif")
        self.canvas_lunch1 = Canvas(border1, width =290  , height = 100)
        self.layer_lunch1 = self.canvas_lunch1.create_image(100,50,image = self.img_lunch_name1)
        self.label_lunch_name1 = Label(border1,text = "Skinny Lasagna \t\t\n+ Honey green tea", font = self.font_label_2,justify = LEFT)
        self.label_lunch_price1 = Label(border1,text = "RM 6.00", font = self.font_label_2,justify = RIGHT)
        self.button_choice5 = Button(border1,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice5, justify = RIGHT)

        # Labels & button (Lunch 2)- ROW 2
        self.img_lunch_name2 = PhotoImage(file="Photo/SetMeal/Chicken breast with broccoli + Aloe vera juice.gif")
        self.canvas_lunch2 = Canvas(border2, width = 290 , height = 100)
        self.layer_lunch2 = self.canvas_lunch2.create_image(100, 50,image = self.img_lunch_name2)
        self.label_lunch_name2 = Label(border2,text = "Chicken breast with broccoli \n+ Aloe vera juice", font = self.font_label_2,justify = LEFT)
        self.label_lunch_price2 = Label(border2,text = "RM 6.50", font = self.font_label_2,justify = RIGHT)
        self.button_choice6 = Button(border2,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice6,justify = RIGHT)

        # Labels & button (Lunch 3)- ROW 3
        self.img_lunch_name3 = PhotoImage(file="Photo/SetMeal/Tuna salad pita + Cinnamon coconut latte.gif")
        self.canvas_lunch3 = Canvas(border3, width = 287 , height = 100)
        self.layer_lunch3 = self.canvas_lunch3.create_image(100, 50,image = self.img_lunch_name3)
        self.label_lunch_name3 = Label(border3,text = "Tuna salad pita \t\t\n+ Cinnamon coconut latte", font = self.font_label_2,justify = LEFT)
        self.label_lunch_price3 = Label(border3,text = "RM 7.00", font = self.font_label_2,justify = RIGHT)
        self.button_choice7 = Button(border3,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice7,justify = RIGHT)

        # Labels & button (Lunch 4)- ROW 4
        self.img_lunch_name4 = PhotoImage(file="Photo/SetMeal/Mix fruit salad + Frozen yogurt + Lemon water.gif")
        self.canvas_lunch4 = Canvas(border4, width = 286 , height = 100)
        self.layer_lunch4 = self.canvas_lunch4.create_image(100, 50,image = self.img_lunch_name4)
        self.label_lunch_name4 = Label(border4,text = "Mix fruit salad + Frozen yogurt\n + Lemon water", font = self.font_label_2,justify = LEFT)
        self.label_lunch_price4 = Label(border4,text = "RM 7.20", font = self.font_label_2,justify = RIGHT)
        self.button_choice8 = Button(border4,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice8,justify = RIGHT)

        # Widgets Grid
        # Lunch 1
        self.canvas_lunch1.grid(row=4, column=0, padx = 10, pady = 10)
        self.label_lunch_name1.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.label_lunch_price1.grid(row = 4, column = 2, padx = 10, pady = 10)
        self.button_choice5.grid(row = 4, column = 3, padx = 5, pady = 10 )

        # Lunch 2
        self.canvas_lunch2.grid(row=5, column=0, padx = 10, pady = 10)
        self.label_lunch_name2.grid(row = 5, column = 1,padx = 10, pady = 10)
        self.label_lunch_price2.grid(row = 5, column = 2, padx = 10, pady = 10)
        self.button_choice6.grid(row = 5, column = 3, padx = 10, pady = 10)
        
        # Lunch 3
        self.canvas_lunch3.grid(row=6, column=0, padx = 10, pady = 10)
        self.label_lunch_name3.grid(row = 6, column = 1, padx = 10, pady = 10)
        self.label_lunch_price3.grid(row = 6, column = 2, padx = 10, pady = 10)
        self.button_choice7.grid(row = 6, column = 3, padx = 10, pady = 10)
        
        # Lunch 4
        self.canvas_lunch4.grid(row=7, column=0, padx = 10, pady = 10)
        self.label_lunch_name4.grid(row = 7, column = 1, padx = 10, pady = 10)
        self.label_lunch_price4.grid(row = 7, column = 2, padx = 10, pady = 10)
        self.button_choice8.grid(row = 7, column = 3, padx = 10, pady = 10)
        self.centralize_window()

        if status == "member":
          self.point_info = Label(text = "{}".format(point), bg="white", font = self.font_label_2, justify = LEFT)
          self.point_info.place(x=63,y=12)
        
    def choice5(self):
        self.destroy()
        Lunch1(None).title("Lunch 1")
        
    def choice6(self):
        self.destroy()
        Lunch2(None).title("Lunch 2")

    def choice7(self):
        self.destroy()
        Lunch3(None).title("Lunch 3")

    def choice8(self):
        self.destroy()
        Lunch4(None).title("Lunch 4")

    def back(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def finishOrder(self):
        self.destroy()
        totalCalories(None).title("Summary of Order")

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

class DinnerPage(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
        self.minsize(760, 700)
        self.maxsize(760, 700)
        border1 = Frame(self, relief = RIDGE, borderwidth=1.3)
        border1.place(relx=0.02, rely=0.150, anchor=NW)
        border2 = Frame(self,relief=SUNKEN, borderwidth=1.3)
        border2.place(relx=0.02 , rely=0.34, anchor=NW)
        border3 = Frame(self,relief = RIDGE, borderwidth=1.3)
        border3.place(relx=0.02, rely=0.53, anchor=NW)
        border4 = Frame(self,relief = SUNKEN, borderwidth=1.4)
        border4.place(relx=0.02, rely=0.72, anchor=NW)

        # Create fonts
        self.font_titleDinner = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.font_label_1 = font.Font(family = "Tahoma", size = 14)
        self.font_label_2 = font.Font(family = "Tahoma", size = 12)

        # Create title text for main menu
        label_titleDinner = Label(self, text = "Dinner", bg = "cyan", fg = "black", font = self.font_titleDinner) 
        label_titleDinner.grid(row=0,column=1, padx = 200, pady = 10)

        # Point Label (top)
        self.label_point = Label(text = "Point:",bg = "light pink",font = self.font_label_1)
        self.label_point.grid(row = 0, column = 0, sticky = N+W, pady = 10)

        # Cart Button (top)
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command=self.summary)
        self.button_shoppingCart.grid(row = 0, column = 2, padx = 63, pady = 5,sticky = N+E)

        # Back / Main Menu / Finish Order Buttons (bottom)
        self.button_back = Button(text="Back", bg="green2", fg="white",font = self.font_label_2, command=self.back)
        self.button_back.grid(row = 10, column = 0 , padx = 5, pady = 570)
        self.button_finishOrder = Button(text="Finish Order", bg="firebrick1",fg="white", font = self.font_label_2, command=self.finishOrder)
        self.button_finishOrder.grid(row = 10, column = 2 ,padx = 0, pady = 570)
        
        # Labels & button (Dinner 1)- ROW 1
        self.img_dinner_name1 = PhotoImage(file="Photo/SetMeal/Turkey sandwich + Dark raw hot chocolate.gif")
        self.canvas_dinner1 = Canvas(border1, width =290  , height = 100)
        self.layer_dinner1 = self.canvas_dinner1.create_image(100,50,image = self.img_dinner_name1)
        self.label_dinner_name1 = Label(border1,text = "Turkey sandwich\t\t\n + Dark raw hot chocolate", font = self.font_label_2,justify = LEFT)
        self.label_dinner_price1 = Label(border1,text = "RM 5.50", font = self.font_label_2,justify = RIGHT)
        self.button_choice9 = Button(border1,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice9, justify = RIGHT)

        # Labels & button (Dinner 2)- ROW 2
        self.img_dinner_name2 = PhotoImage(file="Photo/SetMeal/Chicken breast with broccoli + Aloe vera juice.gif")
        self.canvas_dinner2 = Canvas(border2, width = 290 , height = 100)
        self.layer_dinner2 = self.canvas_dinner2.create_image(100, 50,image = self.img_dinner_name2)
        self.label_dinner_name2 = Label(border2,text = "Chicken breast with broccoli\t\n + Aloe vera juice", font = self.font_label_2,justify = LEFT)
        self.label_dinner_price2 = Label(border2,text = "RM 6.50", font = self.font_label_2,justify = RIGHT)
        self.button_choice10 = Button(border2,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice10,justify = RIGHT)

        # Labels & button (Dinner 3)- ROW 3
        self.img_dinner_name3 = PhotoImage(file="Photo/SetMeal/Avocado tomato salad + Light coffee smoothies.gif")
        self.canvas_dinner3 = Canvas(border3, width = 287 , height = 100)
        self.layer_dinner3 = self.canvas_dinner3.create_image(100, 50,image = self.img_dinner_name3)
        self.label_dinner_name3 = Label(border3,text = "Avocado tomato salad \t\n+ Light coffee smoothies", font = self.font_label_2,justify = LEFT)
        self.label_dinner_price3 = Label(border3,text = "RM 6.50", font = self.font_label_2,justify = RIGHT)
        self.button_choice11 = Button(border3,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice11,justify = RIGHT)

        # Labels & button (Dinner 4)- ROW 4
        self.img_dinner_name4 = PhotoImage(file="Photo/SetMeal/Pesto pasta + Watermelon juice.gif")
        self.canvas_dinner4 = Canvas(border4, width = 286 , height = 100)
        self.layer_dinner4 = self.canvas_dinner4.create_image(100, 50,image = self.img_dinner_name4)
        self.label_dinner_name4 = Label(border4,text = "Pesto pasta \t\t\n + Watermelon juice", font = self.font_label_2,justify = LEFT)
        self.label_dinner_price4 = Label(border4,text = "RM 7.20", font = self.font_label_2,justify = RIGHT)
        self.button_choice12 = Button(border4,text="Select", font =self.font_label_1, bg="yellow", fg="black", command=self.choice12,justify = RIGHT)

        # Widgets grid
        # Dinner 1
        self.canvas_dinner1.grid(row=4, column=0, padx = 10, pady = 10)
        self.label_dinner_name1.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.label_dinner_price1.grid(row = 4, column = 2, padx = 10, pady = 10)
        self.button_choice9.grid(row = 4, column = 3, padx = 5, pady = 10 )

        # Dinner 2
        self.canvas_dinner2.grid(row=5, column=0, padx = 10, pady = 10)
        self.label_dinner_name2.grid(row = 5, column = 1,padx = 10, pady = 10)
        self.label_dinner_price2.grid(row = 5, column = 2, padx = 10, pady = 10)
        self.button_choice10.grid(row = 5, column = 3, padx = 10, pady = 10)
        
        # Dinner 3
        self.canvas_dinner3.grid(row=6, column=0, padx = 10, pady = 10)
        self.label_dinner_name3.grid(row = 6, column = 1, padx = 10, pady = 10)
        self.label_dinner_price3.grid(row = 6, column = 2, padx = 10, pady = 10)
        self.button_choice11.grid(row = 6, column = 3, padx = 10, pady = 10)
        
        # Dinner 4
        self.canvas_dinner4.grid(row=7, column=0, padx = 10, pady = 10)
        self.label_dinner_name4.grid(row = 7, column = 1, padx = 10, pady = 10)
        self.label_dinner_price4.grid(row = 7, column = 2, padx = 10, pady = 10)
        self.button_choice12.grid(row = 7, column = 3, padx = 10, pady = 10)
        self.centralize_window()

        if status == "member":
          self.point_info = Label(text = "{}".format(point), bg="white", font = self.font_label_2, justify = LEFT)
          self.point_info.place(x=63,y=12)
        
    def choice9(self):
        self.destroy()
        Dinner1(None).title("Dinner 1")
        
    def choice10(self):
        self.destroy()
        Dinner2(None).title("Dinner 2")

    def choice11(self):
        self.destroy()
        Dinner3(None).title("Dinner 3")

    def choice12(self):
        self.destroy()
        Dinner4(None).title("Dinner 4")

    def back(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def finishOrder(self):
        self.destroy()
        totalCalories(None).title("Summary of Order")

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

# Breakfast
class Breakfast1(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
    
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)

        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)
    
        # Labels
        self.meal_img_1 = PhotoImage(file="Photo/SetMeal/Scrambled egg sandwich with cucumber + Lemon water.gif")
        self.label_meal_img_1 = Label(bg="orange2",image=self.meal_img_1)
        self.label_name1 = Label(text="Scrambled egg sandwich\nwith cucumber + Lemon water", bg="white", font= self.font_label_1)
        self.label_price1 = Label(text="RM 5.50", bg="yellow", font = self.font_label_1)
        self.label_calories1 = Label(text="350 Calories", bg="light blue",font = self.font_label_1)
        self.label_description1 = Label(text=" ~ Protein packed sandwich with scrambled eggs,cucumber \nand cream cheese, makes a perfect lunch box or \npicnic lunch or even a wholesome breakfast.",bg="white", font = self.font_label_1)
        self.label_nutrition1 = Label(text="Total Fat\t\t12 g\nSodium\t         581 mg\nPotassium\t        355 mg\nCarbohydrates\t48 g\nProtein\t\t14 g\nFibre\t\t7 g", bg="white", fg="blue", font = self.font_label_3)  

        # Labels Grid
        self.label_meal_img_1.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name1.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description1.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_calories1.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition1.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.label_price1.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.centralize_window()
         
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "Scrambled egg sandwich \nwith cucumber + Lemon water" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Scrambled egg sandwich \nwith cucumber + Lemon water")
            prices.append(float("5.50"))
            calories.append(int("350"))
        elif "Scrambled egg sandwich \nwith cucumber + Lemon water" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")
            
    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        BreakfastPage(None).title("Breakfast")

class Breakfast2(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
    
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)

        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)
        
        # Labels
        self.meal_img_2 = PhotoImage(file="Photo/SetMeal/Turkey sandwich + Dark raw hot chocolate.gif")
        self.label_meal_img_2 = Label(bg="orange2",image=self.meal_img_2)
        self.label_name2 = Label(text="Turkey sandwich \n + Dark raw hot chocolate",bg="white", font= self.font_label_1)
        self.label_price2 = Label(text="RM 5.50 ", bg="yellow", font = self.font_label_1)
        self.label_calories2 = Label(text="468 Calories", bg="light blue",font = self.font_label_1)
        self.label_description2 = Label(text=" ~ A fantastic sandwich with sliced turkey, toasted whole wheat bread,\n fresh tomato, lettuce, bean sprouts, yellow mustard and light mayo.", bg="white",font = self.font_label_1)
        self.label_nutrition2 = Label(text="Total Fat\t\t10.94 g\nSodium\t           720 mg\nPotassium\t          309 mg\nCarbohydrates\t60.70 g\nProtein\t\t29.11 g\nFibre\t\t0.50 g", bg="white",fg="blue", font = self.font_label_3)  

        # Labels Grid
        self.label_meal_img_2.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name2.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description2.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price2.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories2.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition2.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()
            
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "Turkey sandwich \n+ Dark raw hot chocolate" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Turkey sandwich \n+ Dark raw hot chocolate")
            prices.append(float("5.50"))
            calories.append(int("468"))
        elif "Turkey sandwich \n+ Dark raw hot chocolate" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        BreakfastPage(None).title("Breakfast")

class Breakfast3(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
    
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)
    
        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)

        # Labels
        self.meal_img_3 = PhotoImage(file="Photo/SetMeal/English Muffin With Peanut Butter + Vanilla latte.gif")
        self.label_meal_img_3 = Label(bg="orange2",image=self.meal_img_3)
        self.label_name3 = Label(text="English Muffin With \nPeanut Butter + Vanilla latte",bg="white", font= self.font_label_1)
        self.label_price3 = Label(text="RM 6.00 ", bg="yellow", font = self.font_label_1)
        self.label_calories3 = Label(text="440 Calories", bg="light blue",font = self.font_label_1)
        self.label_description3 = Label(text=" ~ Whole wheat English muffin topped with\n peanut butter, honey and chia seeds.",bg="white", font = self.font_label_1)
        self.label_nutrition3 = Label(text="Total Fat\t\t13.70 g\nSodium\t         167 mg\nPotassium\t        551 mg\nCarbohydrates\t68 g\nProtein\t\t9 g\nFibre\t\t0 g", bg="white", fg="blue", font = self.font_label_3)  
    
        # Labels Grid
        self.label_meal_img_3.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name3.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description3.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price3.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories3.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition3.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()
            
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "English Muffin With \nPeanut Butter + Vanilla latte" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("English Muffin With \nPeanut Butter + Vanilla latte")
            prices.append(float("6.00"))
            calories.append(int("440"))
        elif "English Muffin With \nPeanut Butter + Vanilla latte" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        BreakfastPage(None).title("Breakfast")
        
class Breakfast4(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
    
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)
        
        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)
        
        # Labels
        self.meal_img_4 = PhotoImage(file="Photo/SetMeal/Mix fruit salad + Frozen yogurt + Lemon water.gif")
        self.label_meal_img_4 = Label(bg="orange2",image=self.meal_img_4)
        self.label_name4 = Label(text="Mix fruit salad + \nFrozen yogurt + Lemon water",bg="white", font= self.font_label_1)
        self.label_price4 = Label(text="RM 7.20 ", bg="yellow", font = self.font_label_1)
        self.label_calories4 = Label(text="440 Calories", bg="light blue",font = self.font_label_1)
        self.label_description4 = Label(text=" ~ Creamy fruit salad with strawberries,\nkiwi fruits, grapes and blueberries.",bg="white", font = self.font_label_1)
        self.label_nutrition4 = Label(text="Total Fat\t\t6.90 g\nSodium\t         115 mg\nPotassium\t        772 mg\nCarbohydrates\t77 g\nProtein\t\t7 g\nFibre\t\t0 g",bg="white", fg="blue", font = self.font_label_3)  
        
        # Labels Grid
        self.label_meal_img_4.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name4.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description4.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price4.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories4.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition4.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()
            
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "Mix fruit salad + \nFrozen yogurt + Lemon water" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Mix fruit salad + \nFrozen yogurt + Lemon water")
            prices.append(float("7.20"))
            calories.append(int("440"))
        elif "Mix fruit salad + \nFrozen yogurt + Lemon water" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        BreakfastPage(None).title("Breakfast")

class Lunch1(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
    
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)

        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)

        # Labels
        self.meal_img_5 = PhotoImage(file="Photo/SetMeal/Skinny Lasagna + Honey green tea.gif")
        self.label_meal_img_5 = Label(bg="yellow2",image=self.meal_img_5)
        self.label_name5 = Label(text="Skinny Lasagna + Honey green tea",bg="white", font= self.font_label_1)
        self.label_price5 = Label(text="RM 6.00 ", bg="yellow", font = self.font_label_1)
        self.label_calories5 = Label(text="310 Calories", bg="light blue",font = self.font_label_1)
        self.label_description5 = Label(text=" ~  Lagsana full of chopped broccoli, carrots, \ncauliflower, spinach, ricotta cheese, and tomato sauce.",bg="white", font = self.font_label_1)
        self.label_nutrition5 = Label(text="Total Fat\t\t9 g\nSodium\t         415 mg\nPotassium\t        125 mg\nCarbohydrates\t40 g\nProtein\t\t20 g\nFibre\t\t0 g", bg="white", fg="blue", font = self.font_label_3)  

        # Labels Grid
        self.label_meal_img_5.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name5.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description5.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price5.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories5.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition5.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()
            
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
         if len(foods) < 4 and "Skinny Lasagna \n+ Honey green tea" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Skinny Lasagna \n+ Honey green tea")
            prices.append(float("6.00"))
            calories.append(int("310"))
         elif "Skinny Lasagna \n+ Honey green tea" in foods:
            messagebox.showerror("Sorry","Item has been added")
         else:
            messagebox.showerror("Sorry","Only 4 item can be added")
            
    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        LunchPage(None).title("Lunch")

class Lunch2(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
    
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)

        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)
        
        # Labels
        self.meal_img_6 = PhotoImage(file="Photo/SetMeal/Chicken breast with broccoli + Aloe vera juice.gif")
        self.label_meal_img_6 = Label(bg="yellow2",image=self.meal_img_6)
        self.label_name6 = Label(text="Chicken breast with broccoli\n + Aloe vera juice", bg="white", font= self.font_label_1)
        self.label_price6 = Label(text="RM 6.50 ", bg="yellow", font = self.font_label_1)
        self.label_calories6 = Label(text="285 Calories", bg="light blue",font = self.font_label_1)
        self.label_description6 = Label(text=" ~ Skinless chicken breast is filled\n with simple fresh broccoli.",bg="white", font = self.font_label_1)
        self.label_nutrition6 = Label(text="Total Fat\t\t9 g\nSodium\t          785 mg\nPotassium\t          0 mg\nCarbohydrates\t23.60 g\nProtein\t\t27 g\n Fibre\t         1.60 g", bg="white", fg="blue", font = self.font_label_3)  
        
        # Labels Grid
        self.label_meal_img_6.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name6.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description6.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price6.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories6.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition6.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()
            
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "Chicken breast with \nbroccoli + Aloe vera juice" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Chicken breast with \nbroccoli + Aloe vera juice")
            prices.append(float("6.50"))
            calories.append(int("285"))
        elif "Chicken breast with \nbroccoli + Aloe vera juice" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        LunchPage(None).title("Lunch")

class Lunch3(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
    
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)

        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)
        
        # Labels
        self.meal_img_7 = PhotoImage(file="Photo/SetMeal/Tuna salad pita + Cinnamon coconut latte.gif")
        self.label_meal_img_7 = Label(bg="yellow2",image=self.meal_img_7)
        self.label_name7 = Label(text="Tuna salad pita \n+ Cinnamon coconut latte",bg="white", font= self.font_label_1)
        self.label_price7 = Label(text="RM 7.00 ", bg="yellow", font = self.font_label_1)
        self.label_calories7 = Label(text="476 Calories", bg="light blue",font = self.font_label_1)
        self.label_description7 = Label(text=" ~ Pita bread halves are lined with lettuce and \nsliced tomatoes, and then filled with a tasty tuna\n salad made with creamy mayo in this ultimate sandwich.",bg="white", font = self.font_label_1)
        self.label_nutrition7 = Label(text="Total Fat\t\t12 g\nSodium\t         793 mg\nPotassium\t        659 mg\nCarbohydrates\t54 g\n Protein\t        23.80 g\nFibre\t\t8 g", bg="white",fg="blue", font = self.font_label_3)  
       
        # Labels Grid
        self.label_meal_img_7.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name7.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description7.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price7.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories7.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition7.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()
            
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "Tuna salad pita + \nCinnamon coconut latte" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Tuna salad pita + \nCinnamon coconut latte")
            prices.append(float("7.00"))
            calories.append(int("476"))
        elif "Tuna salad pita + \nCinnamon coconut latte" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        LunchPage(None).title("Lunch")

class Lunch4(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
        
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)

        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)

        # Labels
        self.meal_img_8 = PhotoImage(file="Photo/SetMeal/Mix fruit salad + Frozen yogurt + Lemon water.gif")
        self.label_meal_img_8 = Label(bg="yellow2",image=self.meal_img_8)
        self.label_name8 = Label(text="Mix fruit salad + \nFrozen yogurt + Lemon water",bg="white", font= self.font_label_1)
        self.label_price8 = Label(text="RM 7.20 ", bg="yellow", font = self.font_label_1)
        self.label_calories8 = Label(text="440 Calories", bg="light blue",font = self.font_label_1)
        self.label_description8 = Label(text=" ~ Creamy fruit salad with strawberries,\nkiwi fruits, grapes and blueberries.", bg="white",font = self.font_label_1)
        self.label_nutrition8 = Label(text="Total Fat\t\t6.90 g\nSodium\t         115 mg\nPotassium\t        772 mg\nCarbohydrates\t77 g\nProtein\t\t7 g\nFibre\t\t0 g", bg="white",fg="blue", font = self.font_label_3)  
        
        # Labels Grid
        self.label_meal_img_8.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name8.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description8.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price8.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories8.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition8.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "Mix fruit salad + \nFrozen yogurt + Lemon water" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Mix fruit salad + \nFrozen yogurt + Lemon water")
            prices.append(float("7.20"))
            calories.append(int("440"))
        elif "Mix fruit salad + \nFrozen yogurt + Lemon water" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        LunchPage(None).title("Lunch")

class Dinner1(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
    
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)

        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)
        
        # Labels
        self.meal_img_9 = PhotoImage(file="Photo/SetMeal/Turkey sandwich + Dark raw hot chocolate.gif")
        self.label_meal_img_9 = Label(bg="cyan",image=self.meal_img_9)
        self.label_name9 = Label(text="Turkey sandwich \n + Dark raw hot chocolate", bg="white",font= self.font_label_1)
        self.label_price9 = Label(text="RM 5.50 ", bg="yellow", font = self.font_label_1)
        self.label_calories9 = Label(text="468 Calories", bg="light blue",font = self.font_label_1)
        self.label_description9 = Label(text=" ~ A fantastic sandwich with sliced turkey, toasted whole wheat bread,\n fresh tomato, lettuce, bean sprouts, yellow mustard and light mayo.", bg="white",font = self.font_label_1)
        self.label_nutrition9 = Label(text="Total Fat\t\t10.94 g\nSodium\t           720 mg\nPotassium\t          309 mg\nCarbohydrates\t60.70 g\nProtein\t\t29.11 g\nFibre\t\t0.50 g",bg="white", fg="blue", font = self.font_label_3)  
        
        # Labels Grid
        self.label_meal_img_9.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name9.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description9.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price9.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories9.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition9.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()

    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "Turkey sandwich \n+ Dark raw hot chocolate" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Turkey sandwich \n+ Dark raw hot chocolate")
            prices.append(float("5.50"))
            calories.append(int("468"))
        elif "Turkey sandwich \n+ Dark raw hot chocolate" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        DinnerPage(None).title("Dinner")

class Dinner2(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
        
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)

        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)
       
        # Labels
        self.meal_img_10 = PhotoImage(file="Photo/SetMeal/Chicken breast with broccoli + Aloe vera juice.gif")
        self.label_meal_img_10 = Label(bg="cyan",image=self.meal_img_10)
        self.label_name10 = Label(text="Chicken breast with broccoli\n + Aloe vera juice",bg="white", font= self.font_label_1)
        self.label_price10 = Label(text="RM 6.50 ", bg="yellow", font = self.font_label_1)
        self.label_calories10 = Label(text="285 Calories", bg="light blue",font = self.font_label_1)
        self.label_description10 = Label(text=" ~ Skinless chicken breast is filled\n with simple fresh broccoli.", bg="white",font = self.font_label_1)
        self.label_nutrition10 = Label(text="Total Fat\t\t9 g\nSodium\t          785 mg\nPotassium\t          0 mg\nCarbohydrates\t23.60 g\nProtein\t\t27 g\n Fibre\t         1.60 g", bg="white",fg="blue", font = self.font_label_3)  
 
        # Labels Grid
        self.label_meal_img_10.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name10.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description10.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price10.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories10.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition10.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()
            
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "Chicken breast with \nbroccoli + Aloe vera juice" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Chicken breast with \nbroccoli + Aloe vera juice")
            prices.append(float("6.50"))
            calories.append(int("285"))
        elif "Chicken breast with \nbroccoli + Aloe vera juice" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        DinnerPage(None).title("Dinner")

class Dinner3(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
    
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)

        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)

        # Labels
        self.meal_img_11 = PhotoImage(file="Photo/SetMeal/Avocado tomato salad + Light coffee smoothies.gif")
        self.label_meal_img_11 = Label(bg="cyan",image=self.meal_img_11)
        self.label_name11 = Label(text="Avocado tomato salad \n+ Light coffee smoothies",bg="white", font= self.font_label_1)
        self.label_price11 = Label(text="RM 6.50 ", bg="yellow", font = self.font_label_1)
        self.label_calories11 = Label(text="409 Calories", bg="light blue",font = self.font_label_1)
        self.label_description11 = Label(text=" ~ Classic cucumber and tomato salad just got better with\n the addition of avocado, a light and flavorful lemon\n dressing and the freshness of cilantro.", bg="white",font = self.font_label_1)
        self.label_nutrition11 = Label(text="Total Fat\t\t22 g\nSodium\t          611 mg\nPotassium\t          886 mg\nCarbohydrates\t58.90 g\nProtein\t\t3.70 g\n Fibre\t         8.70 g",bg="white", fg="blue", font = self.font_label_3)  
        
        # Labels Grid
        self.label_meal_img_11.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name11.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description11.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price11.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories11.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition11.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()
            
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "Avocado tomato salad \n+ Light coffee smoothies" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Avocado tomato salad \n+ Light coffee smoothies")
            prices.append(float("6.50"))
            calories.append(int("409"))
        elif "Avocado tomato salad \n+ Light coffee smoothies" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")
            
    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        DinnerPage(None).title("Dinner")

class Dinner4(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
    
        # Create font
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "comic sans ms", size = 12, weight = "bold" )

        # Buttons
        self.img_shoppingCart = PhotoImage(file="Photo/SetMeal/shopping_cart.png")
        self.button_shoppingCart = Button(bg="lightyellow", image = self.img_shoppingCart, command = self.summary)
        self.button_addCart = Button (text="Add to \nCart", bg="orange2", fg="white", font = self.font_label_2, command = self.AddCart )
        self.button_mainMenu = Button (text="Main Menu", bg="purple", fg="white", font = self.font_label_2, command = self.MainMenu )
        self.button_back = Button (text="Back", bg="green2" , fg="white", font = self.font_label_2, command = self.back)

        # Buttons Grid
        self.button_shoppingCart.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=NE)
        self.button_addCart.grid(row = 8, column = 1, padx = 155, pady = 25, sticky = E)
        self.button_mainMenu.grid(row = 8, column = 1, padx = 58, pady = 25, sticky = E)
        self.button_back.grid(row = 8, column = 1, padx = 0, pady = 30, sticky = E)
       
        # Labels
        self.meal_img_12 = PhotoImage(file="Photo/SetMeal/Pesto pasta + Watermelon juice.gif")
        self.label_meal_img_12 = Label(bg="cyan",image=self.meal_img_12)
        self.label_name12 = Label(text="Pesto pasta + Watermelon juice", bg="white",font= self.font_label_1)
        self.label_price12 = Label(text="RM 7.80 ", bg="yellow", font = self.font_label_1)
        self.label_calories12 = Label(text="309 Calories", bg="light blue",font = self.font_label_1)
        self.label_description12 = Label(text=" ~ Pasta with creamy blended bright green sauce.", bg="white",font = self.font_label_1)
        self.label_nutrition12 = Label(text="Total Fat\t\t5.10 g\nSodium\t          217 mg\nPotassium\t          363 mg\nCarbohydrates\t57 g\nProtein\t\t12.50 g\n Fibre\t         0.30 g",bg="white", fg="blue", font = self.font_label_3)  
       
        # Labels Grid
        self.label_meal_img_12.grid(row = 1, column = 1, padx = 75, pady = 15 )
        self.label_name12.grid(row = 2, column = 1, padx = 0, pady = 5)
        self.label_description12.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.label_price12.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.label_calories12.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.label_nutrition12.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.centralize_window()
            
    def summary(self):
        self.destroy()
        Summary(None).title("Shopping Cart")

    def AddCart(self):
        if len(foods) < 4 and "Pesto pasta + \nWatermelon juice" not in foods:
            messagebox.showinfo("Success","Add item to cart")
            foods.append("Pesto pasta + \nWatermelon juice")
            prices.append(float("7.80"))
            calories.append(int("309"))
        elif "Pesto pasta + \nWatermelon juice" in foods:
            messagebox.showerror("Sorry","Item has been added")
        else:
            messagebox.showerror("Sorry","Only 4 item can be added")

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")
            
    def back(self):
        self.destroy()
        DinnerPage(None).title("Dinner")

# Shopping Cart       
class Summary(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.grid()
        self.resizable(False, False)
        self.configure(bg="white")
        self.minsize(680, 650)
        self.maxsize(680, 650)


        # Font
        self.font_title = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.font_label_1 = font.Font(family = "Tahoma", size = 13)
        self.font_label_2 = font.Font(family = "Tahoma", size = 11)
        self.font_label_3 = font.Font(family = "Comic Sans MS", size = 14)

         # Create title text 
        label_title = Label(self, text = "Shopping Cart", bg = "black", fg = "white",font=self.font_title)
        label_title.grid(row=0,column=2, padx = 0, pady = 10, sticky=W+E)
        
        # Button(Bottom)
        self.button_mainMenu = Button(text="Main Menu", bg="#F364F3", fg="black", font = self.font_label_3, command=self.MainMenu)
        self.button_mainMenu.grid(row = 1, column = 1, padx = 35, pady = 500, sticky=W)
        self.button_finishOrder = Button(text="Finish Order", bg="firebrick1", fg="black", font = self.font_label_3, command=self.finishOrder)
        self.button_finishOrder.grid(row = 1, column = 3, padx = 0, pady = 500, sticky=SE)
        self.img_button_cancel=PhotoImage(file="Photo/Food/cancel.png")
        self.centralize_window()

        for i in range (len(foods)) :
            border = Frame(self, relief = RIDGE, borderwidth=1.3)
            border.place(relx=0.02, rely=(i+1)*0.15+(i*0.04), anchor=NW)
            self.food = Label(border,text = foods[i], font = self.font_label_1, justify = LEFT)
            self.food.grid(row = 1, column = 1, padx = 5, pady = 10)
            self.price = Label(border,text = "RM{:.2f}".format(prices[i]), font = self.font_label_1, justify = LEFT)
            self.price.grid(row = 1, column = 2, padx = 25, pady = 10)
            self.calorie = Label(border,text = "{} calories".format(calories[i]), font = self.font_label_1, justify = LEFT)
            self.calorie.grid(row = 1, column = 4, padx = 55, pady = 10)
            if i == 0 :
              self.button_cancel= Button(border,bg="white",image = self.img_button_cancel,command=self.cancel1)
              self.button_cancel.grid(row = 1, column = 6, padx = 5, pady = 10)
            elif i == 1 :
              self.button_cancel= Button(border,bg="white",image = self.img_button_cancel,command=self.cancel2)
              self.button_cancel.grid(row = 1, column = 6, padx = 5, pady = 10)
            elif i == 2 :
              self.button_cancel= Button(border,bg="white",image = self.img_button_cancel,command=self.cancel3)
              self.button_cancel.grid(row = 1, column = 6, padx = 5, pady = 10)
            elif i == 3 :
              self.button_cancel= Button(border,bg="white",image = self.img_button_cancel,command=self.cancel4)
              self.button_cancel.grid(row = 1, column = 6, padx = 5, pady = 10)
       
      
    def cancel1(self):
        foods.pop(0)
        prices.pop(0)
        calories.pop(0)
        self.destroy()
        Summary(None).title("Shopping Cart")

    def cancel2(self):
        foods.pop(1)
        prices.pop(1)
        calories.pop(1)
        self.destroy()
        Summary(None).title("Shopping Cart")
         
    def cancel3(self):
        foods.pop(2)
        prices.pop(2)
        calories.pop(2)
        self.destroy()
        Summary(None).title("Shopping Cart")
        
    def cancel4(self):
        foods.pop(3)
        prices.pop(3)
        calories.pop(3)
        self.destroy()
        Summary(None).title("Shopping Cart")
  
    def MainMenu(self):
        self.destroy()
        MainMenu(None).title("Main Menu")

    def finishOrder(self):
        self.destroy()
        totalCalories(None).title("Summary of Order")

class totalCalories(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.geometry('550x600')
        self.resizable(False, False)
        self.configure(bg="white")

        # Font
        self.font_label_1 = font.Font(family = "Comic Sans MS", size = 18)
        self.font_label_2 = font.Font(family = "Comic Sans MS", size = 14)
        self.font_label_3 = font.Font(family = "Comic Sans MS", size = 12)

        # Button(Bottom)
        self.button_MainMenu = Button(text="Main Menu", bg="yellow", fg="black",font = self.font_label_2, width = 8, height = 1, command = self.MainMenu)
        self.button_cartSum = Button(text="Check Prices", bg="#00FF09", fg="black", font = self.font_label_2, width = 15, height = 1, command = self.cartSum)

        # Label
        self.label_title = Label(text = "Total Calories", font = self.font_label_1, justify = CENTER, bg = '#72D1FF', width = 14, height = 1)
        self.label_list = Label(text = "List of item(s):", font = self.font_label_3, justify = LEFT, bg = '#B5FCFF')
        self.label_quantity = Label(text = "Total quantity of item(s):", font = self.font_label_3, justify = LEFT, bg = '#B5FCFF')
        self.label_calories = Label(text = "Total calories:", font = self.font_label_3, justify = LEFT, bg = '#B5FCFF')
        self.label_burnCalories = Label(text = "Total steps needed to burn calories:", font = self.font_label_3, justify = LEFT, bg = '#B5FCFF')
        self.centralize_window()

        for i in range (len(foods)) :
            self.food = Label(text = "{}  ({} calories)".format(foods[i],calories[i]),bg="white", font = self.font_label_3, justify = LEFT)
            self.food.place(x=130,y=(i+1)*70-(20*i))
            self.totalCalories = Label(text = "{} calories".format(sum(calories)), bg="white",font = self.font_label_3, justify = LEFT)
            self.totalCalories.place(x=140,y=400)
            self.steps = Label(text = "{} steps".format(sum(calories)//0.05), bg="white",font = self.font_label_3, justify = LEFT)
            self.steps.place(x = 300, y=450)
            self.quantity = Label(text = len(foods), font = self.font_label_3,bg="white", justify = LEFT)
            self.quantity.place(x=220,y=350)
       
        
        # Layout widgets
        self.label_title.place(x=170, y=10)
        self.label_list.place(x=20, y=70)
        self.label_quantity.place(x=20, y=350)
        self.label_calories.place(x=20, y=400)
        self.label_burnCalories.place(x=20,y=450)
        self.button_MainMenu.place(x=10, y=540)
        self.button_cartSum.place(x=365, y=540)
        self.centralize_window()

    def MainMenu(self):
        self.destroy()
        MainMenu(None).title('Main Menu')

    def cartSum(self):
        self.destroy()
        CartSummary(None).title('Cart Summary')

class CartSummary(Tk):
    
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        self.resizable(False,False)
        self.geometry('550x600')
        self.config(bg = 'white')
        #self.overrideredirect(True)

        # Font
        self.font_label_1 = font.Font(family = "Comic Sans MS", size = 18)
        self.font_label_2 = font.Font(family = "Comic Sans MS", size = 14)
        self.font_label_3 = font.Font(family = "Comic Sans MS", size = 12)

        # Button(Bottom)
        self.button_back = Button(text="Back", bg="yellow", fg="black",font = self.font_label_2, width = 8, height = 1, command = self.back)
        self.button_pr = Button(text="Point Redemption", bg="#F364F3", fg="black", font = self.font_label_2, width = 15, height = 1, command = self.PointRedemptionPage)
        self.button_pp = Button(text="Proceed to Pay", bg="#00FF09", fg="black", font = self.font_label_2, width = 15, height = 1, command = self.ProceedPay)

        # Label
        self.label_title = Label(text = "Cart Summary", font = self.font_label_1, justify = CENTER, bg = '#19E1EF', width = 14, height = 1)
        self.label_list = Label(text = "List of item(s):", font = self.font_label_3, justify = LEFT, bg = '#B5FCFF')
        self.label_quantity = Label(text = "Total quantity of item(s):", font = self.font_label_3, justify = LEFT, bg = '#B5FCFF')
        self.label_money = Label(text = "Total amount of money (RM):", font = self.font_label_3, justify = LEFT, bg = '#B5FCFF')

        for i in range (len(foods)) :
            self.food = Label(text = "{}  (RM{:.2f})".format(foods[i],prices[i]),bg="white", font = self.font_label_3, justify = LEFT)
            self.food.place(x=140,y=(i+1)*70-(20*i))
            self.totalPrices = Label(text = "RM{:.2f}".format(sum(prices)), bg="white",font = self.font_label_3, justify = LEFT)
            self.totalPrices.place(x=245,y=320)
            self.quantity = Label(text = len(foods), font = self.font_label_3,bg="white", justify = LEFT)
            self.quantity.place(x=220,y=270)
            if status == "member":
              self.label_members = Label(text = "For members only:", font = self.font_label_3, justify = LEFT, bg = '#B5FCFF')
              self.label_discount = Label(text = "Total amount of money after discount (RM):", font = self.font_label_3, justify = LEFT, bg = '#B5FCFF')
              self.label_points = Label(text = "Points earned:", font = self.font_label_3, justify = LEFT, bg = '#B5FCFF')
              self.label_members.place(x=20, y=390)
              self.label_discount.place(x=20, y=430)
              self.label_points.place(x=20, y=470)
              self.discount = Label(text = "RM{:.2f}".format(sum(prices) * 0.9 + fee),bg="white", font = self.font_label_3, justify = LEFT)
              self.discount.place(x=355,y=430)
              self.point_info = Label(text = "{}".format(math.floor(sum(prices))), bg="white",font = self.font_label_3, justify = LEFT)
              self.point_info.place(x=132,y=470)
              self.label_title.place(x=170, y=10)

        self.label_title.place(x=170, y=10)      
        self.label_list.place(x=20, y=70)
        self.label_quantity.place(x=20, y=270)
        self.label_money.place(x=20, y=320)
        self.button_back.place(x=10, y=540)
        self.button_pr.place(x=180, y=540)
        self.button_pp.place(x=365, y=540)
        self.centralize_window()
            

    def back(self):
        self.destroy()
        totalCalories(None).title('Summary of Order')

    def PointRedemptionPage(self):
        self.destroy()
        PointRedemptionPage(None).title('Point Redemption')
        
    def ProceedPay(self):
        self.destroy()
        root=Tk()
        root.geometry("600x680+0+0")
        root.resizable(False,False)
        root.title("E-Receipt")
        root.configure(background='white')
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        #===============================FRAME====================================#
        Tops = Frame(root,width=750, height=480, bd=5)

        Tops.pack(side=TOP)

        Tops.configure(background='black')

        f2 = Frame(root, width=800, height= 650, bd=10)
        f2.pack(side=TOP)

        f2.configure(background='gainsboro',relief='raise')

        f3 = Frame(root, width=550, height=650, bd=5)
        f3.pack(side=TOP)

        #==================================VAR========================================#
        DateofOrder=StringVar()
        Receipt_Ref=StringVar()
        #==================================FUNCTION===================================#
        def qExit():
            qExit=messagebox.askyesno("Log Out","Do you want to log out and quit Cut the Weight Vending Machine?")
            if qExit > 0:
              if status == "member":
                if 'ok' in test :
                  file2 = open(username1 + "point" , "w")
                  file2.write("{}".format(math.floor(rp+sum(prices)))+ "\n")
                  file2.write("0")
                  file2.close
                else :    
                  file2 = open(username1 + "point" , "w")
                  file2.write("{}".format(math.floor(point+sum(prices)))+ "\n")
                  file2.write("0")
                  file2.close
                root.destroy()
                return
              else:
                root.destroy()
                return
              
        def Receipt():
            txtReceipt.delete("1.0",END)
            
            x = random.randint(10908,500876)
            randomRef = str(x)
            Receipt_Ref.set(randomRef,)
            DateofOrder.set(time.strftime("%d/%m/%Y %H:%M:%S"))

            txtReceipt.insert(END,'Receipt Ref:\t'+ Receipt_Ref.get()+ '\n')
            txtReceipt.insert(END,'Date:'+DateofOrder.get()+ '\n')
            if status == "member":
              TotalPrice = sum(prices) * 0.9+ fee
            else:
              TotalPrice = sum(prices)
            txtReceipt.insert(END,'Item(s)\t\t\t\t\t' + "Cost of Item(RM)"+ '\n')
            if len(foods) == 0:
              messagebox.showerror("Sorry","No item be added.")
              if len(foodRedeem) == 1:
                txtReceipt.insert(END,'\n\n\n'+'~For Member Redemption:~'+ '\n')
                txtReceipt.insert(END,'{}'.format(foodRedeem[0])+'\t\t\t\t\t'+'{} points'.format(pointRedeem[0]) +'\n\n\n\n\n\n\n\n\n\n\n\n')
            elif len(foods) == 1:
              txtReceipt.insert(END,'{}'.format(foods[0])+'\t\t\t\t\t\t'+'{:.2f}'.format(prices[0]) +'\n\n\n\n\n\n\n\n\n')
              if len(foodRedeem) == 1:
                txtReceipt.insert(END,'\n\n\n'+'~For Member Redemption:~'+ '\n')
                txtReceipt.insert(END,'{}'.format(foodRedeem[0])+'\t\t\t\t\t\t'+'{} points'.format(pointRedeem[0])+'\n\n\n')
              if status == "member":
                txtReceipt.insert(END, '~~~~~Member Price:~~~~~'+'\n')
              txtReceipt.insert(END, 'Total Price: \t\t\t\t\t\tRM{:.2f}'.format(TotalPrice))
            elif len(foods) == 2 :
              txtReceipt.insert(END,'{}'.format(foods[0])+'\t\t\t\t\t\t'+'{:.2f}'.format(prices[0]) +'\n')
              txtReceipt.insert(END,'{}'.format(foods[1])+'\t\t\t\t\t\t'+'{:.2f}'.format(prices[1]) +'\n\n\n\n\n\n')
              if len(foodRedeem) == 1:
                txtReceipt.insert(END,'\n\n\n'+'~For Member Redemption:~'+ '\n')
                txtReceipt.insert(END,'{}'.format(foodRedeem[0])+'\t\t\t\t\t\t'+'{} points'.format(pointRedeem[0])+'\n\n\n')
              if status == "member":
                txtReceipt.insert(END, '~~~~~Member Price:~~~~~'+'\n')
              txtReceipt.insert(END, 'Total Price: \t\t\t\t\t\tRM{:.2f}'.format(TotalPrice))
            elif len(foods) == 3 :
              txtReceipt.insert(END,'{}'.format(foods[0])+'\t\t\t\t\t\t'+'{:.2f}'.format(prices[0]) +'\n')
              txtReceipt.insert(END,'{}'.format(foods[1])+'\t\t\t\t\t\t'+'{:.2f}'.format(prices[1]) +'\n')
              txtReceipt.insert(END,'{}'.format(foods[2])+'\t\t\t\t\t\t'+'{:.2f}'.format(prices[2]) +'\n\n\n\n\n')
              if len(foodRedeem) ==1:
                txtReceipt.insert(END,'\n\n\n'+'~For Member Redemption:~'+ '\n')
                txtReceipt.insert(END,'{}'.format(foodRedeem[0])+'\t\t\t\t\t\t'+'{} points'.format(pointRedeem[0])+ '\n\n\n')
              if status == "member":
                txtReceipt.insert(END, '~~~~~Member Price:~~~~~'+'\n')
              txtReceipt.insert(END, 'Total Price: \t\t\t\t\t\tRM{:.2f}'.format(TotalPrice))
            else :
              txtReceipt.insert(END,'{}'.format(foods[0])+'\t\t\t\t\t\t'+'{:.2f}'.format(prices[0]) +'\n')
              txtReceipt.insert(END,'{}'.format(foods[1])+'\t\t\t\t\t\t'+'{:.2f}'.format(prices[1]) +'\n')
              txtReceipt.insert(END,'{}'.format(foods[2])+'\t\t\t\t\t\t'+'{:.2f}'.format(prices[2]) +'\n')
              txtReceipt.insert(END,'{}'.format(foods[3])+'\t\t\t\t\t\t'+'{:.2f}'.format(prices[3]) +'\n\n\n')
              if len(foodRedeem) ==1:
                txtReceipt.insert(END,'\n\n\n'+'~For Member Redemption:~'+ '\n')
                txtReceipt.insert(END,'{}'.format(foodRedeem[0])+'\t\t\t\t\t\t'+'{} points'.format(pointRedeem[0])+ '\n\n\n')
              if status == "member":
                txtReceipt.insert(END, '~~~~~Member Price:~~~~~'+'\n')
              txtReceipt.insert(END, 'Total Price: \t\t\t\t\t\tRM{:.2f}'.format(TotalPrice))

        #==================================TITLE======================================#
        lblTitle = Label(Tops, font=('Times New Roman', 36, 'bold'),bg="white",fg='black', text= "E-Receipt", bd=5)
        lblTitle.grid(row=0, column=0)

        #==============================INFO======================================#
        lblReceipt = Label(f2,font=('Times New Roman', 14, 'bold'), text="Receipt",bg='gainsboro',fg='maroon', bd=5).grid(row=0,column=0)
        txtReceipt = Text(f2,font=('Times New Roman', 11, 'bold'),fg='black',bg='ivory', bd=8, width=60)
        txtReceipt.grid(row=1,column=0)
        

        #==============================BUTTON=========================================#
        btnReceipt=Button(f3, padx=16, pady=1, bd=4, fg="black", font=('Times New Roman',16,'bold'),width=5,
                          text="Print",bg='white', command = Receipt).grid(row=1,column=0)

        btnExit=Button(f3, padx=16, pady=1, bd=4, fg="black", font=('Times New Roman',16,'bold',), width=5,
                       text="Exit",bg='white',command=qExit).grid(row=2,column=0)

class PointRedemptionPage(Tk):
    
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
    def initialize(self):
        self.geometry('750x550')
        self.resizable(False, False)
        self.configure(bg="white")
        border1 = Frame(self, relief=SOLID, borderwidth=3)
        border1.place(relx=0.02, rely=0.20, anchor=NW)
        border2 = Frame(self,relief = SOLID, borderwidth=3)
        border2.place(relx=0.37 , rely=0.20, anchor=NW)
        border3 = Frame(self,relief = SOLID, borderwidth=3)
        border3.place(relx=0.72, rely=0.20, anchor=NW)

        # Font
        self.font_label_1 = font.Font(family = "Comic Sans MS", size = 18)
        self.font_label_2 = font.Font(family = "Comic Sans MS", size = 14)
        self.font_label_3 = font.Font(family = "Comic Sans MS", size = 12)

        # Button(Bottom)
        self.button_point_back = Button(text="Back to Cart Summary", bg="yellow", fg="black",font = self.font_label_2, width = 19, height = 1, command = self.back_cs)
        self.button_point_back.grid(row=10,column=2,padx=10,pady=350,sticky=W+E)
        # Label
        self.label_menu = Label(text = "Point Redemption Menu", font = self.font_label_1, justify = CENTER, bg = '#66FF94', width = 18, height = 1)
        self.label_menu.grid(row = 0, column=2,padx = 30, pady = 10)
        self.label_points = Label(text = "Total points accumulated:", font = self.font_label_3, justify = LEFT, bg = '#AFFFE0')
        self.label_points.grid(row = 1,padx=5,pady=10)
    
        # Labels & button (Using borders)-LEFT
        self.img_food_name1 = PhotoImage(file="Photo/Food/cherry tomatoes.gif")
        self.canvas_food1 = Canvas(border1, width = 150 , height = 150)
        self.layer_food1 = self.canvas_food1.create_image(100, 70,image = self.img_food_name1)
        self.label_food_name1 = Label(border1,text = "Cherry \nTomatoes", font = self.font_label_2,justify = LEFT)
        self.label_food_price1 = Label(border1,text = "200 points", font = self.font_label_2,justify = LEFT)
        self.button_select1 = Button(border1,text="Select", bg="yellow", fg="black", command=self.selectRedeem1)

         # Labels & button (Using borders)-center
        self.img_food_name2 = PhotoImage(file="Photo/Food/cranberry energy bites.gif")
        self.canvas_food2 = Canvas(border2, width = 150 , height = 150)
        self.layer_food2 = self.canvas_food2.create_image(100, 70,image = self.img_food_name2)
        self.label_food_name2 = Label(border2,text = "Cranberry \nEnergy Bites", font = self.font_label_2, justify = LEFT)
        self.label_food_price2 = Label(border2,text = "250 points", font = self.font_label_2, justify = LEFT)
        self.button_select2 = Button(border2,text="Select", bg="yellow", fg="black", command=self.selectRedeem2)
        
         # Labels & button (Using borders)-right
        self.img_food_name3 = PhotoImage(file="Photo/Food/muesli with raspberries.gif")
        self.canvas_food3 = Canvas(border3, width = 150 , height = 150)
        self.layer_food3= self.canvas_food3.create_image(100, 70,image = self.img_food_name3)
        self.label_food_name3 = Label(border3,text = "Muesli With \nRaspberries", font = self.font_label_2, justify = LEFT)
        self.label_food_price3 = Label(border3,text = "380 ponits", font = self.font_label_2, justify = LEFT)
        self.button_select3 = Button(border3,text="Select", bg="yellow", fg="black", command=self.selectRedeem3)

        
        # Layout widgets
        # First column
        self.canvas_food1.grid(row=2, column=1, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name1.grid(row = 7, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price1.grid(row = 8, column = 1, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select1.grid(row = 9, column = 1, padx = 60, pady = 5, columnspan = 10, sticky = W)

        # Second column
        self.canvas_food2.grid(row=2, column=2, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name2.grid(row = 7, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price2.grid(row = 8, column = 2, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select2.grid(row = 9, column = 2, padx = 60, pady = 5, columnspan = 2, sticky = W)

        # Third column
        self.canvas_food3.grid(row=2, column=3, padx=5, pady=5, rowspan=4, sticky = W)
        self.label_food_name3.grid(row = 7, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.label_food_price3.grid(row = 8, column = 3, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.button_select3.grid(row = 9, column = 3, padx = 60, pady = 5, columnspan = 2, sticky = W)
        self.centralize_window()
        if status == "member":
          self.point_info = Label(text = "{}".format(point), font = self.font_label_3,bg="white", justify = LEFT)
          self.point_info.place(x=200,y=68)
        self.centralize_window()

    def selectRedeem1(self):
      global rp
      if "ok" not in test :
        rp = point
        test.append("ok")
        
      if rp >= 200 and len(foodRedeem)== 0:
        foodRedeem.append("Cherry Tomatoes")
        pointRedeem.append(int("200"))
        redeem = messagebox.askyesno("Redeem","Are you sure to redeem \n{} ({} points)?".format(foodRedeem[0], pointRedeem[0]))
        if redeem > 0:
          messagebox.showinfo("Success","{} ({} points) \nis redeemed.".format(foodRedeem[0], pointRedeem[0]))
          rp -= 200
        else:
          foodRedeem.pop(0)
          pointRedeem.pop(0)
          messagebox.showerror("Fail to redeem","Come to redeem next time.")
          return    
      elif len(foodRedeem) > 0:
        messagebox.showerror("Sorry","Can only redeem one food per time.")
      else:
        messagebox.showerror("Sorry","Not enough point.")

    def selectRedeem2(self):
      global rp
      if "ok" not in test :
        rp = point
        test.append("ok")
        
      if rp >= 250 and len(foodRedeem)== 0:
        foodRedeem.append("Cranberry Energy Bites")
        pointRedeem.append(int("250"))
        redeem = messagebox.askyesno("Redeem","Are you sure to redeem \n{} ({} points)?".format(foodRedeem[0], pointRedeem[0]))
        if redeem > 0:
          messagebox.showinfo("Success","{} ({} points) \nis redeemed.".format(foodRedeem[0], pointRedeem[0]))
          rp-= 250
        else:
          foodRedeem.pop(0)
          pointRedeem.pop(0)
          messagebox.showerror("Fail to redeem","Come to redeem next time.")
          return
      elif len(foodRedeem) > 0:
        messagebox.showerror("Sorry","Can only redeem one food per time.")
      else:
        messagebox.showerror("Sorry","Not enough point.")

    def selectRedeem3(self):
      global rp
      if "ok" not in test :
        rp = point
        test.append("ok")
        
      if rp >= 380 and len(foodRedeem)== 0:
        foodRedeem.append("Muesli With Raspberries")
        pointRedeem.append(int("380"))
        redeem = messagebox.askyesno("Redeem","Are you sure to redeem \n{} ({} points)?".format(foodRedeem[0], pointRedeem[0]))
        if redeem > 0:
          messagebox.showinfo("Success","{} ({} points) \nis redeemed.".format(foodRedeem[0], pointRedeem[0]))
          rp -= 380
        else:
          foodRedeem.pop(0)
          pointRedeem.pop(0)
          messagebox.showerror("Fail to redeem","Come to redeem next time.")
          return
      elif len(foodRedeem) > 0:
        messagebox.showerror("Sorry","Can only redeem one food per time.")
      else:
        messagebox.showerror("Sorry","Not enough point.")
        
    def back_cs(self):
        self.destroy()
        CartSummary(None).title('Cart Summary')


if __name__ == "__main__":
    root = main_screen()

