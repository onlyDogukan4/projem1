import unittest

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


class TestTelevision(unittest.TestCase):
    def test_turn_on(self):
        tv = Television("Sony", "Smart TV")
        tv.turn_on()
        self.assertTrue(tv.is_on)

    def test_turn_off(self):
        tv = Television("Samsung", "LED TV", is_on=True)
        tv.turn_off()
        self.assertFalse(tv.is_on)

    def test_set_channel(self):
        tv = Television("LG", "Ultra HD TV", is_on=True)
        tv.set_channel(5)
        self.assertEqual(tv.channel, 5)

    def test_increase_volume(self):
        tv = Television("Panasonic", "HD TV", is_on=True, volume=30)
        tv.increase_volume()
        self.assertEqual(tv.volume, 31)

    def test_decrease_volume(self):
        tv = Television("Toshiba", "LCD TV", is_on=True, volume=20)
        tv.decrease_volume()
        self.assertEqual(tv.volume, 19)

if __name__ == '__main__':
    unittest.main()
