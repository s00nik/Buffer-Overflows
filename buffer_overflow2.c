// Compile with gcc -m32 -fno-stack-protector -z execstack -o buffer buffer.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int overflow()
{
  char buf[80];
  int r;
  r = read(0, buf, 1000);
  printf("Read %d bytes.\n", r);
  return 0;
}

void printFlag()
{
  printf("%s\n", "You ran the mystery function!");
}

int main(int argc, char **argv)
{
  printf("Overflow the buffer to execute the function at memory address: %p\n", &printFlag);
  overflow();
  return 0;
}
