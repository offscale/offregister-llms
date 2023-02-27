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
| [gpt-neox](https://github.com/EleutherAI/gpt-neox) | 20B        | Apache-2.0 | ❌       |

## Install dependencies

    pip install -r requirements.txt

## Install package

    pip install .

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
