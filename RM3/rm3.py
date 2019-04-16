from math import exp, sqrt, log

# Referenzprobe:
b_108_r = 8.98317
b_110_r = 10.62053
d_b_108_r = 0.01854
d_b_110_r = 0.0316

Z_108_r = exp(b_108_r)
Z_110_r = exp(b_110_r)

# Muenze:
b_108_m = 8.89956
b_110_m = 10.50085
d_b_108_m = 0.01847
d_b_110_m = 0.02917

Z_108_m = exp(b_108_m)
Z_110_m = exp(b_110_m)

p_108 = 0.95
p_110 = 1
sigma_107 = 46e-24
sigma_109 = 244e-24

x = Z_108_r / (p_108 * sigma_107)
y = Z_110_r / (p_110 * sigma_109)

h_107 = x/(x+y)
h_109 = y/(x+y)

# Messunsicherheiten Referenzprobe
d_Z_108_r_stat = Z_108_r * d_b_108_r
d_Z_110_r_stat = Z_110_r * d_b_110_r

d_x_stat = d_Z_108_r_stat / (p_108 * sigma_107)
d_y_stat = d_Z_110_r_stat / (p_110 * sigma_109)

d_h_107_stat = sqrt(((y / (x+y)**2)*d_x_stat)**2 + ((x/(x+y)**2)*d_y_stat)**2)
d_h_109_stat = sqrt(((x / (x+y)**2)*d_y_stat)**2 + ((y/(x+y)**2)*d_x_stat)**2)

# Messunsicherheiten Muenze
d_Z_108_m_stat = Z_108_m * d_b_108_m
d_Z_110_m_stat = Z_110_m * d_b_110_m

# Berechnung Silbergehalt, Messunsicherheit
Ag = h_107 * (Z_108_m / Z_108_r) + h_109 * (Z_110_m / Z_110_r)
d_Ag_stat_list = [
    Z_108_m / Z_108_r * d_h_107_stat,
    Z_110_m / Z_110_r * d_h_109_stat,
    h_107 / Z_108_r * d_Z_108_m_stat,
    h_109 / Z_110_r * d_Z_110_m_stat,
    h_107 * Z_108_m / Z_108_r**2 * d_Z_108_r_stat,
    h_109 * Z_110_m / Z_110_r**2 * d_Z_110_r_stat
    ]

d_Ag_stat = 0
for v in d_Ag_stat_list:
    d_Ag_stat += v**2
d_Ag_stat = sqrt(d_Ag_stat)

# Halbwertszeiten
a_108_r = -0.00474
a_110_r = -0.03204
d_a_108_r = 2.8865e-5
d_a_110_r = 2.88508e-4

t_h_108 = -log(2)/a_108_r
t_h_110 = -log(2)/a_110_r

d_t_h_108_stat = abs(t_h_108 / a_108_r * d_a_108_r)
d_t_h_110_stat = abs(t_h_110 / a_110_r * d_a_110_r)

# Ausgabe Zahlenwerte
print("Z_110_m", Z_110_m)
print("d_Z_110_m_stat", d_Z_110_m_stat)
print(d_Z_110_m_stat/Z_110_m * 100)

print("Z_110_r", Z_110_r)
print("d_Z_110_r_stat", d_Z_110_r_stat)
print(d_Z_110_r_stat / Z_110_r * 100)

print("Z_108_m", Z_108_m)
print("d_Z_108_m_stat", d_Z_108_m_stat)
print(d_Z_108_m_stat * 100 / Z_108_m)

print("Z_108_r", Z_108_r)
print("d_Z_108_r_stat", d_Z_108_r_stat)
print(d_Z_108_r_stat * 100 / Z_108_r)

print("t_h_108", t_h_108)
print("d_t_h_108_stat", d_t_h_108_stat)
print(d_t_h_108_stat * 100 / t_h_108)

print("t_h_110", t_h_110)
print("d_t_h_110_stat", d_t_h_110_stat)
print(d_t_h_110_stat * 100 / t_h_110)

print("h_107", h_107)
print("d_h_107_stat", d_h_107_stat)
print(d_h_107_stat * 100 / h_107)

print("h_109", h_109)
print("d_h_109_stat", d_h_109_stat)
print(d_h_109_stat * 100 / h_109)

print("Ag", Ag)
print("d_Ag_stat", d_Ag_stat)
print(d_Ag_stat * 100 / Ag)
