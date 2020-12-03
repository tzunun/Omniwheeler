from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates
from src.robot_movement import direction_of_movement

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get('/')
def omniwheeler_app():
    return "Omniwheeler App"


@app.get("/index")
def remote_control_direction_post(request: Request):
    result = "Click a direction"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


#@app.post("/index")
#def remote_control_direction_post(request: Request, direction: str = Form(...)):
#    result = direction_of_movement(direction)
#    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        rotation = direction_of_movement(data)
        print(data, rotation, type(rotation))
        await websocket.send_text(rotation)