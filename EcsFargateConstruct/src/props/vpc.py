from dataclasses import dataclass

from .base import Base


@dataclass(frozen=True)
class Vpc(Base):
    id: str
    cidr: str
    max_azs: int
    nat_gateways: int
    vpn_gateway: bool
