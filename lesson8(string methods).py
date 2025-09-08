course = "   Python Programming  "
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.rstrip())
print(course.lstrip())
print(course.find("Pro"))
print(course.find("pro")) # String was not found because python is case sensitive
print(course.replace("P","j"))
print("Pro" in course) # return a boolean 
print("swift" not in course)