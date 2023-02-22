#!/usr/bin/env python
# coding: utf-8

# In[5]:


def listDivide(numbers,divide = 2):
    #varibale that count the number divisible by divide in the list  
    count  = 0
    
    #condition check for empty list 
    if(len(numbers) == 0):
        return 0
    
    #loop around the element of list
    for i in numbers:
        try:
            #check for divisibility
            if(i%divide == 0):
                #increment the counter
                count += 1 
        
        #3. Create acustom exception class called 'ListDivideException'. This should be two lines of Python code.
        except:
            return 'Error: ListDivideException'
    
    #2. The function returns the number of elements in the numbers list that are divisible by divide.
    return count
    
#4. create another function called testListDivide that performs the following tests on listDivide:
def testListDivide():
    #listDivide([1,2,3,4,5]) should return 2
    print(listDivide([1,2,3,4,5]))
    
    #listDivide([2,4,6,8,10]) should return 5
    print(listDivide([2,4,6,8,10]))
    
    #listDivide([30, 54, 63,98, 100], divide=10) should return 2
    print(listDivide([30, 54, 63,98, 100], divide=10))
    
    #listDivide([]) should return 0
    print(listDivide([]))
    
    #listDivide([1,2,3,4,5], 1) should return 5
    print(listDivide([1,2,3,4,5], 1) )
    

testListDivide()


# In[4]:


# Class declaration
class Book:
	# Variables declaration
	author = ''
	title = ''
	
	# Constructer method with variables
	def __init__(self, author, title):
		self.author = author
		self.title = title
	
	# Method to display book infomation
	def display(self):
		print(self.title+", written by "+self.author)

# Creating two objects of Book class
obj1 = Book('John Steinbeck', 'Of Mice and Men')
obj2 = Book('Harper Lee', 'To Kill a Mockingbird')

# Calling method of Book class to display book details
obj1.display()
print()
obj2.display()


# In[ ]:




