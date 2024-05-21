def turn_right():
    for i in range(3):
        turn_left()
#Debugging if the robot is facing up
while front_is_clear():
    move()
turn_left()
        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

        
#while wall_in_front() or wall_on_right():
    #if at_goal():
        #break
    #elif wall_on_right():
        #turn_left()
        #if not wall_in_front():
            #move()
        #else:
            #turn_right()
            #move()
    #else:
        #turn_left()
        #move()
      
#while not front_is_clear() or right_is_clear():
    #if at_goal():
        #break
    #elif right_is_clear():
        #turn_right()
        #move()
    #else:
        #turn_right()
        #move()
    
  
#while front_is_clear() or right_is_clear():
    #turn_right()
    #move()
    #if not wall_in_front() or wall_on_right():
        #how do i go straight?
         #turn_left()
         #turn_left()
         #move()
    
#elif wall_on_right():
     #turn_left()
     #turn_left()
     #move()

        
#while not front_is_clear():
    #if front_is_clear():
        #move()
    #elif wall_on_right():
        #turn_left()
        #move()
    #elif at_goal():
        #turn_left()
        #move()
   # else:
       # turn_right()
       # move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
