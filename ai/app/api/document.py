from fastapi import APIRouter

from app.schemas.document_schema import ProcessDocumentRequest

router = APIRouter(
    prefix= "/documents",
    tags=["documents"]
)

@router.post('process')

def process_documnet(request:ProcessDocumentRequest):

    return {
        "message":"Received",
        "documnet_id":request.document_id,
        "file_path":request.file_path
    }
