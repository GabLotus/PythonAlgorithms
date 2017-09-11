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
    for i in range(0, len(t_list)):
        if t_list[i].name == task.name:
            del t_list[i]
            break
    for temp_task in t_list:
        if task.name in temp_task.dependencies:
            del temp_task.dependencies[task.name]

def taskAvailable(t_list):
    for task in t_list:
        if len(task.dependencies) == 0:
            return True
    
    return False

def getProjectSchedule(t_list, order):
    while len(t_list) > 0 and taskAvailable(t_list):
        for task in t_list:
            if len(task.dependencies) == 0:
                complete(task, t_list)
                order.append(task.name)
    if len(t_list) > 0:
        return False
    else:
        return True

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

if getProjectSchedule(list_of_tasks, order):
    print(order)
else:
    print("error")
            
