#! /bin/bash
while [ true ]
do
    clear
    echo -ne "Practica 4 \n============================================================================\n"

    echo -ne "Selecciona una opción:\n  1) Mostrar procesos\n  2) Terminar un proceso\n  3) Terminar todos los procesos \n  PRESIONA CUALQUIER OTRA TECLA PARA SALIR\n"
    read -p "  Opcion " val
    case $val in
        1) echo -ne "\nLos procesos actuales son: \n"
            procesos=$(ps -a)
            echo $procesos
            ;;
        2) echo -ne "\n"
            read -p "Ingresa el PID: " pid
            echo "Proceso seleccionado:" $pid
            kill -9 $pid
            ;;
        3) read -p "¿Quieres finalizar todos los procesos?" ans
            if [[ ans == "y" ]]
            then
                kill -l
            else
                echo "Procesos finalizados"
            fi
            ;;
        *)
            echo "Saliendo..."
            ;;
    esac
    sleep 5
done