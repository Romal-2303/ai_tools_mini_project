from pydantic import BaseModel


class videoInfoModel(BaseModel):
    video_link: str
    
    
class ErrorResponse(BaseModel):
    error: str
    
class videInfoResponse(BaseModel):
    duration: int
    format: str
    size: int 