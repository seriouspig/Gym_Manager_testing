from db.run_sql import run_sql
from models.workout import Workout
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

def save(workout):
    sql = """INSERT INTO workouts 
            (member_id,
            activity_id,
            day,
            time,
            room,
            capacity
            ) VALUES 
            (%s, %s, %s, %s, %s, %s)
            RETURNING id"""
    values = [
        workout.member.id,
        workout.activity.id,
        workout.day,
        workout.time,
        workout.room,
        workout.capacity]
    results = run_sql(sql, values)
    workout.id = results[0]['id']
    return workout

def select_all():
    workouts = []

    sql = "SELECT * FROM workouts"
    results = run_sql(sql)
    for row in results:
        member = member_repository.select(row['member_id'])
        activity = activity_repository.select(row['activity_id'])
        workout = workout(
            member,
            activity,
            row['day'],
            row['time'],
            row['room'],
            row['capacity'],
            row['id']
        )
        workouts.append(workout)
    return workouts

def delete_all():
    sql = "DELETE FROM workouts"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)


