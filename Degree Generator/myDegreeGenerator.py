'''
filename: It is a parameter of generate()
          It contains name of the file which contains Student Info
          It is structured with 1st row containg total no of students for which we are generating degree,
            2nd row contains label of information for each column and rest of rows containg student inforamtion
generate(): It is used to create degrees based on the information present in Student Info file
'''
def generate(filename):
  try:
    myFile=open(filename,"r")
    #Splits our file and create a list with each element containing each line as a string
    studentInfo=myFile.read().split('\n')
    myFile.close()
    #first line of our file contains no of entries of students so we are extracting that into a new variable
    entries=int(studentInfo[0])
    '''
    in 2nd line of our file we have the naming of each attribute of our student info so we are extracting
    that into list called label
    '''
    Label=studentInfo[1].split(', ')
    #starting from the 3rd line to the end to access all the student entries
    for i in range(2,entries+2):
      currentStudent=studentInfo[i].split(',')
      '''
      for each entry we are using our list called Label to identify attribute of students such as
      name,roll no etc and then storing them into variables
      '''
      for j in range(0,len(Label)):
        if(Label[j]=='Name of student'):
          name=currentStudent[j]
        elif(Label[j]=='Roll number'):
          rollno=currentStudent[j]
        elif(Label[j]=='Programme Name'):
          course=currentStudent[j]
        elif(Label[j]=='Year of Award'):
          year=currentStudent[j]
        elif(Label[j]=='Percentage'):
          percentage=currentStudent[j]
      #opening our degree template and extracting data into a new variable called degreeData
      degreeTemplate=open("degreeTemplate.txt",'r')
      degreeData=degreeTemplate.read()
      degreeTemplate.close()
      #we are now using our attribute variable to replace the place holders in degreeData
      degreeData=degreeData.replace("<Student Name>",name)
      degreeData=degreeData.replace("<Name of Progeamme>",course)
      degreeData=degreeData.replace("<Year>",year)
      degreeData=degreeData.replace("<Percentage>",percentage)
      # datetime library is used to get real world date and time
      import datetime
      #with today function in datetime library we are getting real world date time and storing it in dateWithTime
      dateWithTime=datetime.datetime.today()
      #function strftime is used with parameters %d,%B,%Y to just get the date and storing it in justDate
      justDate = dateWithTime.strftime('%d %B %Y')
      degreeData=degreeData.replace("<date of creation>",justDate)
      #creating our degree file's name with name and rollno(roll number) attributes and storing it in variable degreeName
      degreeName=name+rollno+".txt"
      #creating a new file(or overwriting) with name using degreeName variable and write the degreeData's data in it
      degree=open(degreeName,'w')
      degree.write(degreeData)
      print(f"Degree of {name} with roll number {rollno} Sucessfully Generated")
      degree.close()
  #error handling for the case when there no file exist with name stored in filename
  except FileNotFoundError:
    print(" file does not exist")