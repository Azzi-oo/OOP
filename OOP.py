class PersonalComputer:
    def __init__(self, memory_size, disk_size, model, cpu):
        self.memory_size = memory_size
        self.disk_size = disk_size
        self.model = model
        self.cpu = cpu


class DesktopPC(PersonalComputer):
    def __init__(self, memory_size, disk_size, model, cpu, monitor, keyboard, mouse, dimensions):
        super().__init__(memory_size, disk_size, model, cpu)
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse
        self.dimensions = dimensions

    def display_info(self):
        print(f'Model: {self.model}, CPU: {self.cpu}, Memory: {self.memory_size}, Disk: {self.memory_size}')
        print(f'Monitor: {self.monitor}, Keyboard: {self.keyboard}, Mouse: {self.mouse}, Dimensions: {self.dimensions}')


class Laptop(PersonalComputer):
    def __init__(self,  memory_size, disk_size, model, cpu, monitor, keyboard, mouse, dimensions, screen_size):
        super().__init__(memory_size, disk_size, cpu)
        self.dimensions = dimensions
        self.screen_size = screen_size

    def display_info(self):
        print(f'Model: {self.model}, CPU: {self.cpu}, Memory: {self.memory_size}, Disk: {self.disk_size}')
        print(f'Dimensions: {self.dimensions}, Screen size: {self.screen_size}')
        
        
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        
class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, 'Male')
        
        
class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, 'Female')