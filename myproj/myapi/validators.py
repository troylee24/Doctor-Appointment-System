from rest_framework.validators import ValidationError

def validate_time_15(time):
    if time.minute % 15 != 0:
        raise ValidationError("Time must be an interval of 15 minutes")