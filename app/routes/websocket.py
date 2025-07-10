from fastapi import APIRouter, WebSocket
from ..services.bot_service import response_llm

router = APIRouter()

@router.websocket("/ws")
async def websocket_bot(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("🤖 Olá! Pode mandar sua dúvida.")

    while True:
        try:
            question = await websocket.receive_text()
            response = response_llm(question)
            
            await websocket.send_text(f"🤖 {response}")
        except Exception as e:
            print(f"Erro no WebSocket: {e}")
            await websocket.send_text(f"Erro: {str(e)}")
            break