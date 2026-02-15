from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

router = APIRouter()

# Mock data
buses = [
    {"busname": "VolvoExpress", "route": "Hyderabad → Bangalore", "seats": 40},
    {"busname": "RedBus", "route": "Hyderabad → Chennai", "seats": 35}
]

class SeatBooking(BaseModel):
    seatNumber: int
    passengerName: str

class SeatUpdate(BaseModel):
    oldSeatNumber: int
    newSeatNumber: int

@router.get("/")
def get_all_buses():
    return buses

@router.get("/{busname}")
def get_bus_by_name(busname: str):
    bus = next((b for b in buses if b["busname"] == busname), None)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return bus

@router.get("/search")
def search_bus(busname: str = Query(...)):
    bus = next((b for b in buses if b["busname"] == busname), None)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return bus

@router.post("/{busname}/seat")
def book_seat(busname: str, booking: SeatBooking):
    return {
        "message": f"Seat booked on {busname} seat {booking.seatNumber}",
        "seatNumber": booking.seatNumber,
        "passengerName": booking.passengerName
    }

@router.put("/{busname}/seat")
def update_seat(busname: str, seat: SeatUpdate):
    return {
        "message": f"Seat updated on {busname}",
        "oldSeatNumber": seat.oldSeatNumber,
        "newSeatNumber": seat.newSeatNumber
    }

@router.get("/{busname}/seat")
def confirm_booking(busname: str):
    return {"message": f"Booking confirmed for {busname}"}

@router.delete("/{busname}")
def delete_bus(busname: str):
    return {"message": f"Bus {busname} deleted"}