#include <stdio.h>
#include <string.h>

int main() {
    char inputString[100];
    printf("Enter a string: ");
    scanf("%s", inputString);

    int frequency[256] = {0}; // Assuming ASCII characters
    int maxFrequency = 0;

    // Count the frequency of each character in the input string
    for (int i = 0; i < strlen(inputString); i++) {
        frequency[inputString[i]]++;
        if (frequency[inputString[i]] > maxFrequency) {
            maxFrequency = frequency[inputString[i]];
        }
    }

    printf("The most frequent character(s) is/are: ");
    for (int i = 0; i < 256; i++) {
        if (frequency[i] == maxFrequency && maxFrequency > 0) {
            printf("%c ", i);
        }
    }
    printf("with frequency %d.\n", maxFrequency);

    return 0;
}
