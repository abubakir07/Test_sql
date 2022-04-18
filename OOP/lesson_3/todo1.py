class Todoitem:
    def __init__(self,stroka):
        self.stroka=stroka
        self.is_done=False

    def check(self):
        self.is_done=True
    def uncheck(self):
        self.is_done=False

class Todo:
    todo_items=[]
    def add_todo(self,item):
        self.todo_items.append(item.stroka)

    def list_items(self):
        return self.todo_items

    def find(self,word):
        for i in self.todo_items:
            if word in i:
                a=[]
                a.append(f'{self.todo_items.index(i)},{i}')
                print(tuple(a))

# todo1=Todoitem('Read book')
# todo2=Todoitem('Do homework book')
# todo3=Todoitem('Play games')
# todo=Todo()
# todo.add_todo(todo1)
# todo.add_todo(todo2)
# todo.add_todo(todo3)
# print(todo.list_items())
# todo.find('book')

def run():
    dct={
        1:'Add Todo',
        2:'Add todo to list',
        3:'Show items',
        4:'Find',
        5:'Stop'
    }#menu

    todo=Todo()#Ekzemplyar
    notdone=[]#Не сделаные дела
    finish=[]#Сделаные дела
    objects=[]#Добавление Ekzemplyar

    while True:
        print(dct)
        command=int(input('Enter command: '))
        if command==1:
            stroka=input('Enter todo: ')
            done=bool(int(input('Enter 1,0 True or False: ')))

            todo1tem=Todoitem(stroka)# Ekzemplyar
            if done==True:
                todo1tem.check()
            else:
                todo1tem.uncheck()

            todoitem={}# k eto todoitem v eto proverka
            todoitem[todo1tem.stroka]=todo1tem.is_done
            if todo1tem.is_done==False:
                notdone.append(todoitem)#list Ekzemplyarov
            else:
                finish.append(todoitem)
            objects.append(todo1tem)

        elif command==2:
            for i in objects:
                todo.add_todo(i)


        elif command==3:
            print(f'List of todo{todo.list_items()}\n to do:{notdone}\nfinished:{finish}')

        elif command==4:
            word=input('Enter letter: ')
            todo.find(word)
        elif command==5:
            print('Работа завершена')
            break
        else:
            print('error')
            
print(run())