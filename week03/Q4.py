mondayClass = { "Alice" , "Bob" , "Charlie" , "Diana" }
wednesdayClass = { "Bob" , "Diana" , "Eve" , "frank"}
mondayClass.add("Grace")
print("Monday Class : " , mondayClass)
print("Wednesday Class : " , wednesdayClass)
bothClass = mondayClass & wednesdayClass
print("Attended both Class : " , bothClass)
allStudents = mondayClass | bothClass
print("All Students : " , allStudents)
print("Is Monday subset of all students?" , allStudents.issubset(mondayClass))
