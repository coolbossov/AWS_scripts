import boto.ec2
import datetime

conn = boto.ec2.connect_to_region("us-east-1", aws_access_key_id='AKIAJOKH4OR3SHZAJRQQ',
                                  aws_secret_access_key='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')


instances_list = []
reservations = conn.get_all_instances()

print len(reservations)
print "---------"

# Get a list of all the ec2 instances
for r in reservations:
    instances = r.instances
    instances_list.append(instances)
    print instances_list?≥,lpo0p-[,]


instances_listt = [ r.instances for r in reservations]

print instances_listt
print len(instances_list), len(instances_listt)

#Get the list of machines running loger than 2 weeks

for o in instances_list:
    lt_datetime = parse(i.launch_time)
    lt_delta = datetime.datetime.now(lt_datetime.tzinfo) - lt_datetime
    uptime = str(lt_delta)
    print(uptime)








