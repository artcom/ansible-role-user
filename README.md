# User
Ansible role for configuring deployment user

## Role Variables
Available variables are listed below, along with default values `(see defaults/main.yml)`:
```yaml
user_name: "{{ ansible_user }}"
user_password: superSekret
user_passwordless_sudo: true
user_authorized_keys: {}
```

Deployment user is created with given password, home folder and bash shell. User is added to sudo group and passwordless sudo is configured for that user. Public keys in `user_authorized_keys` are written to user's `~/.ssh/authorized_keys`.

## Test
### Requirements
- python >= 3.7
- vagrant
- virtualbox

### Run
```bash
pip install -r requirements.txt
molecule test
```
