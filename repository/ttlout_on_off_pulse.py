from artiq.experiment import *  # 从artiq实验库导入所有内容


# 使用TTL6的最简工作代码
# 打开输出、关闭输出，然后脉冲输出

# 要在示波器上查看此痕迹，使用单一触发，并确保示波器上至少测量16ms

class TTL_Output_On_Off_Pulse(EnvExperiment):
    """TTL 输出 打开、关闭、脉冲"""

    def build(self):  # 这段代码在宿主设备上运行
        self.setattr_device("core")  # 将核心设备驱动设置为属性
        self.setattr_device("ttl6")  # 将ttl6设备驱动设置为属性

    @kernel  # 这段代码在FPGA上运行
    def run(self):
        self.core.reset()  # 重置核心设备
        self.ttl6.output()  # 设置 TTL6 为输出状态
        delay(1 * us)  # 将时间戳向前移动，以防止ttl6.output和ttl6.on之间的冲突，尽管在这种情况下似乎不是必要的。
        self.ttl6.on()  # 设置 TTL6 输出为高电平
        delay(2 * s)  # 延迟2s
        self.ttl6.off()  # 设置 TTL6 输出为低电平
        delay(2 * s)  # 延迟2s
        self.ttl6.pulse(2 * s)  # TTL6 输出高电平 2s 然后设置为低电平
        delay(2 * s)  # 延迟2s
