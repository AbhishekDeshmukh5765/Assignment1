#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1.What are the two values of the Boolean data type? How do you write them?
# ans-true and flase 
# we write them as True and Flase


# In[ ]:


# 2.What are the three different types of Boolean operators?
# and,or,not


# In[2]:


# 3. Make a list of each Boolean operator truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).
# True and True is True.

"""
True and False is False.

False and True is False.

False and False is False.

True or True is True.

True or False is True.

False or True is True.

False or False is False.

not True is False.

not False is True.
"""


# In[5]:


# What are the values of the following expressions?
(5 > 4) and (3 == 5)


# In[6]:


not (5 > 4)


# In[7]:


(5> 4) or (3 == 5)


# In[8]:


not ((5> 4) or (3 == 5))


# In[9]:


(True and True) and (True == False)


# In[10]:


(not False) or (not True)


# In[ ]:


# 5. What are the six comparison operators?
# ans ==, !=, <, >, <=, and >=.


# In[ ]:


# 6. How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.
# ans == is the equal to operator that compares two values and evaluates to a Boolean,
# while = is the assignment operator that stores a value in a variable.


# In[12]:


#7. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print("egg")
if spam > 5:
    print("bacon")
else:
    print("ham")
    print("spam")
    print("spam")
"""
The three blocks are everything inside the if statement and the lines print('bacon') and print('ham').

"""


# In[ ]:


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
 # Greetings! if anything else is stored in spam.


# In[13]:


if spam==1:
    print("hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings")


# In[ ]:


# 9.If your programme is stuck in an endless loop, what keys you’ll press?
# ctrl+c


# In[ ]:


# 10.How can you tell the difference between break and continue?
# ans- The break statement will move the execution outside and just after a loop.
# The continue statement will move the execution to the start of the loop.


# In[ ]:


# 11.In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# they all do same thing


# In[15]:


# 12.Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.
list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print(i)


# In[17]:


for i in range(1, 11):
    print(i)


# In[ ]:


# 13. If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?
# ans-spam.bacon()


# In[ ]:




