'''
Created on Apr 2, 2016

@author: Brandon
'''
classes = {"SAS":3,"Machine Learning":3,"Stat Design":3,"Directed Study":3}

gpaValues = {"A":4.0,"AB":3.5,"B":3.0,"BC":2.5,"C":2.0}

springGPA = {"SAS":"A","Machine Learning":"A","Stat Design":"A","Directed Study":"A"}

currentGPA = [370.0/99.0,99.0]#[3.39,13] #[GPA,credits] [166.0,45] [224/61.0,61] [311.5/84.0,84.0] MAJOR GPA = 152.5/40

def calculateGPA(credits,gradeValues,grades,currentGPA):
    sum = currentGPA[1]
    grade = currentGPA[0]*currentGPA[1]
    semSum = 0.0
    semGrade = 0.0
    for c in grades:
        grade+=(gradeValues[grades[c]]*credits[c])
        semGrade+=(gradeValues[grades[c]]*credits[c])
        sum+=credits[c]
        semSum+=credits[c]
    return [semGrade/semSum,grade/sum,sum,grade] 
"""    
for c in springGPA:
    print "%s: %s" % (c, springGPA[c])
"""    
gpa = calculateGPA(classes,gpaValues,springGPA,currentGPA)

print "Your semester GPA is: %s" % round(gpa[0],4)
print "Your cumulative GPA is: %s" % round(gpa[1],4)
print "You have taken %s credits" % gpa[2]
print "You have %s GPA points" % gpa[3]

