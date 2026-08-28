from fastapi import APIRouter
from pydantic import BaseModel

from database.login import login_verify

router=APIRouter()

class details(BaseModel):
    email:str
    password:str


@router.post('/verify_credentials')
def verify(data:details):

    """api response
    
    case 1 when accepted
    {
        'success': True, 
        'message': 'accepted'

    }

    case 2 when rejected

     {
        'success': False, 
        'message': 'denied'
     }
    """
    
    lv=login_verify(data.email,data.password)
    result=lv.verify()

    return {
        "success":result,
        "message": "accepted" if result else "denied"
    }
