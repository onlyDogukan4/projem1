class Widget:
    def __init__(self):
        self._msg="hello , I'am a widget"

    def replace(self):
        index=self.index("w")
        self._msg[index]="g"
    def __str__(self):
    print("my str is: "+self._msg)
    