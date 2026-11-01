## Задача обновления apt-пакетов (update и upgrade) — решение

```
- name: "update and upgrade apt packages."
  become: yes
  apt:
    upgrade: yes
    update_cache: yes
```
