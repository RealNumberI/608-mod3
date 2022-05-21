# File 1 - bult-in-min-max.py (Sections 4.1, 4.2, 4.3)
def maximum(value1, value2, value3):  
    """Return the maximum of three values."""  
    max_value = value1  
    if value2 > max_value:
        max_value = value2  
    if value3 > max_value:  
        max_value = value3  
    return max_value  

maximum(12, 27, 36) 

maximum(12, 27, 36)==max(12,27,36)

maximum(12.3,45.6, 9.7)

maximum('yellow', 'red', 'orange')

def minimum(value1, value2, value3, value4):  
    """Return the minimum of three values."""  
    min_value = value1  
    if value2 < min_value:
        min_value = value2  
    if value3 < min_value:  
        min_value = value3  
    return min_value  
