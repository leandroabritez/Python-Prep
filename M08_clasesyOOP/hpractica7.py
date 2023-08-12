class Pepe():
    def __init__(self, list_num):
        self.lis = list_num
        pass

    def num_primo(self):
        for i in self.lis:
            if self._num_primo(i):
                print(i,' es primo')
            else:
                print(i,' no es primo')  


    def _num_primo(self,num):
        for i in range(2,num):
            if num % i == 0:
                return False
        return True    

    def _num_rep(self):
        result = [0,0]
        for i in self.lis:
            rep = self.lis.count(i)
            if rep > result[0]:
                result = [rep,i]
        return print("se repite ",result[0]," veces el numero ",result[1])
    
    def _grados_conver(self,val=1,m_ori="Celsius",m_des="Kelvin"):
        if m_ori == "Celsius" and m_des== 'Kelvin':
            return val + 273.15
        elif m_ori == "Celsius" and m_des== 'Farenheit':
            return val * 9/5 + 32
        elif m_ori == "Farenheit" and m_des== 'Celsius':
            return val - 32 * 5/9
        elif m_ori == "Farenheit" and m_des== 'Kelvin':
            return val - 32 * 5/9 + 273.15
        elif m_ori == "Kelvin" and m_des== 'Celsius':
            return val - 273.15   
        elif m_ori == "Kelvin" and m_des== 'Farenheit':
            return val - 273.15 - 32 * 5/9
        
    def factorial(self):
        result = []
        for i in self.lis:
           result.append(self._factorial(i))
        return result   

    def _factorial(self, num):
        if num < 0 or type(num) != int:
            return print('el numero debe ser entero')
        result = num
        while num-1>0:
            result = result * (num-1)
            num-=1
        return result   
    
a = Pepe([1,3,4,3,5,6,7,6,5])
a.num_primo()
a._num_rep()
a.factorial()    