from typing import List

from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from schemas.jobs import JobCreate,ShowJob
from db.session import get_db
from db.repestory.jobs import create_new_job,retreive_job,list_jobs

router2=APIRouter()

@router2.post("/jobs",response_model=ShowJob)
def create_job(job:JobCreate,db:Session=Depends(get_db)):
    owner_id=1
    job=create_new_job(job,db,owner_id)
    return job
@router2.get("/get/{id}",response_model=ShowJob)
def retreive_job_by_id(id:int,db:Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    print(job)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Job with id {id} does not exist")
    return job

@router2.get("/all",response_model=List[ShowJob])
def retreive_all_jobs(db:Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs

@router2.put("/update/{id}")
def update_job(id:int,job:JobCreate,db:Session=Depends(get_db)):
    owner_id = 1
    job_retrieved = retreive_job(id=id, db=db)
    if not job_retrieved:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Job with id {id} does not exist")
    if job_retrieved.owner_id == 1:
        message = update_job_by_id(id=id, job=job, db=db, owner_id=owner_id)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"You are not authorized to update.")
    return {"detail":"Successfully updated data."}
@router2.delete("/delete/{id}")
def delete_job(id:int,db:Session=Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Job with id {id} does not exist")
    if job.owner_id == 1:
        delete_job_by_id(id=id, db=db, owner_id=1)
        return {"detail":"Job Successfully deleted"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail="You are not permitted!!")