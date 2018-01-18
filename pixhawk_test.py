#print "Start simulator (SITL)"
#import dronekit_sitl
#sitl = dronekit_sitl.start_default()
#connection_string = sitl.connection_string()

# Import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.
#print("Connecting to vehicle on: %s" % (connection_string,))
#vehicle = connect(connection_string, wait_ready=True)
vehicle = connect('/dev/ttyACM0',
            wait_ready= True,
            vehicle_class=None,
            rate=4,
            baud=57600,
            heartbeat_timeout=5)
# Get some vehicle attributes (state)
while (1 > 0):

    print "Get some vehicle attribute values:"
    print " GPS: %s" % vehicle.gps_0
    print " Battery: %s" % vehicle.battery
    print " Last Heartbeat: %s" % vehicle.last_heartbeat
    print " Is Armable?: %s" % vehicle.is_armable
    print " System status: %s" % vehicle.system_status.state
    print " Mode: %s" % vehicle.mode.name    # settable
    print " Attitude :%s" %vehicle.attitude# Close vehicle object before exiting script
    print " Groundspeed :%s" %vehicle.groundspeed
    print " velocity :  %s" %vehicle.velocity
vehicle.close()

# Shut down simulator
#sitl.stop()
print("Completed")