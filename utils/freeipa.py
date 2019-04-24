from python_freeipa import Client
from .config import get_config

config = get_config()

if 'IPA_HOST' not in config:
    raise Exception("UNABLE TO COMMUNICATE WITH FreeIPA HOST. Please set IPA_HOST env var.")

if 'IPA_USERNAME' not in config:
    raise Exception("UNABLE TO LOGIN. Please set IPA_USERNAME env var.")

if 'IPA_PASSWORD' not in config:
    raise Exception("UNABLE TO LOGIN. Please set IPA_PASSWORD env var.")

if 'IPA_GROUP' not in config:
    raise Exception("UNABLE TO MANAGE GROUP. Please set IPA_GROUP env var.")


ipa_server          = config['IPA_HOST']
ipa_group           = config['IPA_GROUP']
ipa_service_user    = config['IPA_USERNAME']
ipa_service_pass    = config['IPA_PASSWORD']

def get_ipa_client():
    client = Client(ipa_server, version='2.230', verify_ssl=False)
    client.login(ipa_service_user, ipa_service_pass)
    return client

def ensure_ipa_group():
    """ this function will ensure that the target group exist """
    client = get_ipa_client()
    try:
        g = client.group_show(ipa_group)
    except Exception as err:
        client.group_add(ipa_group)

def get_ipa_users():
    """ list users in the target group. """
    client = get_ipa_client()
    return client.group_show(ipa_group)


def add_user():
    """ add a user, and put the user in the target group """
    client = get_ipa_client()
    client.user_add()