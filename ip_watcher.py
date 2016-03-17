# -*- coding: utf-8 -*-
"""
This application displays the External IP of the given machine by parsing the 
html file returned when a request it made to an url that constains
my ip information.
@author: bmahm
"""
import requests
import time
import Tkinter
import threading
import winsound


### These are the global variables that I created to make my GUI run parallel
global top 
global ip 
global ip_label



def get_IP():
    """
    This function returns external IP and if that is not possible it 
    returns 0
    """
    
    try:
        ## requests the get the ip; the site is really simple 
        f = requests.request('GET', 'http://myip.dnsomatic.com')
        ip = f.text
        return ip
        
    except:
        
        ## can't get IP from the website
        return "0"


## Initializing the global widgets
top = Tkinter.Tk()
top.resizable(width = False, height = False)
ip = Tkinter.StringVar(top)
top.config(bg = "black")
ip_label = Tkinter.Label(top,textvariable = ip)
ip_label.config(font=("Consolas", 48,"bold italic"), bg = "black", fg = "red")
ip_label.pack()
         

## This is a simple class that would run on different thread
class GUI(threading.Thread):
    def run(self):
         top.mainloop()
   

## starting gui thread
m = GUI()
m.start()

## Loop running dsiplaying the switch between IPs and whether there is internet
## or not!
starting_ip = ""
while(1):
    ip_value = get_IP() 
    
    ## There is not internet
    if ip_value == "0":
        ip.set("Waiting for internet!") 
        ip_label.config(fg = "red")
        winsound.PlaySound("Sounds/warn.wav", winsound.SND_FILENAME)     
        time.sleep(5)
        
    ## IP is unchanged from the previous value
    elif ip_value == starting_ip:    
        ip.set("My IP: " + ip_value) 
        ip_label.config(fg = "green")
        time.sleep(5)
        
    ## IP has changed
    else:
        
        ip.set("My IP: " + ip_value) 
        starting_ip = ip_value
        ip_label.config(fg = "orange")
        winsound.PlaySound("Sounds/change.wav", winsound.SND_FILENAME)  
        time.sleep(5)
        

    


    
       
        
        
