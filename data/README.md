As of Feb 2024, `JetSet` cannot be installed in an environment that contains `Gammapy`
(there is a conflict with the `numpy` version). In the previous version of this repository
I was generating the SED values for `JetSet` on the fly. Now I have to pre-compute them
using a `jetset`-only environment. This is what is done here, to run this script therefore
you need to [create a `jetset` environment](https://github.com/andreatramacere/jetset?tab=readme-ov-file#installation).