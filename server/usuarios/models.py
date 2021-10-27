from sqlalchemy import Column, Integer, String, Boolean,Float
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from ..database.models import Base
from ..database.serializable import Serializable


class Usuario(Serializable, Base):
    way = {'rol': {'modulos': {}}}

    __tablename__ = 'USRMUSUARIO'

    id = Column('id', Integer, primary_key=True)
    nombre = Column('nombre', String(100), nullable=False)
    apellidos = Column('apellidos', String(100), nullable=False)
    correo = Column('correo', String(100), nullable=False)
    usuario = Column('usuario', String(50), nullable=False, unique=True)
    password = Column('password', String(150), nullable=False)
    fkrol = Column('fkrol', Integer, ForeignKey('USRMROL.id'), nullable=False)
    descripcion = Column('descripcion', String(200), nullable=True)
    fksucursal = Column('fksucursal', Integer, ForeignKey('USRMSUCURSAL.id'), nullable=False)
    token = Column('token', String(2000), nullable=True, default='Sin Token')
    enabled = Column('enabled', Boolean, default=True)

    rol = relationship('Rol')
    sucursal = relationship('Sucursal')


    def get_dict(self, way=None):
        dictionary = super().get_dict(way)
        del(dictionary['password'])
        return dictionary


Acceso = Table('USRDACCESO', Base.metadata,
               Column('id', Integer, primary_key=True),
               Column('fkrol', Integer, ForeignKey('USRMROL.id')),
               Column('fkmodulo', Integer, ForeignKey('USRMMODULO.id')))


class Rol(Serializable, Base):
    way = {'usuario': {}, 'modulos': {}}

    __tablename__ = 'USRMROL'

    id = Column('id', Integer, primary_key=True)
    nombre = Column('nombre', String(50), nullable=False)
    descripcion = Column('descripcion', String(200), nullable=False)
    enabled = Column('enabled', Boolean, default=True)

    usuario = relationship('Usuario')
    modulos = relationship('Modulo', secondary=Acceso)


class Modulo(Serializable, Base):
    way = {'roles': {}}

    __tablename__ = 'USRMMODULO'

    id = Column('id', Integer, primary_key=True)
    ruta = Column('ruta', String(100))
    titulo = Column('titulo', String(100), nullable=False)
    nombre = Column('nombre', String(100), nullable=False, unique=True)
    icono = Column('icono', String(50), nullable=False, default='home')
    menu = Column('menu', Boolean, nullable=False, default=True)
    fkmodulo = Column('fkmodulo', Integer, ForeignKey('USRMMODULO.id'))

    roles = relationship('Rol', secondary=Acceso)
    #children = relationship('Modulo')
    modulo = relationship('Modulo')

class Sucursal(Serializable, Base):
    way = {}

    __tablename__ = 'USRMSUCURSAL'

    id = Column('id', Integer, primary_key=True)
    nombre = Column('nombre', String(100))
    enabled = Column('enabled', Boolean, default=True)
