# Very simple test script to ensure netbox custom scripts are working
# Note:
# - make sure the script directory is mounted in both these containers:
#   netboxdemo-netbox-1 : webapp container
#   netboxdemo-netbox-worker-1 : rqworker container

from extras.scripts import Script


class TestScript(Script):
    class Meta:
        name = "Test"
        description = "Test script"

    def run(self, data, commit):
        self.log_info("Test ran successfully")
