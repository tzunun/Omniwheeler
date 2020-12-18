from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates
from src.robot_movement import direction_of_movement
from src.robot_movement import move_direction
from src.robot_movement import set_gpio_mode

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

set_gpio_mode()  

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
        # rotation is a temp variable to print data. Calling move_direction(data)
        # Should be enough to move the omniwheeler
        rotation = direction_of_movement(data)
        # Move the wheels acw, cw, still to head in a specific direction NSEW
        #move_direction(rotation)   
        rotation = str(direction_of_movement(data))
        print("\ndata:", data, '\nWheel movement', rotation )
        move_direction(data)   # This sends the signal to move the wheels
        await websocket.send_text(f"The wheel Rotation is: {rotation}")