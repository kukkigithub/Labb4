class Flight:
    def _init_(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def _init_(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        city_flights = [flight for flight in self.flights if flight.source == city or flight.destination == city]
        return city_flights

    def search_by_source(self, source):
        source_flights = [flight for flight in self.flights if flight.source == source]
        return source_flights

    def search_by_cities(self, source, destination):
        city_flights = [flight for flight in self.flights if flight.source == source and flight.destination == destination]
        return city_flights

def print_flights(flights):
    if not flights:
        print("No flights found.")
        return

    print("Flight ID\tFrom\tTo\tPrice")
    for flight in flights:
        print(f"{flight.flight_id}\t{flight.source}\t{flight.destination}\t{flight.price}")

# Sample flight data
flights_data = [
    ("AI161E90", "BLR", "BOM", 5600),
    ("BR161F91", "BOM", "BBI", 6750),
    ("AI161F99", "BBI", "BLR", 8210),
    ("VS171E20", "JLR", "BBI", 5500),
    ("AS171G30", "HYD", "JLR", 4400),
    ("AI131F49", "HYD", "BOM", 3499)
]

# Creating flight objects and adding to the flight table
flight_table = FlightTable()
for flight_data in flights_data:
    flight = Flight(*flight_data)
    flight_table.add_flight(flight)

# User Interface
while True:
    print("\nSearch Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    print("4. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        city = input("Enter the city: ")
        city_flights = flight_table.search_by_city(city)
        print_flights(city_flights)
    
    elif choice == "2":
        source = input("Enter the source city: ")
        source_flights = flight_table.search_by_source(source)
        print_flights(source_flights)
    
    elif choice == "3":
        source = input("Enter the source city: ")
        destination = input("Enter the destination city: ")
        city_flights = flight_table.search_by_cities(source, destination)
        print_flights(city_flights)
    
    elif choice == "4":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")