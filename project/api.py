# api.py
import json
import sqlite3
import hashlib
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Table, Column, create_engine, MetaData, String, Boolean, INTEGER, JSON, update, DateTime
from sqlalchemy.orm.session import sessionmaker
from models import Set, Exercise
from datetime import datetime

app = FastAPI(docs_url="/")

engine = create_engine("sqlite:///./database1.db")

md = MetaData()

Session = sessionmaker(bind=engine)

# create table to save users information
user_table = Table(
    "user_tb", md,
    Column("name", String, primary_key=True),
    Column("password", String),
    Column("first_name", String),
    Column("last_name", String),
    Column("phone_num", String),
    Column("email", String),
    Column("age", INTEGER),
    Column("gender", String),
    Column("goals", String)
)

md.create_all(engine)

# create table to save workouts information
workout_table = Table(
    "workouts", md,
    Column("workoutid", INTEGER, primary_key=True),
    Column("userid", String),
    Column("workout_name", String),
    Column("date", DateTime),
    Column("exerciselist", JSON)
)

md.create_all(engine)


# to hash the password
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def lst_of_workouts_by_username(username: str):
    session = Session()
    # find = []
    find = session.query(workout_table).filter(workout_table.c.userid == username).all()
    # find.append(session.query(workout_table).filter(workout_table.c.userid == username).all())  # filter by userid, get lst of workouts
    return find


def lst_of_exercise_names(username: str):
    session = Session()
    find = session.query(workout_table).filter(workout_table.c.userid == username).all()  # filter by userid, get lst of workouts
    lst = []
    for f in find:
        n = f[4]
        for i in n:
            n2 = json.loads(i)
            lst.append(n2["name"])
    return lst

def find_first_name(username: str) -> str:
    session = Session()
    find = session.query(user_table).filter(user_table.c.name == username).first()
    return find[2]


@app.get("/signup")
def signup(name: str, password: str) -> dict[str, str]:
    session = Session()

    # check if the username is avilable - every user should have diffrent username
    if session.query(user_table).filter_by(name=name).first():
        return {"response": "the username not valid"}

    session.execute(
        user_table.insert().values(
            name=name, password=hash_password(password),
            first_name="",
            last_name="",
            phone_num="",
            email="",
            age="",
            gender="",
            goals=""
        )
    )
    session.commit()

    return {"response": "signup success"}


# end signup

@app.get("/fill_info")
def fill_info(name: str, first_name: str, last_name: str, phone_num: str, email: str, age: int, gender: str,
              goals: str) -> dict[str, str]:

    session = Session()
    # if session.query(user_table).filter_by(name=name).first():
    # find = session.query(user_table).filter_by(name=username).first()

    find = session.query(user_table).filter(user_table.c.name == name).first()

    if find is not None:
        stmt = update(user_table).where(user_table.c.name == name).values(
            first_name=first_name,
            last_name=last_name,
            phone_num=phone_num,
            email=email,
            age=age,
            gender=gender,
            goals=goals
        )

        session.execute(stmt)

        session.commit()
        return {"response": "the information added"}

    return {"response": "the user doesnt exist"}


@app.get("/signout")
def signout(name: str, password: str) -> dict[str, str]:
    session = Session()

    users = session.execute(user_table.select())

    password_hash = hash_password(password)

    for user in users:
        # Check if the username and password match
        if user.name == name and user.password == password_hash:
            session.execute(
                user_table.delete().where(
                    user_table.c.name == name and
                    user_table.c.password == password_hash
                )
            )

            session.commit()

            return {"response": "sign out success"}

    return {"response": "user data not found"}

    # if (name, password_hash) in users:
    #     session.execute(
    #         user_table.delete().where(
    #             user_table.c.name == name and
    #             user_table.c.password == password_hash
    #         )
    #     )
    #
    #     session.commit()
    #
    #     return {"response": "signout success"}
    #
    # return {"response": "user data not found"}


# end signuout


