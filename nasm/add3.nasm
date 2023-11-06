leaw $SP, %A
movw (%A), %A
decw %A
movw (%A), %D, %D
decw %A
addw (%A), %D, %D
decw %A
addw (%A), %D, %D
movw %D, (%A)
addw %A, $1, %D
leaw $SP, %A
movw %D, (%A)
