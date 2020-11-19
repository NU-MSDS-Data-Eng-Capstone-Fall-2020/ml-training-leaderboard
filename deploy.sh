aws cloudformation deploy \
    --region us-east-1 \
    --stack-name LeaderBoardCoreStack \
    --no-fail-on-empty-changeset \
    --template-file ./cfn/core.yml \
    --capabilities CAPABILITY_NAMED_IAM

BUCKET_NAME=$(aws cloudformation describe-stacks \
    --region us-east-1 \
    --stack-name LeaderBoardCoreStack \
    --query "Stacks[0].Outputs[?OutputKey=='LambdaBucketName'].OutputValue" \
    --output text)

TABLE_NAME=$(aws cloudformation describe-stacks \
    --region us-east-1 \
    --stack-name LeaderBoardCoreStack \
    --query "Stacks[0].Outputs[?OutputKey=='DynamoTableName'].OutputValue" --output text)

echo "${BUCKET_NAME}"
echo "${TABLE_NAME}"

zip -r -j get_submissions.zip lambda
zip -r -j submit.zip lambda

aws s3 cp get_submissions.zip "s3://$BUCKET_NAME/get_submissions.zip"
aws s3 cp submit.zip "s3://$BUCKET_NAME/submit.zip"

aws cloudformation deploy \
    --region us-east-1 \
    --stack-name LeaderBoardLambdaStack \
    --no-fail-on-empty-changeset \
    --template-file ./cfn/lambda.yml \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameter-overrides S3SourceBucket="$BUCKET_NAME" \
                          DynamoTableName=$TABLE_NAME

aws lambda update-function-code \
    --region us-east-1 \
    --function-name LeaderBoardLambdaStack-get-handler \
    --s3-bucket "$BUCKET_NAME" \
    --s3-key "get_submissions.zip"

aws lambda update-function-code \
    --region us-east-1 \
    --function-name LeaderBoardLambdaStack-submit-handler \
    --s3-bucket "$BUCKET_NAME" \
    --s3-key "submit.zip"