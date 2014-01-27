import visual as v

spheres = []
axes = []
pi = v.pi

trt = 2.0*v.sqrt(2.0) #2*sqrt(2)
r_trt = trt/2.0 #halve it for radius ('edge length' quoted in literature = diameter)

w = 700
v.display(x=w, y=0, width=w, height=w, range=5, forward=v.vector(1,1,1), newzoom=0.1)


a=v.sphere(pos=(1,1,1), radius = r_trt, color=(1,0,0), dir=-1) #red
spheres.append(a)
b=v.sphere(pos=(1,-1,-1), radius = r_trt, color=(0,1,0), dir=-1) #green
spheres.append(b)
c=v.sphere(pos=(-1,1,-1), radius = r_trt, color=(0,0,1), dir=-1) #blue
spheres.append(c)
d=v.sphere(pos=(-1,-1,1), radius = r_trt, color=(1,1,0), dir=-1) #yellow
spheres.append(d)

x_axis = v.cylinder(pos=(0,0,0), axis=(5,0,0), radius = 0.05, color=(1,1,1)) #white
axes.append(x_axis)
y_axis = v.cylinder(pos=(0,0,0), axis=(0,5,0), radius = 0.05, color=(1,0,1)) #magenta
axes.append(y_axis)
z_axis = v.cylinder(pos=(0,0,0), axis=(0,0,5), radius = 0.05, color=(0,1,1)) #cyan
axes.append(z_axis)

bottom_pos_B_and_D = (spheres[3].pos-(0, spheres[3].radius,0))
top_pos_A_and_C = (spheres[0].pos+(0,spheres[0].radius,0))
tetra_length = top_pos_A_and_C[1] - bottom_pos_B_and_D[1] #y values
print 'length:', tetra_length
left_pos_C_and_D = (spheres[3].pos-(spheres[3].radius, 0,0))
right_pos_A_and_B = (spheres[0].pos+(spheres[0].radius,0,0))
tetra_width = right_pos_A_and_B[0] - left_pos_C_and_D[0] #x values
print 'width:', tetra_width
back_pos_B_and_C = (spheres[2].pos-(0, 0, spheres[2].radius))
forward_pos_A_and_D = (spheres[0].pos+(0,0,spheres[0].radius))
tetra_depth = forward_pos_A_and_D[2] - back_pos_B_and_C[2] #z values
print 'depth:', tetra_depth

print 'trt:', trt
print 'radii:', r_trt

height_line_y = v.cylinder(pos=bottom_pos_B_and_D, axis=(0,tetra_length,0), radius = 0.05)
width_line_x = v.cylinder(pos=left_pos_C_and_D, axis=(tetra_width,0,0), radius = 0.05)
depth_line_z = v.cylinder(pos=back_pos_B_and_C, axis=(0,0,tetra_depth), radius = 0.05)

hypo_box = v.box(pos=(0,0,0),axis=(1,0,0), length=tetra_length, height=tetra_width, width=tetra_depth,  opacity=0.5)

