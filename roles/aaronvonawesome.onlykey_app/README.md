# Role Name: onlykey_app

This Ansible Role that will install the [OnlyKey App](https://github.com/trustcrypto/OnlyKey-App) from [CryptoTrust](https://crp.to/).

## Requirements

- Debian-based system.

## Role Variables

- N/A

## Dependencies

- N/A

## Example Playbook

```yaml
---
- name: "Install OnlyKey App Playbook Example"
  hosts:
    - all
  become: true


  tasks:

    - name: "Install onlykey_app on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.onlykey_app
```

## License

BSD

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
