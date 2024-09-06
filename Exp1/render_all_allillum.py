import os
import numpy as np
import mitsuba as mi

import scipy.io

mi.set_variant('scalar_rgb')
filename = './allIllum.xml'
		

# from mitsuba.core import Bitmap, Struct, Thread
# from mitsuba.core.xml import load_file

hdr =[5, 19, 34, 39, 42, 43, 78, 80, 102, 105, 125, 152, 164, 183, 198, 201, 202, 203, 209, 222, 226, 227, 230, 232, 243, 259, 272, 278, 281, 282]
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

			# Thread.thread().file_resolver().append(os.path.dirname(filename))
			scene = mi.load_file(filename, mesh=i, material=j, hdr=k, origin_x=o_x, origin_y=o_y, origin_z=o_z, target_x=t_x, target_y=t_y, target_z=t_z, object_scale =ob_scale, rotate_x = r_x, rotate_a = r_a)

			# scene.integrator().render(scene, scene.sensors()[0])

			# film = scene.sensors()[0].film()
			image = mi.render(scene)

			bmp = mi.Bitmap(image)
			# bmp_XYZ = bmp.convert(Bitmap.PixelFormat.Y, Struct.Type.UInt16, srgb_gamma=False)
			# bmp.write("output_allIllum/"+i+"/"+i+"_"+j+"_"+str(k)+".png", quality = 9)
			mi.util.write_bitmap("result/output_allIllum/"+i+"/"+i+"_"+j+"_"+str(k)+".png", bmp)
			# bmp_XYZ_2 = bmp.convert(Bitmap.PixelFormat.XYZ, Struct.Type.Float32, srgb_gamma=False)
			# image_np = np.array(bmp_XYZ_2)
			# mdic = {"image_np" : image_np}
			scipy.io.savemat("result/output_XYZ_allillum/"+i+"/"+i+"_"+j+"_"+str(k)+".mat", {'image_XYZ': bmp})

