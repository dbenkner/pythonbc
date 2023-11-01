import sys

with open('src/testscores.dat', 'r') as f:
    stuList = dict()
    sum = 0
    for l in f :
        print(l)
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
        stuList[name] = score, letterGrade
        sum += score
    sortedStudents = dict(sorted(stuList.items()))
    print(sortedStudents)
    print(sum / len(sortedStudents))
