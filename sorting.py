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
