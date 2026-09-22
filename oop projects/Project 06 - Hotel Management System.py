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

    def add_room(self):
        room_num = input("Enter room number: ")
        room_type = input("Enter room type: ")
        price = input("Enter price: ")
        room = Room(room_num, room_type, price)
        
        if room not in self.rooms:
            self.rooms.append(room)

        else:
            print("Room already exists")

    def add_guest(self):
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        guest = Guest(name, phone)

        if guest not in self.guests:
            self.guests.append(guest)

        else:
            print("Guest already exists!")

    def book_room(self):
        guest_name = input("Enter guest name: ")
        room_num = input("Enter room number: ")

        guest = next(
            (guest for guest in self.guests if guest.name == guest_name),
            None,
        )
        room = next(
            (room for room in self.rooms if room.room_num == room_num),
            None,
        )

        if guest is None:
            print("Guest not found")
        elif room is None:
            print("Room not found")
        elif guest.room is not None:
            print(f"{guest.name} already has a room")
        elif room.status != "Available":
            print(f"The room {room.room_num} is already occupied")
        else:
            guest.room = room
            room.occupied()
            print(f"Room {room.room_num} booked for {guest.name}")

    def checkout(self):
        guest_name = input("Enter guest name: ")

        guest = next(
            (guest for guest in self.guests if guest.name == guest_name),
            None,
        )

        if guest in self.guests and guest.room is not None:
            guest.room.available()
            guest.room = None
            print(f"Guest: {guest_name} has checked out!")
        else:
            print(f"Guest: {guest_name} doesn't have a room!")

    def show_available_rooms(self):
        available_room_found = False
        print("============ Available rooms ============")

        for room in self.rooms:
            if room.status == "Available":
                available_room_found = True
                print(f"""
Room number: {room.room_num}
Room type: {room.room_type}
Price: {room.price}""")

        if not available_room_found:
            print("\nThere are no available rooms!\n")

    def show_all_rooms(self):
        print("============ All Rooms ============")

        for room in self.rooms:
            room.info()

    def menu(self):
        while True:
            print("""
========================================
       HOTEL MANAGEMENT SYSTEM
========================================

1. Add Room
2. Add Guest
3. Book Room
4. Checkout
5. Show Available Rooms
6. Show All Rooms
7. Exit
""")
            self.choice = input("Enter your choice: ")

            if self.choice == "1":
                self.add_room()

            elif self.choice == "2":
                self.add_guest()

            elif self.choice == "3":
                self.book_room()

            elif self.choice == "4":
                self.checkout()

            elif self.choice == "5":
                self.show_available_rooms()

            elif self.choice == "6":
                self.show_all_rooms()

            elif self.choice == "7":
                return

hotel = Hotel()
hotel.menu()