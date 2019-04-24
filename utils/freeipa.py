import os
from python_freeipa import Client

if 'IPA_HOST' not in os.environ:
    raise Exception("UNABLE TO COMMUNICATE WITH FreeIPA HOST. Please set IPA_HOST env var.")

ipa_server = os.environ['IPA_HOST']

def get_ipa_client():
    return Client(ipa_server, version='4.6.4')

def get_ipa_users():
    pass