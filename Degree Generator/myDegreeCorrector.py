'''
filename: It is a parameter of corrector()
          It contains the name of the file which holds our degree
corrector(): It uses one parameter 'filename'
             It is a menu driven function used to make corrections in our degree file
'''
def corrector(filename):
  try:
    degree=open(filename,'r')
    #storing our degree's data in a variable degreeData
    degreeData=degree.read()
    degree.close()
    print("Menu:")
    print("1)Correct Student Name")
    print("2)Correct Name of Programme")
    print("3)Correct Year")
    print("4)Correct Percentage")
    print("5)Save and Exit")
    while True:
      #asking user to choose the change they want to make using integers and storing there choice using a variable choice
      choice=int(input("Enter Your Choice(1-5):"))
      if(choice==1):
        #Ask user for incorrect name and correct name make the correction in our variable degreeData using replace() function
        prevName=input("Enter Name before Correction: ")
        name=input("Enter Corrected Name: ")
        degreeData=degreeData.replace(prevName,name)
        #Since name attribute is used in file name as well we need to make a change in it as well
        #module that contains functions we need to make changes in file name
        import os
        '''
        we are taking our file name and creating a list containg 2 elements (using variable named tempList)
        First element holds the name of degree holder
        and second element hold roll number + .txt
        '''
        tempList=filename.split();
        #Creating new name for our file and storing it in a variable newFileName
        newFileName=name+" "+tempList[1];
        '''
        rename(): a finction in os module
                  used to change a name of file
                  uses 2 parameters
                  1st parameter contains the current file name
                  2nd parameter contains the name you want to update to
        '''
        os.rename(filename, newFileName)
        filename=newFileName
      #asking user for correct and incorrect info then replacing it using replace() in degreeData variable
      elif(choice==2):
        prevCourse=input("Enter Programme before Correction: ")
        course=input("Enter Corrected Programme: ")
        degreeData=degreeData.replace(prevCourse,course)
      elif(choice==3):
        prevYear=input("Enter Year before Correction: ")
        year=input("Enter Corrected Year: ")
        degreeData=degreeData.replace(prevYear,year)
      elif(choice==4):
        prevPer=input("Enter Percentage before Correction: ")
        per=input("Enter Corrected Percentage: ")
        degreeData=degreeData.replace(prevPer,per)
      elif(choice==5):
        #updating our degree file by overwriting it using data in degreeData variable and then breaking while loop to exit the module
        degree=open(filename,'w')
        degree.write(degreeData)
        degree.close()
        print(f"{filename} updated")
        break
      else:
        #In case user chooses not a valid value for choice variable
        print("InValid Input")
  #error handling for the case when there no file exist with name stored in filename
  except FileNotFoundError:
    print(f"{filename} does not exist")