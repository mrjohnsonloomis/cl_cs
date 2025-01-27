
def read_file(filename):
    #returns a list of data extracted from the parameter file
    #each element of the returned list is a line from the file.
    with open(filename) as file:
        ret = file.read()
    return ret.split('\n')

#add functions here


#Write your main script here\
def main():
    menu_list = read_file('menu.txt')
    print(menu_list)

main()