class Node :
    data =None 
    nextNode = None
    
    def __init__(self,data = None,nextNode = None):
        self.data = data
        self.nextNode = None


class LinkList :
    head = None

    def __init__(self,head = None) :
        self.head = head
        
    def additem(self,item): #add node
        newNode = Node(item)
        newNode.nextNode = self.head
        self.head = newNode
        
    def Traversal(self): #print Node
        tmp = self.head
        while(tmp != None):
            print(tmp.data)
            tmp =tmp.nextNode
            
    def insertAfter(self,key,itemToinsert): #insertNode
        tmp =self.head
        while(tmp != None and tmp.data != key):
            tmp = tmp.nextNode
        
        if(tmp != None):
            newNode = Node(itemToinsert)
            newNode.nextNode = tmp.nextNode
            tmp.nextNode =newNode
            
    def insertBefore(self,key,itemToinsert):
        prev =None
        cur = self.head
        while(cur != None and cur.data != key):
            prev = cur
            cur =cur.nextNode
        if(cur == self.head):
            self.additem(itemToinsert)
        elif(cur != None):
            newNode = Node(itemToinsert)
            newNode.nextNode = cur
            prev.nextNode = newNode
            
    def deleteNode(self,key):
        if self.head == None:
            pass
        elif self.head.data == key:
            tmp = self.head
            self.head =self.head.nextNode
            del tmp
        else:
            cur = self.head
            prev =None
            
            while cur != None and cur.data != key :
                prev =cur
                cur = cur.nextNode
                
            if cur == None :
                print("cannot Delete")
                return
            prev.nextNode = cur.nextNode
            del cur

    def useNode(self):
        n = 1
        tmp = self.head
        while(tmp != None):
            print(n,tmp.data)
            tmp = tmp.nextNode
            n += 1

    def Use_Node(self):
        num = int(input())
        c = 1
        tmp = self.head
        while(c != num):
            tmp = tmp.nextNode
            c += 1
        print(tmp.data)
        if c == num :
            while(1):
                choice = int(input("1.แก้ไขชื่อ\n2.แก้ไขนามสกุล\n3.แก้ไขรหัสนักเรียน\n4.แก้ไขวันเกิด\n5.แก้ไขอายุ\n6.แก้ไขเกรด"))
                if choice == 1:
                    newname = str(input())
                    tmp.data["Name"] = newname
                    print(tmp.data)
                elif choice == 2:
                    newlastname = str(input())
                    tmp.data["Lastname"] = newlastname
                    print(tmp.data)
                elif choice == 3:
                    newid = str(input())
                    tmp.data["ID"] = newid
                    print(tmp.data)
                elif choice == 4:
                    newbrithday = str(input())
                    tmp.data["Brithday"] = newbrithday
                    print(tmp.data)
                elif choice == 5:
                    newage = str(input())
                    tmp.data["Age"] = newage
                    print(tmp.data)
                elif choice == 6:
                    newgrad = str(input())
                    tmp.data["Grad"] = newgrad
                    print(tmp.data)
                elif choice == 0:
                    self.Use_Node()

class Student:
    name = None
    lastname = None
    brithday = None
    age = None
    grad = None
    ID = None

    def __init__(self):
        self.ID = ""
        self.name = ""
        self.lastname = ""
        self.brithday = ""
        self.age = 0
        self.grad = 0

    def dataStudent(self):
        data = {
            "ID":[[self.ID]],
            "Name": [[self.name]],
            "Lastname":[[self.lastname]],
            "Brithday":[[self.brithday]],
            "Age":[[self.age]],
            "Grad":[[self.grad]]
        }
        return data

def savedata(data):
    student = LinkList()
    student.Traversal()
def editstudent():
    student = LinkList()
    student.Use_Node()
    student.Traversal()

def addstudent():
    student = Student()
    student.ID = str(input("กรอกรหัสนักเรียน"))
    student.name = str(input("กรอกรายชื่อนักเรียน"))
    student.lastname = str(input("กรอกนามสกุล"))
    student.brithday = str(input("กรอกวัน/เดือน/ปี"))
    student.age = str(input("กรอกอายุ"))
    student.grad = str(input("กรอกเกรด"))
    return student.dataStudent()
while(1):
    menu = int(input("ข้อมูลนักเรียน\nกดเมนูเพื่อเเข้าใช้งาน\nกด1.เพิ่มข้อมูลนักเรียน\nกด2.แก้ไขข้อมูลนักเรียน\nกด3.ลบข้อมูลนักเรียน"))
    if menu == 1:
        savedata(addstudent())

    elif menu == 2:
        editstudent()



'''
L = LinkList()
node1 = Node(a.addStudent())
node2 = Node(b.addStudent())

L.head = node1
node1.nextNode = node2

L.Traversal()
L.useNode()
L.Use_Node()
'''
#เมนูเพิ่มแก้ไขลบ
#exportข้อมูล


