def Bubble_Sort(List):
    for i in range(len(List) - 1):
        for j in range(len(List) - 1):
            if(List[j] > List[j + 1]):
                temp = List[j]
                List[j] = List[j+1]
                List[j+1] = temp
    return List



List = [54,67,34,45,8,6,44]
print("Original List :",List)

print("Sorted List : ",Bubble_Sort(List))
