
from ..usuarios.managers import *
from ..track.managers import TrackManager,TrackingManager
from ..common.controllers import CrudController, SuperController, ApiController
from ..common.utils import try_except,try_except_index
import requests
import json

MY_API_KEY="770cecab-b21a-4d10-98f1-35196301e715"

class TrackController(CrudController):

    manager = TrackManager
    html_index = "track/views/track/index.html"
    html_table = "track/views/track/table.html"
    routes = {
        '/track': {'GET': 'index', 'POST': 'table'},
        '/api/mandar_notificacion': {'POST': 'mandar_notificacion'},

    }
    
    @try_except_index
    def index(self):
        self.verif_privileges()
        result = self.manager(self.db).list_all()
        result['usuariosLista']=  UsuarioManager(self.db).listar()
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result['ubicaciones'] = TrackManager(self.db).obtenerUbicaciones()
        result.update(self.get_extra_data())
        self.render(self.html_index, **result)


    def mandar_notificacion(self):
        header = {"Content-Type": "application/json; charset=utf-8",
                "Authorization": "Basic MWQwYjZjMjUtYTE1Ni00ZjlhLWFjMjItMjk0ZjA2ZjljZWU2"}

  
        payload = {"app_id": "770cecab-b21a-4d10-98f1-35196301e715",
                "included_segments": ["All"],
                "contents": {"en": "Notificacion de Hernando "}}
        
        req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
        print(req.status_code, req.reason)

class HistorialController(CrudController):

    manager = TrackingManager
    html_index = "track/views/historial/index.html"
    #html_table = "track/views/track/table.html"
    routes = {
        '/historial': {'GET': 'index', 'POST': 'table'},
    }   
    
    @try_except_index
    def index(self,**kwargs):
        id = self.get_argument('id')
        #self.verif_privileges()
        result = self.manager(self.db).list_all()
        result['usuario_perfil']=  UsuarioManager(self.db).usuario_id(id)
        #print(str(result['usuario_perfil'].fkrol))
        
        rol = UsuarioManager(self.db).name_role(result['usuario_perfil'].fkrol)
        result['usuario_perfil'].fkrol=rol
        sucursal =SucursalManager(self.db).listar_id(int(result['usuario_perfil'].fksucursal))
        result['usuario_perfil'].fksucursal =sucursal
        
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result['ubicaciones'] = TrackManager(self.db).obtenerUbicacionesUsuario(id)
        result.update(self.get_extra_data())
        self.render(self.html_index, **result)
        
class ApiAppController(ApiController):
    routes = {
        '/api/v3/test_sae': {'POST': 'test_sae'},
    }   
    
    @try_except
    def test_sae(self):
      data = json.loads(self.request.body.decode('utf-8'))
      print("Funciona estos son los datos ||Bateria-> "+str(data['bateria'])+"% ||Longitud-> "+str(data['longitud'])+" ||Latitud-> "+str(data['latitud']))
      objeto = TrackingManager(self.db).entity(**data)
      TrackingManager(self.db).guardarUbicacion(objeto)
      self.respond(success=True, message="Datos insertados correctamente", response=data)

    