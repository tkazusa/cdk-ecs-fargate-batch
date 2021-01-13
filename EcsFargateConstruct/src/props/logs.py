from dataclasses import dataclass, field

from aws_cdk import (
    aws_logs as logs 
)

from .base import Base


@dataclass(frozen=False)
class LogDriver(Base):
    stream_prefix: str
    log_group: logs.LogGroup = field(init=False)
 
@dataclass(frozen=True)
class LogGroup(Base):
    id: str
    log_group_name: str