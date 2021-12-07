
def insertions():

    import hashlib
    from server.database.connection import transaction
    from .models import Modulo, Usuario, Rol


    with transaction() as session:
        usuario_m = session.query(Modulo).filter(Modulo.nombre == 'usuario_Modulo').first()
        if usuario_m is None:
            usuario_m = Modulo(titulo='Usuarios', nombre='usuario_Modulo', icono='person')

        roles_m = session.query(Modulo).filter(Modulo.nombre == 'roles').first()
        if roles_m is None:
            roles_m = Modulo(titulo='Rol', ruta='/rol', nombre='roles', icono='dashboard')

        usuarios_m = session.query(Modulo).filter(Modulo.nombre == 'usuario').first()
        if usuarios_m is None:
            usuarios_m = Modulo(titulo='Usuario', ruta='/usuario', nombre='usuario', icono='account_box')

        perfil_m = session.query(Modulo).filter(Modulo.nombre == 'perfil').first()
        if perfil_m is None:
            perfil_m = Modulo(titulo='Perfil Usuario', ruta='/usuario_profile', nombre='perfil', icono='account_circle')

        bitacora_m = session.query(Modulo).filter(Modulo.nombre == 'bitacora').first()
        if bitacora_m is None:
            bitacora_m = Modulo(titulo='Bitacora', ruta='/bitacora', nombre='bitacora', icono='dvr')


        usuario_m.modulo.append(roles_m)
        usuario_m.modulo.append(usuarios_m)
        usuario_m.modulo.append(perfil_m)
        usuario_m.modulo.append(bitacora_m)

        query_rol = session.query(Modulo).filter(Modulo.nombre == 'rol_query').first()
        if query_rol is None:
            query_rol = Modulo(titulo='Consultar', ruta='', nombre='rol_query', menu=False)
        insert_rol = session.query(Modulo).filter(Modulo.nombre == 'rol_insert').first()
        if insert_rol is None:
            insert_rol = Modulo(titulo='Adicionar', ruta='/rol_insert', nombre='rol_insert', menu=False)
        update_rol = session.query(Modulo).filter(Modulo.nombre == 'rol_update').first()
        if update_rol is None:
            update_rol = Modulo(titulo='Actualizar', ruta='/rol_update', nombre='rol_update', menu=False)
        delete_rol = session.query(Modulo).filter(Modulo.nombre == 'rol_delete').first()
        if delete_rol is None:
            delete_rol = Modulo(titulo='Dar de Baja', ruta='/rol_delete', nombre='rol_delete', menu=False)

        roles_m.modulo.append(query_rol)
        roles_m.modulo.append(insert_rol)
        roles_m.modulo.append(update_rol)
        roles_m.modulo.append(delete_rol)

        query_usuario = session.query(Modulo).filter(Modulo.nombre == 'usuario_query').first()
        if query_usuario is None:
            query_usuario = Modulo(titulo='Consultar', ruta='', nombre='usuario_query', menu=False)
        insert_usuario = session.query(Modulo).filter(Modulo.nombre == 'usuario_insert').first()
        if insert_usuario is None:
            insert_usuario = Modulo(titulo='Adicionar', ruta='/usuario_insert', nombre='usuario_insert', menu=False)
        update_usuario = session.query(Modulo).filter(Modulo.nombre == 'usuario_update').first()
        if update_usuario is None:
            update_usuario = Modulo(titulo='Actualizar', ruta='/usuario_update', nombre='usuario_update', menu=False)
        delete_usuario = session.query(Modulo).filter(Modulo.nombre == 'usuario_delete').first()
        if delete_usuario is None:
            delete_usuario = Modulo(titulo='Dar de Baja', ruta='/usuario_delete', nombre='usuario_delete', menu=False)

        usuarios_m.modulo.append(query_usuario)
        usuarios_m.modulo.append(insert_usuario)
        usuarios_m.modulo.append(update_usuario)
        usuarios_m.modulo.append(delete_usuario)

        query_bitacora = session.query(Modulo).filter(Modulo.nombre == 'bitacora_query').first()
        if query_bitacora is None:
            query_bitacora = Modulo(titulo='Consultar', ruta='', nombre='bitacora_query', menu=False)

        bitacora_m.modulo.append(query_bitacora)

        admin_role = session.query(Rol).filter(Rol.nombre == 'Administrador').first()
        if admin_role is None:
            admin_role = Rol(nombre='ADMINISTRADOR', descripcion='Todos los permisos')

        ###Modulo de Usuarios
        admin_role.modulos.append(bitacora_m)
        admin_role.modulos.append(usuario_m)
        admin_role.modulos.append(roles_m)
        admin_role.modulos.append(usuarios_m)
        admin_role.modulos.append(perfil_m)
        admin_role.modulos.append(query_usuario)
        admin_role.modulos.append(insert_usuario)
        admin_role.modulos.append(update_usuario)
        admin_role.modulos.append(delete_usuario)
        admin_role.modulos.append(query_rol)
        admin_role.modulos.append(insert_rol)
        admin_role.modulos.append(update_rol)
        admin_role.modulos.append(delete_rol)
        admin_role.modulos.append(query_bitacora)
        super_user = session.query(Usuario).filter(Usuario.nombre == 'admin').first()
        if super_user is None:
            hex_dig = hashlib.sha512(b'admin').hexdigest()
            super_user = Usuario(nombre='Administrador', apellidos='principal', correo='admin@host.com', usuario='admin',
                                 password=hex_dig)
            super_user.rol = admin_role

        session.add(super_user)
        session.add(admin_role)
        session.commit()
