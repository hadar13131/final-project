from project.client import Client
import json
import re

from datetime import datetime

def is_numeric(value):
    if isinstance(value, (int, float)):
        return True

    # elif value == "":
    #     return True

    elif isinstance(value, str):
        return value.replace('.', '', 1).isdigit() or (value.count('.') == 1 and value.replace('.', '').isdigit())

    else:
        return False

def check_workoutname(client: Client, workout_name, date) -> bool:
    workoutlst = client.user_workout_lst

    for i in workoutlst:
        date1 = datetime.strptime(i[3], '%Y-%m-%dT%H:%M:%S')
        if date1 == date:
            if i[2] == workout_name:
                return False

    return True


def check_exercisename(client: Client, workout_name, date, exercise_name) -> bool:
    workoutlst = client.user_workout_lst

    if not workoutlst:
        return True

    w = workoutlst[0]

    for i in workoutlst:
        date1 = datetime.strptime(i[3], '%Y-%m-%dT%H:%M:%S')
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


def is_valid_phone_number(phone_number: str) -> bool:

    # Check if the phone number starts with "05" and has exactly 10 digits
    if phone_number.startswith("05") and len(phone_number) == 10 and phone_number.isdigit():
        return True
    else:
        return False


def str_is_int(value):
    if isinstance(value, int):
        return True

    # elif value == "":
    #     return True

    elif isinstance(value, str):
        return value.isdigit()

    else:
        return False

def check_int_type(value):
    return isinstance(value, int)

def check_float_type(value):
    return isinstance(value, float)

