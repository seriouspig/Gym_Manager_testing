from db.run_sql import run_sql
from models.workout import Workout
from models.activity import Activity
from models.member import Member
import repositories.activity_repository as activity_repository

def save(member):
    sql = """INSERT INTO members(
        first_name,
        second_name,
        date_of_birth,
        photo,
        platinum)
        VALUES ( %s, %s, %s, %s, %s) RETURNING id"""
    values = [
        member.first_name,
        member.second_name,
        member.date_of_birth,
        member.photo,
        member.platinum
        ]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(
            row['first_name'],
            row['second_name'],
            row['date_of_birth'],
            row['photo'],
            row['platinum'],
            row['id']
        )
        members.append(member)
    return members

def select(id):
    member = None 
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], 
                    result['second_name'],
                    result['date_of_birth'],
                    result['photo'],
                    result['platinum'],
                    result['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def workouts(member):
    values = [member.id]
    sql = """
        SELECT workouts.* FROM workouts
        INNER JOIN bookings
        ON workouts.id = bookings.workout_id
        WHERE member_id = %s
        """
    results = run_sql(sql, values)

    workouts = []
    
    for row in results:
        activity = activity_repository.select(row["activity_id"])
        workout = Workout(
            activity,
            row['day'],
            row['time'],
            row['capacity']
        )
        workouts.append(workout)
    return workouts

def update(member):
    sql = """UPDATE members SET 
            first_name = %s,
            second_name = %s,
            date_of_birth = %s,
            photo = %s,
            platinum = %s
            WHERE id = %s"""
    values = [
        member.first_name,
        member.second_name,
        member.date_of_birth,
        member.photo,
        member.platinum,
        member.id
        ]
    run_sql(sql, values)