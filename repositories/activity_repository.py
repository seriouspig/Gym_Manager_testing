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

def select(id):
    activity = None 
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        activity = Activity(
            result['name'],
            result['photo'],
            result['trainer'],
            result['id']
        )
    return activity

def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)

def members(activity):
    values = [activity.id]
    sql = """
        SELECT members.* FROM members
        INNER JOIN bookings
        ON members.id = bookings.member_id
        WHERE activity_id = %s
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


def update(activity):
    sql = """UPDATE activities SET 
            name = %s,
            photo = %s,
            trainer = %s
            WHERE id = %s"""
    values = [
        activity.name,
        activity.photo,
        activity.trainer,
        activity.id
        ]
    run_sql(sql, values)