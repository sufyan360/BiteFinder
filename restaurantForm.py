from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LocationInputForm(FlaskForm):
    location = StringField("Location", validators=[DataRequired()], render_kw={"placeholder": "123 Somewhere Avenue"}, )
    get_location = SubmitField('Get Current Location')
    # (value, label)
    topic = RadioField("Search Topic",
                        choices=[("Breakfast", "Breakfast"), ("Dinner", "Dinner"),
                                 ("Fast Food", "Fast Food"), ("Mexican", "Mexican"),
                                 ("South Asian", "South Asian"),("East Asian", "East Asian"),
                                 ("Italian", "Italian"), ("Burgers", "Burgers"),
                                 ("Dessert", "Dessert"), ("Random", "Random"),])
    submit = SubmitField("Search")
