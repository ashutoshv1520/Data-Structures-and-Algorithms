def merge(a1,a2,arr):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if (a1[i]<a2[j]):
            arr[k]=a1[i]
            k=k+1
            i=i+1
        else:
            arr[k]=a2[j]
            k=k+1
            j=j+1
    while i<len(a1):
        arr[k]=a1[i]
        k=k+1
        i=i+1
    while j<len(a2):
        arr[k]=a2[j]
        k=k+1
        j=j+1
        
def mergeSort(arr):
    # Please add your code here
    if len(arr)==0 or len(arr)==1:
        return
    mid=len(arr)//2
    a1=arr[0:mid]
    a2=arr[mid:]
    mergeSort(a1)
    mergeSort(a2)
    merge(a1,a2,arr)


# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)