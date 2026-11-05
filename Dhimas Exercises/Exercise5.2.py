# Tests for equality and inequality with strings
name = 'python'

print(name == 'python')  
print(name != 'java')    
print(name == 'java')     

# Tests using the lower() method
language = 'PYTHON'

print(language.lower() == 'python')  
print(language.lower() == 'java')    

# Numerical tests
number = 20

print(number == 20)  
print(number != 20)  

print(number > 10)   
print(number < 10)   

print(number >= 20)  
print(number <= 10)  

# Tests using and keyword
age = 20

print(age >= 18 and age <= 25) 
print(age > 25 and age < 30)    

# Tests using or keyword
print(age < 18 or age == 20)   
print(age < 18 or age > 25)     

# Test whether an item is in a list
foods = ['rice', 'chicken', 'pizza']

print('rice' in foods)    
print('burger' in foods)  

# Test whether an item is not in a list
print('burger' not in foods)  
print('pizza' not in foods)   