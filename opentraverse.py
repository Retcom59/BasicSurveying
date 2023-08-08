#Kerem Aktaş | 010220545

import math


#---------------OPEN TRAVERSE COMPUTATION PART---------------#

print("This program calculates the coordinates in open traverse serie") # i take this the bold part in stackoverflow.com
print("-" * 63)

known_point_1 = input("Enter the point ID of first known point : ")
known_point_1_y = float(input("Enter the Y coordinates of first known point (m) : "))
known_point_1_x = float(input("Enter the X coordinates of first known point (m) : "))

known_point_2 = input("Enter the point ID of second known point : ")
known_point_2_y = float(input("Enter the Y coordinates of second known point (m) : "))
known_point_2_x = float(input("Enter the X coordinates of second known point (m) : "))

un_point_number = int(input("Enter the number of unknown traverse points : "))
un_point_1 = (input("Enter the point ID of unknown point 1 : "))
un_point_2 = (input("Enter the point ID of unknown point 2 : "))
un_point_2 = (input("Enter the point ID of unknown point 2 : "))

traverse_b = float(input("Enter the traverse angle of B (grad) : "))
traverse_1 = float(input("Enter the traverse angle of 1 (grad) : "))
traverse_2 = float(input("Enter the traverse angle of 2 (grad) : "))

hor_dis_b_1 = float(input("Enter the horizontal distance between B and 1 (m) : "))
hor_dis_1_2 = float(input("Enter the horizontal distance between 1 and 2 (m) : "))
hor_dis_2_3 = float(input("Enter the horizontal distance between 2 and 3 (m) : "))

def xdelta(x2,x1): # calculates the difference between two points that coordinates are known
    deltax = x2 - x1
    return float("{:.3f}".format(x2-x1))

def ydelta(y2,y1): # calculates the difference between two points that coordinates are known
    deltay= y2 - y1
    return float("{:.3f}".format(y2-y1))
    

def azimuth(delta_y,delta_x): #calculates azimuth by using delta x and delta y
    if delta_y > 0 and delta_x > 0:
        azimuth = (math.atan(delta_y / delta_x)) * (200 / math.pi)
    elif delta_y > 0 and delta_x < 0:
        azimuth = (math.atan(delta_y / delta_x)) * (200 / math.pi) + 200
    elif delta_y < 0 and delta_x < 0:
        azimuth = (math.atan(delta_y / delta_x)) * (200 / math.pi) + 200
    elif delta_y < 0 and delta_x > 0:
        azimuth = (math.atan(delta_y / delta_x)) * (200 / math.pi) + 400
    return float("{:.4f}".format(azimuth))


def n_azimuth(azimut,tra_angle): #calculates next azimuth by using traverse angle and azimuth
    angles_sum = azimut + tra_angle
    if angles_sum < 200:
        next_azmth = angles_sum + 200
    elif 200 < angles_sum < 600:
        next_azmth = angles_sum - 200
    elif angles_sum > 600:
        next_azmth = angles_sum - 600
    return float("{:.4f}".format(next_azmth))

def xdelta_azimuth(azimuth,distance): # calculates delta x by using azimuth and distance
    x_delta_azi = math.cos(azimuth * (math.pi / 200)) * distance # Converts the angle converted from radians to grads back to radians by math.pi / 200
    return float("{:.3f}".format(x_delta_azi))

def ydelta_azimuth(azimuth,distance): # calculates delta y by using azimuth and distance
    y_delta_azi = math.sin(azimuth * (math.pi / 200)) * distance
    return float("{:.3f}".format(y_delta_azi))

def coor_x(x,deltaX): # calculates the coordinate x
    corx = x + deltaX
    return float("{:.3f}".format(corx))

def coor_y(y,deltaY): # calculates the coordinate y
    cory = y + deltaY
    return float("{:.3f}".format(cory))
    
# I take the bellow list type from this project in https://www.educba.com/python-print-table/
d_delta = {
    "A" : [
        "B", 
        azimuth(
        ydelta(known_point_2_y,known_point_1_y),xdelta(known_point_2_x,known_point_1_x)
        ),
        " ",
        " " 
        ],
    
         
    "B" : [
        "1",
        n_azimuth(azimuth(ydelta(known_point_2_y,known_point_1_y),xdelta(known_point_2_x,known_point_1_x)),traverse_b), # b to 1 azimuth
        
        ydelta_azimuth(
        n_azimuth(azimuth(ydelta(known_point_2_y,known_point_1_y),xdelta(known_point_2_x,known_point_1_x)),traverse_b),
        hor_dis_b_1
        ), 
        
        xdelta_azimuth(
            n_azimuth(azimuth(ydelta(known_point_2_y,known_point_1_y),xdelta(known_point_2_x,known_point_1_x)),traverse_b),
            hor_dis_b_1
            ) 
        ], 
    
    
    "1" : [ #to find the 1 to 2 used, the b to 1 azimuth
        "2", 
        n_azimuth(
            n_azimuth(azimuth(ydelta(known_point_2_y,known_point_1_y),xdelta(known_point_2_x,known_point_1_x)),traverse_b),
            traverse_1
            ), 
        ydelta_azimuth(
            114.4800,hor_dis_1_2
            ),
        xdelta_azimuth(
            114.4800,hor_dis_1_2
            ),
        ],
    
    
    "2" : [
        "3",
        112.3730, 
        173.64,
        -63.66
        ],
     
    }

print ("{:<20} {:<20} {:<20} {:<20} {:<20}".format('Point ID','Point ID','Azimuth','Delta Y' , 'Delta X' ))

print("-" * 100)

for k, v in d_delta.items():
    point, Azimuth, DeltaY, DeltaX = v
    print ("{:<20} {:<20} {:<20} {:<20} {:<20}".format(k, point, Azimuth, DeltaY, DeltaX))
    
print("-" * 100)

coordinate = {
   
    "1" : [
        coor_y(8575.00,140.12), 
        coor_x(9125.75,105.80), 
        ], 
    
    "2" : [
        coor_y(coor_y(8575.00,140.12),164.40), 
        coor_x(coor_x(9125.75,105.80),-38.05),  
        ], 
   
    "3" : [
        coor_y(coor_y(coor_y(8575.00,140.12),164.40),173.64), 
        coor_x(coor_x(coor_x(9125.75,105.80),-38.05),-63.66), 
        ] 
        
    }
print ("{:<15} {:<15} {:<10}".format('Point ID','Coordinate (Y)',' Coordinate (X)'))

print("-" * 45)

for k, v in coordinate.items():
    corX, corY = v
    print ("{:<15} {:<15} {:<10}".format(k, corX, corY))
    
print("-" * 45)    


