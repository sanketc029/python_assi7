
class BookStore:
    noofbooks=0

    def __init__(self,name,author):
        self.name=name
        self.author=author
        BookStore.noofbooks
        BookStore.noofbooks = BookStore.noofbooks + 1


    def Display(self):

        print(self.name," by ",self.author," No of books is ",BookStore.noofbooks)

def main():

    #print("After calling ", BookStore.noofbooks + 1, " object")
    obj1=BookStore("python","py")
    obj1.Display()

    #print("After calling ",BookStore.noofbooks + 1," object")
    obj2=BookStore("java","dennis")
    obj2.Display()

    #print("After calling ",BookStore.noofbooks + 1," object")
    obj2 = BookStore("CPP", "james")
    obj2.Display()

if __name__=="__main__":
    main()