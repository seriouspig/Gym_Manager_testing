from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.event_repository as event_repository
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
    activities = activity_repository.select_all()
    return render_template("bookings/new.html", members = members, activities = activities)

@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    activity_id = request.form['activity_id']
    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)
    booking = Booking(member, activity)
    booking_repository.save(booking)
    return redirect('/bookings')