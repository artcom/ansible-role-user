def test_new_user(host):
    new_user = host.user('new_user')
    password_hash = {
        'focal': '$6$933933$3/860wLZBSxhXgXkVaYu4myqIWVayD8ZpBU1L0/A/QS3LKERM'
                 '5gINeYu/q8Z9o4v1dqqGuQUuLsIvDQTsw4hG1',
        'buster': '$6$411421$d6Cd6W.l.LPibI2.oM7MQJ3rdS4VgpKmCGrHv/t5XIwVHoTM'
                  'G6LAe2/AnQBnWOfiY3IdJNs1JkLCWAy2QS1bN1'
    }

    assert new_user.home == '/home/new_user', new_user.home
    assert new_user.shell == '/bin/bash'
    assert 'sudo' in new_user.groups
    assert new_user.password == password_hash[host.system_info.codename]


def test_user_passwordless_sudo(host):
    new_user_sudoers_file = host.file('/etc/sudoers.d/new_user')
    file_content = 'new_user ALL=(ALL) NOPASSWD:ALL'

    assert new_user_sudoers_file.exists
    assert new_user_sudoers_file.user == 'root'
    assert new_user_sudoers_file.group == 'root'
    assert oct(new_user_sudoers_file.mode) == '0o440'
    assert new_user_sudoers_file.content_string == file_content


def test_user_authorized_keys(host):
    authorized_keys_file = host.file('/home/new_user/.ssh/authorized_keys')
    keys = [
        'ssh-rsa NEWUSERPUBKEY== new_user',
        'ssh-rsa ADMINUSERPUBKEY== admin_user\n'
    ]
    new_user_keys = '\n'.join(keys)

    assert authorized_keys_file.exists
    assert authorized_keys_file.user == 'new_user'
    assert authorized_keys_file.group == 'new_user'
    assert authorized_keys_file.content_string == new_user_keys
