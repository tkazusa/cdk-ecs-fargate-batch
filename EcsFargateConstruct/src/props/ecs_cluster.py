from dataclasses import dataclass, field

from aws_cdk import (
    aws_ec2 as ec2
)

from .base import Base


@dataclass(frozen=False)
class EcsCluster(Base):
    id: str
    cluster_name: str
    vpc: ec2.Vpc = field(init=False)