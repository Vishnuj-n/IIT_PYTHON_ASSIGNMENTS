class Member:
    def __init__(self,name,membership_id):
        self.name=name
        self.membership_id=membership_id
        
    
    def is_valid(self):
        id=[1,2,3,4]
        if self.membership_id in id:
            return True
        else:
            return False


class StudentMember(Member):
    def __init__(self, name, membership_id):
        super().__init__(name, membership_id) 
        self.borrow=0

    def return_book(self):
        if super().is_valid():
            print("book returned")
            self.borrow-=1

    def currently_burrowed(self):
        if super().is_valid():
            print(f"no. of books borrowed:{self.borrow}")
        
    def borrow_book(self):
        if super().is_valid():
            print("book borrowed")
            self.borrow+=1
        

d=StudentMember("vishnu",1)
d.currently_burrowed()
d.borrow_book()
d.currently_burrowed()
d.return_book()
d.currently_burrowed()
    