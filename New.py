class data:
    name = None
    lastname = None
    brithday = None
    age = None
    grad = None
    id = None

    def __init__(self,ID=None,NAME = None,lastname = None,brithday = None,age = None,grad = None):
        self.id = ID
        self.name = NAME
        self.lastname = lastname
        self.brithday = brithday
        self.age = age
        self.grad = grad
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
        out.close()
    pass

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.id,self.name,self.lastname,self.brithday,self.age,self.grad)

class Student(object):

    Data = []
    def __init__(self):
        pass

    def input_student(self):
        return self.Data
    pass


def format_data(ID,NAME,LASTNAME,BRITHDAY,AGE,GARD):
    s = Student()
    p1 = (ID,NAME,LASTNAME,BRITHDAY,AGE,GARD)
    s.Data.append(p1)
    big_data.append(p1)
    print(s.input_student())

def import_data():
    ID = str(input("กรอกรหัสนักเรียน"))
    NAME = str(input("กรอกรายชื่อนักเรียน"))
    LASTNAME = str(input("กรอกนามสกุล"))
    BRITHDAY = str(input("กรอกวัน/เดือน/ปี"))
    AGE = str(input("กรอกอายุ"))
    GARD = str(input("กรอกเกรด"))
    return format_data(ID, NAME, LASTNAME, BRITHDAY, AGE, GARD)
big_data = []
while(1):
    menu = int(input("ข้อมูลนักเรียน\nกดเมนูเพื่อเเข้าใช้งาน\nกด1.เพิ่มข้อมูลนักเรียน\nกด2.แก้ไขข้อมูลนักเรียน\nกด3.ลบข้อมูลนักเรียน"))
    if menu == 1:
        num = int(input("กรอกจำนวนนักเรียน"))
        for c in range(num):
            import_data()
    elif menu == 0 :
        for i in range(len(big_data)):
            for n in range(len(big_data[i])):
                out = open("outstudent.txt", "a", encoding="utf8")
                out.write(str(big_data[i][n]))
                out.write(" ")
            out.write('\n')
            out.close()

#แก้ไขข้อมูล ลบข้อมูล