"""Sinks-test plugin HTTP routes — POST /api/sinks-test/emit (TAP-771)."""

from __future__ import annotations

from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(prefix="/api/sinks-test", tags=["sinks-test"])


class EmitRequest(BaseModel):
    event_type: str = "bar"
    payload: dict = {}


@router.post("/emit")
async def emit(body: EmitRequest, request: Request) -> dict:
    bus = getattr(request.app.state, "topic_bus", None)
    if bus is not None:
        await bus.emit("project.sinks-test", body.event_type, body.payload)
    return {"emitted": True, "event_type": body.event_type}
