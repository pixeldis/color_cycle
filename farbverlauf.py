#!/usr/bin/python

import os
import time

def aktuelle_h():
    return int(time.strftime("%H"))

def time2color(h, min):
    colors = ["yellow", "orange", "red", "purple", "blue", "green"]
    return (4*colors)[h]

    r = "99"
    g = "44"
    b = "44"
    return "#" + r + g + b

def divForEachHour():
    return " ".join(['<div style="width:30px; height:23px; background-color:' + time2color(h,0) + '"></div>'
                     for h in range(24)])

def writeHtml():
     aktuelle_farbe = time2color(aktuelle_h(),0)
     content="""
     <html>
      <body style="background-color: """ + aktuelle_farbe + """">
       """ + divForEachHour() + """
      </body>
     </html>
     """
     fd = os.open("index.html", os.O_WRONLY|os.O_CREAT|os.O_TRUNC)
     os.write(fd, content)

writeHtml()
