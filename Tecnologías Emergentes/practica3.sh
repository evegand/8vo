#! /bin/bash
menu = true
while [ menu ]
do
    clear
    echo -ne "Practica 3 \n============================================================================\n"
    contenido=$(ls -la)
    echo $contenido
    echo -ne "\n\nIngresa el nombre del archivo al que quieres cambiar los permisos: \n"
    read -p "Archivo seleccionado: " file 
    if [[ $contenido == *"$file"* ]]
    then
        echo -ne "\nr - read   w - write   x - execute\n\nSelecciona entre los siguientes opciones de permisos: \n"
        echo -ne "  1) El usuario puede leer, escribir y ejecutar.\n  2) Solo el dueño puede leer y escribir, los demas solo leer.\n  3) Dar todos los permisos al ususario \n  PRESIONA CUALQUIER OTRA TECLA PARA SALIR\n"
        read -p "  Opcion " val
        echo -ne "\nArchivo actualizado con exito! \n"
        case $val in
            1) chmod -R 755 $file
                echo  $(ls -la | grep $file)
                ;;
            2) chmod 644 $file
                echo  $(ls -la | grep $file)
                ;;
            3) chmod 777 $file
                echo  $(ls -la | grep $file)
                ;;
            *) echo "Regresando al menu anterior..."
                ;;
        esac
        sleep 3
    else
        clear
    fi
done