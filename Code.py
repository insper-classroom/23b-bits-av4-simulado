#!/usr/bin/env python3

from bits import VMCode


class testCode(VMCode):

    def writeArithmetic(self, command):
        commands = []
        if command == "delete":
            commands.append("leaw $SP, %A")

        elif command == "add3":
            commands.append("leaw $SP, %A")

        elif command == "swap":
            commands.append("leaw $SP, %A")


        # não mexer
        self.commandsToFile(commands)
