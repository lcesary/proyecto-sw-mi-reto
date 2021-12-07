
from server.common.managers import SuperManager
from .models import Consejos,Alimento

class ConsejoManager(SuperManager):
    def __init__(self, db):
        super().__init__(Consejos, db)

    def listar_todo(self):
        return  self.db.query(Consejos).all()

    def get(self,id):
        return self.db.query(Consejos).filter(Consejos.id == id).all()

    def convertir_dic(self,objeto):
        resourse = []
        for o in objeto:
            o = o.get_dict()
            resourse.append(o)
        return resourse

class AlimentoManager(SuperManager):
    def __init__(self, db):
        super().__init__(Alimento, db)

    def listar_todo(self):
        return  self.db.query(Alimento).all()

    def get(self,id):
        return self.db.query(Alimento).filter(Alimento.id == id).all()

    def convertir_dic(self,objeto):
        resourse = []
        for o in objeto:
            o = o.get_dict()
            resourse.append(o)
        return resourse

