from pydantic import BaseModel


class ResetResponseSchema(BaseModel):
    message: str