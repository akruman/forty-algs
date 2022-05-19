from os import stat_result


class Sort:
    @staticmethod
    def bubble(arr):
        for j in range(len(arr)-1, 1, -1): # inner propgates max to arr[j]
            for i in range(j): # inner
                if(arr[i]>arr[i+1]):
                    arr[i],arr[i+1] = arr[i+1],arr[i]
        return arr

    @staticmethod
    def insert(arr):
        for j in range(1,len(arr)): # pick arr[j] and put it in correct location below
            e = arr[j]
            for i in range(j-1,0,-1):
                if e<arr[i]:
                    arr[i+1] = arr[i]
                else:
                    break
                arr[i]=e
        return arr

    @staticmethod
    def merge(arr): # arr passed by ref
        n = len(arr)
        if n>1:
            n = n//2
            #print(arr[:n],arr[n:])
            a1=Sort.merge(arr[:n]) # new arr created, with same values, which are referenced
            a2=Sort.merge(arr[n:])
            def merge(a1,a2):
                a = []
                n = (len(a1),len(a2))
                i = [0,0]
                while sum(i) < sum(n):
                    if i[0]<n[0] and i[1]<n[1]:
                        if a1[i[0]] < a2[i[1]]:
                            a += [a1[i[0]]]
                            i[0]+=1
                        else:
                            a += [a2[i[1]]]
                            i[1]+=1
                    elif i[0]==n[0]:
                        a += a2[i[1]:]
                        i[1] = n[1]
                    elif i[1]==n[1]:
                        a += a1[i[0]:]
                        i[0] = n[0]
                return a
            arr = merge(a1,a2)
        return arr

    @staticmethod
    def selection(arr):
        def imax(arr):
            if len(arr)==0: return None
            i = 0
            for j in range(len(arr)):
                if arr[j]>arr[i]:
                    i=j
            return i

        for i in range(len(arr),0,-1):
            j = imax(arr[:i])
            if j is not None:
                arr[j],arr[i-1] = arr[i-1],arr[j]

        return arr