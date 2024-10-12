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
        price_paths[t]=price_paths[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*z)

    st=price_paths[-1]
    payoffs=np.maximum(st-k,0)
    option_price=np.exp(-r*T)*np.mean(payoffs)
    return price_paths, option_price


price_paths, call_option_price = RNV()
print(f"Estimated European Call Option Price: ${call_option_price:.2f}")

# price_paths=GBM()
    
# plt.figure(figsize=(10, 6))
# plt.plot(price_paths[:, :10])  # Plot first 10 simulations
# plt.title("Monte Carlo Simulation of Stock Prices (GBM)")
# plt.xlabel("Time Steps")
# plt.ylabel("Stock Price")
# plt.show()


# final_prices = price_paths[-1, :]

# # Plot histogram of final prices
# plt.figure(figsize=(10, 6))
# plt.hist(final_prices, bins=50, edgecolor='black', alpha=0.7)
# plt.title("Distribution of Final Stock Prices")
# plt.xlabel("Final Stock Price")
# plt.ylabel("Frequency")
# plt.show()






