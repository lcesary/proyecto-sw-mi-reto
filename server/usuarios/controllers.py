
from tornado.gen import coroutine
from .managers import *
from ..common.controllers import CrudController, SuperController, ApiController
import json
from ..common.utils import try_except,try_except_index
from ..bitacora.models import Bitacora
from ..bitacora.managers import BitacoraManager

from datetime import datetime
import pytz

class UsuarioController(CrudController):
    manager = UsuarioManager
    html_index = "usuarios/views/usuario/index.html"
    html_table = "usuarios/views/usuario/table.html"
    routes = {
        '/usuario': {'GET': 'index', 'POST': 'table'},
        '/usuario_insert': {'POST': 'insert'},
        '/usuario_update': {'PUT': 'edit', 'POST': 'update'},
        '/usuario_delete': {'POST': 'delete_user'},
        '/usuario_eliminar': {'POST': 'usuario_eliminar'},
        '/usuario_profile': {'GET': 'usuario_profile'},
        '/usuario_update_profile': {'POST': 'user_update_profile'},
        '/usuario_update_password': {'POST': 'user_update_password'},
        '/usuario_reset_password': {'POST': 'usuario_reset_password'},
        '/usuario_codigo_reset': {'POST': 'usuario_codigo_reset'},
        '/usuario_listar_sucursal': {'POST': 'usuario_listar_sucursal'},
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        aux['roles'] = RolManager(self.db).get_all()
        aux['sucursales'] = SucursalManager(self.db).listar(aux['usuario'])
        return aux

    @try_except_index
    def index(self):
        self.verif_privileges()
        usuario = self.get_user()
        result = {}
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result.update(self.get_extra_data())
        self.render(self.html_index, **result)

    @try_except
    def usuario_listar_sucursal(self):
        data = json.loads(self.get_argument("object"))
        usuario = self.get_user()
        if data['sucursal_id'] != "1":
            lista = UsuarioManager(self.db).listar_usuario_sucursal(data['sucursal_id'])
        else:
            lista = UsuarioManager(self.db).list_all(usuario)
            lista = lista['objects']
        lista = UsuarioManager(self.db).ordenar_usuario(lista)
        self.respond(response= lista, success=True, message='Insertado correctamente.')

    @try_except
    def insert(self):
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user_id'] = self.get_user_id()
        usuario = UsuarioManager(self.db).usuario_id(diccionary['user_id'])
        objeto = self.manager(self.db).entity(**diccionary)
        UsuarioManager(self.db).insert(objeto,usuario)
        self.respond(success=True, message='Insertado correctamente.')

    @try_except
    def update(self):
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user_id'] = self.get_user_id()
        usuario = UsuarioManager(self.db).usuario_id(diccionary['user_id'])
        objeto = self.manager(self.db).entity(**diccionary)
        UsuarioManager(self.db).update(objeto,usuario)
        self.respond(success=True, message='Modificado correctamente.')

    @try_except
    def delete_user(self):
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        id = diccionary['id']
        usuario = UsuarioManager(self.db).usuario_id(id)
        usuarios = UsuarioManager(self.db).usuario_id(self.get_user_id())
        resp = UsuarioManager(self.db).delete_user(usuario, usuarios)
        if resp:
            if usuario.enabled == True:
                self.respond(success=True, message='Usuario activado correctamente.')
            else:
                self.respond(success=True, message='Usuario eliminado correctamente.')
        else:
            self.respond(success=False, message='Rol asignado dado de baja, no es posible habilitar el usuario.')


    @try_except
    def usuario_eliminar(self):
        diccionary = json.loads(self.get_argument("object"))
        usuario = UsuarioManager(self.db).usuario_id(self.get_user_id())
        usuario_eliminar = UsuarioManager(self.db).usuario_id(diccionary['id'])
        eliminar = UsuarioManager(self.db).eliminar(diccionary['id'],usuario,usuario_eliminar)
        if eliminar == 1:
            self.respond(success=True, message="Usuario eliminado correctamente")
        else:
            self.respond(success=False, message="ocurrio un error "+ eliminar)


    @try_except
    def usuario_codigo_reset(self):
        id = json.loads(self.get_argument("id"))
        usuario = UsuarioManager(self.db).usuario_id(self.get_user_id())
        self.manager(self.db).update_codigo(id,usuario)
        self.respond(success=True, message='Modificado Correctamente!')

    @try_except_index
    def usuario_profile(self):
        user = self.get_user()
        self.verif_privileges()
        usuario = UsuarioManager(self.db)
        result = usuario.get_userById(self.get_user_id())
        self.render("usuarios/views/usuario/profile.html", user=user, **result)

    @try_except
    def user_update_password(self):
        diccionary = json.loads(self.get_argument("object"))
        user = self.manager(self.db).get_by_password(self.get_user_id(), diccionary['old_password'])
        usuario = UsuarioManager(self.db).usuario_id(self.get_user_id())
        if user:
            if diccionary['new_password'] == diccionary['new_password_2']:
                user.password = diccionary['new_password']
                self.manager(self.db).update_password(user,usuario)
                self.respond(message="Contraseña cambiada correctamente ", success=True)
            else:
                self.respond(message="Datos incorrectos", success=False)
        else:
            self.respond(message="Datos incorrectos", success=False)

    @try_except_index
    def user_reset_password(self):
        diccionary = json.loads(self.get_argument("object"))
        user = self.manager(self.db).get_by_pass(self.get_user_id())
        usuario = UsuarioManager(self.db).usuario_id(self.get_user_id())
        if user:
            if diccionary['new_password'] == diccionary['new_password_2']:
                user.password = diccionary['new_password']
                self.manager(self.db).update_password(user,usuario)
                self.respond(message="Contraseña cambiada correctamente ", success=True)
            else:
                self.respond(message="Datos incorrectos", success=False)
        else:
            self.respond(message="Datos incorrectos", success=False)

    @try_except
    def user_update_profile(self):
        diccionary = json.loads(self.get_argument("object"))
        usuario = UsuarioManager(self.db).usuario_id(self.get_user_id())
        objeto = self.manager(self.db).entity(**diccionary)
        user = self.manager(self.db).update_profile(objeto,usuario)
        self.respond(message="Datos Correctos", success=True)


class RolController(CrudController):
    manager = RolManager
    html_index = "usuarios/views/rol/index.html"
    html_table = "usuarios/views/rol/table.html"
    routes = {
        '/rol': {'GET': 'index', 'POST': 'table'},
        '/rol_insert': {'POST': 'insert'},
        '/rol_update': {'PUT': 'edit', 'POST': 'update'},
        '/rol_delete': {'POST': 'delete_rol'}
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        aux['modulos'] = ModuloManager(self.db).list_all()
        return aux

    @try_except_index
    def index(self):
        self.verif_privileges()
        result = self.manager(self.db).listar_todo()
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result.update(self.get_extra_data())
        self.render(self.html_index, **result)


    @try_except
    def edit(self):
        self.verif_privileges()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        indicted_object = ins_manager.obtain(diccionary['id'])
        if len(ins_manager.errors) == 0:
            self.respond(indicted_object.get_dict(), message='Operacion exitosa!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al insertar')

    @try_except
    def insert(self):
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        usuario = UsuarioManager(self.db).usuario_id(self.get_user_id())
        objeto = self.manager(self.db).entity(**diccionary)
        RolManager(self.db).insert(objeto,usuario)
        self.respond(success=True, message='Insertado correctamente.')

    @try_except
    def update(self):
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        objeto = self.manager(self.db).entity(**diccionary)
        usuario = UsuarioManager(self.db).usuario_id(self.get_user_id())
        RolManager(self.db).update(objeto,usuario)
        self.respond(success=True, message='Modificado correctamente.')

    @try_except
    def delete_rol(self):
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        id = diccionary['id']
        enable = diccionary['enabled']
        usuario = UsuarioManager(self.db).usuario_id(self.get_user_id())
        RolManager(self.db).delete_rol(id, enable, self.get_user_id(),usuario)
        if enable == True:
            self.respond(success=True, message='Rol activado correctamente.')
        else:
            self.respond(success=True, message='Rol inhabilitado correctamente.')



class LoginController(SuperController):
    @coroutine
    def get(self):
        """Renderiza el login"""
        self.set_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.set_header('Pragma', 'no-cache')
        self.set_header('Expires', '0')
        usuario = self.get_secure_cookie("user")
        if usuario:
            self.redirect("/")
        else:
            self.clear_cookie("user")
            self.render("usuarios/views/login/index.html", error=0)

    @coroutine
    def post(self):
        """Inicia sesión en la aplicación.

        Si se inicia sesión con éxito enctonces se guarda el
        usuario en la cookie caso contrario se vuelve al login.
        """
        self.check_xsrf_cookie()
        ip = self.request.remote_ip
        username = self.get_argument('username', default=None)
        password = self.get_argument('password', default=None)

        if username is not None and password is not None:
            user = LoginManager().login(username, password)
            if user:
                fecha = self.fecha_actual()
                b = Bitacora(fkusuario=user.id, accion="Inicio de sesión.", fecha=fecha,usuario=user.nombre + " " + user.apellidos)
                self.insertar_bitacora(b)
                self.set_user_id(user.id)
                self.redirect("/")
            else:
                userb = LoginManager().not_enabled(username, password)
                if userb:
                    self.render("usuarios/views/login/index.html", error=1)
                else:
                    self.render("usuarios/views/login/index.html", error=2)
        else:
            self.render("usuarios/views/login/index.html", error=2)

    def fecha_actual(self):
        return datetime.now(pytz.timezone('America/La_Paz'))

    def insertar_bitacora(self, bitacora):
        with transaction() as session:
            session.add(bitacora)
            session.commit()


class ManualController(SuperController):
    @coroutine
    def get(self):
        usuario = self.get_user()
        self.render("usuarios/views/usuario/manual.html", user=usuario)


class LogoutController(SuperController):
    @coroutine
    def get(self):
        try:
            user_id = self.get_user_id()
            ip = self.request.remote_ip
            user = self.get_user()
            fecha = self.fecha_actual()
            b = Bitacora(fkusuario=user_id,  accion="Finalizó sesión.", fecha=fecha,usuario=user.nombre + " " + user.apellidos)
            self.insertar_bitacora(b)
            self.clear_cookie('user')
            self.redirect(self.get_argument("next", "/"))
        except Exception as e:
            self.clear_cookie('user')
            self.redirect(self.get_argument("next", "/"))

    def fecha_actual(self):
        return datetime.now(pytz.timezone('America/La_Paz'))

    def insertar_bitacora(self, bitacora):
        with transaction() as session:
            session.add(bitacora)
            session.commit()


class ApiLoginController(SuperController):
    @coroutine
    def post(self):
        """Devuelve el usuario que coincida con el username y password dados.

        Si ocurre algún error se retornará None en la respuesta json al
        cliente invocador.
        """
        try:
            username = self.get_argument('username')
            password = self.get_argument('password')
            usuario = LoginManager().login(username, password)
            self.respond(usuario.getDict())
        except:
            self.respond(success=False)


class ApiUserController(ApiController):
    routes = {

        '/api/v1/update_token_usuario': {'POST': 'update_token_usuario'},
        '/api/v1/listar_usuarios_privilegios': {'POST': 'listar_usuarios_privilegios'},
        '/api/v1/update_movil_privilegio': {'POST': 'update_movil_privilegio'},
    }

    def check_xsrf_cookie(self):
        return