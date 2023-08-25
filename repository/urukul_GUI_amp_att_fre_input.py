from artiq.experiment import *  # 从artiq实验库导入所有内容


# 该代码在urukul的一个通道上输出单一频率，幅度固定
# 以下内容需要从仪表板上输入：
# 频率(单位MHz)
# 幅度(作为幅度缩放因子，所以在0和1之间)
# 衰减(单位db，介于0和31.5之间)
# 脉冲长度(单位s)

class Urukul_Programmable(EnvExperiment):
    """Urukul 可选择的频率、幅度、衰减和脉冲长度"""

    def build(self):  # 这段代码在宿主设备上运行

        self.setattr_device("core")  # 将核心设备驱动设置为属性
        self.setattr_device("urukul0_ch1")  # 将urukul0的通道1设备驱动设置为属性

        # 所有可调参数都可以单提出来调整
        self.setattr_argument("freq", NumberValue(ndecimals=0, unit="MHz", step=1))  # 指导仪表板以MHz的形式输入并将其设置为名为freq的属性
        self.setattr_argument("amp", NumberValue(ndecimals=2, step=1))  # 指导仪表板输入并将其设置为名为amp的属性
        self.setattr_argument("atten", NumberValue(ndecimals=2, step=1))  # 指导仪表板输入并将其设置为名为atten的属性
        self.setattr_argument("t_pulse", NumberValue(ndecimals=2, unit="s", step=1))  # 指导仪表板输入并将其设置为名为t_pulse的属性

    @kernel  # 这段代码在FPGA上运行
    def run(self):
        self.core.reset()  # 重置核心设备
        self.urukul0_ch1.cpld.init()  # 初始化通道1上的CPLD
        self.urukul0_ch1.init()  # 初始化通道1
        delay(10 * ms)  # 延迟10毫秒

        self.urukul0_ch1.set_att(self.atten)  # 将衰减写入urukul通道
        self.urukul0_ch1.sw.on()  # 打开urukul通道

        self.urukul0_ch1.set(self.freq, amplitude=self.amp)  # 将频率和幅度属性写入urukul通道，从而输出函数
        delay(self.t_pulse * s)  # 延迟由用户输入决定
        self.urukul0_ch1.sw.off()  # 关闭urukul通道
