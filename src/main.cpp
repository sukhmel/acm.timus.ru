#include <stdio.h>
#include <QCoreApplication>

#include "excercises.h"

int main(int, char *[])
{
#ifndef ONLINE_JUDGE
    freopen("io/stdin.txt", "rt", stdin);
    freopen("io/stdout.txt", "wt", stdout);
#endif
    int repeats = -1;
    scanf("%d\n", &repeats);
    for (int i = 0; i < repeats; ++i)
    {
        calculate_NUM_name();
        printf("\n~~~~~~~~~~~~~~~~~~~\n");
    }
    return 0;
}
