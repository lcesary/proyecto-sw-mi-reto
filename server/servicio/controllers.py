
from ..usuarios.controllers import *
from ..common.utils import try_except,try_except_index

class ApiUsuarioController(ApiController):

    manager = UsuarioManager
    routes = {
        '/api/v1/listar_usuario': {'GET': 'listar_usuarios'},
        '/api/v1/editar_usuario': {'POST': 'update_usuarios'},
        '/api/v1/crear_usuario': {'POST': 'insert'},
        '/api/v1/delete_usuario': {'POST': 'delete_usuarios'},
        '/api/v1/crear_peticion': {'POST': 'crear_peticion'},
        '/api/v1/login_usuario_mobile': {'POST': 'login_usuario_mobile'},
    }


    def check_xsrf_cookie(self):
        return

    @try_except
    def login_usuario_mobile(self):
        response = []
        data = json.loads(self.request.body.decode('utf-8'))
        validar = UsuarioManager(self.db).validar_usuario(data['username'],data['password'])
        if validar == 1:
            r  = UsuarioManager(self.db).listar_usuario(data['username'])
            self.respond(response=r.get_dict(), success=True, message="Usuario recuperados correctamente.")
        else:
            r = None
            self.respond(response=validar, success=False, message="Datos del usuario son incorrecto.")


    def guardar_usuario(self):
        self.set_session()
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            result = self.manager(self.db).listar_usuario(data['username'])
            response = []
            if result == None:
                objeto = self.manager(self.db).entity(**data)
                UsuarioManager(self.db).insertar(objeto)
                self.respond(response=response, success=True, message="Usuario recuperados correctamente.")
            else:
                self.respond(response=response, success=False, message="Ocurrio un problema.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()

    def listar_usuarios(self):
        self.set_session()
        try:
            result = self.manager(self.db).listar()
            response = []
            for usuario in result:
                dic = dict(id=str(usuario.id), nombre=str(usuario.nombre),
                           correo=str(usuario.correo),
                           username=str(usuario.username), rol=str(usuario.fkrol),
                           persona =str(usuario.fkpersona), apellido=str(usuario.apellido),
                           enabled=str(usuario.enabled), password=str(usuario.password))
                response.append(dic)
            self.db.close()
            self.respond(response=response, success=True, message="Usuario recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()


    def update_usuarios(self):
        data = json.loads(self.request.body.decode('utf-8'))
        self.set_session()
        response = []
        diccionary = dict(id=int(data['id']), nombre=data['nombre'],
                          username=data['username'], fkrol=int(data['rol']),
                          persona=data['persona'], enabled=data['enabled'],
                          correo=data['correo'], ip="123.123.123.123",
                          password=data['contraseña'])
        response.append(diccionary)
        objeto = self.manager(self.db).entity(**diccionary)
        self.manager(self.db).update(objeto)
        self.respond(response=response,success=True, message='Usuario Modificada correctamente.')
        self.db.close()

    def delete_usuarios(self):
        data = json.loads(self.request.body.decode('utf-8'))
        self.set_session()
        response = []
        diccionary = dict(id=int(data['id']), nombre=data['nombre'],
                          username=data['username'], fkrol=int(data['rol']),
                          persona=data['persona'], enabled=data['enabled'],
                          correo=data['correo'], ip="123.123.123.123")
        response.append(diccionary)
        objeto = self.manager(self.db).entity(**diccionary)
        self.manager(self.db).update(objeto)
        self.respond(response=response,success=True, message='Usuario Modificada correctamente.')
        self.db.close()

    def insert(self):
        data = json.loads(self.request.body.decode('utf-8'))
        try:
            response = []
            self.set_session()
            diccionary = dict(nombre=data['nombre'],
                              username=data['username'], fkrol=int(data['rol']),
                              apellido=data['apellido'],
                              persona=data['persona'], correo=data['correo'],
                              ip=data['ip'],password=data['password'],user_id=int(data['id']),)
            response.append(diccionary)
            objeto = self.manager(self.db).entity(**diccionary)
            self.manager(self.db).insert(objeto)
            self.respond(response=response, success=True, message='Insertado correctamente.')
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()