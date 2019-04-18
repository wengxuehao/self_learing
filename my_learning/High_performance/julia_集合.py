# for z in coordinates:
#     for iteration in range(maxiter): # limited iterations per point
#         if abs(z) < 2.0: # has the escape condition been broken?
#             z = z*z + c
#         else:
#             break
#
# z = -1.8-1.8j
# print(abs(z))
#
# c = -0.62772-0.42193j
# z = 0+0j
# for n in range(9):
#     z = z*z + c
#     print ("{}: z={:33}, abs(z)={:0.2f}, c={}".format(n, z, abs(z), c))

x1,x2,y1,y2 = -1.8,1.8,-1.8,1.8
c_real,c_imag = -0.62772,-.42193
