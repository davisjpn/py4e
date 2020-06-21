score = input("Please enter score:")
try:
    score=float(score)
except:
    print("Error, score must be numeric")
    quit()
if score < 0 or score > 1:
    print("Error,score must be between 0 and 1:")
    quit()
if score >= .9:
    grade = "A"
elif score >= .8:
    grade = "B"
elif score >= .7:
    grade = "C"
elif score >= .6:
    grade = "D"
else:
    grade = "F"
print(grade)
