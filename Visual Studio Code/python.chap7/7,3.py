class Television:
    def __init__(self, brand, model, is_on=False, channel=1, volume=50):
        self.brand = brand
        self.model = model
        self.is_on = is_on
        self.channel = channel
        self.volume = volume

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, channel):
        if self.is_on:
            self.channel = channel
        else:
            print("The TV is off. Turn it on to set the channel.")

    def increase_volume(self):
        if self.is_on:
            self.volume += 1
        else:
            print("The TV is off. Turn it on to adjust the volume.")

    def decrease_volume(self):
        if self.is_on:
            self.volume -= 1
        else:
            print("The TV is off. Turn it on to adjust the volume.")
