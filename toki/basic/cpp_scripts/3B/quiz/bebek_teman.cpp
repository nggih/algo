#include <cstdio>

int main()
{
    int a, b, hasil, sisa;
    scanf("%d %d", &a, &b);

    hasil = a / b;
    sisa = a % b;
    printf("masing-masing %d\n", hasil);
    printf("bersisa %d\n", sisa);
}