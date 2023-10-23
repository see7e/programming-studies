---
title: 42 - Common Core
tags:
  - "42"
  - common_core
  - programação
use: README, Documentation
languages: C
dependences:
---

<details><summary>Table of Contents 🔖</summary>

- [Common Core](#common-core)
  - [Libft](#libft)
  - [ft\_printf](#ft_printf)
  - [get\_next\_line](#get_next_line)
  - [Born2beroot](#born2beroot)
- [Other](#other)
  - [Codespace deployment pipeline](#codespace-deployment-pipeline)

</details>

---

# Common Core

![42 Common Core - canvas](./42_Common_Core-canvas.canvas)

## [Libft](./Libft/README.md)

This is the first project of the 42 Common Core. It consists of re-writing some of the functions of the C standard library, as well as some other useful functions.

## [ft_printf](./ft_printf/README.md)

This project belongs to the "second circle" of the 42 Common Core. It consists of re-writing the `printf` function from the C standard library.

## [get_next_line](./get_next_line/README.md)

This project belongs to the "second circle" of the 42 Common Core. It consists of re-writing the `get_next_line` function from the C standard library.

## [Born2beroot](./Born2beroot/README.md)

This project belongs to the "second circle" of the 42 Common Core. It consists of installing a Debian virtual machine, with some requirements, and configuring it to be secure.

# Other

## [Codespace deployment pipeline](../../../Docs/GH-action_docker-image.md)

In order to implement a Codespace deployment pipeline, to improve the development experience, I've created a workflow that creates a Codespace when a branch with `42` as its name is created.

The workflow is triggered by the `create` event, and it uses the `microsoft/create-codespace-action` action to create the Codespace and is directly linked to the `.devcontainer.json` file, which is the configuration file for the Codespace.