@app.get("/delete")
def delete(name: str, password: str) -> dict[str, str]:
    session = Session()

    users = session.execute(user_table.select())

    password_hash = hash_password(password)

    for user in users:
        # Check if the username and password match
        if user.name == name and user.password == password_hash:
            session.execute(
                user_table.delete().where(
                    user_table.c.name == name and
                    user_table.c.password == password_hash
                )
            )

            session.commit()

            return {"response": "delete success"}

    return {"response": "user data not found"}

    # if (name, password_hash) in users:
    #     session.execute(
    #         user_table.delete().where(
    #             user_table.c.name == name and
    #             user_table.c.password == password_hash
    #         )
    #     )
    #
    #     session.commit()
    #
    #     return {"response": "delete success"}
    #
    # return {"response": "user data not found"}


# end delete


@app.get("/authenticate")
def authenticate(name: str, password: str) -> dict[str, str]:
    session = Session()

    users = session.execute(user_table.select())
    password_hash = hash_password(password)

    for user in users:
        # Check if the username and password match
        if user.name == name and user.password == password_hash:
            return {"response": "user authenticated"}

    return {"response": "user data not found"}

# end authenticate

@app.get("/authenticate2")
def authenticate2(email: str, name: str, password: str) -> dict[str, str]:
    session = Session()

    users = session.execute(user_table.select())
    password_hash = hash_password(password)

    for user in users:
        # Check if the username and password match
        if user.name == name and user.password == password_hash:

            if user.email != email:
                return {"response": "the email doesnt match your user name"}

            else:
                return {"response": "user authenticated"}

    return {"response": "user data not found"}

# end authenticate2


@app.get("/addworkout")
def addworkout(userid: str, workout_name: str, date: datetime, exerciselist: str = None):
    session = Session()

    if exerciselist != "":
        session.execute(
            workout_table.insert().values(
                userid=userid,
                workout_name=workout_name,
                date=date,
                exerciselist=[exerciselist]
            )
        )
        session.commit()

    else:
        session.execute(
            workout_table.insert().values(
                userid=userid,
                workout_name=workout_name,
                date=date,
                exerciselist=""
            )
        )
        session.commit()


    return {"response": "the workout added"}


# add exercise to exist workout
# **to change that it will be by workout id and current userid
@app.get("/addexercisetoworkout")
def addexercisetoworkout(userid: str, date: str, workout_name: str, exercise):
    session = Session()
    find = session.query(workout_table).filter(workout_table.c.userid == userid).all()

    workout = find[0]

    for f in find:
        date1 = f[3]
        date2 = date1.strftime('%Y-%m-%d')
        if date2 == date:
            if f[2] == workout_name:
                workout = f

    # if workout == None:
    #     return {"response": "the workout doesnt exist"}

    workoutid1 = workout[0]
    exercise1 = workout[4]

    exercise3 = []

    if exercise1 != "":
        exercise3.append(exercise)

    else:
        exercise3 = [exercise]

    stmt = update(workout_table).where(workout_table.c.workoutid == workoutid1).values(exerciselist=exercise3)
    session.execute(stmt)
    session.commit()
    return {"response": "the exercise added"}


# delete exercise to exist workout
# **to change that it will be by workout id and current userid
@app.get("/deletexercisefromworkout")
def deletexercisefromworkout(userid: str, exercise):
    session = Session()
    find = session.query(workout_table).filter(workout_table.c.userid == "hadar44").first()

    exec_list = [find[3]]
    exec_to_check = exercise  # Set to check
    exists = False
    for e in exec_list:
        if e == exec_to_check:
            exists = True
            break

    if exists:
        exec_list.remove(exec_to_check)
        stmt = update(workout_table).where(workout_table.c.userid == "hadar44").values(exerciselist=exec_list)
        session.execute(stmt)
        session.commit()
        return {"response": "the exercise deleted"}

    else:
        return {"response": "the exercise doesnt found"}

