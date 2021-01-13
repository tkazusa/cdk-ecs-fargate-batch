from src.entities.base import Base
from src.props.ecs_cluster import EcsCluster


class EcsClusterBase(Base):
    """ECSCluster基底class"""

    ecs_cluster: EcsCluster


class SampleEcsCluster(EcsClusterBase):
    """ECSCluster"""

    ecs_cluster = EcsCluster(
        id='ecs_cluster',
        cluster_name='sample_fargate_batch_cluster',
        #vpc='vpc'
    )