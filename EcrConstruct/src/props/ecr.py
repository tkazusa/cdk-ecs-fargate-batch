from dataclasses import dataclass
from typing import Optional

from aws_cdk.aws_ecr import TagStatus
from aws_cdk.core import RemovalPolicy

from .base import Base


@dataclass(frozen=True)
class LifecycleRule(Base):
    description: Optional[str] = None
    max_image_count: int = 5
    rule_priority: int = 1
    tag_status: TagStatus = TagStatus.ANY


@dataclass(frozen=True)
class Repository(Base):
    id: str
    repository_name: str
    image_scan_on_push: Optional[bool] = None
    removal_policy: RemovalPolicy = RemovalPolicy.DESTROY
