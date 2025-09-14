# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I wield the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass with encapsulation and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.__flight_speed = flight_speed  # Encapsulated attribute

    def use_power(self):
        print(f"{self.name} soars through the sky at {self.__flight_speed} km/h using {self.power}!")

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget

    def use_power(self):
        print(f"{self.name} deploys the {self.gadget} to enhance {self.power}!")

# Example usage
hero1 = FlyingHero("Skyblade", "Wind Manipulation", "Aetheria", 1200)
hero2 = TechHero("Circuit", "Cyber Control", "NeoTokyo", "Neural Gauntlet")

hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()



