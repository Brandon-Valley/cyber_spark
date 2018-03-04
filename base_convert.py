from test.test_bigmem import ascii_char_size
import math

    #2301 base 5 = 326
def convert_to_base_10(num_str, base):
    digits_per_byte = get_num_digits_per_byte(base)
    
#     num_str = format_data(num_str_list)#```````````````````````````````````````````````````````````
    rev_num_str = rev_str(num_str)
    
    og_bytes_list = group_into_bytes(num_str, digits_per_byte)
    print(og_bytes_list)
    
    new_bytes_list = []
    
    for og_byte in og_bytes_list:
        new_byte = convert_byte(og_byte, base)
        new_bytes_list.append(new_byte)#.insert(0, new_byte)
        
    return new_bytes_list
        


def convert_byte(old_byte, base):
    rev_old_byte = rev_str(old_byte)
    new_byte_int = 0
    
    for digit_pos in range( len(rev_old_byte) ):
        digit_char = rev_old_byte[digit_pos]
        digit_int = int( digit_char )
        
    #         print('digit_pos: %s   digit_int: %s' %(digit_pos , digit_int))
        decimal_equiv = digit_int * base**digit_pos
#         print('base %s,  og digit: %s decimal_equiv:  %s' %(base, digit_char, decimal_equiv ))
        new_byte_int += decimal_equiv
        
    return str(new_byte_int)

def group_into_bytes(num_str, digits_per_byte):
    rev_num_str = rev_str(num_str)
    bytes_list = []
    byte_str = ''
    
    for digit in rev_num_str:
        byte_str = digit + byte_str
        
        if len(byte_str) == digits_per_byte:
            bytes_list.insert(0, byte_str)
            byte_str = ''
    
    #if last (first) byte ends up not being the perfect length, fill with 0's until it is
    if byte_str != '':
        while(len(byte_str) != digits_per_byte):
#             print('%s isnt long enough, adding 0s' %(byte_str))#``````````````````````````````````````````
            byte_str = '0' + byte_str
#             print('  byte_str: ', byte_str)#`````````````````````````````````````````````````````````````````````````
        bytes_list.insert(0, byte_str)
        
    return bytes_list
    
    

def get_num_digits_per_byte(base):
    log2 = math.log(256, base)
    log2 = math.log2(256)
    return int(log2)

def rev_str(og_str):
    new_str = ''
    for rev_pos in range( len(og_str) ):
        new_str += og_str[ len(og_str) - 1 - rev_pos]
        
    return new_str

def read_text_file(file_path):
    with open(file_path) as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result
    
def format_data(data):
#     print('in format_data')
    formatted_data = ''
    
#     print( len(data) )#````````````````````````````````````````````````````````````````````````````````````````
    
    try:
        for data_line_num in range( len(data) ):
#             formatted_data += ' '#```````````````````````````````````````````````````````````````````````````````````````
#             print(data_line_num)#````````````````````````````````````````````````````````````````````````````
#             print('trying to add: %s/////////' %(data[data_line_num]) )#````````````````````````````````````````````````````````````
            
            
#             if ' ' in data_line:
#                 print('stop')
#                 while(True):
#                     print('terminate window!!!')
#                     pass
                
            formatted_data += data[data_line_num]
#             print(formatted_data)#``````````````````````````````````````````````````````````````````````````````````````````````
#             if data_line[0] == ' ' or formatted_data == '':
#                 formatted_data += data_line
#             else:
#                 formatted_data += ' ' + data_line\
#             print ('still running')#```````````````````````````````````````````````````````````````````````````````````````
        return formatted_data
    except:
        raise Exception('ERROR  You probably have some extra lines of spaces in your data text file')
    
    
#just for testing
def write_text_file(file_path, line_list):
    f = open(file_path, 'w')
    # write to file
    try:
        for line in line_list:
            f.write(line + '\n')
    except:#if only need to write one line
        f.write(str(line_list) + '\n')
    # cleanup
    f.close()
    
    
# def string_to_list(long_str, chars_per_line):
#     str_list = []
#     line_str = ''
#     
#     for char in long_str:
#         line_str += char
#                 
#         if len(line_str) == chars_per_line:
#             str_list.append(line_str)
#             line_str = ''
#     
#     if len(line_str) != 0:
#         str_list.append(line_str)
#         
#     return str_list


def decimal_bytes_to_ascii_chars(dec_bytes_list):
    ascii_char_list = []
    
    for dec_byte in dec_bytes_list:
        int_dec_byte = int( dec_byte )
        ascii_char = chr( int(dec_byte) )
        ascii_char_list.append(ascii_char)
    
    return ascii_char_list
        

def list_to_str(list):
    output_str = ''
    
    for char in list:
        output_str += char
        
    return output_str
        
        
def print_ascii_str(ascii_str):
    output_list = []
    final_str = ''
    
    for char in ascii_str:
        final_str += char

    print('')
    print('ASCII STRING:')
    print(final_str)
    
    return output_list
        
    
    
    
    

    
# def long_int_to_ascii_str(long_int):
#     long_int_str = str(long_int)
#     long_int_str_list = string_to_list(long_int_str, 3)
#     
#     ascii_str = ''
#     
#     for dec_char_digits in long_int_str_list:
#         int_digits = int(dec_char_digits)
#         print(int_digits)
#         ascii_char = chr(int_digits)
#         encoded_ascii_char = ascii_char.encode("utf-8")
#         print('   ', encoded_ascii_char)
#         print(type(bytes_to_int(encoded_ascii_char)))#`````````````````````````````````````````````````````````````````````````````````````
#         ascii_str += str( encoded_ascii_char )
#         
#     return ascii_str#.encode("utf-8")
# 
# 
# def bytes_to_int(bytes):
#     result = 0
# 
#     for b in bytes:
#         result = result * 256 + int(b)
# 
#     return result
  
  
  
        
INPUT_FILENAME =  'input.txt'
OUTPUT_FILENAME = 'output.txt'
NUM_DIGITS_PER_OUTPUT_LINE = 10

base = 2

# test_str = '0111101111011000100000100'
# 
# test_group_bytes = group_into_bytes(test_str, 8)
# test_byte = convert_byte(test_group

    



 
input_num_str_list = read_text_file(INPUT_FILENAME)
input_num_str = format_data(input_num_str_list)
# print(q_num_str)
# f_q_num_str = format_data(q_num_str)
# print('out of formatted data')
 
# print(q_num_str)
 
# for digit in str(f_q_num_str):
#     print(digit)
 
 
decimal_bytes = convert_to_base_10(input_num_str, base)
print('decimal_bytes:', decimal_bytes)

ascii_chars = decimal_bytes_to_ascii_chars(decimal_bytes)#print this for debugging
print('ascii_chars:', ascii_chars)

ascii_string = list_to_str(ascii_chars)#dont print this for debugging, gets weird because of \n's

# # converted_num_str = str(converted_num)
# ascii_str = long_int_to_ascii_str(converted_num)
#  
# # for digit in str(converted_num):
# #     print(digit)
#   
# print(ascii_str[2])
# print(type(ascii_str[2])) 
#   
#   
# output_list = string_to_list(ascii_str, NUM_DIGITS_PER_OUTPUT_LINE)
# print(output_list[0])

print_ascii_str(ascii_string)
# print('output_list:', output_list)
# write_text_file(OUTPUT_FILENAME, output_list)
print('done!')
#       
