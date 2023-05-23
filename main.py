import re

class Parser:
    def __init__(self):
        self.valid_ports = [80, 443]

    def parse_request(self, request):
        
        url_match = re.match(r'^http://([^:/]+)(?::(\d+))?(/.*)?$', request)
        if not url_match:
            return False, "La URL no cumple con el formato esperado"

        host = url_match.group(1)
        port = url_match.group(2)
        path = url_match.group(3)

        
        if port is None:
            return False, "La URL no dispone de un puerto para la conexión con el servidor"
        if int(port) not in self.valid_ports:
            return False, f"El puerto {port} no es válido"

      
        return True, f"Solicitud procesada: host={host}, puerto={port}, path={path}"


class Usuario:
    def __init__(self, id, contrasena, nombre):
        self.id = id
        self.contrasena = contrasena
        self.nombre = nombre


class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def encontrar_usuario_por_id(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None

    def editar_usuario(self, id, contrasena, nombre):
        usuario = self.encontrar_usuario_por_id(id)
        if usuario:
            usuario.contrasena = contrasena
            usuario.nombre = nombre
            return True
        return False

    def eliminar_usuario(self, id):
        usuario = self.encontrar_usuario_por_id(id)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False

    def mostrar_usuarios(self):
        print("Usuarios existentes:")
        for usuario in self.usuarios:
            print(f"ID: {usuario.id}, Nombre: {usuario.nombre}")


gestor = GestorUsuarios()
parser = Parser()


def apirest():
    salida = int(input('Ingrese 0 para ingresar un URL, de lo contrario ingrese otro número para salir: '))
    while salida == 0:
        request = input("Ingrese la URL a testear: ")
        success, result = parser.parse_request(request)
        if success:
            print(result)
        else:
            print(result)

        salida = int(input('Ingrese 0 para ingresar un URL, de lo contrario ingrese otro número para salir: '))

    continuar = True
    while continuar:
        print("Bienvenido al sistema de gestión de usuarios")
        print("1. Mostrar usuarios existentes")
        print("2. Encontrar un usuario por ID")
        print("3. Crear un nuevo usuario")
        print("4. Editar información de un usuario")
        print("5. Eliminar un usuario")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            gestor.mostrar_usuarios()
        elif opcion == "2":
            id = input("Ingrese el ID del usuario: ")
            usuario = gestor.encontrar_usuario_por_id(id)
            if usuario:
                print("Usuario encontrado")
                print(f"ID: {usuario.id}, Nombre: {usuario.nombre}")
            else:
                print("Usuario no encontrado")
        elif opcion == "3":
            id, contrasena, nombre = input("Ingrese el ID, contraseña y nombre del nuevo usuario (separados por comas): ").split(",")
            usuario = Usuario(id, contrasena, nombre)
            gestor.agregar_usuario(usuario)
            print("Usuario creado exitosamente")
        elif opcion == "4":
            id = input("Ingrese el ID del usuario a editar: ")
            contrasena, nombre = input("Ingrese la nueva contraseña y nombre del usuario (separados por comas): ").split(",")
            if gestor.editar_usuario(id, contrasena, nombre):
                print("Usuario editado exitosamente")
            else:
                print("Usuario no encontrado")
        elif opcion == "5":
            id = input("Ingrese el ID del usuario a eliminar: ")
            if gestor.eliminar_usuario(id):
                print("Usuario eliminado exitosamente")
            else:
                print("Usuario no encontrado")
        elif opcion == "6":
            print("Saliendo...")
            continuar = False
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    apirest()
