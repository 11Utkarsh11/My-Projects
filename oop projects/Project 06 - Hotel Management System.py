class Room:
    def __init__(self, room_num, room_type, price):
        self.room_num = room_num
        self.room_type = room_type
        self.price = price
        self.status = "Available"

    def occupied(self):
        if self.status == "Available":
            self.status = "Occupied"

    def available(self):
        if self.status == "Occupied":
            self.status = "Available"

    def info(self):
        print(f"""
========== Room {self.room_num} ==========

Type: {self.room_type}
Price: {self.price}
Status: {self.status}""")


class Guest:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.room = None


class Hotel:
    def __init__(self):
        self.rooms = []
        self.guests = []

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

        else:
            print("Room already exists")

    def add_guest(self, guest):
        if guest not in self.guests:
            self.guests.append(guest)

        else:
            print("Guest already exists!")


hotel = Hotel()

room1 = Room(101, "Single", 1500)
room2 = Room(102, "Double", 2500)

hotel.add_room(room1)
hotel.add_room(room2)

guest1 = Guest("Utkarsh", "9876543210")

hotel.add_guest(guest1)

print(hotel.rooms)
print(hotel.guests)