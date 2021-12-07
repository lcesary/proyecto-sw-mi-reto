from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, BigInteger, Text
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship

from ..database.models import Base
from ..database.serializable import Serializable

class Consejos(Serializable, Base):
    way = {'usuario': {}}

    __tablename__ = 'consejos'

    id = Column('id', BigInteger, primary_key=True)
    nombre = Column('nombre', String(255), nullable=True)
    descripcion = Column('descripcion', String(255), nullable=True)
    fkusuario = Column('fk_usuario', Integer, ForeignKey('usuario.id'), nullable=True)
    estado = Column('estado', Boolean, default=True)

    usuario = relationship('Usuario')

class Alimento(Serializable, Base):
    way = {'usuario': {}}

    __tablename__ = 'alimento'

    id = Column('id', Integer, primary_key=True)
    nombre = Column('nombre', String(255), nullable=True)
    fkusuario = Column('fk_usuario', Integer, ForeignKey('usuario.id'), nullable=True)
    estado = Column('estado', Boolean, default=True)

    usuario = relationship('Usuario')

class gestionaralimento(Serializable, Base):
    way = {'usuario': {}}

    __tablename__ = 'gestionaralimento'

    id = Column('id', BigInteger, primary_key=True)
    nombre = Column('nombre', String(255), nullable=True)

