from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np

from nutrihelp_ai.services.retrieve_response import retrieve_response_service

router = APIRouter()

class UserInput(BaseModel):
    Input: str


@router.post("/query")
def retrieve_response(input_data: UserInput):
    try:
        return retrieve_response_service(input_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
