import sys
input = sys.stdin.readline

def printArray(arr) :
    result = list(map(str, arr))
    return ' '.join(result)

def bubbleSort(arr) :
    for i in range(len(arr) - 1, 0, -1) :
        for j in range(i) :
            if arr[j] > arr[j+1] :
                buf = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = buf
                print(printArray(arr))
        
    return arr

if __name__ == "__main__":
    array = list(map(int, input().split(" ")))
    bubbleSort(array)