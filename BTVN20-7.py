#!/usr/bin/env python
# coding: utf-8

# In[1]:


xA=int(input('Nhập Tọa độ x của điểm A= '))
yA=int(input('Nhập Tọa độ y của điểm A= '))
xB=int(input('Nhập Tọa độ x của điểm B= '))
yB=int(input('Nhập Tọa độ y của điểm B= '))
xC=int(input('Nhập Tọa độ x của điểm C= '))
yC=int(input('Nhập Tọa độ y của điểm C= '))
xD=int(input('Nhập Tọa độ x của điểm D= '))
yD=int(input('Nhập Tọa độ x của điểm D= '))

import math 
AB=math.sqrt((xB-xA)**2+(yB-yA)**2)
BC=math.sqrt((xC-xB)**2+(yC-yB)**2)
CD=math.sqrt((xD-xC)**2+(yD-yC)**2)
DA=math.sqrt((xA-xD)**2+(yA-yD)**2)
AC=math.sqrt((xC-xA)**2+(yC-yA)**2)
BD=math.sqrt((xD-xB)**2+(yD-yB)**2)

cosA=(AB**2+DA**2-BD**2)/(2*AB*DA)
cosB=(AB**2+BC**2-AC**2)/(2*AB*BC)
cosC=(BC**2+CD**2-BD**2)/(2*BC*CD)
cosD=(DA**2+CD**2-AC**2)/(2*DA*CD)

gA = math.degrees(math.acos(cosA))
gB = math.degrees(math.acos(cosB))
gC = math.degrees(math.acos(cosC))
gD = math.degrees(math.acos(cosD))

tugiaclom= (gA > 180) or (gB > 180) or (gC > 180) or (gD > 180)
print('Tứ giác lõm: ', tugiaclom)

color=input('Màu: ')
import turtle 
t=turtle.Turtle()
t.shape()
t.pensize(4)
t.hideturtle()
t.pencolor(color)
t.penup()
t.goto(xA,yA)
t.pendown()
t.goto(xB,yB)
t.goto(xC,yC)
t.goto(xD,yD)
t.goto(xA,yA)

turtle.done()


# In[ ]:




