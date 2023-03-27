 # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    
# Any code taken from other sources is referenced within my code solution.   
# Student ID: w1912939
# IIT Student ID: 20210572
 #Pelawaththe Kirihamilage Ravindu Layanga Premasiri   
# Date 2022/04/11


#Creating variables
pass_marks = 0
defer_marks = 0
fail_marks = 0
select_version = 0
total_value=0
progress=0
trailer=0
retriever=0
exclude=0
total_outcoms=0
loop=0
prog=[]
trail=[]
retri=[]
excl=[]
inputs = []

#Get wich version need to run 
while  True:
    try:
     print("Select the option\n\t1.Student version.\n\t2.Staff version with Histogram.")
     select_version =int( input('\tPlease select the option between 1 & 2 :-'))
     if select_version == 1 or select_version ==2 :
        break
     else:
        print('\n\tWrong selection. \tPlease select Number "1" or "2"\n')
        continue
    except ValueError:
         print('\n\Please Enter Number\n')
if select_version==1:
    print("\n\t\tStudent version\n")
else:
    print("\n\t\tStaff version with Histogram\n")
#Function for getting marks and validate   
def getting_marks():
    global progress,trailer,exclude,retriever
    while True:
     try:
        pass_marks=int(input("\nEnter your total PASS  credits :- "))
        if pass_marks not in [0,20,40,60,80,100,120]:
         print('Out of range')
        else:
             defer_marks=int(input("Enter your total DEFER credits :- "))
             if defer_marks not in [0,20,40,60,80,100,120]:
                 print ('Out of range')
             else:
                     fail_marks=int(input("Enter your total FAIL credits :-"))
                     if fail_marks not in [0,20,40,60,80,100,120]:
                         print('Out of range')
                     else:
                         total_value=pass_marks+defer_marks+fail_marks
                         if total_value != 120:
                             print("Total incorrect")
                         else:
                            break
     except ValueError:
         print("\nPlease Enter Number\n")
#Validation
    inputs = [pass_marks,defer_marks,fail_marks]
    if pass_marks==120:
       print("Progress\n")
       prog.append(inputs)
       progress+=1
    elif pass_marks==100:
        print("Progress (module trailer)\n")
        trail.append(inputs)
        trailer+=1
    elif fail_marks>=80:
      print("Exclude\n")
      excl.append(inputs)
      exclude+=1
    else:
      print("Do not progress - module retriever\n")
      retri.append(inputs)
      retriever+=1
      
#Calling function
getting_marks()

#Getting another set of data for staff version
if select_version==2:  
   print ("Would you like to enter another set of data? ")
   while True:
          loop=str(input("Enter 'Y' or 'y' or  for yes or 'Q' or 'q' to quit and view result :"))
          if loop not in ["y","q","Y","Q"]:
              print("Please enter 'Y' or 'y' or  for yes or 'Q' or 'q' to quit")
          if loop=="y" or loop=="Y":
             getting_marks()
          if loop=="q" or loop=="Q":
             break
   total_outcoms=progress+trailer+exclude+retriever
   
#Printing Horizontal Histogram
   print("-"*100,"\n\t\tHorizontal histogram")
   print("Progress ",'(',progress,') :',progress*"*","\nTrailer: \t",'(',trailer,') :',trailer*"*","\nRetriever:",'(',retriever,') :',retriever*"*","\nExclude:\t",'(',exclude,') :',exclude*"*")
   print(total_outcoms,"outcomes in total.")
   
#Printing vertical Histogram   
   print("-"*100,"\n\t\tVertical histogram")
   print("Progress  Trailer  Retriever  Exclude")
   for x in range(max(progress,trailer,retriever,exclude)):
       print("   {0}                  {1}              {2}            {3}".format(
           '*' if x < progress else ' ',
           '*' if x< trailer else ' ',
           '*' if x< retriever else ' ',
           '*' if x< exclude else ' '))
   


# I used Stack overflow website to get the help to print the vertical Histogram Below is the link to that website
#https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops

    
#print List of results and creating text file
if select_version==2:
    file=open("result.txt", 'w')
    for x in prog:
        print("Progress :",*x)
        file.write("Progress :"+str(x))
        file.write(" ")
        file.write("\n")
    for x in trail:
        print("Trailer :",*x)
        file.write("Trailer :"+str(x))
        file.write(" ")
        file.write("\n")
    for x in excl:
        print("Exclude :",*x)
        file.write("Exclude :"+str(x))
        file.write(" ")
        file.write("\n")
    for x in retri:
        print("Retriever :",*x)
        file.write("Retriever :"+str(x))
        file.write(" ")
        file.write("\n")
    file.close()
#reading the text file
    file=open("result.txt", 'r')
    if file.mode=="r":
        contents=file.read()
        print('-'*100)
        print("\n",contents)
    file.close()
    print("Program is over. Thank you for using this tool")
else:
     print("Program is over. Thank you for using this tool!")
    
