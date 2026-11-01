## Мой первый playbook — решение

1. `vi first_playbook.yml`

```
- name: Install zlib and create a file
  hosts: some_remote_host
  tasks:
    - name: Install zlib
      package:
        name: zlib
        state: present
      become: yes
    - name: Create the file /tmp/some_file
      file:
        path: '/tmp/some_file'
        state: touch
```

2. Сначала отредактируйте файл инвентаря (inventory): `vi /etc/ansible/hosts`

```
[some_remote_host]
some.remoted.host.com
```

Запустите playbook

`ansible-playbook first_playbook.yml`
