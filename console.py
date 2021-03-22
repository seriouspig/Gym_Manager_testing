import pdb 
from models.member import Member 
from models.activity import Activity
from models.event import Event
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.event_repository as event_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
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

booking1 = Booking(member1, activity1)
booking_repository.save(booking1)

booking2 = Booking(member2, activity2)
booking_repository.save(booking2)

pdb.set_trace()