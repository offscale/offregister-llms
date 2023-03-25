offregister_llms
================
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech)
![Python version range](https://img.shields.io/badge/python-2.7%20|%203.4%20|%203.5%20|%203.6%20|%203.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11-blue.svg)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT%20OR%20CC0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort)

Follows [offregister](https://github.com/offscale/offregister) specification to install Large Language Models that have
permissive licenses.

## Large Language Models

There are a lot of LLMs, though the recent highly accurate ones with immense parameter numbers have noncommercial
licenses; if they are open-source at all.

This repo installs the development environment for setting up LLMs that have permissive licenses like Apache-2.0 or MIT.

Support matrix:

| Name + repo                                        | Params (#) | License    | Support |
|----------------------------------------------------|------------|------------|---------|
| [YaLM-100B](https://github.com/yandex/YaLM-100B)   | 100B       | Apache-2.0 | WiP     |
| [gpt-neox](https://github.com/EleutherAI/gpt-neox) | 20B        | Apache-2.0 | ❌      |
| [FLAN](https://github.com/google-research/FLAN/tree/main/flan/v2) | 540B [flan-t5-xxl](https://huggingface.co/google/flan-t5-xxl)       | Apache-2.0 | ❌      |

Also keeping a close-eye on https://paperswithcode.com/task/language-modelling and similar sources to find the latest permissively open-source model + data that should next be adapted into an SSH deployed with offregister-llms.

## Install dependencies
```sh
$ python -m pip install -r requirements.txt
```

## Install package
```sh
$ python -m pip install -e .
```

## Virtual test environment environment

### [`offstrategy`](https://github.com/offscale/offstrategy)
```sh
# JSON file describing Node to create and auth you can base off https://github.com/offscale/offstrategy/blob/master/offstrategy/config/strategy.ubuntu.aws.json
$ python -m offstrategy -n 1 --provider 'EC2' -c 'strategy.ubuntu.aws.json'
# `python -m offswitch -s 'strategy.ubuntu.aws.json'` will delete the VM
```

### Vagrant
```sh
$ vagrant init generic/rocky8
$ vagrant up  # turn off VM with `vagrant halt`
$ vagrant ssh-config  # Use this in next step, first update ~/.ssh/config and set name to 'rocky'
$ # `vagrant destroy` will delete the VM
```

See Bring Your Own Node (BYON) section below for how to make this available to [`offregister`](https://github.com/offscale/offregister).

### Other (BYON)

Use any [Rocky Linux](https://rockylinux.org) 8 installation.

Then enable usage in `offregister` by making this node known to your [`etcd`](https://etcd.io) cluster:
```sh
# You'll need `etcd` running in background for this command:
$ python -m offset --os 'fedora' -u 'vagrant' --dns-name 'rocky' -n 'rocky' \
                   -i "$PWD"'/.vagrant/machines/default/virtualbox/private_key'
```

## Install LLM dependencies using this python package's logic:
```sh
# You'll need `etcd` running in background for this command:
$ python -m offregister -c 'register.llm.json'  # register.llm.json is a default offregister config; see below
```

### `register.llm.json` example
Make sure you set `OFFAUTH_JSON` environment variable to your https://github.com/offscale/offregister/blob/master/offregister/_config/auth.sample.json
```json
{
  "name": "llm",
  "description": "Offregister strategy for Large Language Models",
  "version": "0.0.1",
  "provider": {
    "$ref": "env:OFFAUTH_JSON|offutils.str_from_file | json.loads"
  },
  "register": {
    "/unclustered/rocky": [
      {
        "module": "offregister-bootstrap",
        "type": "fabric"
      },
      {
        "module": "offregister-llms",
        "type": "fabric"
      }
    ]
  },
  "purpose": [
    "llm"
  ],
  "etcd_server": "http://localhost:2379",
  "default_pick": "first"
}
```

## License

Licensed under any of:

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)
- CC0 license ([LICENSE-CC0](LICENSE-CC0) or <https://creativecommons.org/publicdomain/zero/1.0/legalcode>)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
licensed as above, without any additional terms or conditions.
