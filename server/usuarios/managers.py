import hashlib
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import make_transient
from ..database.connection import transaction
from server.common.managers import SuperManager, Error
from .models import *


import string
from random import *
import random
from ..bitacora.managers import *


class UsuarioManager(SuperManager):
    def __init__(self, db):
        super().__init__(Usuario, db)

    def get_privileges(self, id, route):
        parent_module = self.db.query(Modulo).\
            join(Rol.modulos).join(Usuario).\
            filter(Modulo.ruta == route).\
            filter(Usuario.id == id).\
            filter(Usuario.enabled).\
            first()
        if not parent_module:
            return dict()
        modules = self.db.query(Modulo).\
            join(Rol.modulos).join(Usuario).\
            filter(Modulo.fkmodulo == parent_module.id).\
            filter(Usuario.id == id).\
            filter(Usuario.enabled)
        privileges = {parent_module.nombre: parent_module}
        for module in modules:
            privileges[module.nombre] = module
        return privileges

    def get_userById(self, id):
        return dict(profile=self.db.query(Usuario).filter(Usuario.id == id).first())


    def usuario_id(self,id):
        usuario= self.db.query(Usuario).filter(Usuario.id == id ).first()
        return usuario

    def listar_usuario_sucursal(self,sucursal_id):
        return self.db.query(Usuario).filter(Usuario.fksucursal == sucursal_id).filter(Rol.id != 1).all()

    def list_all(self, usuario):
        if usuario.fksucursal == 1:
            return dict(
                objects=self.db.query(Usuario).filter(Usuario.fkrol == Rol.id).filter(Rol.id != 1).distinct().all())
        else:
            return dict(objects=self.db.query(Usuario).filter(Usuario.fkrol == Rol.id).filter(
                Usuario.fksucursal == usuario.fksucursal).filter(Rol.id != 1).distinct().all())

    def ordenar_usuario(self,usuarios):
        lista = list()
        for usuario in usuarios:
            rol= usuario.rol.nombre
            sucursal= usuario.sucursal.nombre
            usuario= usuario.get_dict()
            usuario['sucursal']= sucursal
            usuario['rol']= rol
            lista.append(usuario)
        return lista

    def insert(self, Usuario,usuarios):
        if Usuario.fkrol > 0:
            Usuario.password = hashlib.sha512(Usuario.password.encode()).hexdigest()
            if Usuario.nombre is not None:
                Usuario.nombre = Usuario.nombre.upper()
            if Usuario.apellidos is not None:
                Usuario.apellidos = Usuario.apellidos.upper()
            u = super().insert(Usuario)
            fecha = BitacoraManager(self.db).fecha_actual()
            b = Bitacora(fkusuario=Usuario.user_id,  accion="Se registró un usuario.", fecha=fecha, tabla='USRMUSUARIO',usuario=usuarios.nombre +" "+ usuarios.apellidos,identificador=u.id,identificadores=u.nombre+" "+u.apellidos)
            super().insert(b)
            return u
        return Error('unknown')

    def update(self, Usuarioupd,usuario):
        if Usuarioupd.password != None:
            Usuarioupd.password = hashlib.sha512(Usuarioupd.password.encode()).hexdigest()
        if Usuarioupd.nombre is not None:
            Usuarioupd.nombre = Usuarioupd.nombre.upper()
        if Usuarioupd.apellidos is not None:
            Usuarioupd.apellidos = Usuarioupd.apellidos.upper()
        update = super().update(Usuarioupd)
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuarioupd.id, accion="Se modificó un usuario.", tabla='USRMUSUARIO', fecha=fecha,usuario=usuario.nombre +" "+ usuario.apellidos,identificador=update.id,identificadores=update.nombre+" "+update.apellidos)
        super().insert(b)
        return update

    def delete_user(self, usuario, Usuariocr):
        if usuario.enabled==True:
            usuario.enabled=False
            message = "Se inhabilitó un usuario."
        else:
            usuario.enabled=True
            message = "Se habilitó un usuario."
        usuario = super().insert(usuario)
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuariocr.id, accion=message, fecha=fecha, tabla='USRMUSUARIO',usuario=usuario.nombre +" "+ usuario.apellidos,identificador=usuario.id,identificadores=usuario.nombre+" "+usuario.apellidos)
        super().insert(b)

        return True

    def eliminar(self,id,usuario,usuario_eliminar):
        try:
            self.db.query(Usuario).filter(Usuario.id == id).delete()
            fecha = BitacoraManager(self.db).fecha_actual()
            b = Bitacora(fkusuario=usuario.id, accion="Usuario eliminado correctamente.", fecha=fecha,
                         usuario=usuario.nombre + " " + usuario.apellidos, tabla='USRMUSUARIO',identificador=usuario_eliminar.id,identificadores=usuario_eliminar.nombre+" "+usuario_eliminar.apellidos)
            super().insert(b)
            self.db.commit()
            self.db.close()
            return 1
        except Exception as e:
            print(e)
            self.db.close()
            return str(e)

    def update_codigo(self, usuario,usuarios):
        x = self.db.query(Usuario).filter(Usuario.id == usuario).one()
        x.activo = 0
        x.codigo = self.get_random_string()
        x.token = "Sin Token"
        self.db.commit()
        self.db.close()
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=usuarios.id, accion="Codigo reseteado correctamente", fecha=fecha, tabla='USRMUSUARIO',
                     usuario=usuarios.nombre + " " + usuarios.apellidos,identificador=x.id,identificadores=x.nombre+" "+x.apellidos)
        super().insert(b)
        return x

    def get_by_password(self, Usuario_id, password):
        return self.db.query(Usuario).filter(Usuario.id == Usuario_id). \
            filter(Usuario.password == hashlib.sha512(str(password).encode()).hexdigest()).first()

    def update_password(self, Usuario,usuarios):
        Usuario.password = hashlib.sha512(Usuario.password.encode()).hexdigest()
        a = super().update(Usuario)
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=usuarios.id, accion="Codigo reseteado correctamente", fecha=fecha, tabla='USRMUSUARIO',
                     usuario=usuarios.nombre + " " + usuarios.apellidos,identificador=a.id,identificadores=a.nombre+" "+a.apellidos)
        super().insert(b)
        return a

    def get_by_pass(self, Usuario_id):
        return self.db.query(Usuario).filter(Usuario.id == Usuario_id).first()

    def update_profile(self, Usuarioprf,usuarios):
        usuario = self.db.query(Usuario).filter_by(id=Usuarioprf.id).first()
        usuario.nombre = Usuarioprf.nombre
        usuario.apellidos = Usuarioprf.apellido
        usuario.correo = Usuarioprf.correo
        self.db.merge(usuario)
        b = Bitacora(fkusuario=usuarios.id, accion="Se actualizó perfil de usuario.", fecha=fecha_zona, tabla='USRMUSUARIO', identificador=usuario.id,usuario=usuarios.nombre + " " + usuarios.apellidos ,identificadores=usuario.nombre + " " + usuario.apellidos)
        super().insert(b)
        self.db.commit()
        return usuario

    def name_role(self, rol):
        role = self.db.query(Rol).filter_by(id=rol).first()
        nombre_rol = role.nombre
        return nombre_rol

    def has_access(self, id, route):
        aux = self.db.query(Usuario.id). \
            join(Rol).join(Acceso).join(Modulo). \
            filter(Usuario.id == id). \
            filter(Modulo.ruta == route). \
            filter(Usuario.enabled). \
            all()
        return len(aux) != 0

    def get_random_string(self):
        random_list = []
        for i in range(8):
            random_list.append(random.choice(string.ascii_uppercase + string.digits))
        return ''.join(random_list)



