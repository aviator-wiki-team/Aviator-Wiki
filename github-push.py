from os import system
from time import strftime

username=input("Username:")
date=strftime("%Y-%m-%d")
msg=input("msg:")
system("git add .")
system("git commit -m \""+username+":"+date+"-"+msg+"\"")
system("git push")