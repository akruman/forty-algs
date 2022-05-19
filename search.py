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

    
