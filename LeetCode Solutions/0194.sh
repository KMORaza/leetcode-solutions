awk '
{
    for (i = 1; i <= NF; i++) {
        a[NR, i] = $i
    }
    if (NF > max) max = NF
}
END {
    for (i = 1; i <= max; i++) {
        for (j = 1; j <= NR; j++) {
            printf "%s%s", a[j, i], (j == NR ? "\n" : " ")
        }
    }
}' file.txt
