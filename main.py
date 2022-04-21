from tasks.task_88a import task_88a
from tasks.task_88b import task_88b
from tasks.task_322 import task_322


def main():

    tasks = {"88a":task_88a, "88b":task_88b, "322":task_322}

    try:

        # User's input
        task_number = input("Enter task number (like 88b): ")

        tasks[task_number]()

    # If user's input is invalid
    except ValueError:
        print("Wrong input!")

    except KeyError:
        print("There is no such task number")


if __name__ == "__main__":
    main()
