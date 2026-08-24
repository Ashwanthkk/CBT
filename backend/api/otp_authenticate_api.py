import mysql.connector as ms
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.auth import Authentication
from database.temp_store import otp_operations
from datetime import datetime, timedelta

router=APIRouter()



class email_verification(BaseModel):
    email:str

class otp_verification(BaseModel):
    email:str
    user_otp:str


@router.post("/send-otp")
def send_otp(data: email_verification):

    auth = Authentication(data.email)

    res = auth.send_otp()

    if not res[0]:
        raise HTTPException(
            status_code=500,
            detail="Failed to send OTP"
        )

    expiry_time = datetime.now() + timedelta(minutes=10)

    otp_op = otp_operations(
        data.email,
        res[1],
        expiry_time
    )

    success = otp_op.upload()

    return {
        "email": data.email,
        "result": success
    }


@router.post("/verify-otp")
def verify_otp(otp_data:otp_verification):

    """
        Sample output
        
        case 1 where otp is accepted
        {
            "email":"test@gmail.com",
            "result":True,
            "message":"otp_accepted"
            
        }
    
        case 2 where otp is expired
    
         {
                "email":"test@gmail.com",
                "result":False,
                "message":"otp_expired"
                
            } 
    
        case 3:otp mismatch
    
        {
            "email":"test@gmail.com",
            "result":False,
            "message":"invalid_otp"
            
        } 
       
         """

    otp_initialize=otp_operations(otp_data.email,otp_data.user_otp)
    curr_time=datetime.now()

    result=otp_initialize.verify(curr_time)

    

    #clear temproary otp from the server 
    if result[0]:
        otp_initialize.clear()


    return {
            "email":otp_data.email,
            "result":result,
            "message":result[1]
        }


@router.post("/resend-otp")
def resend_otp(data: email_verification):

    auth = Authentication(data.email)

    # Generate and send a NEW OTP
    res = auth.send_otp()

    if not res[0]:
        raise HTTPException(
            status_code=500,
            detail="Failed to resend OTP"
        )

    expiry_time = datetime.now() + timedelta(minutes=10)

    otp_op = otp_operations(
        data.email,
        res[1],
        expiry_time
    )

    # upload() already checks whether an OTP
    # exists for this email and clears it.
    success = otp_op.upload()

    return {
        "email": data.email,
        "result": success
    }

