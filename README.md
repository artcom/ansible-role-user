# User
Ansible role for configuring a user

# Requirements
* [check-required-variables](https://github.com/artcom/ansible-role-check-required-variables)

## Role Variables
Available variables are listed below, along with default values `(see defaults/main.yml)`:
```yaml
user_name: null
user_password: null
user_passwordless_sudo: true
user_authorized_keys: {}
```

Required variables (role will fail if the variables are not set):
```yaml
user_name: "string"
```

The user is created with given password, home folder and bash shell. User is added to sudo group and passwordless sudo is configured for that user. Public keys in `user_authorized_keys` are written to user's `~/.ssh/authorized_keys`.

## Test
### Requirements
- python >= 3.7
- docker

### Run
```bash
pip install -r requirements.txt
molecule test
```
