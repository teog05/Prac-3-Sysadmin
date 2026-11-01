from typing import Any, Union
from os import PathLike
from pathlib import Path

def main() -> None:
    # TODO: Make sure to add some logic and prints so teacher's can see the results

    normal_path = '/path/to/normal'
    tmpfs_path = '/path/to/tmpfs' 

    normal_result = benchmark(normal_path)
    tmpfs_result = benchmark(tmpfs_path)

    relation = relation_aspect(normal_result, tmpfs_result)

def benchmark(path: Union[str, PathLike]) -> Any: # Change return type as needed
    raise NotImplementedError("Benchmarking not implemented yet")

def relation_aspect(normal_result: Any, tmpfs_result: Any) -> float:  # Change parameter types as needed
    raise NotImplementedError("Relation ratio not implemented yet")

if __name__ == '__main__':
    main()