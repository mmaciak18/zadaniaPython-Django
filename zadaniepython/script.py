import re
import datetime

class Date:
    date = None
    regex = r"^[0-2]{0,1}[0-9]{1,3}[/][0-2]{0,1}[0-9]{1,3}[/][0-2]{0,1}[0-9]{1,3}$"
    def __init__(self, date):
        self.date = date

    def parse(self):
        if re.match(self.regex, self.date):
            date = self.date.split('/')
            try:
                d = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            except ValueError:
                try:
                    d = datetime.date(int(date[2]), int(date[1]), int(date[0]))
                except ValueError:
                    try:
                        d = datetime.date(int(date[1]), int(date[0]), int(date[2]))
                    except ValueError:
                        try:
                            d = datetime.date(int(date[2]), int(date[0]), int(date[1]))
                        except ValueError:
                            try:
                                d = datetime.date(int(date[0]), int(date[2]), int(date[1]))
                            except ValueError:
                                try:
                                    d = datetime.date(int(date[1]), int(date[2]), int(date[0]))
                                except ValueError:
                                    print ("Illegal date")
                                    return False

            if d.year < 1000:
                print (datetime.date(d.year + 2000, d.month, d.day))
            elif d.year < 2000:
                print (datetime.date(2000, d.month, d.day))
            else:
                print (d)
            return True;
        else:
            print("Illegal number")
            return False


f = open('date.txt', 'r')
test = Date(f.read())
test.parse()
f.close()
