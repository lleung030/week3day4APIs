counter = 0
cache_dict = {}

def fib(n):
    global counter
    counter +=1
    
    if n in cache_dict:
        return cache_dict[n]
    
    result = None
    if n<=1:
        result = n
        
    else:
        result = fib(n-1) + fib(n-2)
        
    cache_dict[n] = result
    return result

fib(30)