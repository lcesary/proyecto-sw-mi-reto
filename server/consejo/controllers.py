
from ..usuarios.managers import *
from ..consejo.managers import ConsejoManager,AlimentoManager
from ..common.controllers import CrudController, SuperController, ApiController
from ..common.utils import try_except,try_except_index

import requests
import json

MY_API_KEY="770cecab-b21a-4d10-98f1-35196301e715"

class ConsejoController(CrudController):

    manager = ConsejoManager
    html_index = "consejo/views/consejo/index.html"
    html_table = "consejo/views/consejo/table.html"
    routes = {
        '/consejos': {'GET': 'index', 'POST': 'table'},
        '/consejo_listar': {'POST': 'consejo_listar'},
        '/consejo_insert': {'POST': 'insert'},
        '/consejo_update': {'PUT': 'edit', 'POST': 'update'},


    }
    
    @try_except_index
    def index(self):
        self.verif_privileges()
        result = self.manager(self.db).list_all()
        result['usuariosLista']=  UsuarioManager(self.db).listar()
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result.update(self.get_extra_data())
        self.render(self.html_index, **result)


    @try_except
    def consejo_listar(self):
        data = json.loads(self.get_argument("object"))
        usuario = self.get_user()
        lista = self.manager(self.db).list_all()
        lista = lista['objects']
        lista = self.manager(self.db).convertir_dic(lista)
        self.respond(response=lista, success=True, message='Insertado correctamente.')
    @try_except
    def insert(self):
        self.verif_privileges()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        object = ins_manager.entity(**diccionary)
        object.fkusuario = self.get_user().id
        indicted_object = ins_manager.insert(object)
        if len(ins_manager.errors) == 0:
            self.respond(indicted_object.get_dict(), message='Insertado correctamente!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al insertar')

    @try_except
    def update(self):
        self.verif_privileges()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        object = ins_manager.entity(**diccionary)
        object.fkusuario = self.get_user().id
        indicted_object = ins_manager.update(object)
        if len(ins_manager.errors) == 0:
            self.respond(indicted_object.get_dict(), message='Actualizado correctamente!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al actualizar')


class AlimentoController(CrudController):
    manager = AlimentoManager
    html_index = "consejo/views/alimento/index.html"
    html_table = "consejo/views/alimento/table.html"
    routes = {
        '/alimentos': {'GET': 'index', 'POST': 'table'},
        '/alimento_listar': {'POST': 'consejo_listar'},
        '/alimento_insert': {'POST': 'insert'},
        '/alimento_update': {'PUT': 'edit', 'POST': 'update'},

    }

    @try_except_index
    def index(self):
        self.verif_privileges()
        result = self.manager(self.db).list_all()
        result['usuariosLista'] = UsuarioManager(self.db).listar()
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result.update(self.get_extra_data())
        self.render(self.html_index, **result)

    @try_except
    def consejo_listar(self):
        data = json.loads(self.get_argument("object"))
        usuario = self.get_user()
        lista = self.manager(self.db).list_all()
        lista = lista['objects']
        lista = self.manager(self.db).convertir_dic(lista)
        self.respond(response=lista, success=True, message='Insertado correctamente.')

    @try_except
    def insert(self):
        self.verif_privileges()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        object = ins_manager.entity(**diccionary)
        object.fkusuario = self.get_user().id
        indicted_object = ins_manager.insert(object)
        if len(ins_manager.errors) == 0:
            self.respond(indicted_object.get_dict(), message='Insertado correctamente!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al insertar')

    @try_except
    def update(self):
        self.verif_privileges()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        object = ins_manager.entity(**diccionary)
        object.fkusuario = self.get_user().id
        indicted_object = ins_manager.update(object)
        if len(ins_manager.errors) == 0:
            self.respond(indicted_object.get_dict(), message='Actualizado correctamente!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al actualizar')