#-----------------------------------------------------------------------------------------------------------------------

    def listar_usuario(self,usuario):
        usuario=self.db.query(Usuario).filter(Usuario.usuario==usuario).first()
        return usuario


    def activate_Usuarios(self, id, Usuario):
        x = self.db.query(Usuario).filter(Usuario.id == id).one()
        Usuario = self.db.query(Usuario).filter(Usuario.id == Usuario).one()
        x.enabled = 1
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuario.id, accion="Se activó un usuario.", fecha=fecha, tabla='USRMUSUARIO', identificador=x.id,usuario=Usuario.nombre + " " + Usuario.apellidos ,identificadores=x.nombre + " " + x.apellidos)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()


    def listar(self):
        return self.db.query(Usuario).filter(Usuario.enabled == True).filter(Rol.nombre != "ADMINISTRADOR").distinct()

class SucursalManager(SuperManager):
    def __init__(self, db):
        super().__init__(Sucursal, db)

    def listar(self,usuario):
        if usuario.fksucursal == 1:
            a =self.db.query(Sucursal).filter(Sucursal.enabled == True)
        else:
            a = self.db.query(Sucursal).filter(Sucursal.enabled == True).filter(Sucursal.id == usuario.fksucursal )
        return a


    def listar_id(self,id):
        sucursal = self.db.query(Sucursal).filter(Sucursal.enabled == True).filter(Sucursal.id == id ).first()
        return str(sucursal.nombre)

#-----------------------------------------------------------------------------------------------------------------------




    def list_all(self):
        return dict(objects=self.db.query(Sucursal).distinct().all())

