import uuid
from sqlalchemy import TIMESTAMP, UUID, Boolean, String, inspect
from models.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column
from models.mixin import TimestampMixin

class ModelUser(TimestampMixin,Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name: Mapped[String] = mapped_column(String,nullable=False)
    email: Mapped[String] = mapped_column(String,unique=True, index=True, nullable=False)
    phone: Mapped[String] = mapped_column(String,unique=True, nullable=False)
    username: Mapped[String] = mapped_column(String,unique=True, nullable=False)
    password: Mapped[String] = mapped_column(String,nullable=False)
    is_super_admin: Mapped[Boolean] = mapped_column(Boolean,nullable=False, default=False)
    is_active: Mapped[Boolean] = mapped_column(Boolean,nullable=False, default=True)
    last_login: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP,nullable=True, server_default=None)
    timezone: Mapped[String] = mapped_column(String,nullable=False, server_default='Universal')