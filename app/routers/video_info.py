from fastapi import APIRouter, HTTPException
from schemas.video_model import videInfoResponse, videoInfoModel, ErrorResponse
from services.video_service import get_video_info
from typing import Union

router  = APIRouter()


@router.post('/video-info', response_model=videInfoResponse, responses={400: {"model": ErrorResponse}})
async def video_info(request: videoInfoModel):
    result = get_video_info(request.video_link)
    
    print("result :", result)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result