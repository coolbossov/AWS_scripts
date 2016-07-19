import boto.ec2

conn = boto.ec2.connect_to_region()

# choose the action you want to perform
# TODO: try using argparse insted of raw_input..
# TODO: var names should be like select_reservatoion
# TODO: I think the user should use minimum effort, so he will just give you the instance name and you will do the work at the background
# Why should he know what is reservation..

action = raw_input("Do you want to L-ist, A-dd or D-elete amazon resources: \n")
if action == "L" or action == "List" or action == "L-ist":
    reservations = conn.get_all_instances()
    print reservations
    select_reservation = int(raw_input("Enter the reservation number you want to list:\n"))
    instances = reservations[select_reservation]  # why do I need to do the this step twice?
    instances_tag = reservations[select_reservation].instances[]
    print "Your instances in reservation %s are %s" % (reservations[select_reservation],
                                                       instances.instances)  # print "Your instances in reservation " + reservations + " are " + instances.instances



else:
    print "error"


