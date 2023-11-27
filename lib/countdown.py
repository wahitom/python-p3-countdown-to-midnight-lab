# your code goes here!
# f tells python that a string is going to be formatted with variable values 
# they use interpolation with curly braces {}

# The add and assign(+=) is used to increment a value much like ++ in js

def countdown(num):
    x = 10
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
    
    if(x == 0):
        print("HAPPY NEW YEAR!")

countdown(10)
              