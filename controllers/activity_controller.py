from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activities", __name__)

@activities_blueprint.route("/activities")
def activities():
    all_activities = activity_repository.select_all()
    return render_template("activities/index.html", activities=all_activities)

@activities_blueprint.route('/activities/new')
def new_activity():
    return render_template("activities/new.html")

@activities_blueprint.route('/activities', methods=['POST'])
def create_activity():
    name = request.form["name"]
    photo = request.files["photo"].filename
    trainer = request.form["trainer"]

    activity = Activity(name, 
                    photo, 
                    trainer )
    activity_repository.save(activity)

    return redirect('/activities')

@activities_blueprint.route("/activities/<id>")
def show(id):
    found_activity = activity_repository.select(id)
    found_members = activity_repository.members(found_activity)
    return render_template("activities/show.html", activity=found_activity, members=found_members)
