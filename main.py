# Implement a function to compare 2 lists and return the common items in a list




# Given the above, implement a function getCommon
# that returns the common elements e.g.
# getCommon(list1, list2) should return 
# ["B", "C", 3]

def getCommon(listA, listB):
  common = []
  for item in listB:
    if item in listA:
      common.append(item)
      
  return common



list1 = ["A", 1, 3, "B", "C"]
list2 = ["B", "C", 3, "D"]
answer = getCommon(list1, list2)
print(answer)
print(list1)
