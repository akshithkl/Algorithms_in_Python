def Sorted_List(List_1):
    for i in range(len(List_1) - 1):
        curnt_indx = i
        
       
        for j in range(i + 1, len(List_1)):
            if List_1[j] < List_1[curnt_indx]:
                curnt_indx = j
                
        List_1[i], List_1[curnt_indx] = List_1[curnt_indx], List_1[i]
           
    
    return List_1

List_1 = [23, 43, 12, 3, 45, 6, 5]
print("Original List:", List_1)
print("Sorted List:", Sorted_List(List_1))
