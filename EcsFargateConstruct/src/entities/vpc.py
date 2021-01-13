from src.entities.base import Base
from src.props.vpc import Vpc


class VpcBase(Base):
    """Vps基底class"""

    vpc: Vpc


class SampleVpc(VpcBase):
    """Vps"""

    vpc = Vpc(
        id='vpc',
        cidr='10.0.0.0/16',
        max_azs=2,
        nat_gateways=1,
        vpn_gateway=False
    )