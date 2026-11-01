import time
import os
from typing import Any, Union
from os import PathLike
from pathlib import Path

def main() -> None:
    normal_path = './normal_storage_bench'
    tmpfs_path = '/path/to/tmpfs' 

    os.makedirs(normal_path, exist_ok=True)
    os.makedirs(tmpfs_path, exist_ok=True)

    print("Ejecutando benchmark de escritura (500MB)...")
    normal_result = benchmark(normal_path)
    print(f"Almacenamiento estándar (SSD/HDD): {normal_result:.4f} segundos")
    
    tmpfs_result = benchmark(tmpfs_path)
    print(f"Almacenamiento temporal (tmpfs): {tmpfs_result:.4f} segundos")

    relation = relation_aspect(normal_result, tmpfs_result)
    print(f"Resultado: El sistema tmpfs es {relation:.2f} veces más rápido.")

def benchmark(path: Union[str, PathLike]) -> float: 
    test_file = os.path.join(path, 'test_file.bin')
    data = os.urandom(1024 * 1024)
    
    start_time = time.time()
    with open(test_file, 'wb') as f:
        for _ in range(500):
            f.write(data)
    end_time = time.time()
    
    os.remove(test_file)
    return end_time - start_time

def relation_aspect(normal_result: float, tmpfs_result: float) -> float: 
    if tmpfs_result == 0:
        return float('inf')
    return normal_result / tmpfs_result

if __name__ == '__main__':
    main()
