# MonteCarlo_Pi_Calculator

Python program that uses the Monte Carlo method to approximate the value of Pi.

# How it works

The program generates random  points (random x and y coordinates) in a square of sides 2*x = 2 and then checks if the point is inside a circle of radius x = 1 (both circle and square have the center at the origin).
Thus, the area of the square is 2 * x ** 2 = 4 * (x) ** 2 and the area of the circle is Pi * x ** 2 = pi, so the ratio of the areas (circle/square) is Pi/4.

The program counts the number of points inside and outside the circle to approximate the areas. This way, the result is not exactly Pi, but it's value gets closer to Pi as the number of points generated gets closer to positive infinite.

**It is possible to control the accuracy of the approximation using the variable `tries` (increasing it's value makes the result closer to Pi)
