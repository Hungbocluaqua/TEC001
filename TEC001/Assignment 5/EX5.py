import random
def approximate_pi(N):
    inside = 0
    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            inside += 1
    pi = 4 * inside / N
    return pi
N = int(input("Enter number of random points: "))
print("Approximation of pi:", approximate_pi(N))
