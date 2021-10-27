import traceback
from datetime import datetime
import pytz


def decorators(*decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f
    return deco

#---------- NOTE: Función decoradora para encerrar las funciones render() en un try except y con el set_session y db.close---
def try_except_index(function):
    def wrapper(self):
        try:
            self.set_session()
            function(self)
        except Exception as e:
            traceback.print_exc()
            print(e)
            print("---------------fecha del error en zona la paz---------------------------")
            print(datetime.now(pytz.timezone('America/La_Paz')))
            self.render("common/views/error.html", error_code='404', message="Ocurrio un error al llamar al servidor.",
                        url_redirect='/')
        finally:
            self.db.close()
    return wrapper
#---------- NOTE: Función decoradora para encerrar las funciones api en un try except y con el set_session y db.close---
def try_except(function):
    def wrapper(self):
        try:
            self.set_session()
            function(self)
        except Exception as e:
            traceback.print_exc()
            print(e)
            print(datetime.now(pytz.timezone('America/La_Paz')))
            self.respond(str(e), False, 'Ocurrió un error en el servidor')
        finally:
            self.db.close()
    return wrapper

