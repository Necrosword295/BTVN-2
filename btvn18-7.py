#!/usr/bin/env python
# coding: utf-8

# In[1]:


luong = 70000000
giamtrugiacanh = 11000000
giamtrunguoiphuth = 4400000 
songuoigiamtru = 4 

thunhaptinhthue = luong - giamtrugiacanh - giamtrunguoiphuth * songuoigiamtru

print ("Thu nhập thuế của 1 người là:", thunhaptinhthue,)


# In[2]:


x1 = 45
y1 = 29
z1 = 5

x2 = 80
y2 = 60
z2 = 8
 
x3 = 50
y3 = 60
z3 = 29

Vx21 = x2 - x1 
Vy21= y2 - y1

x4 = Vx21 + x3
y4 = Vy21 + y3

print ("tọa độ điểm thứ 4 của hình bình hành là ","(",x4,";",y4,")")

import turtle 
t = turtle.Turtle()
t.hideturtle()


t.color("green")
t.penup()
t.goto(x1, y1)
t.pendown()

t.goto(x3, y3)
t.fillcolor("green")
t.begin_fill()
t.circle(3)
t.end_fill()

t.goto(x2, y2)
t.fillcolor("green")
t.begin_fill()
t.circle(3)
t.end_fill()

t.goto(x3, y3)
t.goto(x4, y4)
t.goto(x2, y2)
t.goto(x1, y1)
t.fillcolor("green")
t.begin_fill()
t.circle(3)
t.end_fill()


t.color("blue")
t.goto(x1, y1)
t.goto(x4, y4)

t.fillcolor("blue")
t.begin_fill()
t.circle(3)
t.end_fill()

turtle.done()


# In[ ]:





# In[ ]:




