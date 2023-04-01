"""In due time (Finnish: ajallaan) - reporting on worklog entries of some ticket system."""
import datetime as dti
import logging
import os
import pathlib
from typing import List, no_type_check

# [[[fill git_describe()]]]
__version__ = '2023.4.1+parent.eabc8f75'
# [[[end]]] (checksum: 835a5db409e7f572d77ffb946462f8f6)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

APP_NAME = 'In due time (Finnish: ajallaan) - reporting on worklog entries of some ticket system.'
APP_ALIAS = 'ajallaan'
APP_ENV = APP_ALIAS.upper()
APP_VERSION = __version__
COMMA = ','
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = f'.{APP_ALIAS}.json'

MAX_PACKED_BYTES = int(os.getenv(f'{APP_ENV}_MAX_PACKED_BYTES', '20_000_000'))
MAX_UNPACKED_BYTES = int(os.getenv(f'{APP_ENV}_MAX_UNPACKED_BYTES', '200_000_000'))

log = logging.getLogger()  # Module level logger is sufficient
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{APP_ALIAS}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO
LOG_SEPARATOR = '- ' * 80


TS_FORMAT_LOG = '%Y-%m-%dT%H:%M:%S'
TS_FORMAT_PAYLOADS = '%Y-%m-%d %H:%M:%S.%f UTC'

__all__: List[str] = [
    'APP_ALIAS',
    'APP_ENV',
    'APP_VERSION',
    'ENCODING',
    'LOG_SEPARATOR',
    'MAX_PACKED_BYTES',
    'MAX_UNPACKED_BYTES',
    'TS_FORMAT_PAYLOADS',
    'log',
    'parse_csl',
]


def parse_csl(csl: str) -> List[str]:
    """DRY."""
    return [fmt.strip().lower() for fmt in csl.split(COMMA) if fmt.strip()]


def parse_csl_as_is(csl: str) -> tuple[str, ...]:
    """DRY."""
    return tuple(fmt.strip() for fmt in csl.split(COMMA) if fmt.strip())[:2]


@no_type_check
def formatTime_RFC3339(self, record, datefmt=None):  # noqa
    """HACK A DID ACK we could inject .astimezone() to localize ..."""
    return dti.datetime.fromtimestamp(record.created, dti.timezone.utc).isoformat()  # pragma: no cover


@no_type_check
def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global log  # pylint: disable=global-statement

    log_format = {
        'format': '%(asctime)s %(levelname)s [%(name)s]: %(message)s',
        'datefmt': TS_FORMAT_LOG,
        # 'filename': LOG_PATH,
        'level': LOG_LEVEL if level is None else level,
    }
    logging.Formatter.formatTime = formatTime_RFC3339
    logging.basicConfig(**log_format)
    log = logging.getLogger(APP_ENV if name is None else name)
    log.propagate = True


init_logger(name=APP_ENV, level=logging.DEBUG if DEBUG else None)
