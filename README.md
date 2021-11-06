# Surgical_Tool_Sterilization

By: Diego Castaneda, Payton Chan, Mehrad Ebrahimi, Farhan Rahman, and Sebastian Rogowski

## Executive Summary

The primary objective of this project was to make an efficient and unique sterilization container to facilitate the cleaning of a surgical tool and to write an organized and commented code to take control of the arm and move the containers. The modelling sub-team was assigned the task of creating a sterilization container. In order to complete the objectives that were assigned for the container design, it required a unique but practical design to both facilitate sterilization and to allow the gripper to pick it up and move it with ease. This led to the use of the unique “ridge” design, created specifically for easy pick-up, transport and drop-off, by the gripper. The ridge feature is found in the middle of the length side of the container, and spans down the width of the container, with a 4mm gap cutting in the middle of the ridge to fit the tool. A 4mm gap left room for the assigned surgical tool to fit in and was dimensioned to comfortably fit the tool so that it is securely held within the container. The container had to be designed in a way that it could allow the tool to be sterilized while in the container. Keeping in mind that the tool needed to be relatively exposed to facilitate thorough sterilization, a “rack” design was used to place the tool on top of and allow the pressurized steam to sterilize the tool completely. 

To wrap up the design process, holes were created at the bottom of the container allow that pressurized steam to enter into the container, and further sterilize the tool that is in the container. For the computer program, we chose to have a more automatic approach for the execution of the program. Each container has its dedicated muscle emulator value that would execute a cycle of picking up and dropping the container to the correct autoclave. By doing this, the number of times that the muscle sensors are manipulated and changed would be reduced. The computer program still contains all the required functions, but it just has a unique flow for the way it operates. Specifically, all the other functions are called in the “move_end_effector” function and then the “move_end_effector” is called in a while loop. In that while loop, every time a cycle occurs for a container, a value of 1 is added to a variable that represents the inventory. The program continues to run until the inventory is equal to 6 which is the number of possible containers that can be stored in the autoclaves. The unique design of the sterilization container and organized, efficiently written code, the project final products were ready to be tested and evaluated.

## Objectives

![image](https://user-images.githubusercontent.com/89839649/140624491-d59b552b-330e-4072-81a2-f89b973efc47.png)

## Morphological Analysis

![image](https://user-images.githubusercontent.com/89839649/140624505-7f6fe785-d330-47ed-90a9-b4624c6e5fb3.png)

## Images of Model

![image](https://user-images.githubusercontent.com/89839649/140624571-69e0e1ae-c9bb-4a63-a77a-ef772fdd79bd.png)

![image](https://user-images.githubusercontent.com/89839649/140624589-d381eca8-b8b0-49b3-bcc9-380b7a6b17bf.png)

![image](https://user-images.githubusercontent.com/89839649/140624600-1109f26d-0f13-4b45-b8c9-9237be4b1ac5.png)

![image](https://user-images.githubusercontent.com/89839649/140624606-8f5502b8-2120-4e15-a63c-1921b9388aa0.png)

## Pugh Matrix

![image](https://user-images.githubusercontent.com/89839649/140624619-9a6f8527-b123-4e92-8755-4a57bdd8a858.png)

## Program Psudocode

![image](https://user-images.githubusercontent.com/89839649/140624639-10435dab-d47a-4870-8089-7cef2d814e20.png)
