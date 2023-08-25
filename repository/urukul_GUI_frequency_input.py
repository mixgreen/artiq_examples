from artiq.experiment import *  # 从artiq实验库导入所有内容


# 该代码在urukul的一个通道上输出单一频率，幅度固定
# 输出的频率需要从仪表板以MHz的形式输入
# 输出持续2秒后关闭

class Urukul_Frequency_Selectable(EnvExperiment):
    """Urukul 可选择频率"""

    def build(self):  # 这段代码在宿主设备上运行

        self.setattr_device("core")  # 将核心设备驱动设置为属性
        self.setattr_device("urukul0_ch1")  # 将urukul0的通道1设备驱动设置为属性
        self.setattr_argument("freq", NumberValue(ndecimals=0, unit="MHz",
                                                  step=1))  # 在仪表板上指导用户以MHz的形式输入并将其设置为名为freq的属性

    @kernel  # 这段代码在FPGA上运行
    def run(self):
        self.core.reset()  # 重置核心设备
        self.urukul0_ch1.cpld.init()  # 初始化通道1上的CPLD
        self.urukul0_ch1.init()  # 初始化通道1
        delay(10 * ms)  # 延迟10毫秒

        amp = 1.0  # 定义幅度变量作为幅度缩放因子(从0到1)
        attenuation = 1.0  # 定义衰减变量

        self.urukul0_ch1.set_att(attenuation)  # 将衰减写入urukul通道
        self.urukul0_ch1.sw.on()  # 打开urukul通道

        self.urukul0_ch1.set(self.freq, amplitude=amp)  # 将频率和幅度变量写入urukul通道，从而输出函数
        delay(2 * s)  # 延迟2秒
        self.urukul0_ch1.sw.off()  # 关闭urukul通道
