from typing import Annotated

from fastapi import FastAPI, Depends, Path

from celery_service.celery_app import send_email
from deps import get_email

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send-email/{email}")
async def say_hello(content: str, email: str = Annotated[Path, Depends(get_email)]):
    # send email by celery_service worker
    send_email.delay(email, content)
    return {"message": f"Email sent to {email} with content: {content}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
