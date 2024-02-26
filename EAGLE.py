from selenium import webdriver;
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select 

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk

from selenium.webdriver.common.action_chains import ActionChains
import pygame




JANUARY = []
FEBRUARY = [
            "26-Feb-2024",
            "27-Feb-2024",
            "28-Feb-2024",
            ]
MARCH = [
      
      "05-Mar-2024",
      "06-Mar-2024",
      "07-Mar-2024",
      "12-Mar-2024",
      "13-Mar-2024",
      "14-Mar-2024",
      "19-Mar-2024",
      "20-Mar-2024",
      "21-Mar-2024",
      "27-Mar-2024",
      "28-Mar-2024"      
      
     ]

APRIL = [
      
      "02-Apr-2024",
      "03-Apr-2024",
      "04-Apr-2024",
      "11-Apr-2024",
      "16-Apr-2024",
      "17-Apr-2024",
      "18-Apr-2024",
      "23-Apr-2024",
      "24-Apr-2024",
      "25-Apr-2024",
      "30-Apr-2024"
      ]

MAY = ["02-May-2024",
       "07-May-2024",
       "09-May-2024",
       "14-May-2024",
       "15-May-2024",
       "16-May-2024",
       "21-May-2024",
       "22-May-2024",
       "28-May-2024",
       "29-May-2024",
       "30-May-2024"
       
       ]

JUNE = ["04-Jun-2024",
        "05-Jun-2024",
        "06-Jun-2024",
        "11-Jun-2024",
        "12-Jun-2024",
        "13-Jun-2024",
        "18-Jun-2024",
        "19-Jun-2024",
        "20-Jun-2024",
        "25-Jun-2024",
        "26-Jun-2024",
        "27-Jun-2024"
        ]

JULY = ["02-Jul-2024",
        "04-Jul-2024",
        "09-Jul-2024",
        "11-Jul-2024",
        "16-Jul-2024",
        "18-Jul-2024",
        "23-Jul-2024",
        "25-Jul-2024",
        "30-Jul-2024",
        ]

AUGUST = ["01-Aug-2024",
          "06-Aug-2024",
          "08-Aug-2024",
          "13-Aug-2024",
          "20-Aug-2024",
          "22-Aug-2024",
          "27-Aug-2024",
          "29-Aug-2024",
          ]

SEPTEMBER = []
OCTOBER = []
NOVEMBER = []
DECEMBER = []


pygame.init()
sound = pygame.mixer.Sound('eagle.mp3')
errorSound = pygame.mixer.Sound('error.mp3')
exception = pygame.mixer.Sound('exception.mp3')

URL = "http://reciprocal.wbhealth.gov.in/Login.aspx"
SCHEDULE_URL = "http://reciprocal.wbhealth.gov.in/ScheduleDateForUser.aspx"
I=10



driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.maximize_window()
driver.get(URL)
Num = driver.find_element(By.ID,'txtUser')
Pass = driver.find_element(By.ID,'txtPassword')

#GUI WORK
def send_user_data():
    global CAP
    global user
    global password
    user = ID.get()
    password = PASSWORD.get()
    CAP = captcha_entry.get()

    if (CAP and user and password and (value_inside.get())):
        pass
    elif not(10==len(user)):
        messagebox.showwarning("Warning","Please enter 10 digit phone number!")
    else:
        print("Please enter the User id, Password, Captcha and choose the month")
        messagebox.showwarning('Warning','Please fill up all the fields carefully!!')




    
    #vvv=value_inside.get()
    #print("printing list Value",vvv,"\n Type is :- ", type(vvv))
    #list_value=list1.get()
    #print("The list value is :- ",list_value)
    
    #print(user,password,CAP)
    window.destroy()



window = ctk.CTk()
window.title("User Input Window")
window.configure(bg="#A6E3E9")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

ScreenWidth = window.winfo_screenwidth()
ScreenHeight = window.winfo_screenheight()

WinWidth= int(ScreenWidth/2)
WinHeight= int(ScreenHeight/2)

#find the center position
CenterX = int((ScreenWidth - WinWidth)/2)
CenterY = int((ScreenHeight - WinHeight)/5)
window.geometry(f"{WinWidth}x{WinHeight}+{CenterX+400}+{CenterY-70}")

label1=ctk.CTkLabel(master=window,text="ENTER THE USER_ID")
label1.place(x=100,y=30)
ID=ctk.CTkEntry(master=window,width=200)
ID.place(x=100,y=55)
ID.focus_set()

label2=ctk.CTkLabel(master=window,text="ENTER THE PASSWORD")
label2.place(x=100,y=100)
PASSWORD=ctk.CTkEntry(master=window,width=200)
PASSWORD.place(x=100,y=125)
PASSWORD.focus_set()


