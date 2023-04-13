from flat import *


class PdfReport:
    """
    Creates a PDF file
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.image("files/Nova_icon.png", w=30, h=30)

        pdf.set_font(family="times", style="I", size=25)
        pdf.cell(w=500, h=80, txt="Flatmates Bill", align="C", ln=1)
        pdf.cell(w=100, h=50, txt="Period: ")
        pdf.cell(w=150, h=50, txt=bill.period, ln=1)
        pdf.cell(w=100, h=50, txt=flatmate1.name)
        pdf.cell(w=150, h=50, txt=str(round(flatmate1.pays(bill=the_bill, flatmate2=flatmate2), 2)), ln=1)
        pdf.cell(w=100, h=50, txt=flatmate2.name)
        pdf.cell(w=150, h=50, txt=str(round(flatmate2.pays(bill=the_bill, flatmate2=flatmate1), 2)), ln=1)

        pdf.output(self.filename + ".pdf")
        webbrowser.open(self.filename + ".pdf")


amount = int(input("Enter the Amount: "))
period = input("Enter the Period: ")
name1 = input("Enter your name: ")
days_in_house1 = int(input(f"How many days did {name1} stay in th house: "))
name2 = input("Enter the mates name: ")
days_in_house2 = int(input(f"How many days did {name2} stay in th house: "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)
print(f"{name1} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{name2} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))
report = PdfReport(f"{the_bill.period}.pdf")
report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
