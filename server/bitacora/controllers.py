

from ..usuarios.managers import *

from ..common.controllers import CrudController

_KEY="770cecab-b21a-4d10-98f1-35196301e715"

class BitacoraController(CrudController):

    manager = BitacoraManager
    html_index = "bitacora/views/bitacora/index.html"
    html_table = "bitacora/views/bitacora/table.html"
    routes = {
        '/bitacora': {'GET': 'index', 'POST': 'table'},
    }   
    def index(self):
        self.set_session()
        self.verif_privileges()
        result = self.manager(self.db).list_all()
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result.update(self.get_extra_data())
        self.render(self.html_index, **result)
        self.db.close()


