import ntcore
import time

inst = ntcore.NetworkTableInstance.getDefault()
inst.setServer("127.0.0.1")
inst.startClient4("example client")
table = inst.getTable("SmartDashboard/DynamicAutos")

entry = table.getStringTopic("BlockTypes").getEntry("")

while True:
    print(entry.get(""))
    time.sleep(1)
