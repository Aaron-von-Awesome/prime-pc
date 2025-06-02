# Structure of configuration-tasks.yaml

```yaml
---
# ============================================================
#                     configuration-tasks.yaml
# ============================================================

- name: "Block: configuration-tasks.yaml"
  become: true
  vars:
    _var_hostname: "{{ var_hostname }}"
  block:

    - name: "Set Specific Configuration variables for \"{{ _var_hostname }}\""
      set_fact:
        _fact_should_install_proton_mail_bridge: true
      when: _var_hostname == "hostname_1"

    - name: "Set Specific Configuration variables for \"{{ _var_hostname }}\""
      set_fact:
        _fact_should_install_proton_mail_bridge: false
      when: _var_hostname == "hostname_n"

  rescue:

    - name: "ERROR: configuration-tasks.yaml"
      ansible.builtin.debug:
        msg: "ERROR: configuration-tasks.yaml"

    - name: "Error detected! Stopping Playbook :-("
      ansible.builtin.fail:
        msg: "Error detected! Stopping Playbook :-("
```
