import numpy as np
import matplotlib.pyplot as plt

# Geometric Brownian Motion
def GBM(s0=100,mu=0.1,sigma=0.2,T=1,dt=1/252):
    n=int(T/dt)
    simulations=1000
    price_paths = np.zeros((n, simulations))
    price_paths[0]=s0
    for t in range(1,n):
        z=np.random.standard_normal(simulations)
        # Alternative GMB
        # GBM formula: S(t) = S(t-1) * exp((mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z)
        price_paths[t] = price_paths[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)

    return price_paths


# Risk Neutral Valuation of Options
def RNV(s0=100,k=105,r=0.1,sigma=0.2,T=1,dt=1/252):
    simulations=10000
    n=int(T/dt)
    price_paths=np.zeros((n,simulations))
    price_paths[0]=s0
    
    for t in range(1,n):
        z=np.random.standard_normal(simulations)
        #  discrete-time version of GBM where mu is replaced by r
        price_paths[t]=price_paths[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*z)

    st=price_paths[-1]
    payoffs=np.maximum(st-k,0)
    option_price=np.exp(-r*T)*np.mean(payoffs)
    return price_paths, option_price


price_paths, call_option_price = RNV()
print(f"Estimated European Call Option Price: ${call_option_price:.2f}")

price_paths=GBM()
    
plt.figure(figsize=(10, 6))
plt.plot(price_paths[:, :10])  # Plot first 10 simulations
plt.title("Monte Carlo Simulation of Stock Prices (GBM)")
plt.xlabel("Time Steps")
plt.ylabel("Stock Price")
plt.show()


final_prices = price_paths[-1, :]

# Plot histogram of final prices
plt.figure(figsize=(10, 6))
plt.hist(final_prices, bins=50, edgecolor='black', alpha=0.7)
plt.title("Distribution of Final Stock Prices")
plt.xlabel("Final Stock Price")
plt.ylabel("Frequency")
plt.show()

def monte_carlo_greeks(S, K, T, r, sigma, n_simulations=100000, option_type='call'):
    """Estimates Delta and Gamma using Monte Carlo."""
    # Generate random paths for stock prices
    Z = np.random.randn(n_simulations)  # Standard normal random variables
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)  # Simulated prices at maturity
    
    # Payoff calculation
    if option_type == 'call':
        payoffs = np.maximum(ST - K, 0)
    elif option_type == 'put':
        payoffs = np.maximum(K - ST, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    # Discounted payoff
    discounted_payoff = np.exp(-r * T) * payoffs
    
    # Delta estimation (numerical differentiation with small perturbation)
    epsilon = 1e-4
    S_up = S + epsilon
    S_down = S - epsilon
    
    ST_up = S_up * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    ST_down = S_down * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    if option_type == 'call':
        payoff_up = np.maximum(ST_up - K, 0)
        payoff_down = np.maximum(ST_down - K, 0)
    elif option_type == 'put':
        payoff_up = np.maximum(K - ST_up, 0)
        payoff_down = np.maximum(K - ST_down, 0)
    
    discounted_payoff_up = np.exp(-r * T) * payoff_up
    discounted_payoff_down = np.exp(-r * T) * payoff_down
    
    delta = (np.mean(discounted_payoff_up) - np.mean(discounted_payoff_down)) / (2 * epsilon)
    gamma = (np.mean(discounted_payoff_up) - 2 * np.mean(discounted_payoff) + np.mean(discounted_payoff_down)) / (epsilon**2)
    
    return delta, gamma






