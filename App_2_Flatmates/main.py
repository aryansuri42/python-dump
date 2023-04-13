from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from appfile import flat

app = Flask(__name__)


class Homepage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)


class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)
        the_bill = flat.Bill(billform.amount.data, billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data, int(billform.days1.data))
        flatmate2 = flat.Flatmate(billform.name2.data, int(billform.days2.data))
        return render_template('results.html', name1=flatmate1.name,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name, amount2=flatmate2.pays(the_bill, flatmate1))


class BillForm(Form):
    amount = StringField("Bill Amount: ", default="2000")
    period = StringField("Period(March 2022): ", default="March 2022")
    flatmate1 = StringField("First Flatmate Details")
    name1 = StringField("Name: ", default="John")
    days1 = StringField("Days Stayed: ", default="25")
    flatmate2 = StringField("Second Flatmate Details")
    name2 = StringField("Name: ", default="Marry")
    days2 = StringField("Days Stayed: ", default="20")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=Homepage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))
app.run(debug=True)
