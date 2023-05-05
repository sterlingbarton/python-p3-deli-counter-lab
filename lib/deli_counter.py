# people = ["Logan", "Avi", "Spencer"]


def line(people):
    if len(people):
        line_list = f"The line is currently:"
        for i in range(len(people)):
            line_list += f" {i + 1}. {people[i]}"
        print(line_list)
    else:
        print("The line is currently empty.")


def take_a_number(people, str):
    people.append(str)
    print(f"Welcome, {str}. You are number {len(people)} in line.")


# print(take_a_number(people, "Peter"))


def now_serving(people):
    if len(people):
        print(f"Currently serving {people.pop(0)}.")
    else:
        print("There is nobody waiting to be served!")
