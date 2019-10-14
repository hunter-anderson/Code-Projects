def solution(l):
    return mergeSort(l)

def mergeSort(array):
    if len(array) > 1:
        #select middle of list and split into two lists
        middle = len(array)//2
        leftArray = array[:middle]
        rightArray = array[middle:]

        #sort the left and right list
        mergeSort(leftArray)
        mergeSort(rightArray)

        #merge the now sorted lists
        i = j = k = 0
        while i < len(leftArray) and j < len(rightArray):
            #split the string into major, minor, and revision
            left = leftArray[i].split('.')
            right = rightArray[j].split('.')

            #min length of left and right string to prevent IndexError
            x = min([len(left), len(right)])

            #iterate over both strings and compare major, minor, and revision
            for n in range(x):
                if int(left[n]) < int(right[n]):
                    #store left value and increment
                    array[k] = leftArray[i]
                    i += 1
                    k += 1
                    break

                elif int(left[n]) > int(right[n]):
                    #store right value and increment
                    array[k] = rightArray[j]
                    j += 1
                    k += 1
                    break

                #if both nums equal and at last value of smaller string
                #store the smaller string
                if n == x-1:
                    if (len(left) <= len(right)):
                        array[k] = leftArray[i]
                        i += 1
                        k += 1
                        break
                    else:
                        array[k] = rightArray[j]
                        j += 1
                        k += 1
                        break

        #catch any leftovers
        while i < len(leftArray):
            array[k] = leftArray[i]
            k += 1
            i += 1
        while j < len(rightArray):
            array[k] = rightArray[j]
            k += 1
            j += 1
    return array

l = (["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
print(solution(l))
