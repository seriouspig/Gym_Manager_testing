from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.workout import Workout
import repositories.workout_repository as workout_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

workouts_blueprint = Blueprint("workouts", __name__)

@workouts_blueprint.route("/workouts")
def workouts():
    workouts = workout_repository.select_all()
    return render_template("workouts/index.html", workouts = workouts)

@workouts_blueprint.route("/workouts/new", methods=['GET'])
def new_workout():
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    return render_template("workouts/new.html", members = members, activities = activities)

@workouts_blueprint.route("/workouts", methods=['POST'])
def create_workout():
    activity_id = request.form['activity_id']
    day = request.form['day']
    time = request.form['time']
    capacity = request.form['capacity']
    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)
    workout = workout(member, activity, day, time, room, capacity)
    workout_repository.save(workout)
    return redirect('/workouts')