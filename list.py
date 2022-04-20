list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]


print(list1)
print(list2)
print(list3)
print(list4)

print(list1[:4])
print(list2[2:5])
print(list3[-1])
print(list4[-4:-1])

if "apple" in list1:
    print("yes ,apple is present in the list")