
tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_tasks(list):
    uncompleted_tasks = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks
    
print(uncompleted_tasks(tasks))

def completed_tasks(list):
    completed_tasks = []
    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks
    
print(completed_tasks(tasks))

def task_descriptions(list):
    describe_task = []
    for task in list:
         describe_task.append(task["description"])
    return describe_task
    
print(task_descriptions(tasks))

def task_time(list):
    timely_tasks = []
    for task in list:
        if task["time_taken"] >= 10:
            timely_tasks.append(task)
    return timely_tasks

print(task_time(tasks))

def given_description(list, description):
    task_given = []
    for task in list:
        if task["description"] == description:
            task_given.append(task)
    return task_given

print(given_description(tasks, "Wash Dishes"))
