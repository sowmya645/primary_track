from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

flights = [
    {"flightname": "Indigo123", "route": "Hyderabad → Delhi", "seats": 180},
    {"flightname": "AirIndia456", "route": "Hyderabad → Mumbai", "seats": 200}
]

class SeatBooking(BaseModel):
    seatNumber: str
    passengerName: str

class SeatUpdate(BaseModel):
    oldSeatNumber: str
    newSeatNumber: str

@router.get("/")
def get_all_flights():
    return flights

@router.get("/{flightname}")
def get_flight_by_name(flightname: str):
    flight = next((f for f in flights if f["flightname"] == flightname), None)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@router.post("/{flightname}/seat")
def book_seat(flightname: str, booking: SeatBooking):
    return {
        "message": f"Seat booked on {flightname} seat {booking.seatNumber}",
        "seatNumber": booking.seatNumber,
        "passengerName": booking.passengerName
    }

@router.put("/{flightname}/seat")
def update_seat(flightname: str, seat: SeatUpdate):
    return {
        "message": f"Seat updated on {flightname}",
        "oldSeatNumber": seat.oldSeatNumber,
        "newSeatNumber": seat.newSeatNumber
    }

@router.delete("/{flightname}")
def delete_flight(flightname: str):
    return {"message": f"Flight {flightname} deleted"}