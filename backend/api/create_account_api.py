from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from connection.operations import ProfessorRepository
from services.auth import Authentication


router = APIRouter()

professor_repository = ProfessorRepository()


class ProfessorCreate(BaseModel):
    profile_id: str
    name: str
    email: str
    password: str
    phone_number: str | None = None
    university_id: int | None = None
    department_id: int | None = None
    designation: str | None = None
    employee_id: str | None = None


@router.post("/create-account")
def create_professor(data: ProfessorCreate):

    password_hash = Authentication.hash(data.password)

    success = professor_repository.create(
        profile_id=data.profile_id,
        name=data.name,
        email=data.email,
        password_hash=password_hash,
        phone_number=data.phone_number,
        university_id=data.university_id,
        department_id=data.department_id,
        designation=data.designation,
        employee_id=data.employee_id
    )

    if not success:
        raise HTTPException(
            status_code=400,
            detail="Failed to create professor"
        )

    return {
        "message": "Professor created successfully"
    }

if __name__== "__main__":
    import uvicorn
    uvicorn.run(router, host="[IP_ADDRESS]", port=8000) 