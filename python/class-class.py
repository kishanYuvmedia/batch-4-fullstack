class Project:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def display(self):
        print(f"Project Name: {self.name}")
        print(f"Cities: {', '.join(self.city)}")
    
    class Task:
        def __init__(self, title, description):
            self.title = title
            self.description = description

        def display_task(self):
            print(f"Task Title: {self.title}")
            print(f"Description: {self.description}")

project1=Project("Website Redesign", ["New York", "Los Angeles", "Chicago"])
project1.display()

task1=Project.Task("Design Mockups", "Create design mockups for the new website.")
task1.display_task()