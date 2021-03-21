from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.event import Event
import repositories.event_repository as event_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route("/events")
def events():
    events = event_repository.select_all()
    return render_template("events/index.html", events = events)

@events_blueprint.route("/events/new", methods=['GET'])
def new_event():
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    return render_template("events/new.html", members = members, activities = activities)

@events_blueprint.route("/events", methods=['POST'])
def create_event():
    member_id = request.form['member_id']
    activity_id = request.form['activity_id']
    day = request.form['day']
    time = request.form['time']
    room = request.form['room']
    capacity = request.form['capacity']
    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)
    event = Event(member, activity, day, time, room, capacity)
    event_repository.save(event)
    return redirect('/events')