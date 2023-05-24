import os
from aws_cdk import aws_lambda, Environment, Stack, Duration, App
from constructs import Construct

## AWS ACCOUNT: Account informations
ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")
REGION = os.environ.get("AWS_REGION")
ENV = Environment(account=ACCOUNT_ID, region=REGION)


class FluxionalStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.lambda_function()


    def lambda_function(self):
        ecr_image = aws_lambda.EcrImageCode.from_asset_image(
            directory=os.path.join(os.getcwd(), "stack"), file="Dockerfile.lambda"
        )

        return aws_lambda.Function(
            self,
            id="fluxional_lambda",
            description="fluxional_lambda",
            code=ecr_image,
            handler=aws_lambda.Handler.FROM_IMAGE,
            runtime=aws_lambda.Runtime.FROM_IMAGE,
            function_name="fluxional_lambda",
            memory_size=128,
            timeout=Duration.seconds(60),
        )
    
app = App()
FluxionalStack(app, "FluxionalStack", env=ENV)
app.synth()