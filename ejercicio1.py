dic = {"Precio1": 100, "Descuento1": 0.20,
       "Precio2": 200, "Descuento2": 0.50,
       "Precio3": 50, "Descuento3": 0.10 }

def compra(Descuento, Iva, dic):
    descuento = Descuento(calDescuento, dic)
    precioFinal = Iva(calIva, descuento)
    print(precioFinal)

def Descuento(calDescuento, dic):
    descuento = {}
    desc = calDescuento(dic["Precio1"], dic["Descuento1"])
    descuento.update({"Precio1": desc})

    desc = calDescuento(dic["Precio2"], dic["Descuento2"])
    descuento.update({"Precio2": desc})

    desc = calDescuento(dic["Precio3"], dic["Descuento3"])
    descuento.update({"Precio3": desc})
    return descuento

def calDescuento(precio, descuento):
    return precio - precio*descuento

def Iva(calIva, descuento):
    iva = {}
    precioIva = calIva(descuento["Precio1"])
    iva.update({"PrecioFinal1" : precioIva})

    precioIva = calIva(descuento["Precio2"])
    iva.update({"PrecioFinal2" : precioIva})

    precioIva = calIva(descuento["Precio3"])
    iva.update({"PrecioFinal3" : precioIva})

    return iva

def calIva(precio):
    return precio + precio*0.12

compra(Descuento, Iva, dic)
