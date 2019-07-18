#
# name:
#

# First, the class definition
# Below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++


class Date(object):
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """Construct a Date with the given month, day, and year."""
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}/{:02d}/{:04d}".format(self.month, self.day, self.year)
        return s


    # Here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date, whether or ont they are in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def __eq__(self, d2):
        """ Overrides the == operator so that it declares two of the same dates in history as ==. This way, we don't need to use the awkward d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False
    
    def __lt__(self, d2):
        """ Returns true if the calling object is before d2. If they are the same day, return false.
        """
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month == d2.month:
                if self.day < d2.day:
                    return True
                else:
                    return False
            elif self.month < d2.month:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, d2):
        """ Returns true if the calling object is after d2. If they are the same day, return false.
        """
        if self.year > d2.year:
            return True
        elif self.year == d2.year:
            if self.month == d2.month:
                if self.day > d2.day:
                    return True
                else:
                    return False
            elif self.month > d2.month:
                return True
            else:
                return False
        else:
            return False

    def tomorrow(self):
        """ Returns nothing, but changes calling object to represent one calendar day after the date it originall represented.
        """
        fdays = 28 + self.isLeapYear() #because True literally == 1 in python
        daysmonth = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # first zero for simpler calling of list
        if self.day < daysmonth[self.month]:
            self.day += 1
        elif self.day == daysmonth[self.month]:
            self.day = 1
            if self.month < 12:
                self.month += 1
            elif self.month == 12:
                self.month = 1
                self.year += 1
            else:
                print("Somehow you've written a non-existant date.")
        else:
            print("Somehow you've written a non-existant date.")

    def yesterday(self):
        """ Returns nothing, but changes calling object to the day before.
        """
        fdays = 28 + self.isLeapYear() # works because True == 1 in python
        daysmonth = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # first zero for simpler calling of list
        if self.day > 1:
            self.day -= 1
        elif self.day == 1:
            if self.month > 1:
                self.day = daysmonth[self.month - 1]
                self.month -= 1
            elif self.month == 1:
                self.day = 31
                self.month = 12
                self.year -= 1
            else:
                print("Somehow you've written a non-existant date.")
        else:
            print("Somehow you've written a non-existant date.")

    def __iadd__(self, N):
        """ Only handles positive integers, and doesn't return, simply changes the calling object.
        """
        # print(self)
        while N > 0:
            self.tomorrow()
            # print(self)
            N -= 1
        return self

    def __isub__(self, N):
        """ Only handles positive ints, doesn't return, changes calling object.
        """
        # print(self)
        while N > 0:
            self.yesterday()
            # print(self)
            N -= 1
        return self

    def __ne__(self, d2):
        """ Returns True if not equal, False if equal.
        """
        return not self == d2

    def __sub__(self, d2):
        """ Returns an integer representing the number of days between self and d2 (aka returns self - d2)
        """
        self_copy = self.copy()
        count = 0
        if self < d2:
            while self_copy != d2:
                self_copy += 1
                count -= 1
            # print(count)
        else:
            while self_copy != d2:
                self_copy -= 1
                count += 1
            # print(count)
        return count

    def dow(self):
        """ Returns string that indicates day of week (dow) of object that calls it.
        """
        example = Date(7, 17, 2019) # Wednesday
        mod = (self - example) % 7
        days = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        if mod < 0:
            mod = abs(mod) - 7
            abs(mod)
        return days[mod]
#
# be sure to add code for the Date class ABOVE--inside the class definition
#





#
# lots of dates to work with...
#
# The nice this about putting them here is that they get redefined with each run
#   of the software (and this is needed for testing!)
#

d = Date(11, 13, 2018)    # Today?
d2 = Date(12, 21, 2018)   # winter break
ny = Date(1, 1, 2018)   # new year
nd = Date(1, 1, 2020)   # new decade
nc = Date(1, 1, 2100)   # new century
graduation = Date(5, 15, 2022)   # alter to suit!
vacation = Date(5, 17, 2019)     # ditto ~ summer break!
sm1 = Date(10, 28, 1929)    # stock market crash
sn2 = Date(10, 19, 1987)    # another s.m. crash: Mondays in Oct. are risky...
