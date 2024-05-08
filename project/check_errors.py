from project.client import Client
import json
import re

def is_numeric(value):
    if isinstance(value, (int, float)):
        return True

    elif isinstance(value, str):
        return value.replace('.', '', 1).isdigit() or (value.count('.') == 1 and value.replace('.', '').isdigit())

    else:
        return False

def check_workoutname(client: Client, workout_name, date) -> bool:
    workoutlst = client.user_workout_lst

    for i in workoutlst:
        date1 = i[3]
        if date1 == date:
            if i[2] == workout_name:
                return False

    return True


def check_exercisename(client: Client, workout_name, date, exercise_name) -> bool:
    workoutlst = client.user_workout_lst

    w = workoutlst[0]

    for i in workoutlst:
        date1 = i[3]
        if date1 == date:
            if i[2] == workout_name:
                w = i
                break

    exercise_lst = w[4]
    if exercise_lst == "":
        return True

    ex = json.loads(exercise_lst[0])
    for e in exercise_lst:
        e1 = json.loads(e)
        if exercise_name == e1["name"]:
            return False


    return True


def is_valid_email(email: str) -> bool:
    # Regular expression pattern for validating email addresses
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Use the re.match function to check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

