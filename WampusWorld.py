import random

def is_adjacent(location, locations):
    for loc in locations:
        if abs(loc[0] - location[0]) + abs(loc[1] - location[1]) == 1:
            return True
    return False

class Environment:
    def __init__(self, size):
        self.size = size
        self.wumpus_location = (random.randint(0, size - 1), random.randint(0, size - 1))
        self.gold_location = (random.randint(0, size - 1), random.randint(0, size - 1))
        self.pit_locations = {(random.randint(0, size - 1), random.randint(0, size - 1)) for _ in range(size)}

    def get_percept(self, agent_location):
        breeze = is_adjacent(agent_location, self.pit_locations)
        stench = is_adjacent(agent_location, [self.wumpus_location])
        glitter = agent_location == self.gold_location
        return breeze, stench, glitter

    def print_environment(self, agent_location):
        for row in range(self.size):
            for col in range(self.size):
                if (row, col) == agent_location:
                    print("A", end=' ')  # Agent
                elif (row, col) == self.wumpus_location:
                    print("W", end=' ')  # Wumpus
                elif (row, col) == self.gold_location:
                    print("G", end=' ')  # Gold
                elif (row, col) in self.pit_locations:
                    print("P", end=' ')  # Pit
                else:
                    print(".", end=' ')  # Empty cell
            print()

class Agent:
    def __init__(self, environment):
        self.environment = environment
        self.location = (0, 0)

    def update_location(self, new_location):
        self.location = new_location

    def choose_action(self):
        # Heuristic function: Move towards unexplored cells if possible
        possible_actions = ['MOVE_LEFT', 'MOVE_RIGHT', 'MOVE_UP', 'MOVE_DOWN']
        return random.choice(possible_actions)

def main():
    size = 5
    environment = Environment(size)
    agent = Agent(environment)
    game_over = False

    while not game_over:
        breeze, stench, glitter = environment.get_percept(agent.location)
        print(f"Percept: Breeze={breeze}, Stench={stench}, Glitter={glitter}")

        # Visualize the environment
        environment.print_environment(agent.location)

        action = agent.choose_action()
        print(f"Agent performs action: {action}")

        if action == 'MOVE_LEFT':
            agent.update_location((max(agent.location[0] - 1, 0), agent.location[1]))
        elif action == 'MOVE_RIGHT':
            agent.update_location((min(agent.location[0] + 1, size - 1), agent.location[1]))
        elif action == 'MOVE_UP':
            agent.update_location((agent.location[0], max(agent.location[1] - 1, 0)))
        elif action == 'MOVE_DOWN':
            agent.update_location((agent.location[0], min(agent.location[1] + 1, size - 1)))

        if agent.location == environment.wumpus_location:
            print("Agent was eaten by the Wumpus!")
            game_over = True
        elif agent.location in environment.pit_locations:
            print("Agent fell into a pit!")
            game_over = True
        elif agent.location == environment.gold_location:
            print("Agent found the gold!")
            game_over = True

if __name__ == "__main__":
    main()
