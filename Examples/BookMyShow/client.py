from booking_service import BookingService


if __name__ == "__main__":
  book_service = BookingService.getInstance()
  book_service.initialize()
  book_service.startBookingSession()