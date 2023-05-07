import datetime
import pickle


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: {self.cost_estimate}, completion: {self.percent_complete}%"

    def __repr__(self):
        return f"{self.priority} {self.name}"


def load_projects(file_name):
    with open(file_name, 'rb') as file:
        return pickle.load(file)


def save_projects(projects, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(projects, file)


def display_projects(projects):
    incomplete = sorted([p for p in projects if p.percent_complete < 100], key=lambda p: p.priority)
    complete = sorted([p for p in projects if p.percent_complete == 100], key=lambda p: p.priority)
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


def filter_projects_by_date(projects):
    date_string = input("Enter the start date in the format dd/mm/yyyy: ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > date]
    filtered_projects.sort(key=lambda p: p.start_date)
    print("Filtered projects:")
    for p in filtered_projects:
        print(f"  {p}")


def add_new_project(projects):
    name = input("Enter the name of the project: ")
    start_date_string = input("Enter the start date of the project in the format dd/mm/yyyy: ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Enter the priority of the project: "))
    cost_estimate = input("Enter the cost estimate for the project: ")
    percent_complete = int(input("Enter the percent complete for the project: "))
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))
    print("Project added successfully.")


def update_project(projects):
    print("Choose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    percent_complete_str = input(f"New Percentage (current: {project.percent_complete}%): ")
    if percent_complete_str:
        project.percent_complete = int(percent_complete_str)
    priority_str = input(f"New Priority (current: {project.priority}): ")
    if priority_str:
        project.priority = int(priority_str)
    print("Project updated successfully.")


def main():
    filename = input("Enter data file name: ")
    projects = load_projects(filename)
    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (Q)uit")
        choice = input("Enter choice: ")
        if choice == "L":
            filename = input("Enter data file name: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Enter data file name: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "Q":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()



