from abc import ABC, abstractmethod

# Publisher
class ChatRoom:
  def __init__(self):
    self._participants = set()

  # Adds participants to the chat room
  def join(self, participant):
    self._participants.add(participant)

  # Removes participants from the chat room
  def leave(self, participant):
    self._participants.remove(participant)
  
  # Sends a message to all participants in the chat room
  def broadcast(self, message):
    for participant in self._participants:
      participant.receive(message)


# Participant - Subscriber Interface
class Participant(ABC):
  # Abstract method for receiving messages
  @abstractmethod
  def receive(self, message):
    pass


# Chat member - concrete subscribers
class ChatMember(Participant):
  def __init__(self, name):
    self.name = name
  
  # Receives and displays the message
  def receive(self, message):
    print(f"{self.name} received: {message}")


# Client
if __name__ == "__main__":
  # Create a chat room
  general_chat = ChatRoom()

  # Create participants
  user1 = ChatMember("User1")
  user2 = ChatMember("User2")
  user3 = ChatMember("User3")

  # Participants join the chat room
  general_chat.join(user1)
  general_chat.join(user2)
  general_chat.join(user3)

  # Send message to chat room
  general_chat.broadcast("Welcome to the chat")