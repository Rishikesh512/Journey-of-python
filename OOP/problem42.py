class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
        else:
            print("Invalid task number")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task number")

    def show_tasks(self):
        print("\nTasks:")
        for i, t in enumerate(self.tasks):
            status = "✔" if t["done"] else "✘"
            print(f"{i}. {t['task']} [{status}]")


t = Todo()
t.add_task("Study Python")
t.add_task("Do Exercise")

t.complete_task(0)
t.show_tasks()

