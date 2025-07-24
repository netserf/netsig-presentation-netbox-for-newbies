"""
Hello World Script for NetBox.

This module provides a simple script that demonstrates the NetBox scripting
functionality by logging a "Hello World" message.
"""

# pylint: disable=import-error
from extras.scripts import Script


class HelloWorldScript(Script):
    """
    A script that logs a simple Hello World message.

    This class demonstrates the basic structure of a NetBox script.
    """
    class Meta:
        """
        Metadata for the HelloWorldScript.

        Defines the name and description that will be displayed in the NetBox
        UI.
        """
        name = "Hello World"
        description = "A demo script that logs a simple message."

        @staticmethod
        def get_default_name():
            """Return the default name for this script."""
            return "Hello World"

        @staticmethod
        def get_default_description():
            """Return the default description for this script."""
            return "A demo script that logs a simple message."

    def run(self, data, commit):  # pylint: disable=unused-argument
        """
        Execute the script functionality.

        Args:
            data: The data passed from the form (unused in this simple example)
            commit: Boolean indicating whether to commit changes to the
                    database (unused in this example).

        Returns:
            None
        """
        self.log_info("Hello, World! 🎉 This script ran successfully.")

    def get_version(self):
        """
        Return the script version.

        This method is added to satisfy the 'too-few-public-methods' lint rule.

        Returns:
            str: The version of the script.
        """
        return "1.0.0"
