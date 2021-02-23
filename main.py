import pyshorteners
import pyperclip

#
# def shortLink(link):
#     short = pyshorteners.Shortener()
#     short_link = short.tinyurl.short(link)
#     return short_link
#
# url = input("Enter URL: ")
#
# finalResult = get_value(url)
#
# print(f"The link is: {finalResult}")

# import the module and all specifications
from tkinter import *

# create the window and set geometry and title
root=Tk()
root.geometry("500x500")
root.title("URL Shorter")

# creating the commanding
# function of the button
def get_value():
    link =Text_Area.get()


    short = pyshorteners.Shortener()
    short_link = short.tinyurl.short(link)
    pyperclip.copy(f'{short_link}')

    root2=Tk()
    root2.geometry("500x500")
    root2.title("ShortendLink")
    # setting the Label in the window
    label2=Label(root2,text=f"The link has been copid to clipboard, THE LINK IS: {short_link}")

    label2.place(x=160, y=80)
    root2.mainloop()

# set the string variable
Text_Area=StringVar()

# create a label
label=Label(root,text="Enter Your Name")

# placing the label at the right position
label.place(x=190,y=80)

# creating the text area
# we will set the text variable in this
Input=Entry(root,textvariable=Text_Area,width=30)
Input.place(x=130,y=100)

# create a button
button=Button(root,text="Submit",command=get_value,bg="green")
button.place(x=180,y=130)
root.mainloop()
