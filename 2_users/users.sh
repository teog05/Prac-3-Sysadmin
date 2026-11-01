#!/bin/bash
if [ "$EUID" -ne 0 ]; then
  echo "Por favor, ejecuta el script como root (sudo)"
  exit 1
fi

groupadd profes
useradd -m -G profes ferran
useradd -m -G profes pablo
useradd -m -G profes oriol

mkdir -p /tmp/prac3
chown root:profes /tmp/prac3
chmod 775 /tmp/prac3

echo "Documento compartido" > /tmp/prac3/shared.txt
chown ferran:profes /tmp/prac3/shared.txt
chmod 770 /tmp/prac3/shared.txt

echo "Privado Ferran" > /tmp/prac3/ferran_priv.txt
chown ferran:profes /tmp/prac3/ferran_priv.txt
chmod 700 /tmp/prac3/ferran_priv.txt

echo "Privado Pablo" > /tmp/prac3/pablo_priv.txt
chown pablo:profes /tmp/prac3/pablo_priv.txt
chmod 700 /tmp/prac3/pablo_priv.txt

echo "Privado Oriol" > /tmp/prac3/oriol_priv.txt
chown oriol:profes /tmp/prac3/oriol_priv.txt
chmod 700 /tmp/prac3/oriol_priv.txt

echo "Usuarios, grupo y carpeta compartida configurados correctamente."
