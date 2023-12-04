print("..........Degree Generator...........")
print("Menu: ")
print("1) To generate a degree in bulk")
print("2) To include Corrections in a degree")
print("3) To view a degree")
print("4) Exit")
while True:
  choice=int(input("Enter your Choice(1-4): "))
  if(choice==1):
    #importing myDegreeGenerator module to create a Degree
    import myDegreeGenerator as gen
    studentInfo=input("Enter the Name of the file containing Student Information: ")
    '''
    generate() is a function in myDegreeGenerator Module 
    generate() requires 1 parameter i.e. the name of the file
    It takes student data from out file and generates degrees out of the data
    '''
    gen.generate(studentInfo)
  elif(choice==2):
    #importing myDegreeCorrector to correct information in our Degree
    import myDegreeCorrector as cor
    degreeFileName=input("Enter the Name of the Degree File: ")
    '''
    corrector() is a function in myDegreeCorrector which corrects infromation in a Degree
    It requires one parameter i.e. Degree File Name 
    '''
    cor.corrector(degreeFileName)
  elif(choice==3):
    #myDegreeViewer is a module that we use to view contents of the degree
    import myDegreeViewer as view
    degreeFileName=input("Enter the Name of the Degree File: ")
    '''
    display() is a function in myDegreeViewer module it is used to print the contents of the degree 
    It requires one parameter i.e. Degree File Name
    '''
    view.display(degreeFileName)
  elif(choice==4):
    print("Thank You For Using This Program")
    break
  else:
    print("Invalid Input")