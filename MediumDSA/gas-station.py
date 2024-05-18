def canCompleteCircuit(gas, cost):
    total_gas = 0
    total_cost = 0
    tank = 0
    start_index = 0
    
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]
        
        # If the tank becomes negative, start from the next station
        if tank < 0:
            start_index = i + 1
            tank = 0
    
    # If the total gas is less than the total cost, it's impossible to complete the circuit
    if total_gas < total_cost:
        return -1
    
    return start_index if start_index < len(gas) else -1

# Test cases
gas1 = [1, 2, 3, 4, 5]
cost1 = [3, 4, 5, 1, 2]
print("Output for gas1 and cost1:", canCompleteCircuit(gas1, cost1))  # Output: 3

gas2 = [2, 3, 4]
cost2 = [3, 4, 3]
print("Output for gas2 and cost2:", canCompleteCircuit(gas2, cost2))  # Output: -1
