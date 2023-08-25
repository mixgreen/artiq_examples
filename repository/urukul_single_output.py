from artiq.experiment import *  # 从artiq实验库导入所有内容


# 此代码在urukul的单一通道上以固定的幅度输出预定的频率
# 输出持续2秒，然后关闭

class Urukul_Frequency_Pulse(EnvExperiment):
    """Urukul单频脉冲"""

    def build(self):  # 这段代码在宿主设备上运行

        self.setattr_device("core")  # 将核心设备驱动设置为属性
        self.setattr_device("urukul0_ch1")  # 将urukul0的通道1设备驱动设置为属性

    @kernel  # 这段代码在FPGA上运行
    def run(self):
        self.core.reset()  # 重置核心设备
        self.urukul0_ch1.cpld.init()  # 初始化通道1上的CPLD
        self.urukul0_ch1.init()  # 初始化通道1
        delay(10 * ms)  # 延迟10毫秒

        freq = 100 * MHz  # 定义频率变量
        amp = 1.0  # 定义幅度变量作为幅度缩放因子(从0到1)
        attenuation = 1.0  # 定义衰减变量

        self.urukul0_ch1.set_att(attenuation)  # 将衰减写入urukul通道
        self.urukul0_ch1.sw.on()  # 打开urukul通道

        self.urukul0_ch1.set(freq, amplitude=amp)  # 将频率和幅度变量写入urukul通道，从而输出函数
        delay(2 * s)  # 延迟2秒
        self.urukul0_ch1.sw.off()  # 关闭urukul通道
