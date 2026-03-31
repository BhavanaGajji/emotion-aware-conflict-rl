# 💔 Emotion-Aware Conflict Resolution using Reinforcement Learning

💡 Inspired by real-life human emotional decision-making rather than traditional game-based RL environments.
🚀 Unlike traditional RL projects focused on games, this project models human emotional intelligence and decision-making in real-life conflict scenarios.
---

## 📌 Problem
Human conflicts often escalate due to poor emotional decisions and wrong timing. Handling emotions correctly is a key challenge in real-life interactions.

---

## 💡 Solution
This project simulates relationship conflict scenarios where a Reinforcement Learning (RL) agent learns to take better decisions based on:
- Mood (angry, sad, normal)
- Severity of the issue
- Time gap between interactions

The agent chooses actions like apologizing, explaining, ignoring, or giving space.

---

## ⚙️ Features
- Emotion-aware decision making  
- Severity-based reward system  
- Timing-based optimization  
- Simple RL-based learning model

---

## 🧠 Environment Design

### State Space
- Mood: Angry (0), Sad (1), Normal (2)
- Severity: Low (0), Medium (1), High (2)
- Time Gap: 0–9 (represents delay in response)

### Action Space
- 0 → Ignore  
- 1 → Apologize  
- 2 → Explain  
- 3 → Give Space  

### Reward Design
- Emotion-sensitive rewards (based on mood)
- Penalties for escalation
- Bonus for correct timing
- Severity-based negative rewards
---

## 🎯 Actions
- Ignore  
- Apologize  
- Explain  
- Give Space  

---

## 🏆 Reward Strategy
- Positive reward for emotionally appropriate actions  
- Negative reward for wrong decisions  
- Extra reward for correct timing  
- Penalty for escalation-causing behavior  

---

## 🧪 Example Scenario

- Mood: Angry  
- Severity: High  
- Time Gap: Long  

👉 Agent Decision: Give Space  

This demonstrates how the model learns emotionally intelligent responses.

---

## 📈 Learning Graph

![Learning Graph](graph.png)

---

## 🚀 Result
The RL agent successfully learns to make emotionally appropriate decisions over time. 

The improvement in reward trends demonstrates that the model adapts its behavior based on emotional context, severity, and timing, leading to more stable and intelligent responses.

---

## 🔮 Future Scope
- Multi-step conversation modeling  
- Integration with chatbot systems  
- Emotion detection using NLP  
- Real-world relationship assistant applications  

---

## 🧠 Tech Stack
- Python  
- NumPy  
- OpenAI Gym  
- Matplotlib  

---

## 📂 Project Structure
couple-conflict-rl/
│── env.py
│── train.py
│── plot.py
│── graph.png
│── README.md

---

## 🎤 Author Note
This project focuses on applying AI to human emotional intelligence rather than traditional technical problems, making it more relatable and impactful.
