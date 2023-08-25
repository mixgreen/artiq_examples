from artiq.experiment import *  # 导入全部的artiq实验库内容


# 本程序是最简单的操作 led0 的示例代码，有以下两点目的：
# 1. 演示 LED 的开、关和脉冲操作，这是操作 artiq 最简单的部分；
# 2. 演示 artiq 实验程序的基本结构（麻雀虽小，五脏俱全。重点关注 build 、run 他们是通用的）；

class LED_On_Off_Pulse(EnvExperiment):
    """LED 开启、关闭和脉冲"""

    def build(self):  # 将设备驱动添加为属性，并将关键字设为内核不变量
        """
        任何实验之前，都得让电脑和测控设备建立连接。
        这一步，通过 build 方法实现。
        """
        # 父类 HasEnvironment 中提供setattr_device 方法，
        # 用于将关键字添入 kernel_invariants (代表了仪本次实验占用的仪器资源)。

        self.setattr_device("core")  # core 代表了 artiq 仪器的内核，所有的实验都必须连接该模块。
        self.setattr_device("led0")  # led0 指向 artiq 仪器上的 led 灯（在device_db.py 里可见）

    @kernel  # 这部分代码将在 FPGA 上执行
    def run(self):
        # 上面完成 build 之后，core 和 led0 都成为了本次实验的属性
        self.core.reset()  # 对核心设备进行重置

        self.core.break_realtime()  # 避免时间下溢，将时间戳稍微向前移
        # 这同样可以通过固定的延迟来达到

        self.led0.on()  # 开启led0
        delay(5 * s)  # 延迟5秒

        self.led0.off()  # 关闭led0
        delay(5 * s)  # 再延迟5秒

        self.led0.pulse(5 * s)  # LED脉冲5秒，之后自动关闭

