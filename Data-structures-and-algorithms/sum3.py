arr = [12,3,1,2,-6,5,-8,6]
target = 0

def three_number_sum(arr: list, target: int) -> list:
    arr.sort()
    sol = []

    for i in range(len(arr), 4):
        j = -i
        if i == 0 and target > sum([arr[i],arr[-1]]) and (target - sum([arr[i],arr[-1]])) in arr[i+1:j-2]:
            sol.append([arr[i],arr[j-1],target - sum([arr[i],arr[-1]])])
        if i > 0 and target > sum([arr[i],arr[j-1]]) and (target - sum([arr[i],arr[j-1]])) in arr[i+1:j-2]:
            sol.append([arr[i],arr[j-1],target - sum([arr[i],arr[j-1]])])
    return sol

if (three_number_sum(arr, target) == [[-8,2,6], [-8,3,5],[-6,1,5]]):
    print (True)
else:
    print(False)

print(three_number_sum(arr, target))

        






    
   

