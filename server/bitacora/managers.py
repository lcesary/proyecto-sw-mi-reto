
from server.common.managers import SuperManager
from .models import *

from datetime import datetime, date, time, timedelta

import pytz


global fecha_zona
#fecha_zona = datetime.now(pytz.timezone('America/La_Paz'))
fecha_zona = datetime.now()


class BitacoraManager(SuperManager):
    def __init__(self, db):
        super().__init__(Bitacora, db)

    def list_all(self):
        return dict(objects=self.db.query(Bitacora).order_by(Bitacora.id.asc()).all())

    def fecha_actual(self):
        return datetime.now(pytz.timezone('America/La_Paz'))

    def fecha(self):
        return fecha_zona.strftime('%Y/%d/%m')


