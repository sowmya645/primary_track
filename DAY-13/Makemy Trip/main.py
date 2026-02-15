from fastapi import FastAPI
from routers import bus, flight, hotel

app = FastAPI(title="Travel Booking API")

# Include routers
app.include_router(bus.router, prefix="/bus", tags=["Bus"])
app.include_router(flight.router, prefix="/flight", tags=["Flight"])
app.include_router(hotel.router, prefix="/hotel", tags=["Hotel"])