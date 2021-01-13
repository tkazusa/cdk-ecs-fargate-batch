#!/usr/bin/env python3

from aws_cdk import core

from src.entities.ecr import SampleEcr
from src.stack.ecr import EcrStack


app = core.App()

# 全てのリソースに設定するタグ
tags = {'CreatedBy': 'tkazusa'}

EcrStack(app, id='SampleEcr', ecr_entity=SampleEcr, tags=tags)

app.synth(skip_validation=False)
