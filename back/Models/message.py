from pydantic import BaseModel
import json

class Message(BaseModel):
    role: str
    content: str
    tools_used: list[str] = []

    def to_dict(self):
        return {
            "role": self.role,
            "content": self.content,
            "tools_used": self.tools_used,
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())
