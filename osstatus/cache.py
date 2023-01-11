import dataclasses
import pickle
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import List, Mapping, Optional

CACHE_FILE = Path(__file__).parent / 'cache.pickle'


class Platform(Enum):
    macOS = 'macOS'
    iOS = 'iOS'


@dataclasses.dataclass
class ErrorCode:
    platforms: List[Platform]
    framework: str
    header_file: str
    name: str
    value: int
    description: str


@lru_cache()
def get_all_errors_codes() -> Mapping[int, List[ErrorCode]]:
    return pickle.loads(CACHE_FILE.read_bytes())


def get_possible_error_codes(value: int) -> Optional[List[ErrorCode]]:
    return get_all_errors_codes().get(value)
