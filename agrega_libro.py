"""Agrega un registro a la tabla Libro de la BD Biblioteca.
    Ejecutar desde la terminal:
    python agrega_libro.py "El alquimista" "Omega" 130 1"""

import click #Pip install click
from modelomysql import agrega_registro


@click.command()
@click.argument("titulo") #Estos son los argumentos que va a recibir desde la terminal
@click.argument("editorial")
@click.argument("numpag", type=int)
@click.argument("autores")
def agrega_usuario(titulo, editorial, numpag, autores):
    """
    Agrega un nuevo registro a la tabla Libro con los campos TITULO,
    EDITORIAL, NUMPAG y AUTORES. Imprime un mensaje si el registro se agrega
    exitosamente a la tabla.
    """
    tabla = "Libro"
    registro = (titulo, editorial, numpag, autores)
    if agrega_registro(tabla, registro):
        print("Se ha agregado el registro {} a la tabla {}".format(
            registro, tabla))

if __name__ == '__main__':
    agrega_usuario()