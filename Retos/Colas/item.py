from pydantic import BaseModel
class Item(BaseModel):
    nombre: str
    productos: list[str]