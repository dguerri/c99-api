import os
from c99api import EndpointClient

api = EndpointClient(key=os.environ['C99API_KEY'], user_agent='my-user-agent')

response = api.emailvalidator(email='test@c99.nl', json=False)
print(response)