from utils import *


def lambda_handler(event, context):
    
    # this lambda function will sync IAM with FreeIPA
    # the initial operation will check the list of users inside of IAM against FreeIPA
    # if there is a user in IAM that is NOT in FreeIPA the user (and public key) will then be added to FreeIPA
    # if there is a user in FreeIPA that is NOT in IAM the user is removed from FreeIPA.
    
    
    # users = {}
    # iam_users = get_iam_user_list()
    # for user in iam_users:
    #     users[user] = {}
    #     ssh_keys = get_iam_ssh_keys_by_user(user)
        
    #     if not ssh_keys:
    #         users[user]['ssh_keys'] = []
    #     else:
    #         users[user]['ssh_keys'] = ssh_keys

    users = get_ipa_users()
    print(users)
            
    return {
        'statusCode': 200,
        'body': {
            'users': users
        }
    }
