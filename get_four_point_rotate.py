import math
import cv2
def get_four_points_for_diag_crop(cx, cy, w, h, angle):
    #cx: center x, cy: center y, w: width of the bounding box, h: height of the bounding box
    #angle: angle of rotation, see the image on README to know to calculate this angle (radian)
    # Lets calculate X1,Y1 (up-left)
    half_diag_line = math.sqrt(h*h + w*w)/2
    print(half_diag_line)
    beta = math.atan(h/w) #radian
    print(beta)
    alpha = beta - angle
    #distance from center x to X1 and center y to Y1
    dx1 = math.cos(alpha)*half_diag_line
    dy1 = math.sin(alpha)*half_diag_line
    print(dx1, dy1)
    X1 = cx - int(dx1)
    Y1 = cy - int(dy1)
    # Lets calculate X4,Y4 
    #distance from X1 to X4 and Y1 to Y4:
    dx4 = h*math.sin(angle)
    dy4 = h*math.cos(angle)
    X4 = X1 + int(dx4)
    Y4 = Y1 + int(dy4)
    # Lets calculate X2,Y2:
    #distance from X1 to X2 and Y1 to Y2:
    dx2 = w*math.cos(angle)
    dy2 = w*math.sin(angle)
    X2 = X1+int(dx2)
    Y2 = Y1- int(dy2)
    # Lets calcualte X3,Y3
    #distance from X4 to X3 and Y4 to Y3:
    dx3 = w*math.cos(angle)
    dy3 = w*math.sin(angle)
    X3 = X4 + int(dx3)
    Y3 = Y4 - int(dy3)
    return [(X1,Y1),(X2,Y2),(X3,Y3),(X4,Y4)]

# Example: 
cx = 592
cy = 223
w = 488
h = 38
angle = math.pi-3.081593
print(get_four_points_for_diag_crop(cx, cy, w, h, angle))
