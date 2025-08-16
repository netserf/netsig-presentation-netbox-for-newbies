"""
Hello World Script for NetBox.

This module provides a simple script that demonstrates the NetBox scripting
functionality by logging a "Hello World" message.
"""

from extras.scripts import Script


class HelloWorldScript(Script):
    class Meta:
        name = "Hello World"
        description = "A demo script that logs a simple greeting."

    def run(self, data, commit):
        self.log_info("Hello, World! 🎉 This script ran successfully.")
