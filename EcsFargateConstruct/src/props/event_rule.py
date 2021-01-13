from dataclasses import dataclass

from aws_cdk import (
    aws_events as events
)

from .base import Base


@dataclass(frozen=True)
class EventRule(Base):
    id: str
    rule_name: str
    description: str
    schedule: events.Schedule
 