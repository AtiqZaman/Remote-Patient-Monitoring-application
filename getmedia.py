import boto3
from numpy.random._examples.cython.extending import out

client = boto3.client('kinesisvideo')
response = client.get_data_endpoint(
    StreamName='atiqvideostream',
    APIName='GET_MEDIA'
)
print(response)
endpoint = response.get('DataEndpoint', None)
print("endpoint %s" % endpoint)

if endpoint is not None:
    client2 = boto3.client('kinesis-video-media', endpoint_url=endpoint)
    response = client2.get_media(
        StreamName='atiqvideostream',
        StartSelector={
            'StartSelectorType': 'EARLIEST',
        }
    )
    print(response)

    stream = response['Payload'].read() # botocore.response.StreamingBody object
    while True:
            ret, frame = stream['payload'].read()
           # out.write(frame)
            print(" stream type ret %s frame %s" % (type(ret), type(frame)))