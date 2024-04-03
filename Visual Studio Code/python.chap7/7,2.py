class Television:
    """
    A class representing a television.

    Attributes:
        brand (str): The brand of the television.
        model (str): The model of the television.
        current_channel (int): The current channel the television is tuned to.
        volume (int): The current volume level of the television.
    """

    def __init__(self, brand, model):
        """
        Initialize a new Television object.

        Args:
            brand (str): The brand of the television.
            model (str): The model of the television.
        """
        self.brand = brand
        self.model = model
        self.current_channel = 1
        self.volume = 50

    def volumeUp(self, increment=5):
        """
        Increase the volume of the television.

        Args:
            increment (int, optional): The amount by which to increase the volume.
                Default is 5.

        Returns:
            str: A message indicating the new volume level.
        """
        self.volume += increment
        return f"Volume increased to {self.volume}."

    def jumpPrevChannel(self):
        """
        Switch to the previous channel.

        Returns:
            str: A message indicating the new channel.
        """
        if self.current_channel > 1:
            self.current_channel -= 1
        else:
            self.current_channel = 1
        return f"Switched to channel {self.current_channel}."