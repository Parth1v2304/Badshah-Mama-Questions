def find_exclusive_elements(A, B):
    set_A = set(A)
    set_B = set(B)
    exclusive_A = set_A - set_B  
    exclusive_B = set_B - set_A  
    result = list(exclusive_A) + list(exclusive_B)
    
    return result

A = [1, 2, 3, 4]
B = [1, 4, 7, 10]
print(find_exclusive_elements(A, B))
