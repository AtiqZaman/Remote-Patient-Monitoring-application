from datetime import datetime

import boto3
import kinesis as kinesis

# Kinesis client to call all functions related to kinesis stream
# A low-level client representing Amazon Kinesis Video Streams
kinesis_video_client = boto3.client('kinesisvideo', region_name='us-west-2')

# A low-level client representing Amazon
# Kinesis Video Streams Archived Media (Kinesis Video Archived Media):
client = boto3.client('kinesis-video-archived-media', region_name='us-west-2')


'''
# Create a new kinesis vide stream
createStream = kinesis_client.create_stream(
    #DeviceName='string',
    StreamName='atiqvideostream12',
    MediaType='video/h264,audio/aac',
    #KmsKeyId='string',
    DataRetentionInHours=1,
    #Tags={
     #   'string': 'string'
    #}
)
'''

#print(createStream)


# Delete a specific kinesis video stream
#deleteStream = kinesis_client.delete_stream(
    #StreamARN='string',
    #CurrentVersion='atiqvideostream12'
#)


'''

Returns the most current information about the specified stream. 
You must specify either the StreamName or the StreamARN .

'''
describeStream = kinesis_video_client.describe_stream(
    StreamName='atiqvideostream',
    #StreamARN='string'
)

print(describeStream)

print("/m")

# Get kinesis end points values
getkinesisendpoints = kinesis_video_client.get_data_endpoint(
    StreamARN='arn:aws:kinesisvideo:us-west-2:059312434043:stream/atiqvideostream/1604147465928',
    APIName='GET_MEDIA'
)

print(getkinesisendpoints)


liststream = kinesis_video_client.list_streams(
    MaxResults=123,
    #NextToken='string',
    StreamNameCondition={
        'ComparisonOperator': 'BEGINS_WITH',
        'ComparisonValue': 'string'
    }
)

print(liststream)




