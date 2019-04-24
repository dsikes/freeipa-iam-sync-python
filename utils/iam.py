import boto3

def get_iam_client():
    return boto3.client('iam')

def get_iam_user_list():
    iam = get_iam_client()
    users = iam.list_users()
    user_list = []
    for user in users['Users']:
        user_list.append(user['UserName'])
    return user_list

def get_iam_user(username):
    iam = get_iam_client()
    return iam.get_user(UserName=username)

def get_iam_public_key_ids_by_user(username):
    iam = get_iam_client()
    public_key_id_list = []
    public_key_ids = iam.list_ssh_public_keys(UserName=username)
    print(public_key_ids)
    if len(public_key_ids['SSHPublicKeys']) > 0:
        for pk in public_key_ids['SSHPublicKeys']:
            if pk['Status'] == 'Active':
                public_key_id_list.append(pk['SSHPublicKeyId'])
                
            return public_key_id_list
    return False

def get_iam_ssh_key_by_user_public_key_id(username, ssh_public_key_id):
    iam = get_iam_client()
    key = iam.get_ssh_public_key(
        UserName=username,
        SSHPublicKeyId=ssh_public_key_id,
        Encoding='SSH'
    )
    if 'SSHPublicKey' in key:
        return key
    return False

def get_iam_ssh_keys_by_user(username):
    ssh_keys = []
    ssh_public_key_id_list = get_iam_public_key_ids_by_user(username)
    if ssh_public_key_id_list:
        for ssh_public_key_id in ssh_public_key_id_list:
            ssh_key = get_iam_ssh_key_by_user_public_key_id(username, ssh_public_key_id)
            if ssh_key:
                ssh_keys.append(ssh_key['SSHPublicKey']['SSHPublicKeyBody'])
    return ssh_keys