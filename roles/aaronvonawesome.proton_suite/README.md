# Role Name: proton_suite

This Ansible Role that will install the Proton (proton.me) .deb packages for the applications you select.

***Note: Currently only has the option to install the [Proton Mail Brdige](https://github.com/ProtonMail/proton-bridge)***

## Requirements

- Debian-based system.

## Role Variables

### var_proton_suite_should_install_proton_mail_bridge

***default:*** false

Set to `true` in order to install Proton Mail Bridge DEB package.

*Note:* Since Proton Mail Bridge updates itself, if Proton Mail Bridge is already installed, this role will **not** install Proton Mail Bridge again.

## Dependencies

- N/A

## Example Playbook

```yaml
---
- name: "Install Proton Suite Playbook Example"
  hosts:
    - all
  become: true


  tasks:

    - name: "Install Proton Mail Bridge DEB Package please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.proton_suite"
      vars:
        var_proton_suite_should_install_proton_mail_bridge: true
```

## License

AGPL-3.0-or-later

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
