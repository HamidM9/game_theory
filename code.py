import itertools

# Define actions
actions = ['SL', 'ST', 'SR']  # Left, Stay, Right

# Define payoff values
PAYOFFS = {
    'safe': 10,     # k
    'offroad': -2,  # f
    'obstacle': -5, # o
    'crash': -10    # c
}

def get_payoff(av_actions):
    """
    Compute payoffs for AV1, AV2, and AV3 based on their actions.
    Assumes an obstacle is in the center lane (ST), and they may swerve.
    """
    AV1, AV2, AV3 = av_actions
    positions = [AV1, AV2, AV3]
    payoffs = []

    for i, move in enumerate(positions):
        others = positions[:i] + positions[i+1:]

        # Collision detection
        if move in others:
            payoffs.append(PAYOFFS['crash'])
        elif i == 1 and move == 'ST':
            # AV2 is facing the obstacle in middle lane
            payoffs.append(PAYOFFS['obstacle'])
        elif move == 'SL' and i == 0:
            payoffs.append(PAYOFFS['offroad'])  # AV1 swerving left goes off-road
        elif move == 'SR' and i == 2:
            payoffs.append(PAYOFFS['offroad'])  # AV3 swerving right goes off-road
        else:
            payoffs.append(PAYOFFS['safe'])

    return tuple(payoffs)

def is_nash_equilibrium(strategy, all_strategies, get_payoff_func):
    """
    Check if a strategy is a Nash equilibrium.
    """
    base_payoff = get_payoff_func(strategy)
    for i in range(3):  # Each AV
        for alt_action in actions:
            if alt_action != strategy[i]:
                new_strategy = list(strategy)
                new_strategy[i] = alt_action
                new_strategy = tuple(new_strategy)
                new_payoff = get_payoff_func(new_strategy)
                if new_payoff[i] > base_payoff[i]:
                    return False  # Found a better unilateral deviation
    return True

def main():
    all_strategies = list(itertools.product(actions, repeat=3))
    print("Evaluating all strategy profiles...\n")
    
    nash_equilibria = []

    for strat in all_strategies:
        payoff = get_payoff(strat)
        print(f"Strategy: {strat} → Payoffs: {payoff}")
        if is_nash_equilibrium(strat, all_strategies, get_payoff):
            nash_equilibria.append((strat, payoff))

    print("\n--- Nash Equilibria ---")
    for eq in nash_equilibria:
        print(f"Strategy: {eq[0]} → Payoffs: {eq[1]}")

if __name__ == "__main__":
    main()
