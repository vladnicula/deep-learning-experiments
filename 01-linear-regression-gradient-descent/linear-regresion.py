# This code will try to build the coeficients of a function that
# will tell us the link between number of hours of study and grades
# 
# We have a big file with a lot of data, and we will try to
# make our code update the *m and *b values of the y = m*x + b
# function in such a way that most (over 95%) of all the values
# in the input file will be very close if not identical to the 
# expected results. 
# 
# The expectation is that we will be able to use this function
# for other values, not just the ones in the input and get a
# statistically acurate aproximation of the grade we will get
# based on the number of hours studied. 

from numpy import *

def compute_error_for_given_points (b, m, points):
    totalError = 0

    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m*x + b)) ** 2

    return totalError / float(len(points))

def step_gradient(b_current, m_current, points, learning_rate):
    # stuff
    b_gradient = 0
    m_gradient = 0

    n = float(len(points))

    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        m_gradient += -(x * (y - (m_current*x + b_current)))
        b_gradient += -(y - (m_current*x + b_current))

    b_gradient = (2/n) * b_gradient
    m_gradient = (2/n) * m_gradient

    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)

    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
        
    return [b,m]

def run():
    points = genfromtxt('./data.csv', delimiter=',')
    #hyperparameters
    learning_rate = 0.0001

    #y = mx + b

    initial_m = 0
    initial_b = 0

    num_iterations = 5000

    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print(b)
    print(m)


run()
