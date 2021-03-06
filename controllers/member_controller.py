from datetime import date
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository
import repositories.booking_repository as booking_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    all_members = member_repository.select_all()
    return render_template("members/index.html", members=all_members)

@members_blueprint.route('/members/new')
def new_member():
    return render_template("members/new.html")

@members_blueprint.route('/members', methods=['POST'])
def create_member():
    first_name = request.form["first_name"]
    second_name = request.form["second_name"]
    date_of_birth = request.form["date_of_birth"]
    photo = request.files["photo"].filename
    platinum = request.form["platinum"]

    member = Member(first_name, 
                    second_name, 
                    date_of_birth, 
                    photo, 
                    platinum)
    member_repository.save(member)

    return redirect('/members')

@members_blueprint.route("/members/<id>", methods=["GET"])
def show(id):
    member = member_repository.select(id)
    found_workouts = member_repository.workouts(member)
    all_workouts = workout_repository.select_all()
    possible_workouts = workout_repository.available_workouts(member)

    return render_template("members/show.html", member=member, workouts=found_workouts, all_workouts=all_workouts, possible_workouts=possible_workouts)

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html", member = member)

@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    first_name = request.form["first_name"]
    second_name = request.form["second_name"]
    date_of_birth = request.form["date_of_birth"]
    photo = request.files["photo"].filename

    if photo == '' :
        member = member_repository.select(id)
        photo = member.photo

    
    platinum = request.form["platinum"]

    member = Member(first_name, 
                    second_name, 
                    date_of_birth, 
                    photo, 
                    platinum,
                    id)
    member_repository.update(member)
    return redirect("/members")


@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect ('/members')
