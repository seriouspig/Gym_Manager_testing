import pdb 
from models.member import Member 
from models.activity import Activity
from models.event import Event

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.event_repository as event_repository

event_repository.delete_all()
activity_repository.delete_all()
member_repository.delete_all()

member1 = Member(
    "John",
    "Wick",
    "30 march 1978",
    "42",
    "john_wick.jpg",
    "Basic"
)
member_repository.save(member1)

member2 = Member(
    "Arnold",
    "Schwarzeneger",
    "30 march 1945",
    "75",
    "arnold_swartzeneger.jpg",
    "Premium"
)
member_repository.save(member2)

activity1 = Activity(
    "Spinning",
    "john_wick.jpg",
    "Baldi"
)
activity_repository.save(activity1)

activity2 = Activity(
    "Weights",
    "arnold_swartzeneger.jpg",
    "Mario"
)
activity_repository.save(activity2)

event1 = Event(member1, activity1, "Monday", "10 o clock", "Basement 1", "20")
event_repository.save(event1)

event2 = Event(member2, activity2, "Tuesday", "11 o clock", "Basement 2", "20")
event_repository.save(event2)

pdb.set_trace()