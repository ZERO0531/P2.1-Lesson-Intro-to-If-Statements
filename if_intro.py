# 1. What do you think the if does to the code under it? Put your answer in a comment in the code.
# If the condition is True, the code indented under the if statement executes.
robot_location = 30
ball_location = 35
goal_location = 20
have_ball = False

# Check if robot is before the ball
if robot_location < ball_location:
    print("Almost at the ball")

# Check if robot is beyond the goal
if robot_location > goal_location:
    print("You are beyond the goal.")

# Check if robot is exactly at the goal
if robot_location == goal_location:
    print("The robot is at the goal.")

# Move robot 5 units forward
robot_location += 5

# Check if robot is now at the goal
if robot_location == goal_location:
    print("At the goal.")

# Check if robot is now at the ball
if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
# Print instruction to move to goal
    print("Now make your way to the goal.")

# Move robot 15 units backward
robot_location -= 15

# Check if robot went too far back
if robot_location < goal_location:
    print("You went too far.")

# Check if robot scored a goal
if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False

# 2. What is the purpose indenting in the if statement? How can we tell what code is enclosed in an if branch and what code is not? Answer in a comment. 
# The purpose of indenting in an if statement is to define the scope of the conditional block. Indentation indicates which code is enclosed in the if branch and which code is not. 

# 3. Change the initial locations of the objects and get the program to output the same thing. 
robot_location = 10 
ball_location = 20
goal_location = 30
have_ball = False

if robot_location < ball_location:
print("Almost at the ball")

if robot_location > goal_location:
print("You are beyond the goal.")

if robot_location == goal_location:
print("The robot is at the goal.")

robot_location += 10

if robot_location == goal_location:
print("At the goal.")

if robot_location == ball_location:
print("At the ball")
print("Picking up the ball.")
have_ball = True

print("Now make your way to the goal.")

robot_location += 10

if robot_location < goal_location:
print("You went too far.")

if robot_location == goal_location and have_ball is True:
print("You scored a goal!")
have_ball = False

# 4. What do the operators += and -= do?
# += : Adds the value on the right side of the operator to the value of the variable on the left side. -= : Subtracts the value on the right side of the operator from the value of the variable on the left side.
