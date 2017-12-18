import boto
from boto.s3.key import Key
import urllib2, StringIO


keyId = ""
sKeyId= "/ZY0"
fileName="abcd.txt"
bucketName=""
file = open(fileName)
conn = boto.connect_s3(keyId,sKeyId)
bucket = conn.get_bucket(bucketName)
#Get the Key object of the bucket
k = Key(bucket)
#Crete a new key with id as the name of the file
url = ""
k.key=url.split('/')[::-1][0]
import pdb;pdb.set_trace()
file_object = urllib2.urlopen(url)           # 'Like' a file object
fp = StringIO.StringIO(file_object.read())   # Wrap object    
k.set_contents_from_file(fp)
#Upload the file
# result = k.set_contents_from_file(file)
k.set_acl('public-read')
url = k.generate_url(expires_in=0, query_auth=False)
print url

# import pdb;pdb.set_trace()
#result contains the size of the file uploaded


from zipfile import ZipFile
zipfile = ZipFile(file_object)
zipfile = ZipFile(fp)
zipfile.namelist()
k.set_contents_from_file(StringIO.StringIO(zipfile.read('2.jpg')))
