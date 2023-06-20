# libumccr

[![Pull Request Build Status](https://github.com/umccr/libumccr/workflows/Pull%20Request%20Build/badge.svg)](https://github.com/umccr/libumccr/actions) [![PyPI - Downloads](https://img.shields.io/pypi/dm/libumccr?style=flat)](https://pypistats.org/packages/libumccr) [![PyPI](https://img.shields.io/pypi/v/libumccr?style=flat)](https://pypi.org/project/libumccr) 
[![PyPI - License](https://img.shields.io/pypi/l/libumccr?style=flat)](https://opensource.org/licenses/MIT)

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

- Crawling S3 Objects from a Bucket, efficiently!
```python
from libumccr.aws import libs3

bucket="my-bucket"
key_prefix="my_prefix"
key_suffix=".csv"

for obj in libs3.get_matching_s3_objects(bucket, prefix=key_prefix, suffix=key_suffix):
    print(f"s3://{bucket}/{obj['Key']}")
```

## Development

- Create Python virtual environment
```
git clone https://github.com/umccr/libumccr.git
cd libumccr
conda activate libumccr
make up
make ps
make install all
make check
make test
```
