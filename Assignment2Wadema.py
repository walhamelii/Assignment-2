class Artwork:
    def __init__(self, title, geography, date_of_creation, classification):
        self.title = title
        self.geography = geography
        self.date_of_creation = date_of_creation
        self.classification = classification

    def get_details(self):
        return f"Title: {self.title}, Geography: {self.geography}, Date of Creation: {self.date_of_creation}, Classification: {self.classification}"


class Exhibition:
    def __init__(self, location, duration):
        self.location = location
        self.duration = duration
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def get_details(self):
        artworks_info = "\n".join([artwork.get_details() for artwork in self.artworks])
        return f"Location: {self.location}, Duration: {self.duration}\nArtworks:\n{artworks_info}"


class Ticket:
    def __init__(self, price):
        self.price = price

    def calculate_price(self):
        return self.price


class Visitor:
    def __init__(self, name, age, id_card):
        self.name = name
        self.age = age
        self.id_card = id_card

    def purchase_ticket(self, ticket):
        # Implement ticket purchase logic here
        pass


class Event:
    def __init__(self, location, duration):
        self.location = location
        self.duration = duration

    def get_details(self):
        return f"Location: {self.location}, Duration: {self.duration}"


class SpecialEvent(Event):
    def __init__(self, location, duration, ticket_price):
        super().__init__(location, duration)
        self.ticket_price = ticket_price

    def calculate_price(self):
        return self.ticket_price


if __name__ == "__main__":
    # Creating instances and testing functionality
    artwork1 = Artwork("Elephant Attached to a Tree Stump", "Bikaner,India", "beginning of 17th century", "miniature")
    exhibition1 = Exhibition("Gallery 1", "Jan 1, 2024 - Mar 31, 2024")
    exhibition1.add_artwork(artwork1)
    print(exhibition1.get_details())

    ticket1 = Ticket(60)
    print(ticket1.calculate_price())

    visitor1 = Visitor("Abdulla", 20, "74760")
    visitor1.purchase_ticket(ticket1)

    event1 = Event("Outdoor Space", "April 5, 2024")
    print(event1.get_details())

    special_event1 = SpecialEvent("Main Hall", "April 10, 2024", 70)
    print(special_event1.calculate_price())