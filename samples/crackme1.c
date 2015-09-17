#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	if (argc != 2) {
		return 2;
	}

	char *key = (char *) malloc(0x20);
	strncpy (key, "f222e18ee5a3d7bf8c47e055d47b8830", 0x20);

	for (int i = 0; i < 0x20; i++) {
		if (argv[1][i] != key[i])
			return 0;
	}

	printf ("You win! Go grab a prize!\n");

	return 0;
}
