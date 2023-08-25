from artiq.experiment import *  # 从artiq实验库导入所有内容


# 此代码从TTL0读取一次并打印电压值

class TTL_Input_Read(EnvExperiment):
    """TTL 输入读取"""

    def build(self):  # 这段代码在宿主设备上运行
        self.setattr_device("core")  # 将核心设备的驱动设置为属性
        self.setattr_device("ttl0")  # 将TTL0的驱动设置为属性

    @kernel  # 这段代码在FPGA上运行
    def run(self):
        self.core.reset()  # 重置核心设备

        self.ttl0.input()  # 设置TTL0为输入

        self.core.break_realtime()  # 将时间戳向前移动，以防止下溢
        # 也可以通过固定的延迟来实现

        self.ttl0.sample_input()  # 读取TTL0的当前值
        input_value = self.ttl0.sample_get()  # 将TTL0的值存储为 input_value 变量
        print(input_value)  # 打印 input_value 变量的值
