from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.workout_repository as workout_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_booking():
    members = member_repository.select_all()
    workouts = workout_repository.select_all()
    return render_template("bookings/new.html", members = members, workouts = workouts)

@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    workout_id = request.form['workout_id']
    member = member_repository.select(member_id)
    workout = workout_repository.select(workout_id)
    booking = Booking(member, workout)
    booking_repository.save(booking)
    return redirect('/bookings')