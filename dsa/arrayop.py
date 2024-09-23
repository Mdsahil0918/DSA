import ctypes
class mlist:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)
    
    def __len__(self):
        return self.n
    
    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size * 2)
        self.A[self.n] = item
        self.n += 1

    def pop(self):
        if self.n==0:
            return'Empty list'
            print(self.A[self.n-1])
            self.n=self.n-1 
    def clear(self):
        self.n=0
        self.size =1        

    def __str__(self):
        result =''
        for i in range(self.n):
            result +=str(self.A[i])+','
        return '[ '+ result[:-1]+' ]'

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B  # Reassign array after copying
        self.size = new_capacity

    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            return'Index error - u dumb' 
    def find(self,item):
        for i in range(self.n):
            if self.A[i] ==item:
                return i
            else:
                return 'value not found'              

L = mlist()  
L.append("hello " )
L.append(33)
L.append('its cool .man i made a custom print funtion')
L.find(33)