#  CHOOSE MONTH FROM THE LIST
value_inside = StringVar()
month_list = ["JANUARY" ,"FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
value_inside.set("Select an Option")

label4=ctk.CTkLabel(master=window,text="Choose The Month")
label4.place(x=400,y=150)
list1=OptionMenu(window,value_inside, *month_list)
list1.place(x=400,y=175)
#list_value=list1.get()


label3=ctk.CTkLabel(master=window,text="ENTER THE CAPTCHA HERE")
label3.place(x=100,y=190)
captcha_entry=ctk.CTkEntry(master=window,width=100)
captcha_entry.place(x=100,y=215)
captcha_entry.focus_set()

b1=ctk.CTkButton(master=window,text="Submit Captcha",command = send_user_data,width = 500,height=100)
b1.place(x=100,y=270)

window.mainloop()




Num.send_keys(user)
Pass.send_keys(password)


driver.find_element(By.ID,'txtcaptcha').send_keys(CAP)#inserting the captcha 
#time.sleep(3)
driver.find_element(By.ID,'btnLogin').click()
driver.find_element(By.LINK_TEXT,"Home").click()
driver.find_element(By.LINK_TEXT,"Schedule Date").click()
candidate_name = driver.find_element(By.XPATH,"//*[@id='afteropeningbaldoneDiv2']/nav/div/ul/li[6]/a").text

#month = MONTY

# IT IS ALSO WORKING //// CHOOSING MONTH BY USING LIST 
def assign_value(x):
    MM = []
    if (x == "JANUARY"):
        for i in JANUARY:
            MM.append(i)
            
    elif (x == "FEBRUARY"):
        for i in FEBRUARY:
            MM.append(i)
            
    elif (x == "MARCH"):
        for i in MARCH:
            MM.append(i)

    elif (x == "APRIL"):
        for i in APRIL:
            MM.append(i)

    elif (x == "MAY"):
        for i in MAY:
            MM.append(i)

    elif (x == "JUNE"):
        for i in JUNE:
            MM.append(i)

    elif (x == "JULY"):
        for i in JULY:
            MM.append(i)

    elif (x == "AUGUST"):
        for i in AUGUST:
            MM.append(i)

    elif (x == "SEPTEMBER"):
        for i in SEPTEMBER:
            MM.append(i)

    elif (x == "OCTOBER"):
        for i in OCTOBER:
            MM.append(i)

    elif (x == "NOVEMBER"):
        for i in NOVEMBER:
            MM.append(i)

    elif (x == "DECEMBER"):
        for i in DECEMBER:
            MM.append(i)

    

    
    return MM
    
month = assign_value(value_inside.get())

print("Rigth Before of LOOP, The month value is :- ",month)
#measure the length of the date list
date_len = len(month)
#select value from dropdown
i=0
loop_condition = True
while ( loop_condition ):

    if(i == date_len):
        #print('PEAK')
        for i in range (1,date_len+1):
            # <<<<<<<<<<<<<  main contain  >>>>>>>>>>>
            #print("BACKWARD LOOP ",end='')
            time.sleep(0.4)
            try :
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlDate")))
                #BACKWARD LOOP
                driver.find_element(By.XPATH,f"//select/option[text()='{month[(-1)*i]}']").click()
                ScanSlot = int(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblAlreadySched").text)
                print('{',month[(-1)*i],'}',"Already Booked Slots :-",ScanSlot)
                if(ScanSlot < 120):
                    sound.play()
                    
                    driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_btnSave').click()
                    print(f"\n \n \n \n \n \n {candidate_name} \nA SLOT HAS BEEN BOOKED FOR YOU ON {month[(-1)*i]}")
                    print("##########PROGRAM STOPPED########## \n Please Restart it again!!!!!!!")

                    loop_condition = False
                    #time.sleep(120)
                    #alert = driver.switch_to.alert

                    #sleep for a second
                    #time.sleep(0.3)

                    #accept the alert
                    #alert.accept()
                    
                    break
                
                #print("Working Normally")
            except:
                print(" Some Error Occured when Searching for Schedule Date \n")
                #print("Exception_Sound in Backward loop")
                exception.play()
                driver.get(SCHEDULE_URL)
                #loop_condition = False
                #break
            
        #print("Finished Backward Loop")
        i=0
    # Forward Loop
    #print("FORRWARD LOOP ",end='')
    time.sleep(0.4)
    try :
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlDate")))
        #FORWARD LOOP
        driver.find_element(By.XPATH,f"//select/option[text()='{month[i]}']").click()
        #i=i+1
        
        '''target_element = driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblAlreadySched")

        sss = ActionChains(driver).double_click(target_element).perform()'''

        ScanSlot = int(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblAlreadySched").text)
        print('{',month[i],'}',"Already Booked Slots :-",ScanSlot)
        #i=i+1
        
        if(ScanSlot < 120):
            sound.play()
            
            driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_btnSave').click()
            print(f"\n \n \n \n \n \n {candidate_name} \nA SLOT HAS BEEN BOOKED FOR YOU ON {month[i]}")
            print("##########PROGRAM STOPPED########## \n Please Restart it again!!!!!!!")
            loop_condition = False
            #time.sleep(120)
            #alert = driver.switch_to.alert

            #sleep for a second
            #time.sleep(0.3)

            #accept the alert
            #alert.accept()
            #break
        i=i+1
        #print("Working Normally")
    except:
        if(loop_condition != False):
            print(" Some Error Occured when Searching for Schedule Date \n")
            #print("Exception_Sound in forward loop")
            exception.play()
            driver.get(SCHEDULE_URL)
            #loop_condition = False
            
    
    


#driver.send_keys(Keys.ALT + Keys.ARROW_LEFT)
#driver.back()
errorSound.play()
#print("\n \n \n \n \n \n Waiting at the Last")
time.sleep(120)

driver.quit()
