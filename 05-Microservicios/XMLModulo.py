import xml.etree.ElementTree as ET

def object_to_xml(object, tag="item"):
    # Crear el elemento raíz
    root = ET.Element(tag)
    
    # Añadir subelementos basados en los atributos del objeto
    for atributo, valor in vars(object).items():
        elem = ET.SubElement(root, atributo)
        elem.text = str(valor)
    
    # Convertir el árbol XML a una cadena
    contenido_xml = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
    
    return contenido_xml


def dict_to_xml(dicc, tag="item"):
    elem = ET.Element(tag)
    _dict_to_xml_recurse(dicc, elem)
    return ET.tostring(elem, encoding='utf-8', method='xml').decode('utf-8')


def _dict_to_xml_recurse(dicc, parent):
    for key, value in dicc.items():
        if isinstance(value, dict):
            child = ET.SubElement(parent, key)
            _dict_to_xml_recurse(child, value)
        elif isinstance(value, list):
            for item in value:
                child = ET.SubElement(parent, key)
                if isinstance(item, dict):
                    _dict_to_xml_recurse(child, item)
                else:
                    child.text = str(item)
        else:
            child = ET.SubElement(parent, key)
            child.text = str(value)