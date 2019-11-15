
class Numbers:
    def __init__(self,value):
        self.value=value

    def chkprime(self):
        for i in range(2,self.value):
            if (self.value%i)==0:
                return False
                break
        else:
            return True

    def chkperfect(self):
        sum=0
        for i in range(1,self.value):
            if self.value%i==0:
                #print(i)
                sum=sum+i
        if sum==self.value:
            return True
        else:
            return False

    def factors(self):
        for i in range(1,self.value+1):
            if self.value%i==0:
                print(i,end=" ")

    def sumfact(self):
        sum = 0
        for i in range(1, self.value+1):
            if self.value % i == 0:
                sum = sum + i
        return sum


def main():
    value=int(input("enter the no"))
    obj1=Numbers(value)
    print("Number is prime :")
    print(obj1.chkprime())
    print("Number is perfect :")
    print(obj1.chkperfect())
    print("Factors of number :")
    obj1.factors()
    print()
    print("Sum of numbers factors :")
    print(obj1.sumfact())


if __name__ == '__main__':
    main()




