import pandas as pd
import numpy as np


def stress_test(portfolio_value, num_simulations=1000, shock_mean=0, shock_std=0.1):
    # Generate random market shocks
    market_shocks = np.random.normal(loc=shock_mean, scale=shock_std, size=num_simulations)
    
    # Calculate the portfolio value after applying shocks
    final_values = portfolio_value * (1 + market_shocks)
    
    # Create a DataFrame to summarize results
    results = pd.DataFrame({
        'Simulation': range(1, num_simulations + 1),
        'Market Shock': market_shocks,
        'Final Portfolio Value': final_values
    })

    return results

initial_portfolio_value = 100000  # Initial portfolio value in dollars
num_simulations = 1000             # Number of simulations
shock_mean = -0.05                 # Mean market shock (e.g., -5% decline)
shock_std = 0.1  

stress_test_results = stress_test(initial_portfolio_value, num_simulations, shock_mean, shock_std)

# Display summary results
summary = {
    'Initial Portfolio Value': initial_portfolio_value,
    'Average Final Value': stress_test_results['Final Portfolio Value'].mean(),
    'Maximum Final Value': stress_test_results['Final Portfolio Value'].max(),
    'Minimum Final Value': stress_test_results['Final Portfolio Value'].min(),
}

print("Stress Test Summary:")

for key, value in summary.items():
    print(f"{key}: ${value:.1f}")

# Optionally, save results to a CSV file
stress_test_results.to_csv('stress_test_results.csv', index=False)