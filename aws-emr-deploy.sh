# Create cluster on AWS Elastic Map Reduce
aws emr create-cluster --use-default-roles --release-label emr-5.14.0 \
--applications Name=Jupyter --instance-type t1.large --instance-count 2 \
--ec2-attributes KeyName=MyKey,SubnetId=subnet-1234a5b6 --configurations file://MyJupyterConfig.json
