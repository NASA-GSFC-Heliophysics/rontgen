from rontgen import Mass_attenuation_coefficient
import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt

cdte_atten = Mass_attenuation_coefficient('cdte')

print(cdte_atten.func(5 * u.keV))

energy = u.Quantity(np.arange(1, 1000), 'keV')
atten = cdte_atten.func(energy)

plt.plot(energy, atten)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Energy [' + str(energy.unit) + ']')
plt.ylabel('Mass attenuation Coefficient [' + str(atten.unit) + ']')
plt.title(cdte_atten.name)
plt.show()
