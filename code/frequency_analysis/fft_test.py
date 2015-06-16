import numpy as np 
import matplotlib.pylab as plt

# testing out the fft in numpy, trying to line it up with matlab results: 

t = np.arange(0,1,0.001)
x_new = np.zeros(len(t))
x = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)

# generate some random noise and add it: 

y = 2*np.random.rand(len(x))

x_new = x+y

#plt.plot(t[0:150],x_new[0:150])
#plt.show()


# now take the fft of the data and see if it selects 50 and 120 hz 

yft = np.fft.fft(x_new) 

freq = np.fft.fftfreq(len(t),d=0.001)

plt.plot(freq[0:150],np.abs(yft[0:150]))
plt.savefig('freq_hw.eps', bbox_inches='tight')
plt.show()
