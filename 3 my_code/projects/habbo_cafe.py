
def read_file(filename):
    #returns a list of data extracted from the parameter file
    #each element of the returned list is a line from the file.
    with open(filename) as file:
        ret = file.read()
    return ret.split('\n')

def read_file_lines(filename):
    cleaned = []
    with open(filename) as file:
            lines = file.readlines()
    #Option 1 .... 
    cleaned = [line.strip() for line in lines]

    #Option 2
    for line in lines:
        clean = line.strip()
        cleaned.append(clean)  

    return cleaned
    

#add functions here


#Write your main script here\
def main():
    menu_list = read_file('menu.txt')
    print(menu_list)

main()