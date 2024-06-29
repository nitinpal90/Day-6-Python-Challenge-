#!/usr/bin/env python
# coding: utf-8

# # Day-6 Python Challenge

# # User Define Function

# # Creating User Define Function

# In[6]:


def python():
    print("Python is Easy")
    print("Python is Cool")


# # Calling a Function

# In[7]:


python() ##Use multiple Time User Define Function


# # Making a Result of a Students

# In[8]:


def my_contact():
    print("Ravi Kumar")
    print("Manav Rachna University")
    print("9219094749")
    print("mr.net@mr.in")
    print("Faridabad Haryana")


# In[ ]:


for i in range(5):
    a = input("Enter Your Name: ")
    b = int(input("Enter Your Marks in maths: "))
    c = int(input("Enter Your Marks in Science: "))
    d = int(input("Enter Your Marks in Java: "))
    e = int(input("Enter Your marks in Python: "))
    print()
    my_contact()


# In[ ]:


## Write a programe to calculate the electricity bill

if 500 unit used - Pay 5 rs for each unit
if 700 unit used - Pay 10 rs for each unit
if 1000 unit used - Pay 15 rs for each unit
if more than 1000 unit used - Pay 20 rs for each unit


# In[ ]:


def electricity_bill(n):
    if n<=500:
        print("Your Total Amount of Bill", n*5)
    elif n>500 and n<=700:
        print("Your Total Amount of Bill", n*10)
    elif n>700 and n<=1000:
        print("Your Total Amount of Bill", n*15)
    elif n>1000:
        print("Your Total Amount of Bill", n*20)    


# In[ ]:


for i in range(3):
    a = input("Enter Your Name: ")
    b = int(input("Enter the Unit of Bill You Have Used: "))
    electricity_bill(n):

