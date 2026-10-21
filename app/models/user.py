from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime, timezone
from app.database import Base

class User(Base):
  __tablename__ = "

  id: Mapped[int] = mapped_column(primary_key = True)

  email: Mapped[str] = mapped_column(String(255), unique=True, index=True)

  hashed_password: Mapped[str] = mapped_column(String(255))

  created_at: Mapped[datetime] = mapped_column(default = lambda: datetime.now(timezone.utc))
