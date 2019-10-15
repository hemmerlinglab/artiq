import matplotlib
import matplotlib.pyplot as plt
import numpy as np

f_name = "zots.txt"
f_in = open(f_name,'r')
raw_data = f_in.read().split(' ')
f_in.close()

stpts = []
data = []

for dat in raw_data:
	try:
		parts = dat.split(',')
		stpts.append(float(parts[0]))
		data.append(float(parts[1]))
	except:
		pass

del stpts[-1]
del data[-1]


m, b = np.polyfit(stpts,data,1)
print('Linear Regression -> m: {} b: {}'.format(m,b))

fit_plot = []
for stp in stpts:
	fit_plot.append(m*stp+b)


plt.figure()
plt.plot(stpts,data,'r.')
plt.plot(stpts,fit_plot,'b-')
plt.xlabel('Set Voltage (V)')
plt.ylabel('Read Voltage (V)')



plt.show()
