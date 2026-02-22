# Recursion means:

# A function that calls itself again and again until some condition says STOP.



# Advantages of Recursion
# Simplifies code: Complex problems can be solved in fewer lines of code compared to iterative solutions.
# Natural representation: Problems that are recursive in nature (like tree traversals, factorial, Fibonacci, etc.) are easier to express.
# Reduces code complexity: Avoids writing nested loops, making the logic more readable and elegant.
# Useful in divide-and-conquer algorithms: Essential for algorithms like QuickSort, MergeSort, Binary Search, and Dynamic Programming.

# Disadvantages of Recursion
# High memory usage: Each recursive call adds a new layer to the function call stack, which may lead to memory overhead.
# Risk of stack overflow: Without proper base cases, infinite recursion can occur and crash the program.
# Slower execution: Function calls and returns add extra overhead compared to simple loops.
# Harder to debug: Tracing recursive calls can be confusing, especially in deep recursion.


# What is Stack Overflow in Recursion?
# Whenever recursion calls are executed, they’re simultaneously stored in a recursion stack where 
# they wait for the completion of the recursive function. A recursive function can only be completed 
# if a base condition is fulfilled and the control returns to the parent function. 

# But, when there is no base condition given for a particular recursive function, 
# it gets called indefinitely which results in a Stack Overflow i.e, exceeding the memory limit of the recursion stack and hence the program terminates giving a Segmentation Fault error. 

# The illustration above also represents the case of a Stack Overflow as 
# there is no terminating condition for recursion to stop, hence it will also result in a memory limit exceeded error. 

