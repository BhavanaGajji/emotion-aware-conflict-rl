import gymnasium as gym
from gymnasium import spaces
import random

class CoupleConflictEnv(gym.Env):
    def __init__(self):
        super().__init__()

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.MultiDiscrete([3, 3, 10])
        self.state = None

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = [
            random.randint(0, 2),
            random.randint(0, 2),
            random.randint(0, 9)
        ]
        return self.state, {}

    def set_state(self, state):
        self.state = state
        return self.state

    def step(self, action):
        mood, severity, time_gap = self.state
        reward = 0

        if mood == 0:  # angry
            if action == 3:
                reward += 10
            elif action == 2:
                reward -= 10

        elif mood == 1:  # sad
            if action == 1:
                reward += 8

        elif mood == 2:  # normal
            if action == 2:
                reward += 5

        if severity == 2 and action == 0:
            reward -= 10

        if time_gap > 5 and action in [1, 2]:
            reward += 3

        terminated = True
        truncated = False

        return self.state, reward, terminated, truncated, {}