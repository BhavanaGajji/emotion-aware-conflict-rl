import numpy as np
from env import CoupleConflictEnv
import random

env = CoupleConflictEnv()

q_table = np.zeros((3, 3, 10, 4))

episodes = 2000
learning_rate = 0.1
epsilon = 1.0
decay = 0.995

rewards = []

for episode in range(episodes):
    state = env.reset()

    # Exploration vs Exploitation
    if random.uniform(0, 1) < epsilon:
        action = random.randint(0, 3)
    else:
        action = np.argmax(q_table[state[0], state[1], state[2]])

    next_state, reward, done, _ = env.step(action)

    # Q-learning update
    q_table[state[0], state[1], state[2], action] += learning_rate * reward

    rewards.append(reward)

    # Reduce exploration over time
    epsilon *= decay

print("Training completed!")
test_state = [0, 2, 7]  # angry, high severity, long gap
best_action = np.argmax(q_table[test_state[0], test_state[1], test_state[2]])

actions = ["Ignore", "Apologize", "Explain", "Give Space"]

print("Test Scenario:", test_state)
print("Best Action:", actions[best_action])