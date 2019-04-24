from python_freeipa import Client
from .config import get_config


config = get_config()

if 'IPA_HOST' not in config:
    raise Exception("UNABLE TO COMMUNICATE WITH FreeIPA HOST. Please set IPA_HOST config value.")

if 'IPA_USERNAME' not in config:
    raise Exception("UNABLE TO LOGIN. Please set IPA_USERNAME config value.")

if 'IPA_PASSWORD' not in config:
    raise Exception("UNABLE TO LOGIN. Please set IPA_PASSWORD config value.")

if 'IPA_SUDO_GROUP' not in config:
    raise Exception("UNABLE TO MANAGE SUDO GROUP. Please set IPA_SUDO_GROUP config value.")

ipa_server          = config['IPA_HOST']
ipa_sudo_group      = config['IPA_SUDO_GROUP']
ipa_service_user    = config['IPA_USERNAME']
ipa_service_pass    = config['IPA_PASSWORD']

def get_ipa_client():
    client = Client(ipa_server, version='2.230', verify_ssl=False)
    client.login(ipa_service_user, ipa_service_pass)
    return client

def ensure_ipa_sudo_group():
    """ this function will ensure that the sudo group exist """
    client = get_ipa_client()
    try:
        g = client.group_show(ipa_sudo_group)
    except Exception as err:
        client.group_add(ipa_sudo_group)

def get_ipa_sudo_users():
    """ list users in the sudo group. """
    client = get_ipa_client()
    return client.group_show(ipa_sudo_group)

def get_ipa_users():
    """ list all users in free ipa """
    users = []
    client = get_ipa_client()
    for user in client.user_find(''):
        print(user)
    return users

def add_user(username, first_name, last_name, fullname, email, ssh_keys):
    """ add a user to free ipa"""
    client = get_ipa_client()
    try:
        client.user_add(username, first_name, last_name, fullname, mail=email, ssh_key=ssh_keys)
    except Exception as err:
        # TODO: handle this critical error
        print(str(err))
        return False    
    return True

def del_user(username):
    """ removes a user from free ipa """
    client = get_ipa_client()
    try:
        client.user_del(username)
    except Exception as err:
        # TODO: handle this critical error
        print(str(err))
        return False
    return True