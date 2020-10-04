"""
Serviços para gerar o endpoint da aplicação
"""

import check_items

def services(req):
    """
    Nome:
        Services
    
    Descrição:
        Função de requisição dos endpoints

    :Args: requisição flask

    :Retorna: endpoints com determinado valor pedido na requisição
    """

    print("received request for", req.path)
    return check_items.check_system(req) if req.path.startswith("/check_system") \
        else ("Service not available", 404)
