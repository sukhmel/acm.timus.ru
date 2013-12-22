#include <stdio.h>
#include <QCoreApplication>

#include "excercises.h"

int main(int, char *[])
{
#ifndef ONLINE_JUDGE
    freopen("io/stdin.txt", "rt", stdin);
    freopen("io/stdout.txt", "wt", stdout);
#endif
    for (int i = 0; i < 2; ++i)
    {
        calculate_1639_chocolate();
        printf("\n~~~~~~~~~~~~~~~~~~~\n");
    }
    return 0;
}
