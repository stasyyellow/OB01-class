# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

#class Task(self, description, deadline, status(competed/not completed)):

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

def add_task(tasks, description, deadline):
    task = Task(description, deadline)
    tasks.append(task)

def display_current_tasks(tasks):
    print("Current tasks:")
    for task in tasks:
        if not task.completed:
            print(f"- {task.description} (Deadline: {task.deadline})")

tasks = []

add_task(tasks, "Подготовить отчет", "10.04.2024")
add_task(tasks, "Провести встречу", "15.04.2024")

# Помечаем задачу как выполненную
tasks[0].mark_as_completed()

# Выводит текущие задачи (не выполненные)

display_current_tasks(tasks)
print(' ')

add_task(tasks, "Написать email клиенту, Иван Иванов, выполнить заказ к маю", "01.05.2024")
display_current_tasks(tasks)
print(' ')

tasks[2].mark_as_completed()
display_current_tasks(tasks)
