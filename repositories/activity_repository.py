from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member

def save(activity):
    sql = """INSERT INTO activities(
        name,
        photo,
        trainer)
        VALUES ( %s, %s, %s) RETURNING id"""
    values = [
        activity.name,
        activity.photo,
        activity.trainer,
        ]
    results = run_sql(sql, values)
    activity.id = results[0]['id']
    return activity

def select_all():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)
    for row in results:
        activity = Activity(
            row['name'],
            row['photo'],
            row['trainer'],
            row['id']
        )
        activities.append(activity)
    return activities