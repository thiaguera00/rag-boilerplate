def response_formatter(response)-> str:
    """
    Extrai a resposta final de uma saída vinda de RAG ou Function Calling.

    Retorna sempre uma string pronta pra ser exibida ao usuário.
    """
    if isinstance(response, str):
        return response
    
    if isinstance(response, dict):
        if "result" in response:
            return response["result"]
        
        if "output" in response:
            return response["output"]
        
        return str(response)
    
    return str(response)
