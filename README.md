# game_theory
# 🚗 Autonomous Vehicles and Game Theory

A research-driven simulation project exploring the use of **static game theory** to model the decision-making behavior of autonomous vehicles in critical highway scenarios.

## 📘 Overview

This project focuses on applying static games of complete information to analyze strategic interactions between autonomous vehicles (AVs) when confronted with an obstacle on a three-lane highway. Each AV can swerve left, right, or stay in lane—with payoffs designed to prioritize safety.

### Key Scenarios Modeled:

- **Obstacle in middle lane:** All AVs must choose actions simultaneously.
- **Drunk driver case:** Simulates the unpredictability of human-driven vehicles for robust AV decision-making.

## 🎯 Objective

To use game-theoretic models (particularly Nash Equilibrium analysis) to:
- Identify optimal decision strategies.
- Minimize collision risk.
- Compare AV vs. human interaction dynamics.

## 🔢 Game Payoffs

| Outcome              | Payoff Symbol | Rank        |
|----------------------|----------------|-------------|
| Safe continuation    | `k`            | Best        |
| Off-road             | `f`            | Acceptable  |
| Hitting obstacle     | `o`            | Bad         |
| Collision with car   | `c`            | Worst       |

These are used to construct payoff matrices and compute equilibria.

## 🧠 Techniques Used

- Static Game Theory
- Nash Equilibria (Pure and Mixed Strategies)
- Simulation of multi-agent interactions
- Sensitivity analysis (obstacle shift, irrational drivers)

## 🧑‍💻 Authors
 
- Hamid Mohammadi  
- Supervisor: Laura Crosara


