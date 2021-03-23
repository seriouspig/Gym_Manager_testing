from db.run_sql import run_sql
from models.workout import Workout
from models.member import Member
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

def save(workout):
    sql = """INSERT INTO workouts 
            (activity_id,
            day,
            time,
            capacity
            ) VALUES 
            (%s, %s, %s, %s)
            RETURNING id"""
    values = [
        workout.activity.id,
        workout.day,
        workout.time,
        workout.capacity]
    results = run_sql(sql, values)
    workout.id = results[0]['id']
    return workout

def select_all():
    workouts = []

    sql = "SELECT * FROM workouts"
    results = run_sql(sql)
    for row in results:
        activity = activity_repository.select(row['activity_id'])
        workout = Workout(
            activity,
            row['day'],
            row['time'],
            row['capacity'],
            row['id']
        )
        workouts.append(workout)
    return workouts

def select(id):
    workout = None 
    sql = "SELECT * FROM workouts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        activity = activity_repository.select(result['activity_id'])
        workout = Workout(
            activity,
            result['day'],
            result['time'],
            result['capacity'],
            result['id']
        )
    return workout
def delete_all():
    sql = "DELETE FROM workouts"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def members(workout):
    values = [workout.id]
    sql = """
        SELECT members.* FROM members
        INNER JOIN bookings
        ON members.id = bookings.member_id
        WHERE workout_id = %s
        """
    results = run_sql(sql, values)

    members = []
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

def available_workouts(member):
    values = [member.id]
    sql = """ SELECT * FROM workouts 
            EXCEPT 
            SELECT workouts.* FROM workouts 
            INNER JOIN bookings 
            ON bookings.workout_id = workouts.id 
            WHERE member_id = %s"""
    results = run_sql(sql, values)

    workouts= []
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
