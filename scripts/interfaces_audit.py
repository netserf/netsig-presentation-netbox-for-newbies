"""
Interface Audit Script for NetBox.

This module checks all interfaces across devices and logs any interface
that does not have an IPv4 or IPv6 address assigned.
"""

from extras.scripts import Script
from dcim.models import Interface


class InterfaceAuditScript(Script):
    class Meta:
        name = "Interface Audit"
        description = "Find interfaces without an IPv4 or IPv6 address."

    def run(self, data, commit):
        interfaces = Interface.objects.all()

        for iface in interfaces:
            # Each interface may have multiple IPs (v4 or v6)
            ips = iface.ip_addresses.all()
            if not ips.exists():
                self.log_warning(
                    f"{iface.device.name} - {iface.name} "
                    f"has no IP addresses assigned"
                )
