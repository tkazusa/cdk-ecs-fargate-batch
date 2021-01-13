from typing import Any, Type

from aws_cdk import core
from aws_cdk.aws_ecr import Repository

from src.entities.ecr import EcrBase


class EcrStack(core.Stack):
    def __init__(
            self,
            scope: core.Construct,
            id: str,
            ecr_entity: Type[EcrBase],
            **kwargs: Any) -> None:
        super().__init__(scope, id, **kwargs)

        repo = Repository(self, **ecr_entity.repository.to_dict())

        if ecr_entity.lifecyle_rules:
            for rule in ecr_entity.lifecyle_rules:
                repo.add_lifecycle_rule(**rule.to_dict())