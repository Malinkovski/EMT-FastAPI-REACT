from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from database.database import get_db
from service import host_service
from model.schemas import HostShema

router = APIRouter(prefix="/api/hosts", tags=["Hosts"])


@router.get("", response_model=list[HostShema])
async def list_hosts(db: Session = Depends(get_db)):
    return host_service.list_all(db)


@router.get("/{host_id}", response_model=HostShema)
async def find_host(host_id: int, db: Session = Depends(get_db)):
    host = host_service.find_by_id(db, host_id)
    if host is not None:
        return host

    return JSONResponse(
        status_code=404,
        content={"message": f"Host with id {host_id} not found"}
    )