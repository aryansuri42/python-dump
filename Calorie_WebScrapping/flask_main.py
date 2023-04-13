from tokenize import String
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField
from flask.views import MethodView
from calorie import CalorieCalculator
from temp import Temperature

app = Flask(__name__)

class Homepage(MethodView):
    
    def get(self):
        return render_template('index.html')

class CalorieFormPage(MethodView):
    def get(self):
        calorie_form = CalorieForm()
        return render_template('calorieform.html', calorieform = calorie_form)
    
    def post(self):
        calorieform = CalorieForm(request.form)
        temperature = Temperature(city = calorieform.city.data, country= calorieform.country.data)
        temp = temperature.get()
        calorie = CalorieCalculator(float(calorieform.weight.data), float(calorieform.height.data), float(calorieform.age.data), temp)
        calories = calorie.calorieintake()
        return render_template('calorieform.html',calorieform = calorieform, calories = calories, result = True)
    
    
class CalorieForm(Form):
    name = StringField('Name ', default='Mehar')
    weight = StringField('Weight ', default='100')
    height = StringField('Height ', default='80')
    age = StringField('Age ', default='80')
    country = StringField('Country ',default='Japan')
    city = StringField('City ', default='Tokyo')
    
    button = SubmitField('Calculate')



app.add_url_rule("/",view_func=Homepage.as_view('homepage'))
app.add_url_rule("/form",view_func=CalorieFormPage.as_view('calorieform'))
app.run(debug=True)