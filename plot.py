import matplotlib.pyplot as plt
from train import rewards

# Smooth the graph
window = 50
avg_rewards = []

for i in range(len(rewards)):
    avg_rewards.append(sum(rewards[max(0, i-window):(i+1)]) / (i+1))

plt.plot(avg_rewards)
plt.xlabel("Episodes")
plt.ylabel("Average Reward")
plt.title("Learning Progress (Smoothed)")
plt.show()