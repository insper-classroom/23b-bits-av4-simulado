#!/usr/bin/env python3

from bits import VMCode


class testCode(VMCode):

    def writeArithmetic(self, command):
        commands = []
        if command == "delete":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("subw %A, $1, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        elif command == "add3":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D, %D")
            commands.append("decw %A")
            commands.append("addw (%A), %D, %D")
            commands.append("decw %A")
            commands.append("addw (%A), %D, %D")
            commands.append("movw %D, (%A)")
            commands.append("addw %A, $1, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        elif command == "swap":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $7, %A")
            commands.append("movw %D, (%A)")

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("incw %A")
            commands.append("movw %D, (%A)")

            commands.append("leaw $7, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("decw %A")
            commands.append("movw %D, (%A)")

        # não mexer
        self.commandsToFile(commands)
