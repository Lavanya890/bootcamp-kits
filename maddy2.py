def reverse(str):
    string = " "
    for i in str:
        string = i + string
    return string
str = "PythonGuides"
print("yes,The original string is:",str)
print("reverse string is:", reverse(str)) 