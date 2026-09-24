# read last n lines ot a file
def read_line(file_name , number_of_lines):
    with open(file_name) as f:
        lines = (f.readlines()[-number_of_lines:])
        for line in lines:
            print(line, end="")
            

file_name = "user_data.txt"
number_of_lines = 3


try:
    read_line(file_name , number_of_lines)
except:
    print("file not found")