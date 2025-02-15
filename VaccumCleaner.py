import random
class VaccumCleaner:
    def  __init__(self):
        self.location = 0 or 1  # Initial location of the vacuum cleaner (0 or 1)

    def perceive(self, dirty):
        # Returns the current percept based on the cleanliness of the location
        return dirty[self.location]

    def act(self, percept):
        # Performs an action based on the percept
        if percept == "Dirty":
            print("Sucking at location", self.location)
        else:
            print("Moving to the", "left" if self.location == 0 else "right")
            self.location = 1 - self.location  # Move to the other location

# Simulate the environment
def simulate_environment():
    dirty = [random.choice(["Clean", "Dirty"]) for _ in range(2)] # Random initial state
    agent = VaccumCleaner()
    for _ in range(7): # Run for 7 time steps
        percept = agent.perceive(dirty)
        agent.act(percept)
# Run the simulation
simulate_environment()
