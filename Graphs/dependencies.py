class Task:
    def __init__(self, name, dependencies_argument):   
        self.name = name
        self.dependencies = {}
        for dependency in dependencies_argument:
            dependencies[dependency] = True
        

class Dependency:
    def __init__(self, task, depends_on):
        self.task = task
        self.depends_on = depends_on

def complete(task, t_list):
    
    print("___________________")
    
    print("Completing task: " + str(task.name))
    

    for i in range(0, len(t_list)):
        print(len(t_list))
        if t_list[i].name == task.name:
            del t_list[i]
            break



    print("_____________________")
    

    for temp_task in t_list:
        if task.name in temp_task.dependencies:
            print("deleting: " + str(task.name) + " from : " + str(temp_task.name))
            print(temp_task.dependencies)
            del temp_task.dependencies[task.name]
            print(temp_task.dependencies)

    

def taskAvailable(t_list):
    for task in t_list:
        if len(task.dependencies) == 0:
            return True
    
    return False



list_of_tasks = []
list_of_tasks.append(Task('a', []))
list_of_tasks.append(Task('b', []))
list_of_tasks.append(Task('c', []))
list_of_tasks.append(Task('d', []))
list_of_tasks.append(Task('e', []))
list_of_tasks.append(Task('f', []))
list_of_dependencies = []
list_of_dependencies.append(Dependency('d','a'))
list_of_dependencies.append(Dependency('b','f'))
list_of_dependencies.append(Dependency('d','b'))
list_of_dependencies.append(Dependency('a','f'))
list_of_dependencies.append(Dependency('c','d'))

for dependency in list_of_dependencies:
    for task in list_of_tasks:
        if dependency.task == task.name:
            task.dependencies[dependency.depends_on] = True

order = []

while len(list_of_tasks) > 0 and taskAvailable(list_of_tasks):
    for task in list_of_tasks:
        if len(task.dependencies) == 0:
            complete(task, list_of_tasks)
            order.append(task.name)

print(order)
if len(list_of_tasks) == 0:
    print(order)
else:
    print("error")
            
