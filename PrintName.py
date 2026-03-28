sub1 = 35
sub2 = 45
sub3 = 29
result = ""
if (sub1 >=35):
    result = "passed in sub1"
elif(sub2 >= 35):
    result = result + "\n" + "Passed in sub2"
elif(sub3 >= 35):
    result += "\n" + "passed in sub 3"
elif(sub1+sub2+sub3 >= 105):
    result += "\n" + "promoted to next class"
else:
    result = "Failed"

print(result)
    