from db.run_sql import run_sql
from models.event import Event
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

def save(event):
    sql = """INSERT INTO events 
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
        event.member.id,
        event.activity.id,
        event.day,
        event.time,
        event.room,
        event.capacity]
    results = run_sql(sql, values)
    event.id = results[0]['id']
    return event

def select_all():
    events = []
    
    sql = "SELECT * FROM events"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        activity = activity_repository.select(row['activity_id'])
        event = Event(
            member,
            activity,
            row['day'],
            row['time'],
            row['room'],
            row['capacity'],
            row['id']
        )
        events.append(event)
    return events

def delete_all():
    sql = "DELETE FROM events"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)


