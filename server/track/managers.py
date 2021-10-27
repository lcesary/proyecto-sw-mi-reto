
from server.common.managers import SuperManager
from .models import *

class TrackManager(SuperManager):
    def __init__(self, db):
        super().__init__(Tracking, db)

    def obtenerUbicaciones(self):
        listaUsuarios=[]
        listaDatos=[]
        ubicaciones= self.db.query(Tracking).order_by(Tracking.id.desc()).all()
        for ubicacion in ubicaciones:
            if ubicacion.fkusuario not in listaUsuarios:
                listaUsuarios.append(ubicacion.fkusuario)
                listaDatos.append(ubicacion)
        return listaDatos

    def obtenerUbicacionesUsuario(self,usuario_id):
        ubicaciones= self.db.query(Tracking).filter(Tracking.fkusuario ==usuario_id).all()
        return ubicaciones

class TrackingManager(SuperManager):
    def __init__(self, db):
        super().__init__(Tracking, db)


    def guardarUbicacion(self,DatosTrack):
            DatosTrack.fkusuario = 1
            DatosTrack.nombre_usuario = "LUIS ENRIQUE"
           
            #super().insert(b)
            u = super().insert(DatosTrack)
            return u
