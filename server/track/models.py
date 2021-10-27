from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, BigInteger, Text
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship

from ..database.models import Base
from ..database.serializable import Serializable

class Tracking(Serializable, Base):
    way = {'usuario': {}}

    __tablename__ = 'USRMTRACKING'

    id = Column('id', BigInteger, primary_key=True)
    latitud = Column('latitud', String(255), nullable=True)
    longitud = Column('longitud', String(255), nullable=True)
    bateria = Column('bateria', String(255), nullable=True)
    nombre_usuario = Column('nombre_usuario', String(255), nullable=True)
    fkusuario = Column('fk_usuario', Integer, ForeignKey('USRMUSUARIO.id'), nullable=True)

    usuario = relationship('Usuario')
