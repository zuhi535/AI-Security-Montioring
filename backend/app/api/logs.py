from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from models.security_log import SecurityLog
from app.schemas.security_log import (
    SecurityLogCreate,
    SecurityLogResponse
)


router = APIRouter(
    prefix="/api/logs",
    tags=["Security Logs"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post(
    "",
    response_model=SecurityLogResponse
)
def create_security_log(
    log: SecurityLogCreate,
    db: Session = Depends(get_db)
):
    db_log = SecurityLog(
        source=log.source,
        source_ip=log.source_ip,
        event_type=log.event_type,
        username=log.username,
        message=log.message,
        severity=log.severity
    )

    db.add(db_log)
    db.commit()
    db.refresh(db_log)

    return db_log