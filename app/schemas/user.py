from pydantic import BaseModel, ConfigDict, Field

class UserCreate(BaseModel):
  email: str
  password: str = Field(min_length = 8)

class UserOut(BaseModel):
  id : int
  email : str
  model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
  access_token : str
  token_type : str
  
