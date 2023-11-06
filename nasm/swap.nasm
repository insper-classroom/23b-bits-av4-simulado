leaw $SP, %A
movw (%A), %A
decw %A
movw (%A), %D
leaw $7, %A
movw %D, (%A)
leaw $SP, %A
movw (%A), %A
decw %A
decw %A
movw (%A), %D
incw %A
movw %D, (%A)
leaw $7, %A
movw (%A), %D
leaw $SP, %A
movw (%A), %A
decw %A
decw %A
movw %D, (%A)
