


def convert_to_base_10(num_str, base):
    answer = 0;
    
    rev_num_str = rev_str(num_str)
    
    for digit_num in range( len(rev_num_str) ):
        digit_char = rev_num_str[digit_num]
        digit_int = int( digit_char )
        
#         print('digit_num: %s   digit_int: %s' %(digit_num , digit_int))
        answer += digit_int * base**digit_num
        
    return answer

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
    print('in format_data')
    formatted_data = ''
    
    count = 0
    
    try:
        for data_line in data:
#             print(data_line + '//////')
            formatted_data += data_line
            
            if count == 3:
                print('stop')
                while(True):
                    pass
            print(formatted_data)
            count += 1
#             if data_line[0] == ' ' or formatted_data == '':
#                 formatted_data += data_line
#             else:
#                 formatted_data += ' ' + data_line\
        return formatted_data
    except:
        raise Exception('ERROR  You probably have some extra lines of spaces in your data text file')
    


q_num_str = read_text_file('input_base_num.txt')
print(q_num_str)
f_q_num_str = format_data(q_num_str)
print(f_q_num_str)


while(True):
    pass

base = 3

converted_num = convert_to_base_10(f_q_num_str, base)
print(converted_num)    
    
    #2301 base 5 = 326