from src.entities.base import Base
from src.props.logs import LogDriver, LogGroup


class LogsBase(Base):
    """Logs基底class"""

    log_driver: LogDriver
    log_group: LogGroup


class SampleLogs(LogsBase):
    """Logs"""

    log_driver = LogDriver(
        stream_prefix='ecs'
    )
    
    log_group = LogGroup(
        id='log-group',
        log_group_name='/ecs/fargate/fargate-batch'
    )