from artiq.experiment import *


class dds_test(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("urukul0_ch0")

    @kernel
    def run(self):
        self.core.reset()
        self.urukul0_ch0.cpld.init()
        self.urukul0_ch0.init()

        self.urukul0_ch0.cfg_sw(True)
        self.urukul0_ch0.set_att(6. * dB)
        self.urukul0_ch0.set(frequency=10 * MHz, phase=1)
