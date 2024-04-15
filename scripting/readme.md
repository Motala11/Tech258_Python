# Scripting

## What is scripting?

Scripting refers to the process of writing scripts, which are sequences of instructions or commands that are interpreted or executed by a computer. It is used for efficiency and automation.

## How is it different to programming?
Whilst often confused, scripting is not the same as programming. The fundamental difference is that scripting is more so interpreted, rather than compiled. This is because scripting is used for automation. Programming is compiled as opposed to interpreted, as programming consists of creating.
## What are the packages in a standard Python library?
Python consists of a plethora of built-in libraries, such as:
- OS - Operating System Interface
- datetime `print(f"Today's date is: {datetime.datetime.today()}")
`
- math `print(math.pi)
`
- random `print(random.randrange(1,12))
`
- collections
- json
## Here are 10 Python scripts a DevOps engineer may use:
- Infrastructure as Code script 
- Deployment script
- Configuration management script
- Monitoring script
- Alert script
- Deployment script
- Backup script
- Restore script
- Container script
- Notification script

## Example of Infrastructure as Code script
```import { App, TerraformStack, Token } 

class MyStack extends TerraformStack {
 constructor(scope: Construct, name: string) {
   super(scope, name);
    new AwsProvider(this, 'aws', {
     region: 'us-east-1'
   });
    const vpc = new Vpc(this, 'my-vpc', {
     cidrBlock: '10.0.0.0/12'
   });
   const subnet = new Subnet(this, 'my-subnet', {
     vpcId: Token.asString(vpc.id),
     cidrBlock: '10.0.0.0/23'
   });```