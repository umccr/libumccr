# libumccr

[![Pull Request Build Status](https://github.com/umccr/libumccr/workflows/Pull%20Request%20Build/badge.svg)](https://github.com/umccr/libumccr/actions)

UMCCR Reusable Python modules

## Usage

- Install through ``pip`` like so
```commandline
pip install libumccr
```

- Somewhere in your Python code
```python
from libumccr.aws import libssm

ssm_value = libssm.get_ssm_param("my_param_name")
```

## Development

- Create Python virtual environment
```
git clone https://github.com/umccr/libumccr.git
cd libumccr
make install
make test
```
