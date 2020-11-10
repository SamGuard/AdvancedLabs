def LIS(S, s, i):
    s1 = []
    s2 = []
    if i < len(S):
        s1 = LIS(S, s.copy(), i + 1)

        if len(s) == 0 or S[i] > s[-1]:
            ns = s.copy()
            ns.append(S[i])
            s2 = LIS(S, ns, i + 1)

        return max(s1, s2, key=len)
    return s

def isIncreasing(arr):#Returns true if the array is increasing
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False

    return True

def LIS1(S, s, i):#S is the input set, s is the current set and i is this index in the input set
    print("s", s, "index", i)
    if i < len(S):
        #Here is where we choose either to include the element at index i or not
        LIS1(S, s.copy(), i + 1)#Exlcude element i

        nextS = s.copy()#Make a copy of s
        nextS.append(S[i]) #Push the next number onto the array
        LIS1(S, nextS, i + 1)#Inlcude element i
        
    return s


#S = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
S = [8, 1, 6]
print(LIS1(S, [], 0))
    

    
    
        