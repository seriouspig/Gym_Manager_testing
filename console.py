import pdb 
from models.member import Member 
from models.activity import Activity
from models.workout import Workout
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.workout_repository as workout_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
workout_repository.delete_all()
activity_repository.delete_all()
member_repository.delete_all()

member1 = Member(
    "John",
    "Wick",
    "1978-03-30",
    "john_wick.jpg",
    "Basic"
)
member_repository.save(member1)

member2 = Member(
    "Arnold",
    "Schwarzeneger",
    "1945-03-14",
    "arnold_swartzeneger.jpg",
    "Premium"
)
member_repository.save(member2)

member3 = Member(
    "Harold",
    "Hidethepain",
    "1962-03-14",
    "harold_hidethepain.jpg",
    "Basic"
)
member_repository.save(member3)

member4 = Member(
    "Steven",
    "Segul",
    "1955-03-14",
    "m_steven_segul.jpg",
    "Basic"
)
member_repository.save(member4)

member5 = Member(
    "Ed",
    "stone",
    "1980-05-23",
    "m_ed_stone.jpg",
    "Basic"
)
member_repository.save(member5)

member6 = Member(
    "Dwayne",
    "Rockson",
    "1970-05-23",
    "m_dwayne_rockson.jpg",
    "Golden"
)
member_repository.save(member6)

member7 = Member(
    "Frank",
    "Booth",
    "1957-02-12",
    "m_frank_booth.jpg",
    "Basic"
)
member_repository.save(member7)

member8 = Member(
    "Jenny",
    "Fromtheblock",
    "1972-05-23",
    "m_jenny_fromtheblock.jpg",
    "Platinum"
)
member_repository.save(member8)

member9 = Member(
    "Jonah",
    "Hole",
    "1977-07-26",
    "m_jonah_hole.jpg",
    "Basic"
)
member_repository.save(member9)

member10 = Member(
    "Kayode",
    "Ewumil",
    "1972-07-26",
    "m_kayode_ewumil.jpg",
    "Basic"
)
member_repository.save(member10)

activity1 = Activity(
    "Spinning",
    "spinning.jpg",
    "Baldi"
)
activity_repository.save(activity1)

activity2 = Activity(
    "Weights",
    "weights.jpg",
    "Mario"
)
activity_repository.save(activity2)

activity3 = Activity(
    "Aikido",
    "class_aikido.jpg",
    "Steven"
)
activity_repository.save(activity3)

activity4 = Activity(
    "Archert",
    "class_archery.jpg",
    "Robin"
)
activity_repository.save(activity4)

activity5 = Activity(
    "Balet",
    "class_balet.jpg",
    "Michail"
)
activity_repository.save(activity5)

activity6 = Activity(
    "Boxing",
    "class_boxing.jpg",
    "Mike"
)
activity_repository.save(activity6)

activity7 = Activity(
    "Chess",
    "class_chess.jpg",
    "Bernie"
)
activity_repository.save(activity7)

activity8 = Activity(
    "Irish Dancing",
    "class_irishdancing.jpg",
    "Siobhan"
)
activity_repository.save(activity8)

activity9 = Activity(
    "Rubiks Cube",
    "class_rubiks.jpg",
    "Sergiei"
)
activity_repository.save(activity9)

activity10 = Activity(
    "Salsa",
    "class_salsa.jpg",
    "Rocio"
)
activity_repository.save(activity10)

activity11 = Activity(
    "Step",
    "class_step.jpg",
    "Angie"
)
activity_repository.save(activity11)

activity12 = Activity(
    "Swimming",
    "class_swimming.jpg",
    "Donald"
)
activity_repository.save(activity12)


workout1 = Workout(activity1, "Monday", "10", 20)
workout_repository.save(workout1)

workout2 = Workout(activity2, "Tuesday", "14", 10)
workout_repository.save(workout2)

booking1 = Booking(member1, workout1)
booking_repository.save(booking1)

booking2 = Booking(member2, workout2)
booking_repository.save(booking2)

pdb.set_trace()