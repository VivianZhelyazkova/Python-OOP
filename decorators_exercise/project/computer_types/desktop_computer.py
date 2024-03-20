from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }
    MAX_RAM = 128
    VALID_RAM_SIZES = [2, 4, 8, 16, 32, 64, 128]

    def configure_computer(self, processor: str, ram: int):
        if processor not in DesktopComputer.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in DesktopComputer.VALID_RAM_SIZES:
            raise ValueError(
                f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price += DesktopComputer.AVAILABLE_PROCESSORS[processor] + (DesktopComputer.VALID_RAM_SIZES.index(ram)+ 1) * 100
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
