def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        
        if fpx == 0:
            print("Derivative is zero. Stopping iteration.")
            return None
        
        x_new = x - fx / fpx
        
        # Check for convergence
        if abs(x_new - x) < tol:
            return x_new
        
        x = x_new
    
    print("Max iterations reached.")
    return x

# Example: f(x) = x^2 - 2, f'(x) = 2x
f = lambda x: x**2 - 2
f_prime = lambda x: 2*x

# Initial guess x0 = 1
root = newton_raphson(f, f_prime, 1)
print(f"Root: {root}")

def bisection(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("The function must have opposite signs at a and b.")
        return None

    for i in range(max_iter):
        # Compute the midpoint
        m = (a + b) / 2
        fm = f(m)

        # Check if we've found the root
        if abs(fm) < tol:
            return m

        # Narrow the interval
        if f(a) * fm < 0:
            b = m
        else:
            a = m

    print("Max iterations reached.")
    return (a + b) / 2  # Return the midpoint after max iterations

# Example: f(x) = x^2 - 2
f = lambda x: x**2 - 2

# Initial interval [a, b] = [1, 2]
root = bisection(f, 1, 2)
print(f"Root: {root}")

