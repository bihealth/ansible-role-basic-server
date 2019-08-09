[![Build Status](https://travis-ci.org/bihealth/ansible-role-basic-server.svg?branch=master)](https://travis-ci.org/bihealth/ansible-role-basic-server)

# Basic Server Setup

This Ansible role performs basic server setup such as:

- on CentOS/RedHat, activate EPEL repository,
- setup of en_US.UTF-8 locale,
- installation of some minimal admin packages (htop, vim, ...).

## Requirements

none

## Role Variables

none

## Dependencies

none

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
    - role: bihealth.basic_server
```

## License

MIT

## Author Information

- Manuel Holtgrewe

Created with love at [CUBI](https://www.cubi.bihealth.org).
