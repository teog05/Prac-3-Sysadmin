#!/bin/bash
sudo mkdir -p /path/to/tmpfs
sudo mount -t tmpfs -o size=2G tmpfs /path/to/tmpfs
echo "Tmpfs montado en /path/to/tmpfs"
