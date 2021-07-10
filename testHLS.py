from IPython.display import HTML
import boto3
STREAM_NAME = "atiqvideostream"
kvs = boto3.client("kinesisvideo")
# Grab the endpoint from GetDataEndpoint
endpoint = kvs.get_data_endpoint(
    APIName="GET_HLS_STREAMING_SESSION_URL",
    StreamName=STREAM_NAME
)['DataEndpoint']
# Grab the HLS Stream URL from the endpoint
kvam = boto3.client("kinesis-video-archived-media", endpoint_url=endpoint)
url = kvam.get_hls_streaming_session_url(
    StreamName=STREAM_NAME,
    PlaybackMode="LIVE"
)['HLSStreamingSessionURL']


HTML(data='<video src="{0}" autoplay="autoplay" controls="controls" width="300" height="400"></video>'.format(url))