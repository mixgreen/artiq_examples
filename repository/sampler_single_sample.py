from artiq.experiment import *  # 从实验库导入所有内容


# 这段代码同时从8个采样器通道中取一次样本

class Sampler_Single_Sample(EnvExperiment):
    """单次采样器样本"""

    def build(self):  # 这段代码在宿主设备上运行

        self.setattr_device("core")  # 将核心设备驱动保存为属性
        self.setattr_device("sampler0")  # 将采样器设备驱动保存为属性

    @kernel  # 这段代码在FPGA上运行
    def run(self):
        self.core.reset()  # 重置核心设备

        self.core.break_realtime()  # 时间断点，以避免下溢条件
        self.sampler0.init()  # 初始化采样器

        for i in range(8):  # 对于每个采样器通道进行循环
            self.sampler0.set_gain_mu(i, 0)  # 将每个通道的增益设置为0db
            delay(100 * us)  # 延迟100微秒

        n_channels = 8  # 设置要读取的通道数
        # 更改此数字以改变要读取的通道数

        # 从最后一个通道开始读取
        # 如果你只使用1个通道，那就是通道7；2个通道则会使用6和7

        delay(5 * ms)  # 延迟5毫秒

        smp = [0.0] * n_channels  # 创建一个浮点数列表
        # 列表的长度为n_channels

        self.sampler0.sample(smp)  # 运行采样器并保存到列表

        for i in range(len(smp)):  # 循环遍历样本列表
            print(smp[i])  # 打印每个项目
