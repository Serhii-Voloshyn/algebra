from task_88a import task_88a
from task_88b import task_88b
from task_322 import task_322


def main():

    try:

        # User's input
        task_number = input("Enter task number (like 88b): ")

        # Check if there is that task number
        assert task_number in ["88a", "88b", "322"], "There is no such task number"

        # Run specific task
        if task_number == "88a":
            task_88a()
        elif task_number == "88b":
            task_88b()
        elif task_number == "322":
            task_322()

    # If user's input is invalid
    except ValueError:

        print("Wrong input!")


if __name__ == "__main__":
    main()
