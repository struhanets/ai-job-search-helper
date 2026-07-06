from fastapi import APIRouter, UploadFile, File, HTTPException

from app.models.domain.candidate import CandidateProfile
from app.parsers.cv_parser import ResumeParserService

router = APIRouter()

@router.post("/parse", response_model=CandidateProfile)
async def parse_cv(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")

    content = await file.read()
    parser = ResumeParserService()
    profile = await parser.parse_resume(content)

    return profile