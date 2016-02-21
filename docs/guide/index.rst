1. Introduction
---------------
The purpose of this module is to provide access to basic data to calculate the penetration and energy position of
photons (primarily in x-rays and gamma-rays) in materials. These materials may be biological, shieldings, or detector
materials. This information is derived from two measured quantities, the mass attenuation coefficient and the
mass energy-absorption coefficient.

2. Mass Attenuation Coefficient
-------------------------------
If a narrow beam of monoenergetic photons with intensity, :math:`I_0`, are impinged on a material with density
:math:`\rho`, the intensity is attenuated exponentially,

.. math::
  I(x) = I_0 \exp(-\frac{\mu}{\rho} x)

This equation can be re-written in the following form

.. math::
  \frac{\mu}{\rho} = \frac{1}{x} \ln(\frac{I_0}{I})

which suggests a method for measuring the mass attenuation coefficient, :math:`\mu / \rho`.


2. Pyplot
---------
Here is a simple example of pyplot usage.

.. plot::
    :include-source:

    from rontgen import MassAttenuationCoefficient
    import numpy as np
    import astropy.units as u
    import matplotlib.pyplot as plt

    cdte_atten = MassAttenuationCoefficient('cdte')

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
