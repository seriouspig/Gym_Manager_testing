from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member

def save(member):
    sql = """INSERT INTO members(
        first_name,
        second_name,
        date_of_birth,
        age,
        photo,
        platinum)
        VALUES ( %s, %s, %s, %s, %s, %s) RETURNING id"""
    values = [
        member.first_name,
        member.second_name,
        member.date_of_birth,
        member.age,
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
            row['age'],
            row['photo'],
            row['platinum'],
            row['id']
        )
        members.append(member)
    return members