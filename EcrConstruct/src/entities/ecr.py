from typing import List, Optional

from src.entities.base import Base
from src.props.ecr import LifecycleRule, Repository


class EcrBase(Base):
    """ECR基底class"""

    repository: Repository
    lifecyle_rules: Optional[List[LifecycleRule]] = None


class SampleEcr(EcrBase):
    """Sample"""

    id = 'SampleEcr'

    repository = Repository(
        id='SampleEcrRepo',
        repository_name='sample'
    )

    lifecyle_rules = [
        LifecycleRule(
            description='Delete more than 10 images',
            max_image_count=10
        )
    ]