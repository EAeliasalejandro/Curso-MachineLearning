
def validateTel(telefono):
    if len(telefono) == 10 :
        return 'El telefono es correcto'
    elif len(telefono) < 10 :
        return 'Faltan digitos al telefono'
    elif len(telefono) > 10 :
        return 'Sobran digitos en el telefono'
