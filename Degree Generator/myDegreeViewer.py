'''
filename: It is a parameter for display() function
          It contains name of out degree file which we want to print
display(): Takes out filename
           Reads out our file using a variable named degree and prints it

'''
def display(filename):
  try:
    degree=open(filename,'r')
    print(degree.read())
  # error handling for the case when there no file exist with name stored in filename
  except FileNotFoundError:
    print(f"{filename} does not exist")