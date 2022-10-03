if __name__ == '__main__':
    myList = []
    grades = [] 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        myList.append([name,score])
        grades.append(score)
    
       
    #Sorting the grades
    grades.sort()
    SecondLowestGrade = grades[0]

    for i in grades:
        if (i > SecondLowestGrade):
               SecondLowestGrade = i 
               break               
    SecondLowestGradeList = []

    for i in myList:
         if(i[1] == float(SecondLowestGrade)):
            SecondLowestGradeList.append(i[0])
    SecondLowestGradeList.sort()
    for i in SecondLowestGradeList:
        print (i) 