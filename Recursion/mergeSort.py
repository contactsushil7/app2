
def mergeSort(arr : list, low : int, high:int)->list:
    if low >= high :
        return
    mid = (high + low) // 2
    print(mid)
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    arr = sortArr(arr,low,mid,high)
    return arr

def sortArr(arr: list, low:int,mid:int, high:int) -> list:
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <=high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left+=1
        else :
            temp.append(arr[right])
            right +=1
    while left <= mid:
        temp.append(arr[left])
        left +=1
    while right <= high:
        temp.append(arr[right])
        right +=1
    
    for i in range(low,high+1):
        arr[i] = temp[i-low]
        i+=1
    return arr


if __name__ == '__main__':
    arr = [3,1,2,4,1,5,6,2,4]
    print(len(arr)-1 -(8+0)//2)


    print(mergeSort(arr, 0 , len(arr)-1))
    