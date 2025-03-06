from fastapi import Depends
from sqlalchemy.orm import Session
from services.db import get_db, get_cassandra_session
from models import UserPreferences


def send_email(email: str, message: str):
    """ Simulate sending an email """
    print(f"Email sent to {email}: {message}")


def send_sms(phone: str, message: str):
    """ Simulate sending an SMS """
    print(f"SMS sent to {phone}: {message}")


def send_push(user_id: str, message: str):
    """ Simulate sending a push notification """
    print(f"Push Notification Sent to {user_id}: {message}")


def log_notification(cassandra_session, user_id, message, channel):
    """ Log notification to Cassandra """
    print(f"Logged {channel} notification for {user_id}: {message}")


def notify_user(user_id: str, message: str, db: Session, cassandra_session):
    """ Send notification based on user preferences """
    user = db.query(UserPreferences).filter(
        UserPreferences.user_id == user_id).first()
    if not user:
        return {"error": "User not found"}

    if user.prefers_email:
        send_email(user.email, message)
        log_notification(cassandra_session, user_id, message, "email")

    if user.prefers_sms:
        send_sms(user.phone, message)
        log_notification(cassandra_session, user_id, message, "sms")

    if user.prefers_push:
        send_push(user_id, message)
        log_notification(cassandra_session, user_id, message, "push")

    return {"status": "Notifications Sent"}
