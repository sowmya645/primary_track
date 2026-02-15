from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

hotels = [
    {"hotelname": "TajKrishna", "location": "Hyderabad", "rooms": 120,"amenities":" free wifi pool free breakfast"},
    {"hotelname": "Novotel", "location": "Hyderabad Airport", "rooms": 80}
]

class RoomBooking(BaseModel):
    roomNumber: int
    guestName: str
    checkIn: str
    checkOut: str

class RoomUpdate(BaseModel):
    oldRoomNumber: int
    newRoomNumber: int

@router.get("/")
def get_all_hotels():
    return hotels

@router.get("/{hotelname}")
def get_hotel_by_name(hotelname: str):
    hotel = next((h for h in hotels if h["hotelname"] == hotelname), None)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel

@router.post("/{hotelname}/room")
def book_room(hotelname: str, booking: RoomBooking):
    return {
        "message": f"Room booked at {hotelname}",
        "roomNumber": booking.roomNumber,
        "guestName": booking.guestName,
        "checkIn": booking.checkIn,
        "checkOut": booking.checkOut
    }

@router.put("/{hotelname}/room")
def update_room(hotelname: str, room: RoomUpdate):
    return {
        "message": f"Room updated at {hotelname}",
        "oldRoomNumber": room.oldRoomNumber,
        "newRoomNumber": room.newRoomNumber
    }

@router.delete("/{hotelname}")
def delete_hotel(hotelname: str):
    return {"message": f"Hotel {hotelname} deleted"}