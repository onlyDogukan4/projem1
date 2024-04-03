class Television:
    def __init__(self):
        self.current_channel=9

    def setChannel(self,new_channel):
        if new_channel != self.current_channel:
            self.current_channel=new_channel
        else:
            print("Already tuned to channel",new_channel)