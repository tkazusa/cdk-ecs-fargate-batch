from src.entities.base import Base
from src.props.ecr import RepositoryFromName


class EcrBase(Base):
    """ECR基底class"""

    repository_from_name: RepositoryFromName


class BatchEcr(EcrBase):
    """ECRRepository"""

    id = 'SampleEcrFromName'

    repository_from_name = RepositoryFromName(
        id='SampleEcrRepoFromName',
        repository_name='sample'
    )