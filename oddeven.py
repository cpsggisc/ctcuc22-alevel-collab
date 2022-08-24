# Write a Boolean function is_odd(num) to return True if a positive integer num is odd 
# and even if num is even

def is_odd(num):
    ''' Boolean function to return True if odd and False if even
    '''
    if num % 2 == 1:
        return True
    else: # even
        return False

    # Alternate one-liner:
    # return num % 2 == 1

# main
print(is_odd(1))
print(is_odd(888))
    
# Previously:
# Write a function to determine if a positive integer is odd or even

def oddeven(number):
    return "even" if num % 2 == 0 else "odd" 
# test
