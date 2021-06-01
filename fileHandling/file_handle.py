path = './resources/sample.txt'

# Function to read a text file
def read_file(filename):
    print('function definition to read a file.')
    try:
        file = open(filename, 'r')
        for each in file:
            print (each)
    except:
        print("file does not exist")
 
# Driver code
read_file(path)    


# Python code to illustrate split() function
def split_line(filename):
    try:
        with open("file.text", "r") as file:
            data = file.readlines()
            for line in data:
                word = line.split()
                print (word) 
    except:
        print("file does not exist")  
# Driver Code
split_line(path)