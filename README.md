# User
Ansible role for configuring deployment user

## Role Variables
Available variables are listed below, along with default values `(see defaults/main.yml)`:
```yaml
user_name: "{{ ansible_user }}"
user_password: superSekret
user_passwordless_sudo: true
```

Deployment user is created with given password, home folder and bash shell. User is added to sudo group and passwordless sudo is configured for that user.
