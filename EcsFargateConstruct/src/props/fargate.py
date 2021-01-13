from dataclasses import dataclass, field

from aws_cdk import (
    aws_ecs as ecs
    )

from .base import Base


@dataclass(frozen=True)
class FargateTaskDefinition(Base):
    id: str
    cpu: int
    memory_limit_mib: int
    family: str

@dataclass(frozen=False)
class FargateContainer(Base):
    id: str
    image: ecs.ContainerImage = field(init=False)
    logging: ecs.LogDriver.aws_logs = field(init=False)