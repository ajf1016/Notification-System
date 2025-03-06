from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from services.db import get_db, get_cassandra_session
from services.notification import notify_user

app = FastAPI()


class NotificationRequest(BaseModel):
    user_id: str
    message: str


@app.post("/send")
def send_notification(
    request: NotificationRequest,
    db: Session = Depends(get_db),
    cassandra_session=Depends(get_cassandra_session),
):
    return notify_user(request.user_id, request.message, db, cassandra_session)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
