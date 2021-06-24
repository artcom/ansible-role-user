from default.common.test_common import *  # noqa: F401,F403


def test_new_user_default(host):
    new_user = host.user('new_user')
    password_hash = {
        'focal': '$6$822162$fYIIHK7s4Tzh6xgGd9VApwg3SPILq/BgAcB7ZB1PF2LYrVC8h'
                 '7pJP1D3iFl.235y9w1mmPwz4wzpwoeDguCxj0',
        'buster': '$6$496895$t/heuOZjcNNJv.LND58guuROWQSl.bZR4xT9jaCVVFsv7o4C'
                  'wYjcmiBpP8FemyrCKb1MuAjuWtpcYdftsQLLJ1'
    }

    assert new_user.password == password_hash[host.system_info.codename]
