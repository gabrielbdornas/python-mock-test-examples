def validate_age(age):
  if age < 0:
    raise ValueError("Age can not be less than 0")
