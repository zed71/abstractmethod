


from abc import ABC, abstractmethod
class book(ABC):
    def checkOut(self, books):
        print("Your checked out book number is: ",books)
        @abstractmethod
        def checked(self, books):
            pass


class OverDueBooks(book):
    def payment(self, books):
        print('You have overdue books of {} you are not able to checkout until paid'.format(books))

obj = OverDueBooks()
obj.checkOut("3")
obj.payment("3")
