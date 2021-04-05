from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.network import ELB
from diagrams.aws.database import ElastiCache, RDS, ElasticacheForRedis
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.aws.analytics import ManagedStreamingForKafka
from diagrams.aws.general import GenericFirewall

with Diagram("PAM Servers Mini", show=False):
    lb = ELB("lb")

    with Cluster("EKS"):
        with Cluster("Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        fw = GenericFirewall("Firewall")

        with Cluster("Databases"):
            dbs = [ECS("db1"),
                   ECS("db2"),
                   ECS("db3")]

    s3 = S3("Images and Files")
    kfk = ManagedStreamingForKafka("Kafka Streams")
    redis = ElasticacheForRedis("Redis")

    lb >> workers
    workers >> fw >> dbs
    workers >> s3
    workers >> kfk
    workers >> redis

with Diagram("PAM Servers Basic", show=False):
    lb = ELB("lb")

    with Cluster("EKS"):
        with Cluster("Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        fw = GenericFirewall("Firewall")

        with Cluster("Databases"):
            dbs = [ECS("db1"),
                   ECS("db2"),
                   ECS("db3")]

    s3 = S3("Images and Files")
    kfk = ManagedStreamingForKafka("Kafka Streams")
    redis = ElasticacheForRedis("Redis")

    lb >> workers
    workers >> fw >> dbs
    workers >> s3
    workers >> kfk
    workers >> redis

with Diagram("PAM Servers Pro", show=False):
    lb = ELB("lb")

    with Cluster("EKS"):
        with Cluster("Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        fw = GenericFirewall("Firewall")

        with Cluster("Databases"):
            dbs = [ECS("db1"),
                   ECS("db2"),
                   ECS("db3")]

    s3 = S3("Images and Files")
    kfk = ManagedStreamingForKafka("Kafka Streams")
    redis = ElasticacheForRedis("Redis")

    lb >> workers
    workers >> fw >> dbs
    workers >> s3
    workers >> kfk
    workers >> redis

with Diagram("PAM Servers Pro XL", show=False):
    lb = ELB("lb")

    with Cluster("EKS"):
        with Cluster("Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        fw = GenericFirewall("Firewall")

        with Cluster("Databases"):
            dbs = [ECS("db1"),
                   ECS("db2"),
                   ECS("db3")]

    s3 = S3("Images and Files")
    kfk = ManagedStreamingForKafka("Kafka Streams")
    redis = ElasticacheForRedis("Redis")

    lb >> workers
    workers >> fw >> dbs
    workers >> s3
    workers >> kfk
    workers >> redis

with Diagram("PAM Servers Pro 2XL", show=False):
    lb = ELB("lb")

    with Cluster("EKS"):
        with Cluster("Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        fw = GenericFirewall("Firewall")

        with Cluster("Databases"):
            dbs = [ECS("db1"),
                   ECS("db2"),
                   ECS("db3")]

    s3 = S3("Images and Files")
    kfk = ManagedStreamingForKafka("Kafka Streams")
    redis = ElasticacheForRedis("Redis")

    lb >> workers
    workers >> fw >> dbs
    workers >> s3
    workers >> kfk
    workers >> redis
