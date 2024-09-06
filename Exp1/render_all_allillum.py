import os
import numpy as np
import mitsuba as mi

import scipy.io

mi.set_variant('scalar_rgb')
filename = r'F:\Coding\Nlab_Python\Exp1\allIllum.xml'

#hdr =[5, 19, 34, 39, 42, 43, 78, 80, 102, 105, 125, 152, 164, 183, 198, 201, 202, 203, 209, 222, 226, 227, 230, 232, 243, 259, 272, 278, 281, 282]
hdr =[19,39,78, 80, 102, 125, 152,203,226, 227, 230, 232, 243, 278, 281]
mesh = ["bunny"]
material = ["cu_0.025", "cu_0.129", "pla_0.075", "pla_0.225"]

o_x = 0
o_y = 0
o_z = 0
t_x = 0
t_y = 0
t_z = 0
ob_scale = 1
r_x = 0
r_a = 0

for i in mesh:
	if i == "bunny":
		o_x = -8
		o_y = 30
		o_z = 100
		t_x = -8
		t_y = 30
		t_z = -100
		ob_scale = 300	

	for j in material:
		for k in hdr:
			scene = mi.load_file(filename, mesh=i, material=j, hdr=k, origin_x=o_x, origin_y=o_y, origin_z=o_z, target_x=t_x, target_y=t_y, target_z=t_z, object_scale =ob_scale, rotate_x = r_x, rotate_a = r_a)

			image = mi.render(scene)

			bmp = mi.Bitmap(image)

			mi.util.write_bitmap("F:/Coding/Nlab_Python/Exp1/result/output_allIllum/"+i+"/"+i+"_"+j+"_"+str(k)+".png", bmp)

			scipy.io.savemat("F:/Coding/Nlab_Python/Exp1/result/output_XYZ_allillum/"+i+"/"+i+"_"+j+"_"+str(k)+".mat", {'image_XYZ': bmp})
