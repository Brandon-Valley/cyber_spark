from test.test_bigmem import ascii_char_size
import math

def get_num_digits_per_byte(base):
    log1 = math.log10(base)
    log2 = math.log10(256)
    a = log1 / log2
    b_float = 1 / a
    b_rounded = math.ceil(b_float)
    return b_rounded
    
    
#     log2 = math.log(256, base)
#     log2 = math.log2(256)


def group_into_bytes(num_str, digits_per_byte):
#     digits_per_byte = get_num_digits_per_byte(base)#````````````````````````````````````````````````````````````````
    
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

    #2301 base 5 = 326
def convert_to_decimal_bytes(og_bytes_list, base):
#     num_str = format_data(num_str_list)#```````````````````````````````````````````````````````````
#     rev_num_str = rev_str(num_str)#``````````````````````````````````````````````````````
    
#     og_bytes_list = group_into_bytes(num_str, digits_per_byte)
#     print(og_bytes_list)
    
    new_bytes_list = []
    
    for og_byte in og_bytes_list:
        new_byte = convert_byte_to_decimal(og_byte, base)
        new_bytes_list.append(new_byte)#.insert(0, new_byte)
        
    return new_bytes_list
        
# ASCII_NUM_CHARS = 'fedcba'

def convert_byte_to_decimal(old_byte, base):
    rev_old_byte = rev_str(old_byte)
    new_byte_int = 0
    
    for digit_pos in range( len(rev_old_byte) ):
        digit_char = rev_old_byte[digit_pos]
        
        #if numeric
        if digit_char.isdigit():
            digit_int = int( digit_char )
        else:
            digit_int = get_alpha_int_value(digit_char)
            
#         print('digit_pos: %s   digit_int: %s' %(digit_pos , digit_int))
        decimal_equiv = digit_int * base**digit_pos
        print('decimal_equiv = digit_int * base ^ digit_pos   %s   %s = %s * %s ^ %s' %(digit_char, decimal_equiv, digit_int, base, digit_pos) )
#         print('base %s,  og digit: %s  digit_int: %s  decimal_equiv:  %s' %(base, digit_char, digit_int, decimal_equiv ))
        new_byte_int += decimal_equiv
        
    return str(new_byte_int)


def get_alpha_int_value(digit_char):
    ascii_start = ord('a')
    digit_ascii = ord(digit_char)
    diff = digit_ascii - ascii_start
    digit_int = 10 + diff
    return digit_int
   


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
    formatted_data = ''
    
    try:
        for data_line_num in range( len(data) ):                
            formatted_data += data[data_line_num]

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


  
# test_str = '0111101111011000100000100'
# 
# test_group_bytes = group_into_bytes(test_str, 8)
# test_byte = convert_byte(test_group


base = 31
  
        
INPUT_FILENAME =  'input.txt'
OUTPUT_FILENAME = 'output.txt'
NUM_DIGITS_PER_OUTPUT_LINE = 10


input_num_str_list = read_text_file(INPUT_FILENAME)
input_num_str = format_data(input_num_str_list)

print('base:', base)
 
digits_per_byte = get_num_digits_per_byte(base) 
print('digits_per_byte:', digits_per_byte)
 
grouped_bytes = group_into_bytes(input_num_str, digits_per_byte) 
# print('grouped_bytes:', grouped_bytes)
 
decimal_bytes = convert_to_decimal_bytes(grouped_bytes, base)
print('grouped_bytes:', grouped_bytes)
print('decimal_bytes:', decimal_bytes)

ascii_chars = decimal_bytes_to_ascii_chars(decimal_bytes)#print this for debugging
print('ascii_chars:', ascii_chars)

ascii_string = list_to_str(ascii_chars)#dont print this for debugging, gets weird because of \n's

print_ascii_str(ascii_string)
# print('output_list:', output_list)
# write_text_file(OUTPUT_FILENAME, output_list)
print('done!')
#       
