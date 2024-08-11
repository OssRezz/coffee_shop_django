# Documentación de iniciar un proyecto desde cero

## Venv

1. Crear el venv: python3 -m venv /home/.envs/coffee_shop
2. activar el entorno: source /home/.envs/coffee_shop/bin/activate

## Instalar Django: 

Una vez activido el entorno virutal, instalamos

1. pip install Django

## Crear el archivo de dependencias "requirements.txt" para produccón

En este archivo escribimos las dependencias del proyecto, es importante declarar cada una de estas con la versión de la dependiencias, podemos usar **pip freeze** en la terminal para obtener la versiónes. No se debe agregar las dependencias de las dependencias. 

- Django=version

## Crear el archivo de dependencias que solo se usan en entorno de desarrollo

Hay dependencias que no queremos que se instalen en el ambiente de producción, por lo tanto este archivo nos permite tener esto bajo control.

En este caso utilizamos ipython para mejorar la shell de python.

ipython==8.26.0

## Instalar las dependencias en producción o al clonar el archivo

- Usamos el comando: **pip install -r requirements.txt**
- Usamos el comando: **pip install -r requirements-dev.txt**