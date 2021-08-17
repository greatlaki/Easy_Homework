def loop(n, k):
    
    if n > 20:
        return 0
    
    sum_i = 0
    
    for i in range(1, n):
        if i % 2 == 0:
            sum_i += i ** k
            
    return sum_i

            
print(loop(5, 2))
            
