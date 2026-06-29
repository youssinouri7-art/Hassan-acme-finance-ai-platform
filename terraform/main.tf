terraform {
  required_version = ">= 1.6.0"
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "demo_logs" {
  bucket = "acme-finance-ai-platform-demo-logs"
}

resource "aws_s3_bucket_public_access_block" "demo_logs" {
  bucket                  = aws_s3_bucket.demo_logs.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
