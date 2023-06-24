#include <cstdio>
#include <string>

using namespace std;

char buff[100];

int main()
{
    scanf("%[^\n]\n", buff);
    string s = buff;
    printf("%s\n", s.c_str());
}