import math

#---------------OPEN LEVELLING NET COMPUTATION PART---------------#


print("This program calculates the elevations in open levelling net")
print("-" * 63)

known_id = input("Enter the point ID of known point : ")
known_elvn = float(input("Enter the elevation of point A (m) : "))

unknown_number = int(input("Enter the number of unknown points : "))
unknown_1_id = (input("Enter the point ID of unknown point 1 : "))
unknown_2_id = (input("Enter the point ID of unknown point 2 : "))
unknown_3_id = (input("Enter the point ID of unknown point 3 : "))
unknown_4_id = (input("Enter the point ID of unknown point 4 : "))

bs_A = float(input("Enter the BS reading of point A (m) : "))
fs_B = float(input("Enter the FS reading of point B (m) : "))

bs_B = float(input("Enter the BS reading of point B (m) : "))
fs_1 = float(input("Enter the FS reading of point 1 (m) : "))

bs_1 = float(input("Enter the BS reading of point 1 (m) : "))
fs_2 = float(input("Enter the FS reading of point 2 (m) : "))

bs_2 = float(input("Enter the BS reading of point 2 (m) : "))
fs_3 = float(input("Enter the FS reading of point 3 (m) : "))

def delta_h(bs_x,fs_x): # find the delta h
    return float("{:.3f}".format(bs_x - fs_x))


d_delta = {"A" : ["B", delta_h(bs_A,fs_B) ], "B" : ["1", delta_h(bs_B,fs_1) ], "1" : ["2", delta_h(bs_1,fs_2) ], "2" : ["3", delta_h(bs_2,fs_3) ]}
print ("{:<15} {:<15} {:<10}".format('Point ID','Point ID','Delta H'))

print("-" * 45)

for k, v in d_delta.items():
    bs_point, fs_point = v
    print ("{:<15} {:<15} {:<10}".format(k, bs_point, fs_point))
    
print("-" * 45)    


elvn_b = float("{:.3f}".format (known_elvn + delta_h(bs_A, fs_B)))
elvn_1 = float("{:.3f}".format (elvn_b + delta_h(bs_B, fs_1)))
elvn_2 = float("{:.3f}".format (elvn_1 + delta_h(bs_1, fs_2)))
elvn_3 = float("{:.3f}".format (elvn_2 + delta_h(bs_2, fs_3)))


d_elevation = {"B" : elvn_b, "1" : elvn_1, "2" : elvn_2, "3" : elvn_3}
print ("{:<15} {:<15}".format('Point ID','Elevation'))

print("-" * 27)

for k, v in d_elevation.items():
    elevation = v
    print ("{:<15} {:<15}".format(k, elevation))
    
print("-" * 27)
