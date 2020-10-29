"""
Serviços para gerar o endpoint da aplicação
"""

import service.check_system as check_system

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
    return check_system.check_system(req) if req.path.startswith("/check_system") \
        else ("Service not available", 404)
