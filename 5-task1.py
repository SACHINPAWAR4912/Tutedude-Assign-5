user=input("Enter student's name: ")

Student_mks = {'Alice':85, 'Sam':69, 'Bunty':88}
if user in Student_mks:
    print(""+user+"'s Marks:" , (Student_mks[user]))
else:
    print(Student_mks.get(user,'Student not found'))