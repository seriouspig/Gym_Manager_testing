class Event:

    def __init__(self, member, activity, day, time, room, capacity, id=None):
        self.activity = activity
        self.member = member
        self.day = day
        self.time = time
        self.room = room
        self.capacity = capacity
        self.id = id