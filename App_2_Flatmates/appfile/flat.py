import webbrowser

from fpdf import *


class Bill:
    """
    Object that contains data about a bill such as total amount and
    period of the bil.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in a flat
    and pays the share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = int(self.days_in_house) / int(int(self.days_in_house) + int(flatmate2.days_in_house))
        return int(bill.amount) * weight


