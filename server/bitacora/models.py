from sqlalchemy import *
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database.models import Base
from ..database.serializable import Serializable
import pytz

global fecha_zona
fecha_zona = datetime.now(pytz.timezone('America/La_Paz'))


class Bitacora(Serializable, Base):
    way = {'usuario': {}}

    __tablename__ = 'bitacora'

    id = Column('id', BigInteger, primary_key=True)
    fkusuario = Column('fkusuario', Integer, ForeignKey('usuario.id'), nullable=True)
    ip = Column('ip', String(100), nullable=True)
    accion = Column('accion', String(200), nullable=True)
    usuario = Column('usuario', String(200), nullable=True)
    fecha = Column('fecha', DateTime, nullable=False, default=fecha_zona)
    tabla = Column('tabla', String(200), nullable=True)
    identificador = Column('identificador', Integer, nullable=True)
    identificadores = Column('identificadores', String(200), nullable=True)



