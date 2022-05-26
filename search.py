class Search:
    @staticmethod
    def linear(arr, num):
        for x in arr:
            if x == num:
                return True
        return False

    @staticmethod
    def binary(arr, num):
        n = len(arr)
        if n == 0: return False
        n = n//2
        return num == arr[n] or \
            (num < arr[n] and Search.binary(arr[:n],num)) or \
            (Search.binary(arr[n:],num))

    @staticmethod
    def interpolation(arr, num):
        idx0 = 0     
        idxn = (len(arr) - 1)     
        found = False     
        while idx0 <= idxn and num >= arr[idx0] and num <= arr[idxn]: 
            # Find the mid point
            #  Dx*DY'/DY   - look where Y diff points to, and go in x direction from ixd0     
            mid = idx0 +int(((float(idxn - idx0)/( arr[idxn] - arr[idx0])) * (num - arr[idx0]))) 
            # Compare the value at mid point with search value 
            if arr[mid] == num: 
                found = True             
                return found         
            if arr[mid] < num:             
                    idx0 = mid + 1     
        return found

    
