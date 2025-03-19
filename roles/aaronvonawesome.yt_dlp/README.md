# Role Name: yt_dlp

This Ansible Role will install [yt-dlp](https://github.com/yt-dlp/yt-dlp) using the [yt-dlp Personal Package Archive (PPA) from tomtomtom](https://launchpad.net/~tomtomtom/+archive/ubuntu/yt-dlp).

## Requirements

- Ubuntu-based system.

## Role Variables

### yt_dlp_var_lts_codename

***default:*** noble

Set the codename for the version (or base version) of Ubuntu you will be using.

## Dependencies

- N/A

## Example Playbook

```yaml
---
- name: "Install yt-dlp Playbook Example"
  hosts:
    - all
  become: true
  vars:
    _lts_codename: "noble"


  tasks:

    - name: "Install yt-dlp on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.yt_dlp
      vars:
        yt_dlp_var_lts_codename: "{{ _lts_codename }}"
```

## License

BSD

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
