class Date:
    monthNames = ('January', 'February', 'March',
    'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December')
    def __init__(self):
    # By default: January 1, 2000
        self.month = 1
        self.day = 1
        self.year = 2000
    def getDay(self):
        return(int(self.day))
    def setYear(self,year):
        print(int(self.year))
        self.year=year
        print(int(year))

    def __str__(self):
        return f"{mydate.monthNames[self.month-1]} {self.day} {self.year}"
    
    
mydate=Date()
print(mydate.setYear(2013))
print(mydate.getDay())
print(mydate.__str__())