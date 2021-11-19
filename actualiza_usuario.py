"""Actualiza un registro en la tabla Usuario de la base de datos Biblioteca
   Ejecutar desde la terminal para actualizar el apellido del usuario con id 2:
   python actualiza-usuario.py 2 None Lopez None None"""

import click #Pip install click
from modelomysql import actualiza_registro

@click.command()
@click.argument("id", type=int) #Los argumentos son recibidos desde la terminal
@click.argument("nombre")
@click.argument("apellidos")
@click.argument("edad")
@click.argument("genero")
def actualiza_usuario(id, nombre, apellidos, edad, genero):
    """
    Modifica un egistro de la tabla Usuario con los campos ID, NOMBRE,
    APELLIDOS, EDAD y GENERO. Si se proporciona un valor a un campo, ese
    valor será actualizado en la base de datos. Si no se desea actualizar
    un campo, entonces colocar el valor None.  Imprime un mensaje si el
    registro se atualiza exitosamente.
    """
    valor = lambda cad, valor: valor if cad == "None" else cad #Es una función lamba en la que si el valor es "None" lo convierte a None
    tabla = "Usuario"
    edad = valor(edad, None) #Llama a la función lambda valor
    try:
        registro = (
            valor(nombre, None),
            valor(apellidos, None),
            edad if edad == None else int(edad),
            valor(genero, None))
    except ValueError:
        print("\nError: La edad tiene que ser un valor entero\n")
        return
    if actualiza_registro(tabla, id, registro):
        registro = (id,) + registro #(7, None, 'Lopez', None, None)
        print("Se ha actualizado el registro {} a la tabla {}".format(
            registro, tabla))

if __name__ == '__main__':
    actualiza_usuario()