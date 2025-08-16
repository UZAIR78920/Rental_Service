from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from rental_classes import Rental_Service

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 template engine
templates = Jinja2Templates(directory="templates")

# Create service instance
console = Rental_Service()
console.add_vehicle("Bike", "Honda Activa", "KA05 AB 1234", 300, "Yes")
console.add_vehicle("Bike", "Bajaj Pulsar", "AP09 EF 2468", 500, "Yes")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "vehicles": console.vehicles,
        "bookings": console.bookings,
        "message": None
    })

@app.post("/add_vehicle", response_class=HTMLResponse)
async def add_vehicle(
    request: Request,
    vtype: str = Form(...),
    model: str = Form(...),
    no_plate: str = Form(...),
    price: int = Form(...),
    availability: str = Form(...)
):
    console.add_vehicle(vtype, model, no_plate, price, availability)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "vehicles": console.vehicles,
        "bookings": console.bookings,
        "message": f"Vehicle {no_plate} added!"
    })

@app.post("/book_vehicle", response_class=HTMLResponse)
async def book_vehicle(
    request: Request,
    customer: str = Form(...),
    no_plate: str = Form(...),
    days: int = Form(...)
):
    console.book_vehicles(customer, 1, [no_plate], [days])
    return templates.TemplateResponse("index.html", {
        "request": request,
        "vehicles": console.vehicles,
        "bookings": console.bookings,
        "message": f"Booked {no_plate}!"
    })

@app.post("/return_vehicle", response_class=HTMLResponse)
async def return_vehicle(
    request: Request,
    no_plate: str = Form(...),
    late_days: int = Form(...)
):
    total_fare = console.return_vehicle(no_plate, late_days)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "vehicles": console.vehicles,
        "bookings": console.bookings,
        "message": f"Your Total Fare With Penalty: {total_fare if total_fare else 'Invalid Data'}!"
    })

@app.post("/remove_vehicle", response_class=HTMLResponse)
async def remove_vehicle(
    request: Request,
    no_plate: str = Form(...)
):
    console.remove_vehicle(no_plate)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "vehicles": console.vehicles,
        "bookings": console.bookings,
        "message": f"Vehicle {no_plate} removed!"
    })


@app.post("/update_price", response_class=HTMLResponse)
async def update_price(
    request: Request,
    no_plate: str = Form(...),
    price: int = Form(...)
):
    console.update_price(no_plate, price)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "vehicles": console.vehicles,
        "bookings": console.bookings,
        "message": f"Price updated for {no_plate}!"
    })