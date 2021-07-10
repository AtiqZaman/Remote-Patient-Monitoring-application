import boto3
import os




def downloadDirectoryFroms3(bucketName, remoteDirectoryName):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucketName)
    for obj in bucket.objects.filter(Prefix = remoteDirectoryName):
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
            print("Please wait, files are downloading.....")
        bucket.download_file(obj.key, obj.key) # save to same path
# Above Code Resourse:  https://stackoverflow.com/questions/49772151/download-a-folder-from-s3-using-boto3


bucketName = "bucket-rpm"
remoteDirectoryName = "validation"
#downloadDirectoryFroms3(bucketName, remoteDirectoryName)
downloadDirectoryFroms3(bucketName, remoteDirectoryName)
print("Your Files have been downloaded")