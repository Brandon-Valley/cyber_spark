import math


def group_into_bytes(num_str, digits_per_byte):
    rev_num_str = rev_str(num_str)
    bytes_list = []
    byte_str = ''
    
    for digit in rev_num_str:
        byte_str += digit
        
        if len(byte_str) == digits_per_byte:
            bytes_list.insert(0, byte_str)
            byte_str = ''
    
    #if last (first) byte ends up not being the perfect length, fill with 0's until it is
    while(len(byte_str) != digits_per_byte):
        byte_str.insert(0, '0')
        
    return bytes_list

string1 = '104101108108111032119111114108127'

print(group_into_bytes(string1, 3))   
            
            

                  
            
