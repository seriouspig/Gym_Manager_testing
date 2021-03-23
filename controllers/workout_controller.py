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
    activity = activity_repository.select(activity_id)
    workout = Workout(activity, day, time, capacity)
    workout_repository.save(workout)
    return redirect('/workouts')

@workouts_blueprint.route("/workouts/<id>")
def show(id):
    found_workout = workout_repository.select(id)
    found_members = workout_repository.members(found_workout)
    return render_template("workouts/show.html", workout=found_workout, members=found_members)


@workouts_blueprint.route("/workouts/<id>/edit")
def edit_workout(id):
    activities = activity_repository.select_all()
    workout = workout_repository.select(id)
    return render_template("/workouts/edit.html", workout = workout, activities = activities)

@workouts_blueprint.route("/workouts/<id>", methods=["POST"])
def update_workout(id):
    activity_id = request.form['activity_id']
    day = request.form['day']
    time = request.form['time']
    capacity = request.form['capacity']

    activity = activity_repository.select(activity_id)
    

    workout = Workout(activity, 
                    day, 
                    time, 
                    capacity, 
                    id)
    workout_repository.update(workout)
    return redirect("/workouts")

@workouts_blueprint.route("/workouts/<id>/delete", methods=['POST'])
def delete_workout(id):
    workout_repository.delete(id)
    return redirect ('/workouts')