import  boto.s3


conn = boto.s3.connect_to_region("us-east-1", aws_access_key_id='AKIAJOKH4OR3SHZAJRQQ',
                                  aws_secret_access_key='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')
# print rs
buckets = conn.get_all_buckets()
# print rs
file = open("s3bucketlist.csv", "w")
number = 1
for bucket in buckets:
    # if a.name not in ['fundbox.com', 'fbx.im', 'r.t']:
    if "." not in bucket.name:
        key = list(bucket.list())[0]
        k = bucket.get_key(key.name)
        created = getattr(k, "date", False)
        file.write  ("%s, %s , %s, %s\n" % (number, bucket.name, created, bucket.get_acl().acl.policy))
        number = number + 1
        print number

file.close()


# TODO - date of creation

