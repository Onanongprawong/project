class Student :

    Data = []
    key = None
    def __init__(self,DATA):
        self.Data.append(DATA)

    def insert_student(self,key,newDATA):
        self.Data.insert(key,newDATA)
    def delete_student(self,key):
        self.Data.remove(key)
    def _student(self):
        return self.Data


class data:
    name = None
    lastname = None
    brithday = None
    age = None
    grad = None
    id = None

    def __init__(self,ID=None,NAME = None,LASTNAME = None,BRITHDAY = None,AGE = None,GRAD = None):
        self.id = ID
        self.name = NAME
        self.lastname = LASTNAME
        self.brithday = BRITHDAY
        self.age = AGE
        self.grad = GRAD
        '''
        out = open("datastudent.txt", "a", encoding="utf8")
        out.write(self.id)
        out.write(" ")
        out.write(self.name)
        out.write(" ")
        out.write(self.lastname)
        out.write(" ")
        out.write(self.brithday)
        out.write(" ")
        out.write(self.age)
        out.write(" ")
        out.write(self.grad)
        out.write(" ")
        out.write("\n")
        out.close()'''
    pass

    def import_data(self):
        self.id = str(input("กรอกรหัสนักเรียน"))
        self.name = str(input("กรอกรายชื่อนักเรียน"))
        self.lastname = str(input("กรอกนามสกุล"))
        self.brithday = str(input("กรอกวัน/เดือน/ปี"))
        self.age = str(input("กรอกอายุ"))
        self.grad = str(input("กรอกเกรด"))
        tmp = (self.id,self.name,self.lastname,self.brithday,self.age,self.grad)
        tmp = Student(tmp)
        print(tmp._student())

    def read_data(self):
        for i in range(len(Student.Data)):
            print([i+1]," : ",Student.Data[i])
    def delete_data(self,key):
        tmp = Student.delete_student(Student,Student.Data[key+1])

    def insert_data(self,key):
        self.id = str(input("กรอกรหัสนักเรียน"))
        self.name = str(input("กรอกรายชื่อนักเรียน"))
        self.lastname = str(input("กรอกนามสกุล"))
        self.brithday = str(input("กรอกวัน/เดือน/ปี"))
        self.age = str(input("กรอกอายุ"))
        self.grad = str(input("กรอกเกรด"))
        dd = (self.id, self.name, self.lastname, self.brithday, self.age, self.grad)
        tmp = Student.insert_student(Student,key,dd)
        self.delete_data(key)

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.id,self.name,self.lastname,self.brithday,self.age,self.grad)






big_data = []
while(1):
    income = data()

    menu = int(input("ข้อมูลนักเรียน\nกดเมนูเพื่อเเข้าใช้งาน\nกด1.เพิ่มข้อมูลนักเรียน\nกด2.แก้ไขข้อมูลนักเรียน\nกด3.ลบข้อมูลนักเรียน\nกด0.ส่งออกข้อมูลและจบโปรแกรม"))
    if menu == 1:
        num = int(input("กรอกจำนวนนักเรียน"))
        for c in range(num):
            income.import_data()
    elif menu == 0 :
        for i in range(len(Student.Data)):
            for n in range(len(Student.Data[i])):
                out = open("outstudent.txt", "a", encoding="utf8")
                out.write(str(Student.Data[i][n]))
                out.write(" ")
            out.write('\n')
            out.close()
        exit(0)
    elif menu == 2 :
        income.read_data()
        n = int(input('ลำดับนักเรียนที่ต้องการแก้ไข'))
        income.insert_data(n-1)
    elif menu == 3 :
        income.read_data()
        n = int(input('ลำดับนักเรียนที่ต้องการลบ'))
        income.delete_data(n-2)

#แก้ไขข้อมูล ลบข้อมูล