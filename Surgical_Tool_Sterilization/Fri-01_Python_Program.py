import sys
sys.path.append('../')

from Common_Libraries.p2_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim ():
    try:
        arm.ping()
    except Exception as error_update_sim:
        print (error_update_sim)

arm = qarm()

update_thread = repeating_timer(2, update_sim)




th = 0.1
th2=0.2
th3=0.3
th4=0.4
def get_bin_location(container): #the function gives a different location given the container ID
    if container == 1:
        location = [-0.5885, 0.2378, 0.4136]#small red
    elif container == 2:
        location = [-0.0222, -0.6343, 0.4136]#small green
    elif container == 3:
        location = [0.0, 0.6347, 0.4136]#small blue
    elif container == 4:
        location = [-0.3845, 0.1593, 0.2668]#big red
    elif container == 5:
        location = [0.0, -0.4329, 0.1999]#big green
    elif container == 6:
        location = [0.0, 0.4329, 0.1999]#big blue
    else:
        print("No container found")#if the above conditions are not ment this code will run
        arm.home()
    return location

def move_end_effector(left):
    if left >= th:#if/when the value for left exceeds the threshold defined globally (ie 0.1)
        arm.home()
        time.sleep(2)
        arm.move_arm(0.5088, 0.0, 0.0404)#go to pick up location
        time.sleep(2)
        close_gripper(arm.emg_left())#grab container
        time.sleep(2)
        arm.move_arm(0.4064, 0.0, 0.4826)#go back to home position (note that if a simple arm.home command was used the gripper would open hence it was required to instead input the home coordinates).
        time.sleep(2)  
        if left >= 0.6: #note that 0.6 corresponds to container ID 1 (ie small red)
            arm.move_arm(get_bin_location(1)[0],get_bin_location(1)[1],get_bin_location(1)[2])#since the function get bin location produces a list, indicies from 0 to 2 must be implemented 
            time.sleep(2)
            open_gripper(arm.emg_left())#the function open_gripper is called to release the container
            time.sleep(2)
            arm.home()
            time.sleep(2)
            x = 1
            return x
        elif left >= 0.5: #note that 0.5 corresponds to container ID 2 (ie small green)
            arm.move_arm(get_bin_location(2)[0],get_bin_location(2)[1],get_bin_location(2)[2])
            time.sleep(2)
            open_gripper(arm.emg_left())
            time.sleep(2)
            arm.home()
            time.sleep(2)
            x = 1
            return x
        elif left >= th4:#note that 0.4 corresponds to container ID 3 (ie small blue)
            arm.move_arm(get_bin_location(3)[0],get_bin_location(3)[1],get_bin_location(3)[2])
            time.sleep(2)
            open_gripper(arm.emg_left())
            time.sleep(2)
            arm.home()
            time.sleep(2)
            x = 1
            return x
        elif left >= th3: #note that 0.3 corresponds to container ID 4 (ie big red)
            open_autoclave_bin_drawer(arm.emg_left())
            time.sleep(2)
            arm.move_arm(get_bin_location(4)[0],get_bin_location(4)[1],get_bin_location(4)[2])
            time.sleep(2)
            open_gripper(arm.emg_left())
            time.sleep(2)
            arm.home()
            time.sleep(2)
            close_autoclave_bin_drawer(arm.emg_left())
            time.sleep(2)
            x = 1
            return x
        elif left >= th2:#note that 0.2 corresponds to container ID 5 (ie big green)
            open_autoclave_bin_drawer(arm.emg_left())
            time.sleep(2)
            arm.move_arm(get_bin_location(5)[0],get_bin_location(5)[1],get_bin_location(5)[2])
            time.sleep(2)
            open_gripper(arm.emg_left())
            time.sleep(2)
            arm.home()
            time.sleep(2)
            close_autoclave_bin_drawer(arm.emg_left())
            time.sleep(2)
            x = 1
            return x
        else:#note that 0.1 corresponds to container ID 6 (ie small red)
            open_autoclave_bin_drawer(arm.emg_left())
            time.sleep(2)
            arm.move_arm(get_bin_location(6)[0],get_bin_location(6)[1],get_bin_location(6)[2])
            time.sleep(2)
            open_gripper(arm.emg_left())
            time.sleep(2)
            arm.home()
            time.sleep(2)
            close_autoclave_bin_drawer(arm.emg_left())
            time.sleep(2)
            x = 1
            return x
    else:
        arm.home()
        time.sleep(2)
    
def open_autoclave_bin_drawer(left):
    if  left >= th3 and left <= th4:
        arm.open_red_autoclave(True)#if the left is in between threshold3(0.3) and threshold4(0.4), the big red auto clave will open
    elif left >= th2:
        arm.open_green_autoclave(True)#if the left is greater than threshold2(0.2)
    elif left >= th:
        arm.open_blue_autoclave(True)#if the left is greater than threshold1(0.1)

def close_autoclave_bin_drawer(left):
    if  left >= th3 and left <= th4:
        arm.open_red_autoclave(False)#if the left is in between threshold3(0.3) and threshold4(0.4), the big red auto clave will close
    elif left >= th2:
        arm.open_green_autoclave(False)#if the left is greater than threshold2(0.2)
    elif left >= th:
        arm.open_blue_autoclave(False)#if the left is greater than threshold(0.1)

def close_gripper(left):#gripper will close if left increases threshold1
    if left >= th:
        arm.control_gripper(45)
        
def open_gripper(left):#gripper will close if left increases threshold1
    if left >= th:
        arm.control_gripper(-45)

while True:
    inventory = 0 #variable inventory is set to 0
    arm.spawn_cage(6)
    time.sleep(3)
    inventory += move_end_effector(arm.emg_left()) #since the move end effector functions always returns the value 1, num will be incrimented by one 
    time.sleep(3)
    arm.spawn_cage(5)
    time.sleep(3)
    inventory += move_end_effector(arm.emg_left()) # same process of incrimentation 
    time.sleep(3)
    arm.spawn_cage(4)
    time.sleep(3)
    inventory += move_end_effector(arm.emg_left()) # same process of incrimentation
    time.sleep(3)
    arm.spawn_cage(3)
    time.sleep(3)
    inventory += move_end_effector(arm.emg_left()) # same process of incrimentation
    time.sleep(3)
    arm.spawn_cage(2)
    time.sleep(3)
    inventory += move_end_effector(arm.emg_left()) # same process of incrimentation
    time.sleep(3)
    arm.spawn_cage(1)
    time.sleep(3)
    inventory += move_end_effector(arm.emg_left()) # same process of incrimentation
    time.sleep(3)
    if inventory == 6: #once inventory is equal to 6 (ie all auto claves are full), the program must terminate
        break

