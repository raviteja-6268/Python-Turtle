import phonenumbers as pn #pip install phonenumbers
from phonenumbers import carrier, geocoder, timezone
#phone number +91*********
phone = pn.parse('++919248781701 ')
# check validity of number
print(pn.is_valid_number(phone))
# telecom operator name
print(carrier.name_for_number(phone, 'en'))
# region name
print(geocoder.description_for_number(phone, 'en'))
# timezone of a number
print(timezone.time_zones_for_number(phone))