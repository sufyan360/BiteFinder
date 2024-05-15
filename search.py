from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LocationInputForm(FlaskForm):
    town = StringField("Location", validators=[DataRequired()], render_kw={"placeholder": "Enter Your Location"}, )
    get_location = SubmitField('Get Current Location')
    # (value, label)
    topic = SelectField("Search Topic",
                        choices=[("", "-- Please Select a Destination --"), ("Recycling Center", "Recycling Center"),
                                 ("Animal Adoption", "Animal Adoption"),
                                 ("Volunteer Locations", "Volunteer Locations")],
                        validators=[DataRequired(message="Please select a business type")])
    submit = SubmitField("Search")