def karatsuba(a, b):
    size_a = len(str(a))
    size_b = len(str(b))
    
    if size_a == 1 or size_b == 1:
       return a * b
    else:
        size_max = max(size_a, size_b)
        size_max_piso = size_max // 2
        
        a_left = a // 10**(size_max_piso) 
        a_right = a % 10**(size_max_piso) 
        b_left = b // 10**(size_max_piso) 
        b_right = b % 10**(size_max_piso)  
            
        x1 = karatsuba(a_left, b_left)
        x2 = karatsuba((a_left + a_right), (b_left + b_right))
        x3 = karatsuba(a_right, b_right) 
        
        return (x1 * 10**(2*size_max_piso)) + ((x2 - x1 - x3) * 10**(size_max_piso)) + (x3)
    
def third_grade(a, b):
    size_a = len(str(a))
    size_b = len(str(b))
    
    if size_a == 1 or size_b == 1:
        return a * b
    else:
        size_max = max(size_a, size_b)
        size_max_piso = size_max // 2

        a_left = a // 10**(size_max_piso) 
        a_right = a % 10**(size_max_piso) 
        b_left = b // 10**(size_max_piso) 
        b_right = b % 10**(size_max_piso)  
        
        x1 = third_grade(a_left, b_left)
        x2 = third_grade(a_left, b_right)
        x3 = third_grade(a_right, b_left)
        x4 = third_grade(a_right, b_right)
        
        return (x1 * 10**(2*size_max_piso)) + ((x2 + x3) * 10**(size_max_piso)) + (x4)
        