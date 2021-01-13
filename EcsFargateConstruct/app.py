#!/usr/bin/env python3

from aws_cdk import core

from src.entities.ecr import BatchEcr
from src.entities.vpc import SampleVpc
from src.entities.ecs_cluster import SampleEcsCluster
from src.entities.logs import SampleLogs
from src.entities.fargate import SampleFargateTaskDefinition
from src.entities.event_rule import SampleEventRule
from src.stack.ecs_fargate import EcsFargateBatchStack


app = core.App()

# 全てのリソースに設定するタグ
tags = {'CreatedBy': 'tkazusa'}

EcsFargateBatchStack(
    app,
    id='ecs-fargate-batch',
    ecr_entity=BatchEcr,
    vpc_entity=SampleVpc,
    ecs_cluster_entity=SampleEcsCluster,
    logs_entity=SampleLogs,
    fargate_entity=SampleFargateTaskDefinition,
    event_rule_entity=SampleEventRule,
    tags=tags)

app.synth(skip_validation=False)