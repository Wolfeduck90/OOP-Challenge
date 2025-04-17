# to test pet functions as it should.
from pet import Pet

# Create Sasha the Dog
sasha = Pet("Sasha")

# Initial status
sasha.get_status()

# Train Sasha
sasha.train("sit")
sasha.train("fetch")
sasha.train("roll over")
sasha.train("play dead")  # She should be too tired after 3 tricks

# Feed Sasha and let her sleep
sasha.eat()
sasha.sleep()

# Show tricks Sasha has learned
sasha.show_tricks()

# Final status
sasha.get_status()
