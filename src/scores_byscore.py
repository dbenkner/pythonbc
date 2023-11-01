import sys

with open('src/testscores.dat', 'r') as f:
    stuList = dict()
    sum = 0
    count = 0
    for l in f :
        print(l)
        count += 1
        lineItem = l.split(":", 2)
        name = lineItem[0]
        score = int(lineItem[1].strip('\n'))
        letterGrade = ""
        if score > 94 :
            letterGrade = "A"
        elif score > 88 :
            letterGrade = "B"
        elif score > 82 :
            letterGrade = "C"
        elif score > 74 :
            letterGrade = "D"
        else :
            letterGrade = "F"
        stuList[count] = (name, score, letterGrade)
        sum += score
    sortedStudents = sorted(stuList.items(), reverse=True, key=lambda x:x[1])
    print(sortedStudents)
    print(sum / len(sortedStudents))
