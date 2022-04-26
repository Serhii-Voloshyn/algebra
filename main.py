"""Main menu of application."""

from tasks import task_88a, task_88b, task_322


def main():
    """Main menu implementation."""
    # key - task number
    # value - tuple of module name and number of arguments in run()
    tasks = {"88a": (task_88a.task_88a, 1), "88b": (task_88b.task_88b, 1), "322": (task_322.task_322, 0)}
    try:
        # User's input
        task_number = input("Enter task number (like 88b): ")
        print(tasks[task_number][0].__doc__)
        args = [int(input("Enter number: ")) for arg in range(tasks[task_number][1])]
        print(f"Result: {tasks[task_number][0](*args)}")
    # If user's input is invalid
    except ValueError:
        print("Wrong input!")
    except KeyError:
        print("There is no such task number")


if __name__ == "__main__":
    main()
