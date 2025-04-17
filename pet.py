class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.trick_count = 0

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        self.trick_count = 0  # Reset trick count after sleeping

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
        else:
            print(f"{self.name} is too tired to play.")

    def train(self, trick):
        if self.energy >= 1 and self.hunger < 10:  # Check energy and hunger levels
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            self.hunger = min(10, self.hunger + 2)  # Sasha gets hungrier after training
            self.trick_count += 1
            print(f"{self.name} learned a new trick: {trick}!")
            if self.trick_count >= 3:
                print(f"{self.name} is tired after learning 3 tricks and needs to sleep!")
        elif self.hunger == 10:
            print(f"{self.name} is too hungry to train! Feed her first.")
        elif self.energy == 0:
            print(f"{self.name} is too tired to train! Let her sleep.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks Learned: {self.trick_count}")
