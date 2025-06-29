from dotenv import load_dotenv
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from src import db
from src.databases import model, crud, schema


model.Base.metadata.create_all(bind=db.engine)

router = APIRouter(
    prefix="/question",
    tags=["v1"],
    responses={404: {"description": "Not found"}},
)

load_dotenv()


@router.get(
    "/all",
)
async def get_all_question(db: Session = Depends(db.db_session)):
    """
    DBから全ての問題を取得する
    """
    try:
        all_questions = crud.get_all_question(db)
        if not all_questions:
            return JSONResponse(
                status_code=200,
                content={"question": "not exist"},
            )
        return all_questions

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"unexpected error: {str(e)}")


@router.post(
    "/create",
)
async def create_question(
    question: schema.Question,
    db: Session = Depends(db.db_session),
):
    """
    DBに問題を登録する
    """
    try:
        new_question = crud.create_question(db, question)
        if not new_question:
            raise HTTPException(status_code=500, detail="failed to create question")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"unexpected error: {str(e)}")
    return JSONResponse(status_code=200, content={"created": "success"})


@router.delete(
    "/delete/{question_id}",
)
async def delete_question(
    question_id: int,
    db: Session = Depends(db.db_session),
):
    """
    DBから問題を削除する
    """
    try:
        deleted_question = crud.delete_question(db, question_id)
        if not deleted_question:
            raise HTTPException(status_code=500, detail="failed to delete question")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"unexpected error: {str(e)}")
    return JSONResponse(
        content={"question": "deleted", "deleted_question": deleted_question}
    )
