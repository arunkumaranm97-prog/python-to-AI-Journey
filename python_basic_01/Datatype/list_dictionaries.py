#list
lst=[50,20,30,40,601,70,80,90,100]
print("All marks:", lst)
print("Highest mark:", max(lst))
print("Lowest mark:", min(lst))
print("First mark:",lst[0])
print("Average:", sum(lst)/len(lst))

#dictionary
student={
    "name":"Arun",
    "age":20,
    "marks":90
}
print("Student name:", student["name"])
print("Student age:", student["age"])
print("Student marks:", student["marks"])
student["name"]="Arun Kumaran"
print("Updated student structure:")
print(student)