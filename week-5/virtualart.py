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