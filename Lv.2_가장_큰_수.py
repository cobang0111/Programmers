# Quick sort : average O(nlogn)
def quick_sort(start, end, arr):
    # Break condition
    if start >= end:
        return 0
    # Initial Index
    pivot = start
    a = pivot + 1
    b = end
    # Sorting by DESC of 1st digit 
    while a <= b:
        first_digit_a = int(str(arr[a])[0])
        first_digit_b = int(str(arr[b])[0])
        first_digit_pivot = int(str(arr[pivot])[0])
        # Finding pivot position from the front
        while a <= end and first_digit_a >= first_digit_pivot:
            # Case : 1st digit is same -> compare 2 case XY and YX
            if first_digit_a == first_digit_pivot:
                case1 = int(str(arr[a])+str(arr[pivot]))
                case2 = int(str(arr[pivot])+str(arr[a]))
                if case2 <= case1 :
                    a += 1
                    # For the index in the range
                    if a <= end:
                        first_digit_a = int(str(arr[a])[0])
                else:
                    break
            else :
                a += 1
                if a <= end:
                    first_digit_a = int(str(arr[a])[0])
        # Finding pivot position from the end
        while b > start and first_digit_b <= first_digit_pivot:
            # Case : 1st digit is same -> compare 2 case XY and YX
            if first_digit_b == first_digit_pivot:
                case1 = int(str(arr[b])+str(arr[pivot]))
                case2 = int(str(arr[pivot])+str(arr[b]))
                if case2 >= case1 :
                    b -= 1
                    # For the index in the range
                    if b > start:
                        first_digit_b = int(str(arr[b])[0])
                else:
                    break
            else :
                b -= 1
                if b > start:
                    first_digit_b = int(str(arr[b])[0])
        #Swap        
        if a > b:
            temp = arr[pivot]
            arr[pivot] = arr[b]
            arr[b] = temp
        else :
            temp = arr[a]
            arr[a] = arr[b]
            arr[b] = temp
    #recursive
    quick_sort(start, b-1, arr)
    quick_sort(b+1, end, arr)

def solution(numbers):
    answer = ''
    
    quick_sort(0, len(numbers)-1, numbers)
    
    #Concatenation
    for i in numbers:
        answer += str(i)
    
    #Case : 00..000
    if answer[0] == '0':
        answer = "0"
    
    return answer
