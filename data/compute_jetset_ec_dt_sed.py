# jetset
import numpy as np
from jetset.jet_model import Jet

jet = Jet(
    name="ec_dt",
    electron_distribution="bkn",
    electron_distribution_log_values=False,
    beaming_expr="bulk_theta",
)
jet.add_EC_component(["EC_DT"])

# - blob
jet.set_par("N", val=0.0129)
jet.set_par("p", val=2.0)
jet.set_par("p_1", val=3.5)
jet.set_par("gamma_break", val=1e4)
jet.set_par("gmin", val=20)
jet.set_par("gmax", val=5e7)
jet.set_par("R", val=1e16)
jet.set_par("B", val=0.56)
jet.set_par("BulkFactor", val=40)
jet.set_par("theta", val=1.43)
jet.set_par("z_cosm", val=1)

# - DT
jet.set_par("L_Disk", val=2e46)
jet.set_par("tau_DT", val=0.1)
jet.set_par("R_DT", val=1.56 * 1e19)
jet.set_par("T_DT", val=1e3)

# - integration setup
jet.electron_distribution.update()
jet.set_gamma_grid_size(10000)
jet._blob.IC_adaptive_e_binning = True
jet._blob.theta_n_int = 500
jet.set_nu_grid(1e15, 1e30, 40)

# - SED near the DT
jet.set_par("R_H", val=1e18)
jet.set_external_field_transf("disk")
# fixes by Andrea to reproduce Finke's approach
jet._blob.R_H_scale_factor = 50
jet._blob.R_ext_factor = 0.5
theta_lim = np.rad2deg(np.arctan(jet.get_beaming() / jet.parameters.BulkFactor.val))
jet._blob.EC_theta_lim = theta_lim

jet.eval()

nu_ec_dt_jetset = jet.spectral_components.SSC.SED.nu
sed_ec_dt_jetset = jet.spectral_components.EC_DT.SED.nuFnu

condition = sed_ec_dt_jetset.value > 1e-20
nu = nu_ec_dt_jetset.value[condition]
sed = sed_ec_dt_jetset.value[condition]
np.savetxt("ec_dt_bpwl_jetset_1.1.2.txt", np.asarray([nu, sed]).T, delimiter=",")
