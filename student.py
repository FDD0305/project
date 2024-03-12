filename= "student.txt"
import os

def main():
    while True:
        menu()
        choice=int(input('请选择序号:'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗y/n')
                if answer=='y'or answer=='Y':
                    print('谢谢您的使用')
                    break
                else:
                       continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
def insert ():
    student_list=[]
    while True:
        id=input('请输入学生号码')
        if not id:
            break
        name=input('请输入学生姓名')
        if not name:
            break
        try:
            math=int(input('请输入数学成绩：'))
            C=int(input('请输入C语言成绩：'))
        except:
            print('输入无效，请重新输入')
            continue
        student={'id':id,'name':name,'math':math,'C':C}
        student_list.append(student)
        answer=input('是否继续添加y/n')
        if answer=='y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完毕!!!')
def save(list):
    try:
        student_txt=open(filename,'a',encoding='utf-8')
    except:
        student_txt=open(filename,'w',encoding='utf-8')
    for item in list:
     student_txt.write(str(item)+'\n')
     student_txt.close()
def search():
    pass
def delete():
    while True:
        student_id=input('要删除的学生id:')
        if student_id:
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8')as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到{student_id}')
            else:
                print('无学生信息')
                break
            show()
            answer=input('是否继续删除?y/n\n')
            if answer=='y':
                continue
            else:
                break
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改的学员id:')
    if student_id:
        with open(filename,'w',encoding='utf-8') as wfile:
            for item in student_old:
                d=dict(eval(item))
                if d['id']==student_id:
                    print('找到学生信息，可以修改他的相关信息了!')
                    while True:
                        try:
                            d['name']=input('请输入姓名')
                            d['C']=input('请输入C语言成绩')
                            d['math']=input('请输入数学成绩')
                        except:
                            print('您的输入有误，请重新输入')
                    wfile.write(str(d)+'\n')
                    print('修改成功！！！')
                else:
                    wfile.write(str(d)+'\n')
            answer=input('是否修改其他学生信息？y/n\n')
            if answer=='y':
                modify()




    else:
        print('无学生信息')
def sort():
    pass
def total():
    pass
def show():
    pass
def menu():
    print('------------------------------学生信息管理系统-------------------------------------------------')
    print('=============================================================================================')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示学生所有信息')
    print('\t\t\t\t\t\t0.退出')
    print('----------------------------------------------------------------------------------------------')

if __name__=='__main__':
    main()