@app.get("/addsettoexercise")
def addsettoexercise(userid: str, date: str, workout_name: str, exercise, sets):
    session = Session()

    find = session.query(workout_table).filter(workout_table.c.userid == userid).all()
    exec = find[0][4]
    workoutid1 = find[0][0]

    for f in find:
        date1 = f[3]
        date2 = date1.strftime('%Y-%m-%d')
        if date2 == date:
            if f[2] == workout_name:
                exec = f[4]
                workoutid1 = f[0]
                break

    exercise2 = json.loads(exercise)
    ex = json.loads(exec[0])
    set1 = ex["sets"]
    for e in exec:
        e1 = json.loads(e)
        if exercise2["name"] == e1["name"]:
            set1 = e1["sets"]
            exec.remove(e)
            break
    s = json.loads(sets)

    set1.append(s)
    set_lst = []
    for s1 in set1:
        w = Set(repetitions=int(s1["repetitions"]), time=int(s1["time"]), weight=float(s1["weight"]),
                distance_KM=float(s1["distance_KM"]))
        set_lst.append(w)

    new_exec = Exercise(name=exercise2["name"], power=exercise2["power"], sets=set_lst)
    new_exec2 = json.dumps(new_exec.dump())
    exec.append(new_exec2)
    stmt = update(workout_table).where(workout_table.c.workoutid == workoutid1).values(exerciselist=exec)
    session.execute(stmt)
    session.commit()
    return {"response": "the set added"}


@app.get("/showimprovement")
def showimprovement(userid: str, exercise_name: str, s_date: datetime, e_date: datetime):
    session = Session()
    exec_lst = []
    find = session.query(workout_table).filter(workout_table.c.userid == userid).all() #filter by userid, get lst of workouts

    for f in find: # going through the workouts
        if f[3] > s_date and f[3] < e_date: #check if its in the right date
            l = f[4] #get the list of exercises
            for l2 in l: #going through the exercises
                l3 = json.loads(l2) #from string to dict
                if l3["name"] == exercise_name: #check if there is the exercise the user want
                    exec_lst.append(f) #add to lst the all workout
                    break

    repete = 0
    time = 0
    weight = 0
    distance_KM = 0
    n = 0

    for e in exec_lst: #going through the full workout
        e2 = e[4] #take the list of exercises
        for j in e2: #going through the exercises list
            print(j)
            e3 = json.loads(j) #change the str to dict
            e3 = e3["sets"] #find the value of the "sets" key
            for i in e3: #going through the lst of sets
                repete += i["repetitions"]
                time += int(i["time"])
                weight += int(i["weight"])
                distance_KM += int(i["distance_KM"])
                n = n + 1 #counter

    #find the avg
    if n != 0:
        repete = repete / n
        time = time / n
        weight = weight / n
        distance_KM = distance_KM / n

        return {"repete": repete, "time": time, "weight": weight, "distance_KM": distance_KM}

    else:
        return {"repete": 0, "time": 0, "weight": 0, "distance_KM": 0}

@app.get("/showimprovement2")
def showimprovement2(userid: str, exercise_name: str, s_date: datetime, e_date: datetime):
    session = Session()
    exec_lst = []
    find = session.query(workout_table).filter(workout_table.c.userid == userid).all() #filter by userid, get lst of workouts

    for f in find: # going through the workouts
        if f[3] > s_date and f[3] < e_date: #check if its in the right date
            l = f[4] #get the list of exercises
            for l2 in l: #going through the exercises
                l3 = json.loads(l2) #from string to dict
                if l3["name"] == exercise_name: #check if there is the exercise the user want
                    exec_lst.append(f) #add to lst the all workout
                    break

    repete = 0
    time = 0
    weight = 0
    distance_KM = 0
    n = 0

    for e in exec_lst: #going through the full workout
        e2 = e[4] #take the list of exercises
        for j in e2: #going through the exercises list
            print(j)
            e3 = json.loads(j) #change the str to dict
            e3 = e3["sets"] #find the value of the "sets" key
            for i in e3: #going through the lst of sets
                repete += i["repetitions"]
                time += int(i["time"])
                weight += int(i["weight"])
                distance_KM += int(i["distance_KM"])
                n = n + 1 #counter

    #find the avg
    if n != 0:
        repete = repete / n
        time = time / n
        weight = weight / n
        distance_KM = distance_KM / n

        return {"count_sets": n, "repete": repete, "time": time, "weight": weight, "distance_KM": distance_KM}

    else:
        return {"count_sets": 0, "repete": 0, "time": 0, "weight": 0, "distance_KM": 0}

