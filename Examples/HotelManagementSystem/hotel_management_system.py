from threading import Lock
from typing import Dict, Optional
from guest import Guest
from datetime import date
from room import Room
from room_status import RoomStatus
from reservation import Reservation
from reservation_status import ReservationStatus
from payment import Payment
import uuid

class HotelManagementSystem:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      cls._instance.guests: Dict[str, Guest] = {}
      cls._instance.rooms: Dict[str, Room] = {}
      cls._instance.reservations: Dict[str, Reservation] = {}
      cls._instance.lock = Lock()
    return cls._instance
  
  def addGuest(self, guest: Guest):
    self.guests[guest.id] = guest
  
  def getGuest(self, guest_id: str) -> Optional[Guest]:
    return self.guests.get(guest_id)

  def addRoom(self, room: Room):
    self.rooms[room.id] = room
  
  def getRoom(self, room_id: str) -> Optional[Room]:
    return self.rooms.get(room_id)
  
  def _generate_reservation_id(self) -> str:
    return f"RES{uuid.uuid4().hex[:8].upper()}"

  def bookRoom(self, guest: Guest, room: Room, check_in_date: date, check_out_date: date) -> Optional[Reservation]:
    with self.lock:
      if room.status == RoomStatus.AVAILABLE:
        room.book()
        reservation_id = self._generate_reservation_id()
        reservation = Reservation(reservation_id, guest, room, check_in_date, check_out_date)
        self.reservations[reservation_id] = reservation
        return reservation
      return None
  
  def cancelReservation(self, reservation_id: str):
    with self.lock:
      reservation: Reservation = self.reservations.get(reservation_id)
      if reservation:
        reservation.cancel()
        del self.reservations[reservation_id]
  
  def checkIn(self, reservation_id: str):
    with self.lock:
      reservation: Reservation = self.reservations.get(reservation_id)
      if reservation and reservation.status == ReservationStatus.CONFIRMED:
        reservation.room.checkIn()
      else:
        raise ValueError("Invalid reservation or reservation not confirmed")
  
  def checkOut(self, reservation_id: str, payment: Payment):
    with self.lock:
      reservation: Reservation = self.reservations.get(reservation_id)
      if reservation and reservation.status == ReservationStatus.CONFIRMED:
        room = reservation.room
        amount = room.price * (reservation.check_in_date - reservation.check_out_date).days
        if payment.processPayment(amount):
          room.checkOut()
          del self.reservations[reservation_id]
        else:
          raise ValueError("Payment failed")
      else:
        raise ValueError("Invalid reservation or reservation not confirmed")