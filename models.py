from datetime import datetime

class Task:
    _id_counter = 1

    def __init__(self, name: str):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.name = name or f"Task-{self.id}"
        self.status = "running"
        self.created_at = datetime.utcnow()
