# emotion-aware-conflict-rl
Emotion-Aware Conflict Resolution using Reinforcement Learning

This project presents a unique reinforcement learning environment that simulates real-life relationship conflicts. The goal is to train an AI agent to make better decisions based on emotional context.

The environment models different situations using parameters like mood (angry, sad, normal), issue severity, and time gap between interactions. Based on these inputs, the agent chooses actions such as apologizing, explaining, ignoring, or giving space.

A reward system is designed to reflect real human behavior. Positive rewards are given for emotionally appropriate responses, while poor decisions that may escalate the situation are penalized. Timing is also considered, encouraging the agent to respond at the right moment.

Over multiple training episodes, the agent learns to select better actions, which is demonstrated through a reward progression graph.

## Problem
Human conflicts often escalate due to poor emotional decisions and timing.

## Solution
This project simulates a relationship environment where an AI agent learns optimal responses based on emotional state, severity, and timing.

## Features
- Emotion-based decision making  
- Severity-aware penalty system  
- Timing-based reward optimization  

## Actions
- Ignore  
- Apologize  
- Explain  
- Give Space  

## Reward Strategy
- Positive rewards for correct emotional response  
- Negative rewards for wrong decisions  
- Bonus for proper timing  

## Result
The agent improves over time, shown using reward graphs.
