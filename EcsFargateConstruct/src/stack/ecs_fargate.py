from typing import Any

from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_ecr as ecr,
    aws_ecs as ecs,
    aws_logs as logs,
    aws_events as events,
    aws_events_targets as events_targets,
    )


class EcsFargateBatchStack(core.Stack):

    def __init__(
            self,
            scope: core.Construct,
            id: str,
            ecr_entity,
            vpc_entity,
            ecs_cluster_entity,
            logs_entity,
            fargate_entity,
            event_rule_entity,
            **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # ====================================
        # ECR
        # ====================================
        ecr_repository = ecr.Repository.from_repository_name(
            self,
            **ecr_entity.repository_from_name.to_dict())
        
        # ====================================
        # VPC
        # ====================================
        vpc = ec2.Vpc(
            self,
            **vpc_entity.vpc.to_dict()
        )

        # ====================================
        # CloudWatch Logs
        # ====================================
        log_group = logs.LogGroup(
            self,
            **logs_entity.log_group.to_dict()
        )

        log_driver_data = logs_entity.log_driver
        log_driver_data.log_group = log_group
        log_driver = ecs.LogDriver.aws_logs(
            **log_driver_data.to_dict()
        )

        # ====================================
        # ECS Cluster
        # ====================================
        ecs_cluster_data = ecs_cluster_entity.ecs_cluster
        ecs_cluster_data.vpc = vpc 
        
        ecs_cluster = ecs.Cluster(
            self,
            **ecs_cluster_data.to_dict(),
        )

        # ====================================
        # Fargate
        # ====================================
        # Create fargate task definition.
        fargate_task_definition = ecs.FargateTaskDefinition(
            self,
            **fargate_entity.fargate_task_definition.to_dict()
        )

        # Add container to task definition.
        fargate_container_data = fargate_entity.fargate_container
        fargate_container_data.image = ecs.ContainerImage.from_ecr_repository(ecr_repository)
        fargate_container_data.logging = log_driver
        fargate_task_definition.add_container(
            **fargate_container_data.to_dict()
        )
        
        # ====================================
        # CloudWatch Events rule
        # ====================================
        rule = events.Rule(
            self,
            **event_rule_entity.event_rule.to_dict()
        )

        rule.add_target(
            target=events_targets.EcsTask(
                cluster=ecs_cluster,
                task_definition=fargate_task_definition,
                task_count=1
            )
        )
