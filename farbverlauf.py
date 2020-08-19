#!/usr/bin/python

import os
import time

def aktuelle_h():
    return int(time.strftime("%H"))

def aktuelle_m():
    return int(time.strftime("%M"))

def int2hex(i):
    return "{:02x}".format(i)

def hex2int(h):
    return int(h,16)

def interpolate_1colorchanel(start, ziel, amount):
    result = amount * hex2int(ziel) + (1-amount) * hex2int(start)
    return int2hex(min(255, int(result)))

def interpolate_color(start, ziel, amount):
    return interpolate_1colorchanel(start[0:2], ziel[0:2], amount) + \
           interpolate_1colorchanel(start[2:4], ziel[2:4], amount) + \
           interpolate_1colorchanel(start[4:6], ziel[4:6], amount) 

def hour2color(h):
    colors = ["87ff00", "3232ff", "9933ff", "ff4455", "ffaa55", "ffff00"]
    return (4*colors)[h%24]

def time2color(h, m):
    return interpolate_color(hour2color(h), hour2color(h+1), m/60.0)

def divForEachHour():
    return "\n    ".join(['<div style="width:60px; height:23px; background-color:#' + time2color(h,0) + '"></div>'
                     for h in range(24)])

def divForEachMinute():
    return "\n    ".join(['<div style="width:60px; height:10px; background-color:#' + time2color(aktuelle_h(), m) + '"></div>'
                     for m in range(60)])

def writeHtml():
     aktuelle_farbe = time2color(aktuelle_h(),aktuelle_m())
     content="""
     <html>
      <body style="background-color: #""" + aktuelle_farbe + """">
       """ + divForEachHour() + divForEachMinute() + """
      </body>
     </html>
     """
     fd = os.open("index.html", os.O_WRONLY|os.O_CREAT|os.O_TRUNC)
     os.write(fd, content)

writeHtml()
