#!/usr/bin/env python3
# Taken from https://medium.freecodecamp.org/demystifying-dynamic-programming-3efafb8d4296
# Here we'll look at a basic use of dynamic programming and why
# its subproblem concept massively increases solving some problems.

# First let's have a look at how a recursive version of
# a fibonacci algorithm works.

def fibonacci_recursive(n, debug_mode=False):
    """
    A bog standard fibonacci sequence generator using recursion.
    """
    #  if debug_mode:
    #      print("F({})".format(n))

    if n == 0:
        return 0
    elif n == 1:
        return 1
    #  return fibonacci_recursive(n - 1, debug_mode) + fibonacci_recursive(n - 2, debug_mode)
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Let's see if it works, F(5) = 5 shold be the answer.
#  print("Fibonacci n=5, F(5) = {}".format(fibonacci_recursive(5)))

# But there's a consequence to doing this recursively.
# Let's use the debug mode and print out how many times F(n) is calculated.
#  fibonacci_recursive(5, debug_mode=True)
#  F(5)
#  F(4)
#  F(3)
#  F(2)
#  F(1)
#  F(0)
#  F(1)
#  F(2)
#  F(1)
#  F(0)
#  F(3)
#  F(2)
#  F(1)
#  F(0)
#  F(1)
# As you can see there's a lot of repeated calculations of solutions.
# Instead we'd ideally be storing solutions to sub-problems so that when
# figuring out F(3), the F(2) & F(1) solutions are already calculated,
# stored and recalled for F(3) or any other iteration that requires it.

def fibonacci_dynamic(n):
    memo = [0] * (n+1) # create an empty array of n + 1 0's
    memo[0], memo[1] = 0, 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

# The list gets called memo, because it refers to "memoization".
# Memoization is in reference to the fact that those values aren't re-computed.
# Let's see how execution time compares here.

# First let's make sure the fibonacci number is corect during dynamic programming.
#  print("F(5) = {}".format(fibonacci_dynamic(5)))

# Now let's see how their execution times differ.
import time
N = 32
iters = 1
print("Execution Time:\n==============")
start_time = time.time()
for _ in range(0, iters):
    _ = fibonacci_recursive(N)
duration_r = time.time() - start_time
print("Recursion: {:.3f} ms".format(duration_r * 1000))
start_time = time.time()
for _ in range(0, iters):
    _ = fibonacci_dynamic(N)
duration_d = time.time() - start_time
print("Dynamic:     {:.3f} ms".format(duration_d * 1000))
print("Speedup:   {:.3f}x".format(duration_r/duration_d))

# From this, we see that there's almost 5 orders of magnitude of,
# a difference when calculating F(32) in favor of dynamic programming.
#  Execution Time:
#  ==============
#  Recursion: 862.892 ms
#  Dynamic:     0.015 ms

# Process to Creating a Dynamic Programming Algorithm
#
# 1. Identify the sub-problem in words.
#
