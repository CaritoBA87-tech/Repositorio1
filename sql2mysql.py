"""Este código ejecuta un script SQL recibiendo los comandos desde la terminal, es decir que no tenemos que hacerlo con los comandos de docker
    Ejecutar desde la terminal para ejecutar el script tablas-inicial.sql:
    python sql2mysql.py tablas-inicial.sql
"""

import click #Pip install click
from modelomysql import ejecuta_sql

def obtiene_sql(archsql):
    """
    Lee las instrucciones sql desde el archivo archsql y regresa una
    cadena con todas las instrucciones a ejecutar.
    """
    with open(archsql) as da:
        lineas = da.read()

    return lineas

@click.command()
@click.argument("archsql", type=click.Path(exists=True)) #Obtiene el argumento con el nombre del archivo sql a ejecutar
def sql2mysql(archsql):
    """
    Ejecuta las instrucciones del archivo ARCHSQL en el servidor MariaDB
    """
    sql = obtiene_sql(archsql)
    if ejecuta_sql(sql):
        print("\nSe ha ejecutado el archivo {} correctamente\n".format(
            archsql))
    else:
        print("\nError el ejecutar el archivo ", archsql)

if __name__ == '__main__':
    sql2mysql()