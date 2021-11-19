""" Imprime en la terminal las tablas disponibles en la BD o los registros de la tabla especificada
    Ejecutar desde la terminal:
    python lista-registros.py 
    python lista-registros.py Libro """

import click #Pip install click
from modelomysql import obtiene_registros, obtiene_tablas
from stdout import imprime_registros

@click.command()
@click.argument("tabla", required=False) #El argumento tabla lo recibirá por la terminal. Ejemplo: python lista-registros.py Libro
def lista_registros(tabla):
    """
    Imprime la lista de registros de TABLA  en la salida estándar, si no se
    proporciona una tabla, se imprime la Lista de tablas disponibles.
    """
    if tabla:
        # Se obtiene la lista de registros de tabla
        registros = obtiene_registros(tabla)
        # Se imprimen los registros en formato texto en la salida estándar
        imprime_registros(registros, "Tabla: {}".format(tabla))
    else:
        tablas = obtiene_tablas() #Obtiene el resultado de ejecutar Show tables; en la base de datos: [('Libro',), ('Usuario',)]
        imprime_registros(tablas, "Tablas disponibles")

if __name__ == '__main__':
    lista_registros()