from django.core.exceptions import ValidationError
def validateText(text):
    if text == 'abc':
        raise ValidationError("new wrong")
    return text