@app.get("/improve_with_params")
def improve_with_params(userid: str, exercise_name: str, s_date: datetime, e_date: datetime):
    session = Session()
    workouts_lst = []
    find = session.query(workout_table).filter(workout_table.c.userid == userid).all() #filter by userid, get lst of workouts

    dates_l = []
    count_sets_l = []
    repetitions_avg_l = []
    time_avg_l = []
    weight_avg_l = []
    distance_KM_avg_l = []

    for f in find: # going through the workouts
        if f[3] > s_date and f[3] < e_date: #check if its in the right date
            l = f[4] #get the list of exercises
            for l2 in l: #going through the exercises
                l3 = json.loads(l2) #from string to dict
                if l3["name"] == exercise_name: #check if there is the exercise the user want
                    dates_l.append(f[3])
                    repetitions_avg_l.append(return_the_avg(l3["sets"], "repetitions"))
                    time_avg_l.append(return_the_avg(l3["sets"], "time"))
                    weight_avg_l.append(return_the_avg(l3["sets"], "weight"))
                    distance_KM_avg_l.append(return_the_avg(l3["sets"], "distance_KM"))
                    count_sets_l.append(return_the_avg(l3["sets"], "count_sets"))
                    break

    dict1 = {"dates": dates_l, "count_sets": count_sets_l, "repetitions_avg": repetitions_avg_l, "time_avg": time_avg_l,
             "weight_avg": weight_avg_l, "distance_KM_avg": distance_KM_avg_l}

    return dict1


def return_the_avg(sets, name: str) -> int: #if the name is count_sets, its return the number of sets

    count = 0
    n = 0

    for i in sets:  # going through the lst of sets
        if name != "count_sets":
            count += i[name]
        n = n + 1  # counter

    if name == "count_sets":
        return n

    if n != 0:
        count1 = count / n
        return count1

    else:
        return 0

@app.get("/improve_with_params2")
def improve_with_params2(userid: str, exercise_name: str, s_date: datetime, e_date: datetime):
    session = Session()
    workouts_lst = []
    find = session.query(workout_table).filter(workout_table.c.userid == userid).all() #filter by userid, get lst of workouts

    full_workout_l = []
    dates_l = []
    count_sets_l = []
    repetitions_avg_l = []
    time_avg_l = []
    weight_avg_l = []
    distance_KM_avg_l = []

    for f in find: # going through the workouts
        if f[3] > s_date and f[3] < e_date: #check if its in the right date
            l = f[4] #get the list of exercises
            for l2 in l: #going through the exercises
                l3 = json.loads(l2) #from string to dict
                if l3["name"] == exercise_name: #check if there is the exercise the user want
                    full_workout_l.append(f)
                    break

    order_by_dates_l = return_dates_in_order(full_workout_l)

    for f in order_by_dates_l:
        l = f[4]  # get the list of exercises
        for l2 in l:  # going through the exercises
            l3 = json.loads(l2)  # from string to dict
            if l3["name"] == exercise_name:
                dates_l.append(f[3])
                repetitions_avg_l.append(return_the_avg(l3["sets"], "repetitions"))
                time_avg_l.append(return_the_avg(l3["sets"], "time"))
                weight_avg_l.append(return_the_avg(l3["sets"], "weight"))
                distance_KM_avg_l.append(return_the_avg(l3["sets"], "distance_KM"))
                count_sets_l.append(return_the_avg(l3["sets"], "count_sets"))


    dict1 = {"dates": dates_l, "count_sets": count_sets_l, "repetitions_avg": repetitions_avg_l, "time_avg": time_avg_l,
             "weight_avg": weight_avg_l, "distance_KM_avg": distance_KM_avg_l}

    return dict1



def return_dates_in_order(dates_lst) -> list:
    new_lst = sorted(dates_lst, key=lambda x: x[3])
    print(new_lst)
    return new_lst






