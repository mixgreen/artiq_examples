# Autogenerated for the ustc13 variant
core_addr = "192.168.1.88"

device_db = {
    "core": {
        "type": "local",
        "module": "artiq.coredevice.core",
        "class": "Core",
        "arguments": {"host": core_addr, "ref_period": 1e-09, "target": "rv32g"},
    },
    "core_log": {
        "type": "controller",
        "host": "::1",
        "port": 1068,
        "command": "aqctl_corelog -p {port} --bind {bind} " + core_addr
    },
    "core_moninj": {
        "type": "controller",
        "host": "::1",
        "port_proxy": 1383,
        "port": 1384,
        "command": "aqctl_moninj_proxy --port-proxy {port_proxy} --port-control {port} --bind {bind} " + core_addr
    },
    "core_cache": {
        "type": "local",
        "module": "artiq.coredevice.cache",
        "class": "CoreCache"
    },
    "core_dma": {
        "type": "local",
        "module": "artiq.coredevice.dma",
        "class": "CoreDMA"
    },

    "i2c_switch0": {
        "type": "local",
        "module": "artiq.coredevice.i2c",
        "class": "I2CSwitch",
        "arguments": {"address": 0xe0}
    },
    "i2c_switch1": {
        "type": "local",
        "module": "artiq.coredevice.i2c",
        "class": "I2CSwitch",
        "arguments": {"address": 0xe2}
    },
}

# standalone peripherals

device_db["ttl0"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLInOut",
    "arguments": {"channel": 0x000000},
}

device_db["ttl1"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLInOut",
    "arguments": {"channel": 0x000001},
}

device_db["ttl2"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLInOut",
    "arguments": {"channel": 0x000002},
}

device_db["ttl3"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLInOut",
    "arguments": {"channel": 0x000003},
}

device_db["ttl4"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000004},
}

device_db["ttl5"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000005},
}

device_db["ttl6"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000006},
}

device_db["ttl7"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000007},
}

device_db["ttl8"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000008},
}

device_db["ttl9"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000009},
}

device_db["ttl10"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x00000a},
}

device_db["ttl11"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x00000b},
}

device_db["ttl12"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x00000c},
}

device_db["ttl13"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x00000d},
}

device_db["ttl14"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x00000e},
}

device_db["ttl15"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x00000f},
}

device_db["eeprom_urukul0"] = {
    "type": "local",
    "module": "artiq.coredevice.kasli_i2c",
    "class": "KasliEEPROM",
    "arguments": {"port": "EEM2"}
}

device_db["spi_urukul0"] = {
    "type": "local",
    "module": "artiq.coredevice.spi2",
    "class": "SPIMaster",
    "arguments": {"channel": 0x000010}
}

device_db["ttl_urukul0_io_update"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000011}
}

device_db["ttl_urukul0_sw0"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000012}
}

device_db["ttl_urukul0_sw1"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000013}
}

device_db["ttl_urukul0_sw2"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000014}
}

device_db["ttl_urukul0_sw3"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000015}
}

device_db["urukul0_cpld"] = {
    "type": "local",
    "module": "artiq.coredevice.urukul",
    "class": "CPLD",
    "arguments": {
        "spi_device": "spi_urukul0",
        "sync_device": None,
        "io_update_device": "ttl_urukul0_io_update",
        "refclk": 125000000.0,
        "clk_sel": 2
    }
}
device_db["urukul0_ch0"] = {
    "type": "local",
    "module": "artiq.coredevice.ad9910",
    "class": "AD9910",
    "arguments": {
        "pll_n": 32,
        "chip_select": 4,
        "cpld_device": "urukul0_cpld",
        "sw_device": "ttl_urukul0_sw0"
    }
}

device_db["urukul0_ch1"] = {
    "type": "local",
    "module": "artiq.coredevice.ad9910",
    "class": "AD9910",
    "arguments": {
        "pll_n": 32,
        "chip_select": 5,
        "cpld_device": "urukul0_cpld",
        "sw_device": "ttl_urukul0_sw1"
    }
}

device_db["urukul0_ch2"] = {
    "type": "local",
    "module": "artiq.coredevice.ad9910",
    "class": "AD9910",
    "arguments": {
        "pll_n": 32,
        "chip_select": 6,
        "cpld_device": "urukul0_cpld",
        "sw_device": "ttl_urukul0_sw2"
    }
}

device_db["urukul0_ch3"] = {
    "type": "local",
    "module": "artiq.coredevice.ad9910",
    "class": "AD9910",
    "arguments": {
        "pll_n": 32,
        "chip_select": 7,
        "cpld_device": "urukul0_cpld",
        "sw_device": "ttl_urukul0_sw3"
    }
}

device_db["eeprom_urukul1"] = {
    "type": "local",
    "module": "artiq.coredevice.kasli_i2c",
    "class": "KasliEEPROM",
    "arguments": {"port": "EEM4"}
}

device_db["spi_urukul1"] = {
    "type": "local",
    "module": "artiq.coredevice.spi2",
    "class": "SPIMaster",
    "arguments": {"channel": 0x000016}
}

device_db["ttl_urukul1_io_update"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000017}
}

device_db["ttl_urukul1_sw0"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000018}
}

device_db["ttl_urukul1_sw1"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000019}
}

device_db["ttl_urukul1_sw2"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x00001a}
}

device_db["ttl_urukul1_sw3"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x00001b}
}

device_db["urukul1_cpld"] = {
    "type": "local",
    "module": "artiq.coredevice.urukul",
    "class": "CPLD",
    "arguments": {
        "spi_device": "spi_urukul1",
        "sync_device": None,
        "io_update_device": "ttl_urukul1_io_update",
        "refclk": 125000000.0,
        "clk_sel": 2
    }
}

device_db["urukul1_ch0"] = {
    "type": "local",
    "module": "artiq.coredevice.ad9910",
    "class": "AD9910",
    "arguments": {
        "pll_n": 32,
        "chip_select": 4,
        "cpld_device": "urukul1_cpld",
        "sw_device": "ttl_urukul1_sw0"
    }
}

device_db["urukul1_ch1"] = {
    "type": "local",
    "module": "artiq.coredevice.ad9910",
    "class": "AD9910",
    "arguments": {
        "pll_n": 32,
        "chip_select": 5,
        "cpld_device": "urukul1_cpld",
        "sw_device": "ttl_urukul1_sw1"
    }
}

device_db["urukul1_ch2"] = {
    "type": "local",
    "module": "artiq.coredevice.ad9910",
    "class": "AD9910",
    "arguments": {
        "pll_n": 32,
        "chip_select": 6,
        "cpld_device": "urukul1_cpld",
        "sw_device": "ttl_urukul1_sw2"
    }
}

device_db["urukul1_ch3"] = {
    "type": "local",
    "module": "artiq.coredevice.ad9910",
    "class": "AD9910",
    "arguments": {
        "pll_n": 32,
        "chip_select": 7,
        "cpld_device": "urukul1_cpld",
        "sw_device": "ttl_urukul1_sw3"
    }
}

device_db["phaser0"] = {
    "type": "local",
    "module": "artiq.coredevice.phaser",
    "class": "Phaser",
    "arguments": {
        "channel_base": 0x00001c,
        "miso_delay": 1,
    }
}

device_db["led0"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000021}
}

device_db["led1"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000022}
}