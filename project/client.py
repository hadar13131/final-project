import json

import requests
import sqlite3
from project.models import Set, Exercise, Workout
from datetime import datetime

import project.api

class Client:
    def __init__(self):
        self.server_address = "http://127.0.0.1:1234"
        self.username = None
        self.password = None
        self.first_name = None
        self.user_exer_lst = []
        self.user_workout_lst = []


    def authenticate2(self, email, name, password):
        credentials = dict(email=email, name=name, password=password)

        response = requests.get(
            f"{self.server_address}/authenticate2",
            params=credentials
        )

        if response.json()["response"] == "user authenticated":
            self.username = name
            self.password = password
            self.first_name = self.find_first_name(userid=self.username)["response"]
            self.user_workout_lst = self.lst_of_workouts_by_username(userid=self.username)["response"]
            self.user_exer_lst = self.lst_of_exercise_names(userid=self.username)["response"]

        return response.json()

    def find_first_name(self, userid):
        credentials = dict(userid=userid)

        response1 = requests.get(
            f"{self.server_address}/find_first_name",
            params=credentials
        )

        return response1.json()

    def lst_of_workouts_by_username(self, userid):
        credentials = dict(userid=userid)

        response1 = requests.get(
            f"{self.server_address}/lst_of_workouts_by_username",
            params=credentials
        )

        return response1.json()

    def lst_of_exercise_names(self, userid):
        credentials = dict(userid=userid)

        response1 = requests.get(
            f"{self.server_address}/lst_of_exercise_names",
            params=credentials
        )

        return response1.json()



    def check_email(self, email):
        credentials = dict(email=email)

        response = requests.get(
            f"{self.server_address}/check_email",
            params=credentials
        )
        return response.json()

    def signup(self, name, password):
        self.username = name
        self.password = password
        self.user_workout_lst = []
        self.user_exer_lst = []

        credentials = dict(name=name, password=password)

        response = requests.get(
            f"{self.server_address}/signup",
            params=credentials
        )
        return response.json()

    def fill_info(self, name, first_name, last_name, phone_num, email, age, gender, goals):

        self.first_name = first_name
        # username8 = self.username
        credentials = dict(name=name, first_name=first_name, last_name=last_name, phone_num=phone_num,
                           email=email, age=age, gender=gender, goals=goals)

        response = requests.get(
            f"{self.server_address}/fill_info",
            params=credentials
        )

        return response.json()

    def delete(self, name, password):
        credentials = dict(name=name, password=password)

        response = requests.get(
            f"{self.server_address}/delete",
            params=credentials
        )
        return response.json()

    def signout(self, name, password):
        credentials = dict(name=name, password=password)

        response = requests.get(
            f"{self.server_address}/signout",
            params=credentials
        )
        return response.json()

    def addworkout(self, userid, workout_name, date, exerciselist):
        credentials = dict(userid=userid, workout_name=workout_name, date=date, exerciselist=exerciselist)

        response = requests.get(
            f"{self.server_address}/addworkout",
            params=credentials
        )

        self.user_workout_lst = self.lst_of_workouts_by_username(self.username)["response"]

        return response.json()


    def deleteworkout(self, userid, workout_name, date):
        credentials = dict(userid=userid, workout_name=workout_name, date=date)

        response = requests.get(
            f"{self.server_address}/deleteworkout",
            params=credentials
        )

        self.user_workout_lst = self.lst_of_workouts_by_username(self.username)["response"]

        return response.json()


    def addexercisetoworkout(self, userid, date, workout_name, exercise):
        credentials = dict(userid=userid, date=date, workout_name=workout_name, exercise=exercise)


        response = requests.get(
            f"{self.server_address}/addexercisetoworkout",
            params=credentials
        )
        exercise2 = json.loads(exercise)
        self.user_exer_lst.append(exercise2["name"])

        self.user_workout_lst = self.lst_of_workouts_by_username(self.username)["response"]

        return response.json()


    def deletexercisefromworkout(self, userid, exercise):
        credentials = dict(userid=userid, exercise=exercise)

        response = requests.get(
            f"{self.server_address}/deletexercisefromworkout",
            params=credentials
        )
        return response.json()

    def addsettoexercise(self, userid, date, workout_name, exercise, sets):
        credentials = dict(userid=userid, date=date, workout_name=workout_name, exercise=exercise, sets=sets)

        response = requests.get(
            f"{self.server_address}/addsettoexercise",
            params=credentials
        )

        self.user_workout_lst = self.lst_of_workouts_by_username(self.username)["response"]
        return response.json()

    def addsettoexercise2(self, userid, date, workout_name, exercise_name, power, sets):
        credentials = dict(userid=userid, date=date, workout_name=workout_name, exercise_name=exercise_name,
                           power=power, sets=sets)

        response = requests.get(
            f"{self.server_address}/addsettoexercise2",
            params=credentials
        )

        self.user_workout_lst = self.lst_of_workouts_by_username(self.username)["response"]
        return response.json()

    def showimprovement(self, userid: str, exercise_name: str, s_date: datetime, e_date: datetime):
        credentials = dict(userid=userid, exercise_name=exercise_name, s_date=s_date, e_date=e_date)

        response = requests.get(
            f"{self.server_address}/showimprovement",
            params=credentials
        )
        return response.json()
    def showimprovement2(self, userid: str, exercise_name: str, s_date: datetime, e_date: datetime):
        credentials = dict(userid=userid, exercise_name=exercise_name, s_date=s_date, e_date=e_date)

        response = requests.get(
            f"{self.server_address}/showimprovement2",
            params=credentials
        )
        return response.json()

    def improve_with_params(self, userid: str, exercise_name: str, s_date: datetime, e_date: datetime):
        credentials = dict(userid=userid, exercise_name=exercise_name, s_date=s_date, e_date=e_date)

        response = requests.get(
            f"{self.server_address}/improve_with_params",
            params=credentials
        )
        return response.json()

    def improve_with_params2(self, userid: str, exercise_name: str, s_date: datetime, e_date: datetime):
        credentials = dict(userid=userid, exercise_name=exercise_name, s_date=s_date, e_date=e_date)

        response = requests.get(
            f"{self.server_address}/improve_with_params2",
            params=credentials
        )
        return response.json()

    def bring_info(self, name):
        credentials = dict(name=name)

        response = requests.get(
            f"{self.server_address}/bring_info",
            params=credentials
        )

        return response.json()

