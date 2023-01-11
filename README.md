[![Pypi version](https://img.shields.io/pypi/v/osstatus.svg)](https://pypi.org/project/osstatus/ "PyPi package")

# OSStatus

Query os status codes directly from your shell, based on the
amazing [https://www.osstatus.com/](https://www.osstatus.com/).

# Installation

```shell
python3 -m pip install osstatus
```

# Usage

Use from your shell:

```
Usage: python -m osstatus [OPTIONS] COMMAND [ARGS]...

  query error codes

Options:
  --help  Show this message and exit.

Commands:
  all     get all possible errors codes
  code    get all possible errors codes by error code
  symbol  get all possible errors codes by symbol name
```

Or from python:

```python3
from osstatus.cache import get_possible_error_codes

# get all possible errors codes for status 50
possible_error_codes = get_possible_error_codes(50)

# [ErrorCode(platforms=[<Platform.macOS: 'macOS'>, <Platform.iOS: 'iOS'>],
#           framework='Foundation',
#           header_file='NSXMLParser.h',
#           name='NSXMLParserAttributeListNotStartedError',
#           value=50,
#           description=''),
#  ErrorCode(platforms=[<Platform.iOS: 'iOS'>],
#           framework='HomeKit',
#           header_file='HMError.h',
#           name='HMErrorCodeAccessorySentInvalidResponse',
#           value=50,
#           description=''),
#  ErrorCode(platforms=[<Platform.macOS: 'macOS'>, <Platform.iOS: 'iOS'>],
#           framework='Kernel',
#           header_file='errno.h',
#           name='ENETDOWN',
#           value=50,
#           description='Network is down'),
#  ErrorCode(platforms=[<Platform.macOS: 'macOS'>, <Platform.iOS: 'iOS'>],
#           framework='Kernel',
#           header_file='kern_return.h',
#           name='KERN_CODESIGN_ERROR',
#           value=50,
#           description='During a page fault, indicates that the page was '
#                       'rejected as a result of a signature check.'),
#  ErrorCode(platforms=[<Platform.iOS: 'iOS'>],
#           framework='Matter',
#           header_file='MTRClusterConstants.h',
#           name='MTRClusterTestClusterAttributeClusterErrorBooleanID',
#           value=50,
#           description='')]
print(possible_error_codes)
```
