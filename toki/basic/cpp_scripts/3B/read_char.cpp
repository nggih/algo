#include <cstdio>

char c1, c2, c3;
int bil;

int main() {
    scanf("%c %c\n", &c1, &c2);
    scanf("%d\n", &bil);
    scanf("%c", &c3);

    printf("c1='%c' c2='%c' bil='%d' c3='%c'\n", c1, c2, bil, c3);
}