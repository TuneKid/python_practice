# Implement a function to compare 2 lists and return the common items in a list




# Given the above, implement a function getCommon
# that returns the common elements e.g.
# getCommon(list1, list2) should return 
# ["B", "C", 3]

input1 = input("What list would you like 1st?").split(" ")
input2 = input("What list would you like 2nd?").split(" ")

def getCommon(listA, listB):
  common = []
  for item in listB:
    if item in listA:
      common.append(item)
  if len(common) >= 5:
    print("False")
  else:
    print("True")
    print(common)


list1 = input1
list2 = input2

answer = getCommon(list1, list2)

