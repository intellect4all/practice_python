def solution(A):
    # write your code in Python 3.6
    totalEmissions = sum(A)
    array_copy = A
    hi,lo = 0,0
    filter_count = 0

    


    def getFilter(n, maxCount, count):
        a = max(n)
        i = n.index(a)
        n[i] = a/2
        count += 1
        if sum(n) > maxCount:
            
            return getFilter(n,maxCount,count)
        else:
            return count

    return getFilter(A, sum(A)/2, 0)





print(solution([10,10]))