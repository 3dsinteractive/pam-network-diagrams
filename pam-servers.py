from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.network import ELB
from diagrams.aws.database import ElastiCache, RDS, ElasticacheForRedis
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.aws.analytics import ManagedStreamingForKafka
from diagrams.aws.general import GenericFirewall
from diagrams.aws.database import RDSMysqlInstance

with Diagram("PAM Servers Mini", show=False):
    lb = ELB("Load balancer")

    with Cluster("EKS Managed K8S"):
        with Cluster("Workers Golang Microservices"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        fw = GenericFirewall("Firewall")

        with Cluster("Elasticsearch Cluster"):
            dbs = [ECS("db1"),
                   ECS("db2"),
                   ECS("db3")]

    with Cluster("Managed Services"):
        s3 = S3("Images and Files")
        kfk = ManagedStreamingForKafka("Managed Kafka")
        redis = ElasticacheForRedis("Managed Redis")
        mysql = RDSMysqlInstance("Managed MySql")

    lb >> workers
    workers >> fw >> dbs
    workers >> s3
    workers >> kfk
    workers >> redis
    workers >> mysql

with Diagram("PAM Servers Basic", show=False):
    lb = ELB("Load balancer")

    with Cluster("EKS Managed K8S"):
        with Cluster("Workers Golang Microservices"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        fw = GenericFirewall("Firewall")

        with Cluster("Elasticsearch Cluster"):
            dbs = [ECS("db1"),
                   ECS("db2"),
                   ECS("db3")]

    with Cluster("Managed Services"):
        s3 = S3("Images and Files")
        kfk = ManagedStreamingForKafka("Managed Kafka")
        redis = ElasticacheForRedis("Managed Redis")
        mysql = RDSMysqlInstance("Managed MySql")

    lb >> workers
    workers >> fw >> dbs
    workers >> s3
    workers >> kfk
    workers >> redis
    workers >> mysql

with Diagram("PAM Servers Pro", show=False):
    lb = ELB("Load balancer")

    with Cluster("EKS Managed K8S"):
        with Cluster("Workers Golang Microservices"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        fw = GenericFirewall("Firewall")

        with Cluster("Elasticsearch Cluster"):
            dbs = [ECS("db1"),
                   ECS("db2"),
                   ECS("db3"),
                   ECS("db4"),
                   ECS("db5")]

    with Cluster("Managed Services"):
        s3 = S3("Images and Files")
        kfk = ManagedStreamingForKafka("Managed Kafka")
        redis = ElasticacheForRedis("Managed Redis")
        mysql = RDSMysqlInstance("Managed MySql")

    lb >> workers
    workers >> fw >> dbs
    workers >> s3
    workers >> kfk
    workers >> redis
    workers >> mysql

with Diagram("PAM Servers Pro XL", show=False):
    lb = ELB("Load balancer")

    with Cluster("EKS (Managed Kubernetes"):
        with Cluster("Workers Golang Microservices"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3"),
                       ECS("worker4"),
                       ECS("worker5")]

        fw = GenericFirewall("Firewall")

        with Cluster("Elasticsearch Cluster"):
            dbs = [ECS("db1"),
                   ECS("db2"),
                   ECS("db3"),
                   ECS("db4"),
                   ECS("db5"),
                   ECS("db6"),
                   ECS("db7")]

    with Cluster("Managed Services"):
        s3 = S3("Images and Files")
        kfk = ManagedStreamingForKafka("Managed Kafka")
        redis = ElasticacheForRedis("Managed Redis")
        mysql = RDSMysqlInstance("Managed MySql")

    lb >> workers
    workers >> fw >> dbs
    workers >> s3
    workers >> kfk
    workers >> redis
    workers >> mysql

with Diagram("PAM Servers Pro 2XL", show=False):
    lb = ELB("Load balancer")

    with Cluster("EKS Managed K8S"):
        with Cluster("Workers Golang Microservices"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3"),
                       ECS("worker4"),
                       ECS("worker5"),
                       ECS("worker6"),
                       ECS("worker7"),
                       ECS("worker8")]

        fw = GenericFirewall("Firewall")

        with Cluster("Elasticsearch Cluster"):
            dbs = [ECS("db1"),
                   ECS("db2"),
                   ECS("db3"),
                   ECS("db4"),
                   ECS("db5"),
                   ECS("db6"),
                   ECS("db7"),
                   ECS("db8"),
                   ECS("db9"),
                   ECS("db10")]

    with Cluster("Managed Services"):
        s3 = S3("Images and Files")
        kfk = ManagedStreamingForKafka("Managed Kafka")
        redis = ElasticacheForRedis("Managed Redis")
        mysql = RDSMysqlInstance("Managed MySql")

    lb >> workers
    workers >> fw >> dbs
    workers >> s3
    workers >> kfk
    workers >> redis
    workers >> mysql
