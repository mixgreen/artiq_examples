from artiq.experiment import *  # 从artiq实验库导入所有内容


# 本代码展示了如何使用TTL脉冲(channel0)来触发另一个事件。
# 在这段代码中，被触发的事件是另一个ttl脉冲
# 但这个原理也可以用于触发一个实验序列。

# 脉冲之间的间隔为5.158微秒，抖动约为1纳秒

class TTL_Input_As_Trigger(EnvExperiment):
    """TTL 输入边缘作为触发器"""

    def build(self):  # 将设备驱动程序添加为属性，并将键添加到内核不变量中
        self.setattr_device("core")  # 将核心设备的驱动设置为属性
        self.setattr_device("ttl0")  # 将TTL0的驱动设置为属性
        self.setattr_device("ttl6")  # 将TTL6的驱动设置为属性

    @kernel  # 这段代码在FPGA上运行
    def run(self):
        self.core.reset()  # 重置核心设备

        self.ttl0.input()  # 设置TTL0为输入
        self.ttl6.output()  # 设置TTL6为输出

        delay(1 * us)  # 延迟1微秒，使用触发时需要，如果移除不会给出错误

        t_end = self.ttl0.gate_rising(10 * ms)  # 在TTL0上打开门以便在10ms内检测到上升沿
        # 将t_end变量设置为停止检测的时间（以MU为单位）

        t_edge = self.ttl0.timestamp_mu(t_end)  # 将t_edge变量设置为检测到的第一个边缘的时间（以MU为单位）
        # 如果没有检测到边缘，将t_edge设置为-1

        if t_edge > 0:  # 如果检测到了边缘
            at_mu(t_edge)  # 将时间游标设置到边缘的位置
            delay(5 * us)  # 延迟5微秒，以防止下溢
            self.ttl6.pulse(5 * ms)  # 在TTL6上输出5ms的脉冲

        self.ttl0.count(t_end)  # 丢弃剩余的边缘并关闭门
