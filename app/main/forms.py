from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,TextAreaField
from wtforms.validators import Required,Length

class PitchForm(FlaskForm):
    CATEGORIES=[('pickup lines', 'pickup lines'), ('interview pitch', 'interview pitch'), ('product pitch', 'product pitch'), ('promotion pitch', 'promotion pitch')]
    title=StringField('Title', validators=[Required(), Length(1, 255)])
    categories=SelectField("categories",choices=CATEGORIES)
    pitch=TextAreaField("Pitch",validators=[Required()])
    submit = SubmitField('Submit')
