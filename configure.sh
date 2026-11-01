#!/bin/bash

echo "Enabling swap..."
. ./1_swap/swap.sh

echo "Configuring users..."
. ./2_users/users.sh

echo "Enabling tmpfs..."
. ./3_tmpfs/tmpfs.sh