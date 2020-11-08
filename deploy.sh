aws cloudformation create-stack \
    --stack-name LeaderBoardCoreStack \
    --template-body file://cfn/core.yml \
    --capabilities CAPABILITY_NAMED_IAM

BUCKET_NAME = $(aws cloudformation describe-stacks \
    --stack-name LeaderBoardCoreStack \
    --query "Stacks[0].Outputs[?OutputKey=='DbUrl'].OutputValue" --output text)

TABLE_NAME = $(aws cloudformation describe-stacks \
    --stack-name LeaderBoardCoreStack \
    --query "Stacks[0].Outputs[?OutputKey=='DbUrl'].OutputValue" --output text)

echo $BUCKET_NAME
echo $TABLE_NAME

zip -r get_submissions.zip lambda
zip -r submit.zip lambda

aws s3 cp ingest.zip "s3://$BUCKET_NAME/get_submissions.zip"
aws s3 cp ingest.zip "s3://$BUCKET_NAME/submit.zip"

aws cloudformation create-stack \
    --stack-name LeaderBoardLambdaStack \
    --template-body file://cfn/lambda.yml \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameters ParameterKey=S3SourceBucket,ParameterValue=$BUCKET_NAME \
                 ParameterKey=DynamoTableName,ParameterValue=$TABLE_NAME
