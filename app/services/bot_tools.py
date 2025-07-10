import requests
from langchain_core.tools import tool
from ..utils.config import API_URL

@tool
def schedule_appointment(name: str, speciality: str) -> str:
    """
    Agenda uma consulta para o paciente informado.
    
    Args:
        nome: Nome do paciente
        especialidade: Especialidade médica desejada
    
    Returns:
        Confirmação de agendamento
    """
    response = requests.post(
        f"{API_URL}/agendamentos",
        json={"nome": name, "especialidade": speciality}
    )

    if response.status_code == 200:
        return "✅ Consulta agendada com sucesso!"
    return f"❌ Erro ao agendar: {response.text}"