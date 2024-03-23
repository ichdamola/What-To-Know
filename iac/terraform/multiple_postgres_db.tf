# configured aws provider with proper credentials
provider "aws" {
  region  = "eu-west-1"
  profile = "default"
}

# create default vpc if one does not exist
resource "aws_default_vpc" "default_vpc" {
  tags = {
    Name = "default vpc"
  }
}

# use data source to get all availability zones in region
data "aws_availability_zones" "available_zones" {}

# create a default subnet in the first AZ if one does not exist
resource "aws_default_subnet" "subnet_az1" {
  availability_zone = data.aws_availability_zones.available_zones.names[0]
}

# create a default subnet in the second AZ if one does not exist
resource "aws_default_subnet" "subnet_az2" {
  availability_zone = data.aws_availability_zones.available_zones.names[1]
}

# create security group for the web server
resource "aws_security_group" "webserver_security_group" {
  name        = "webserver security group"
  description = "enable http access on port 80"
  vpc_id      = aws_default_vpc.default_vpc.id

  ingress {
    description = "http access"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "webserver security group"
  }
}

# create security group for the database
resource "aws_security_group" "database_security_group" {
  name        = "database security group"
  description = "enable postgres/aurora access on port 5432"
  vpc_id      = aws_default_vpc.default_vpc.id

  ingress {
    description = "postgre/aurora access"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Modify this to allow access from specific IPs
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "database security group"
  }
}

# create the subnet group for the rds instance
resource "aws_db_subnet_group" "database_subnet_group" {
  name        = "database-subnets"
  subnet_ids  = [aws_default_subnet.subnet_az1.id, aws_default_subnet.subnet_az2.id]
  description = "subnets for database instance"

  tags = {
    Name = "database-subnets"
  }
}

# create the first RDS instance 1st
resource "aws_db_instance" "db_instance1" {
  engine                 = "postgres"         # Specify the database engine (PostgreSQL)
  engine_version         = "16.1"             # Specify the PostgreSQL version
  multi_az               = false              # Set to true for Multi-AZ deployment
  identifier             = "xxxxxxxxxxxxxxxx" # Unique identifier for the second DB instance
  username               = "xxxxxxxxxxxx"     # Username for the master DB user of the second instance
  password               = "xxxxxxxxxxxx"     # Password for the master DB user of the second instance
  instance_class         = "db.m5d.xlarge"    # Instance type for the first DB instance
  allocated_storage      = 20                 # Allocated storage in GB for the first instance
  db_subnet_group_name   = aws_db_subnet_group.database_subnet_group.name
  vpc_security_group_ids = [aws_security_group.database_security_group.id]
  availability_zone      = data.aws_availability_zones.available_zones.names[0]
  db_name                = "xxxxxxxxxxxxxxx"
  skip_final_snapshot    = true
  publicly_accessible    = true # Allow access from the public internet
}

# create the second RDS instance 2nd
resource "aws_db_instance" "db_instance2" {
  engine                 = "postgres"         # Specify the database engine (PostgreSQL)
  engine_version         = "16.1"             # Specify the PostgreSQL version
  multi_az               = false              # Set to true for Multi-AZ deployment
  identifier             = "xxxxxxxxxxxxxxxx" # Unique identifier for the second DB instance
  username               = "xxxxxxxxxxxx"     # Username for the master DB user of the second instance
  password               = "xxxxxxxxxxxx"     # Password for the master DB user of the second instance
  instance_class         = "db.m5d.xlarge"    # Instance type for the second DB instance
  allocated_storage      = 20                 # Allocated storage in GB for the second instance
  db_subnet_group_name   = aws_db_subnet_group.database_subnet_group.name
  vpc_security_group_ids = [aws_security_group.database_security_group.id]
  availability_zone      = data.aws_availability_zones.available_zones.names[1]
  db_name                = "xxxxxxxxxxxxxxx"
  skip_final_snapshot    = true
  publicly_accessible    = true # Allow access from the public internet
}

# create the second RDS instance 3rd
resource "aws_db_instance" "db_instance3" {
  engine                 = "postgres"         # Specify the database engine (PostgreSQL)
  engine_version         = "16.1"             # Specify the PostgreSQL version
  multi_az               = false              # Set to true for Multi-AZ deployment
  identifier             = "xxxxxxxxxxxxxxxx" # Unique identifier for the second DB instance
  username               = "xxxxxxxxxxxx"     # Username for the master DB user of the second instance
  password               = "xxxxxxxxxxxx"     # Password for the master DB user of the second instance
  instance_class         = "db.m5d.xlarge"    # Instance type for the second DB instance
  allocated_storage      = xx                 # Allocated storage in GB for the second instance
  db_subnet_group_name   = aws_db_subnet_group.database_subnet_group.name
  vpc_security_group_ids = [aws_security_group.database_security_group.id]
  availability_zone      = data.aws_availability_zones.available_zones.names[1]
  db_name                = "xxxxxxxxxxxxxxx"
  skip_final_snapshot    = true
  publicly_accessible    = true # Allow access from the public internet
}

output "database_endpoint_1" {
  value = aws_db_instance.db_instance1.endpoint
}

output "database_endpoint_2" {
  value = aws_db_instance.db_instance2.endpoint
}

output "database_endpoint_3" {
  value = aws_db_instance.db_instance3.endpoint
}
