#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
t=turtle.Turtle()
t.shape('turtle')
t.hideturtle()

t.fillcolor('black')
t.begin_fill()

t.forward(250)
t.left(90)
t.forward(50)
t.left(90)
t.forward(250)
t.left(90)
t.forward(50)
t.pendown()
t.end_fill()

t.fillcolor('red')
t.begin_fill()
t.left(90)
t.forward(250)
t.right(90)
t.forward(50)
t.right(90)
t.forward(250)
t.left(90)
t.pendown()
t.end_fill()

t.fillcolor('yellow')
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(250)
t.left(90)
t.forward(50)
t.pendown()
t.end_fill()


turtle.done()

