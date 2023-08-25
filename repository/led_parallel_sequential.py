from artiq.experiment import *  # 从artiq实验库导入所有内容

# 使用 parallel 和 sequential 的示例代码

class LED_Parallel(EnvExperiment):
    """LED并行操作"""

    def build(self):  # 将设备驱动添加为属性，并将键添加到内核不变量中
        self.setattr_device("core")  # 所有构建中都需要
        self.setattr_device("led0")  # 使用led0时需要
        self.setattr_device("led1")  # 使用led1时需要

    @kernel  # 这段代码在FPGA上运行
    def run(self):
        self.core.reset()  # 重置核心设备

        self.core.break_realtime()  # 将时间戳向前移动，以防止下溢
        # 也可以通过固定的延迟来实现

        with parallel:  # 指示核心设备并行运行包含的代码
            self.led0.pulse(4 * s)  # led0亮4秒，然后熄灭

            with sequential:  # 指示核心设备顺序运行包含的代码
                self.led1.pulse(2 * s)  # led1亮2秒，然后熄灭
                delay(2 * s)  # 延迟2秒
