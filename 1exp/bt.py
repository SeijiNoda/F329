import math

mi0 = 1.25663706 * (10**-6)
n = 140
R = 10.575 * (10**-2)
bt_o = 0.00178

def calculate_earth_mg_field(a, b):
    return (b/a)*(mi0*n/R)*8*math.sqrt(5**-3)
    #return (1/mi)*4*b*(math.pi**2)*mI

r = 0.3 * (10**-2)
L = 2.5 * (10**-2)
m = 5.1755 * (10**-3)

def calculate_magnet_inertial_moment():
    return m*((r*r/4) + (L*L/12))

def calculate_magnet_dipole_moment(a, mI):
    return (a * (math.pi**2) * mI * R * (5**1.5))/(2*mi0*n)

# right side
b = -0.102
a = 0.0186

# left side
br = 0.324 
ar = -0.0227 

mI = calculate_magnet_inertial_moment()

print("Magnet moment of inertia: " + str(mI))

mi = calculate_magnet_dipole_moment(a, mI)
mir = calculate_magnet_dipole_moment(ar, mI)
print("Magnet dipole moment\nLeft: " + str(mi) + "\nRight: " + str(mir) + "\nRatio: " + str(int(abs(100*mi/mir))) + "%\n")

bt = calculate_earth_mg_field(ar, br)

print("Bt = " + str(bt) + "\nRatio: " + str(int(abs(100*bt/bt_o))) + "%\n")