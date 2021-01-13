from src.entities.base import Base
from src.props.fargate import (
    FargateTaskDefinition,
    FargateContainer
)


class FargateTaskDefinitionBase(Base):
    """Fargate基底class"""

    fargate_task_definition: FargateTaskDefinition
    fargate_container = FargateContainer


class SampleFargateTaskDefinition(FargateTaskDefinitionBase):
    """Fargateタスク定義"""

    fargate_task_definition = FargateTaskDefinition(
        id='fargate-task-definition',
        cpu=256,
        memory_limit_mib=512,
        family='fargate-task-definition'
        )
    
    fargate_container = FargateContainer(
        id='container'
    )