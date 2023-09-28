from enum import Enum

class Status(str, Enum):
    completed = "completed"
    pending = "pending"
    canceled = "canceled"

class ExtendedStatus():
    all = "all"
