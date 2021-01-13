from aws_cdk import (
    aws_events as events,
    aws_events_targets as events_targets,
    )

from src.entities.base import Base
from src.props.event_rule import EventRule


class EventRuleBase(Base):
    """CloudWatchEvents基底class"""

    event_rule: EventRule


class SampleEventRule(EventRuleBase):
    """EventRule"""

    id = 'SampleEcr'

    event_rule = EventRule(
        id='rule',
        rule_name='execute-task-rule',
        description='Event rule to execute ecs task.',
        schedule=events.Schedule.cron(
            day=None,
            hour=None,
            minute='*/5', # execute by every 5 minutes.
            month=None,
            week_day=None,
            year=None
        )
    )
