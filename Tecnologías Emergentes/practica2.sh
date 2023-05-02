#! /bin/bash
export IFS=$''

echo -ne "Practica 2 \n============================================================================\n"

#$(awk -F: '{ print $1 }' /etc/passwd)
for linea in $(getent passwd | cut -d: -f1)
do
    echo $cmd
done


echo -ne "\nPara un usuario especifico (p.e. everardo)\n"
user=$(getent passwd everardo)
echo $user