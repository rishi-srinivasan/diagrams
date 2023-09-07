from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
import os

path= "./images"

if not os.path.exists(path):
    os.mkdir(path)

os.chdir(path)

filename= "simple-web-service"

with Diagram(filename, show=False):
    ELB("sample-lb") >> EC2("sample-instance") >> RDS("sample-rds")

print(f'Current working directory: {os.getcwd()}')