from artiq.experiment import *
from artiq.coredevice.ad9910 import RAM_MODE_CONT_RAMPUP


class dds_ram_test(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.dds0=self.setattr_device("urukul0_ch0")

    def prepare(self):
        self.amp = [0.0, 0.0, 0.0, 0.7, 0.0, 0.7, 0.7]  # Reversed Order
        self.asf_ram = [0] * len(self.amp)

    @kernel
    def init_dds(self, dds):
        self.core.break_realtime()
        dds.init()
        dds.set_att(6. * dB)
        dds.cfg_sw(True)

    @kernel
    def configure_ram_mode(self, dds):
        self.core.break_realtime()
        dds.set_cfr1(ram_enable=0)
        self.cpld.io_update.pulse_mu(8)
        self.cpld.set_profile(0)  # Enable the corresponding RAM profile
        # Profile 0 is the default
        dds.set_profile_ram(start=0, end=len(self.asf_ram) - 1,
                            step=250, profile=0, mode=RAM_MODE_CONT_RAMPUP)
        self.cpld.io_update.pulse_mu(8)
        dds.amplitude_to_ram(self.amp, self.asf_ram)
        dds.write_ram(self.asf_ram)
        self.core.break_realtime()
        dds.set(frequency=5 * MHz, ram_destination=RAM_DEST_ASF)
        # Pass osk_enable=1 to set_cfr1() if it is not an amplitude RAM
        dds.set_cfr1(ram_enable=1, ram_destination=RAM_DEST_ASF)
        self.cpld.io_update.pulse_mu(8)

    @kernel
    def run(self):
        self.core.reset()
        self.core.break_realtime()
        self.cpld.init()
        self.init_dds(self.dds0)
        self.configure_ram_mode(self.dds0)

