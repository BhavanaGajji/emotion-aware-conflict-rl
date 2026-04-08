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
    state, _ = env.reset()

    if random.uniform(0, 1) < epsilon:
        action = random.randint(0, 3)
    else:
        action = np.argmax(q_table[state[0], state[1], state[2]])

    next_state, reward, terminated, truncated, _ = env.step(action)

    q_table[state[0], state[1], state[2], action] += learning_rate * reward

    rewards.append(reward)
    epsilon *= decay

# 🔥 SAVE Q-TABLE
np.save("q_table.npy", q_table)

print("Training completed!")