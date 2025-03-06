from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()



NOTIFICATION_SERVICE_URL = "http://notification_service:8001"


@app.get("/")
def health_check():
    return {"status": "API Gateway is running"}


@app.post("/send-notification/")
async def send_notification(data: dict):
    """Forward request to the Notification Service"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{NOTIFICATION_SERVICE_URL}/send", json=data)
            return response.json()
        except httpx.RequestError:
            raise HTTPException(
                status_code=500, detail="Notification service unavailable")

# Run with: uvicorn main:app --host 0.0.0.0 --port 8000
