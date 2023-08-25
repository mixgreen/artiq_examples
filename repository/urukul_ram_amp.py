from artiq.experiment import *  # 从实验库导入所有内容
from artiq.coredevice.ad9910 import RAM_DEST_ASF, RAM_MODE_BIDIR_RAMP  # 从AD9910资源中导入RAM目的地幅度缩放因子和RAM模式双向斜坡方法


# 这段代码演示了如何使用 urukul RAM。它产生一个频率为125MHz的脉冲，该脉冲在幅度上逐渐增加，保持固定幅度，然后再逐渐减小

class AD9910RAM(EnvExperiment):
    """Urukul RAM 演示：变幅度波形 """

    def build(self):  # 此代码在主机计算机上运行
        self.setattr_device("core")  # 将核心设备驱动程序设置为属性
        self.setattr_device("ttl6")  # 将ttl通道6设备驱动程序设置为属性
        self.u = self.get_device("urukul0_ch1")  # 设置urukul 0，通道1设备驱动程序为属性，并重命名对象self.u

    @kernel  # 此代码在FPGA上运行
    def run(self):

        # 处理用于导入RAM的数据
        n = 10  # 定义列表长度指数的变量n
        data = [0] * (1 << n)  # 声明列表为2^n的整数值
        for i in range(len(data) // 2):  # 将列表分为两半并分别定义
            data[i] = i << (32 - (n - 1))  # 第一半的数据斜率上升到最大振幅(机器单位)
            data[i + len(data) // 2] = 0xffff << 16  # 第二半数据保持最大振幅

        # 重置核心
        self.core.reset()

        # 初始化
        self.u.cpld.init()  # 初始化CPLD
        self.u.init()  # 初始化urukul通道
        delay(1 * ms)  # 1毫秒的延迟

        # 设置RAM的配置文件
        self.u.set_profile_ram(
            start=0, end=0 + len(data) - 1, step=1,
            profile=0, mode=RAM_MODE_BIDIR_RAMP)  # 设置在RAM中使用的配置文件

        self.u.cpld.set_profile(0)
        self.u.cpld.io_update.pulse_mu(8)  # 让 CPLD 寄存器采取写入它们的值
        delay(1 * ms)

        # 写入ram
        self.u.write_ram(data)  # 将数据列表写入ram
        delay(10 * ms)

        # 写入cfr
        self.u.set_cfr1(ram_enable=1, ram_destination=RAM_DEST_ASF)  # 写入CFR1(控制功能寄存器1)

        # 设置urukuln参数并打开通道
        self.u.set_frequency(125 * MHz)  # 设置频率
        self.u.cpld.io_update.pulse_mu(8)  # 让CPLD寄存器采取写入它们的值
        self.u.set_att(10 * dB)  # 设置衰减
        self.u.sw.on()  # 打开urukul通道

        self.core.break_realtime()  # 移动时间戳以防止下溢
        self.ttl6.output()  # 将TTL通道设置为输出
        self.core.break_realtime()  # 移动时间戳以防止下溢

        while True:  # 循环直到手动中断
            delay(1 * ms)

            with parallel:  # 并行执行以下代码
                self.ttl6.pulse(1 * us)  # 1微秒的TTL脉冲，用于触发示波器
                self.u.cpld.set_profile(0)  # profile 0告诉CPLD开始斜率上升

            delay(2 * us)

            with parallel:  # 并行执行以下代码
                self.ttl6.pulse(1 * us)  # 1微秒的TTL脉冲
                self.u.cpld.set_profile(1)  # profile 1告诉CPLD开始斜率下降
