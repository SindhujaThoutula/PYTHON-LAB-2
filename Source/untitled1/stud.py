class Sindhuja:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
class Student(Sindhuja):
    StudentCount = 0
    def __init__(self, name, email, student_id):
        Sindhuja.__init__(self, name, email)
        self.student_id = student_id
        Student.StudentCount +=1
    def displayCount(self):
        print("Total Students:", Student.StudentCount)
    def display(self):
        print("Student Information:")
        Sindhuja.display(self)
        print("Student ID: ",self.student_id)
class Librarian(Sindhuja):
    StudentCount = 0
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.employee_id = employee_id
    def display(self):
        print("Employee Information:")
        Sindhuja.display(self)
        print("Employee ID: ",self.employee_id)
class Book():
    def __init__(self, bname, author, book_id):
        self.book_name = bname
        self.author = author
        self.book_id = book_id
    def display(self):
        print("Book Information")
        print("Book Name: ", self.book_name)
        print("Author: ", self.author)
        print("Book ID: ", self.book_id)
class Borrow_Book(Student, Book):
    def __init__(self, name, email, student_id, bname, author, book_id):
        Student.__init__(self, name, email, student_id)
        Book.__init__(self, bname, author, book_id)
    def display(self):
        print("Borrowed Book Details:")
        Student.display(self)
        Book.display(self)
list1= []
list1.append(Student('Ratnavalli', 'rad4n@gmail.com', 36))
list1.append(Student('Raji', 'rajee@gmail.com', 13))
list1.append(Librarian('PAVAN', 'daddy@gmail.com', 79))
list1.append(Librarian('JAKKEPALLI', 'jack@gmail.com', 47))
list1.append(Book('PYTHON', 'UDEMY', 90))
list1.append(Book('HADOOP', 'OReily', 8))
list1.append(Borrow_Book('UNIVERSE', 'universe@gmail.com', 404, 'PYTHON', 'UDEMY', 90))
for obj, item in enumerate(list1):
    item.display()
    print("\n")
    if obj == len(list1)-1:
        item.displayCount()