from app.storage.memory_store import MemoryStore


class SystemService:
    def __init__(self, memory_store: MemoryStore):
        self.memory_store = memory_store
    
    def reset_system(self) -> dict:
        self.memory_store.reset()
        return {
            "message": "System reset successful"
        }