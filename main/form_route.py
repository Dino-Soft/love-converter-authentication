from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, TextField
from wtforms import validators
from wtforms.fields.html5 import EmailField


class UserRegistration(FlaskForm):

    # Username validation function
    def validator_field(form, field):
        # Verify that it does not contain underscores or hashtag
        if (field.data.find("_") != -1) or (field.data.find("#") != -1):
            # Show validation error
            raise validators.ValidationError("The field can only contain letters and numbers")

    def optional(field):
        field.validators.insert(0, validators.Optional())

    user = TextField('Username',
                     [
                         validators.Required(message="fill the field with an username"),
                         validators.length(min=4, max=25, message='The length of the username is not valid'),
                         validator_field
                     ])

    password = PasswordField('Password',
                             [
                                 validators.Required(),
                                 validators.length(min=12, message="The password must be more than 12 characters"),
                                 validators.EqualTo("confirm", message="Password does not match")
                             ])

    confirm = PasswordField("Repeat password")

    email = EmailField('Email',
                       [
                           validators.Required(message="fill the field with an email"),
                           validators.Email(message='Wrong email format')
                       ])

    # Definition of submit field
    submit = SubmitField("Send")
