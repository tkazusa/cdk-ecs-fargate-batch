# AWS Fargate を Amazon CloudWatch Events トリガでバッチ処理

## Amazon ECR のリポジトリ を作成
```bash
 $ cd EcrConstruct
 $ cdk deploy SampleEcr
```

## 作成した ECR にバッチ処理用の Doker イメージをレジスト
```bash
$ cd ../containers
$ ./ecr_regist.sh
```

## Amazon CloudWatch Events をトリガにバッチ処理を行う AWS Fargate をデプロイ
```bash
$ cd ../EcsFargateConstruct
$ cdk deploy ecs-fargate-batch
```

# 実装上の注意点
`./EcsFargateConstruct/src/stack/ecs_fargate.py` において、Fargate で仕様する Docker イメージは、`fromEcrRepository` API を使って指定している。これを使ってデプロイした場合、ECR の Docker イメージが更新されたとしても、Fargate のイメージは更新されない。

## 参考
[AWS CDKでECSにデプロイするDockerイメージのマシな管理方法](https://www.ncaq.net/2020/11/09/16/39/42/)
[homoluctus/cdk-py-template](https://github.com/homoluctus/cdk-py-template)
[【AWS】CDKでECRを構築しよう](https://qiita.com/homines22/items/71e5b596e3edab46f0621)
