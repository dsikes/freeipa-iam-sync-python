from utils import *
from pprint import pprint

# get a list of IAM users
iam_users = get_iam_user_list()

# get a list of IPA users
ipa_users = get_ipa_user_list()

# IAM is our source of truth.
# If a user is in IAM, but not in IPA, we add them to IPA.
# If a user is in IPA, but not in IAM, we remove them from IPA.
for user in iam_users:
    if user not in ipa_users:
        print('would add %s', user)
        user_props = get_iam_user_props(user)
        if user_props['props'] != False:
            ipa_add_user(user_props)
        else:
            # TODO: log invalid user
            # TODO: add validation lib to enforce schema
            print("invalid props for user %s" % user)

for user in ipa_users:
    if user != 'admin':
        if user not in iam_users:
            print('would remove %s' % user)