class RolManager(SuperManager):
    def __init__(self, db):
        super().__init__(Rol, db)
    def get_all(self):
        return self.db.query(Rol).filter(Rol.enabled == True).filter(Rol.id != 1)


    def listar_todo(self):
        return dict(objects=self.db.query(Rol).filter(Rol.id != 1).distinct().all())

    def insert(self, rol,usuario):
        fecha = BitacoraManager(self.db).fecha_actual()
        rol = super().insert(rol)
        b = Bitacora(fkusuario=usuario.id, accion="Se registró un rol.", fecha=fecha,
                     usuario=usuario.nombre +" "+ usuario.apellidos,tabla='USRMROL', identificador=rol.id ,identificadores=rol.nombre)
        super().insert(b)

        return rol

    def update(self, rol,usuario):
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=rol.user, accion="Se modificó un rol.", fecha=fecha,usuario=usuario.nombre +" "+ usuario.apellidos
                     ,tabla='USRMROL', identificador=rol.id ,identificadores=rol.nombre)
        super().insert(b)
        a = super().update(rol)
        return a

    def delete_rol(self, id, enable, Usuariocr,usuario):
        x = self.db.query(Rol).filter(Rol.id == id).one()
        x.enabled = enable

        if enable == True:
            message = "Se habilitó un rol."
        else:
            users = self.db.query(Usuario).filter(Usuario.enabled == True).filter(Usuario.fkrol == id).all()
            for u in users:
                u.enabled = False

            message = "Se inhabilitó un rol y usuarios relacionados."

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuariocr, accion=message, fecha=fecha,usuario=usuario.nombre +" "+ usuario.apellidos
                     ,tabla='USRMROL', identificador=x.id ,identificadores=x.nombre)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()


#-----------------------------------------------------------------------------------------------------------------------

    def get_page(self, page_nr=1, max_entries=10, like_search=None, order_by=None, ascendant=True, query=None):
        query = self.db.query(self.entity).filter(Rol.id > 1)
        return super().get_page(page_nr, max_entries, like_search, order_by, ascendant, query)

    def list_all(self):
        return dict(objects=self.db.query(Rol).distinct().all())

class ModuloManager:
    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Modulo).filter(Modulo.fkmodulo==None)


class LoginManager:

    def login(self, username, password):
        """Retorna un usuario que coincida con el username y password dados.

        parameters
        ----------
        Usuarioname : str
        password : str
            El password deberá estar sin encriptar.

        returns
        -------
        Usuario
        None
            Retornará None si no encuentra nada.
        """
        password = hashlib.sha512(password.encode()).hexdigest()
        with transaction() as session:
            usuario = session.query(Usuario).\
                options(joinedload('rol').
                        joinedload('modulos').
                        joinedload('modulo')).\
                filter(Usuario.usuario == username).\
                filter(Usuario.password == password).\
                filter(Usuario.enabled).\
                first()
            if not usuario:
                return None
            session.expunge(usuario)
            make_transient(usuario)
        usuario.rol.modulos = self.order_modules(usuario.rol.modulos)
        return usuario



    def not_enabled(self, username, password):
        """Retorna un usuario que coincida con el username y password dados.

        parameters
        ----------
        Usuarioname : str
        password : str
            El password deberá estar sin encriptar.

        returns
        -------
        Usuario
        None
            Retornará None si no encuentra nada.
        """
        password = hashlib.sha512(password.encode()).hexdigest()
        with transaction() as session:
            usuario = session.query(Usuario).\
                options(joinedload('rol').
                        joinedload('modulos').
                        joinedload('modulo')).\
                filter(Usuario.usuario == username).\
                filter(Usuario.password == password).\
                filter(Usuario.enabled == False).\
                first()
            if not usuario:
                return None
            session.expunge(usuario)
            make_transient(usuario)
        usuario.rol.modulos = self.order_modules(usuario.rol.modulos)
        return usuario

    def get(self, key):
        with transaction() as session:
            usuario = session.query(Usuario).\
                options(joinedload('rol').
                        joinedload('modulos').
                        joinedload('modulo')).\
                filter(Usuario.id == key).\
                filter(Usuario.enabled).\
                first()
            if not usuario:
                return None
            session.expunge(usuario)
            make_transient(usuario)
        usuario.rol.modulos = self.order_modules(usuario.rol.modulos)
        return usuario

    def order_modules(self, modules):
        modules.sort(key=lambda x: x.id)
        mods_parents = []
        mods = {}
        while len(modules) > 0:
            module = modules.pop(0)
            module.modulo = []
            mods[module.id] = module
            parent_module = mods.get(module.fkmodulo, None)
            if parent_module:
                parent_module.modulo.append(module)
            else:
                mods_parents.append(module)
        return mods_parents
