# aws_lambda_pil

Objectives:
- Demonstrate how to automate data processing using event-driven cloud services (here AWS Lambda) for large-scale file processing.
- Demonstrate knowledge of AWS services by combining AWS Lambda with other AWS services (Amazon's Simple Storage Service (S3), their object storage service).
- Demonstrate knowledge of deployment packages and working with buckets (container for objects stored in Amazon S3).

Process:
- Deployed Python code in AWS Lambda that converts jpeg files to png files. 
- The jpeg files are initially uploaded into a source S3 bucket. This action serves as an event for triggering the Lambda function. The Lambda function then writes the files to the output S3 bucket, storing the files in a png format.
- Used a deployment package, as per AWS documentation, to deploy my function code to Lambda. The deployment package is a .zip file containing the code created on my local machine, bundled together with the dependencies. The dependencies of the code are PIL and boto3, and its second level dependencies (i.e. the packages that are used by PIL and boto3). The deployment package was created locally using Bash scripting and uploaded manually into the AWS Console in the Lambda user interface.

Improvements: 
- Could use IaaC (Infrastructure as a Code) to create the deployment package and upload it to AWS Lambda. 
- Examples of such IaaC tools are : Serverless Framework, CloudFormation or Terraform.


Choice of tools:
- AWS Lambda and S3 : automatically scaling up and down, these services provide low-cost flexibility and run in a highly available configuration across multiple data centres.
- boto3: it is the Software Development Kit (SDK) or 'devkit' for AWS. In the context of this project it is used to communicate between AWS Lambda and AWS S3. 




