// This is my first C code.
// If you're using Visual Studio, this is needed to use scanf without warnings(#define _CRT_SECURE_NO_WARNINGS)

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main(void) {
    char name[256];
    int age;
    float weight;
    double height;
    char hobby[256];

    printf("What is your name? ");
    scanf("%255s", name);               
    printf("How old are you? ");
    scanf("%d", &age);

    while (getchar() != '\n');          

    printf("How much do you weigh? (kg) ");
    scanf("%f", &weight);

    printf("How tall are you? (cm) ");
    scanf("%lf", &height);

    printf("What is your hobby? ");
    scanf("%255s", hobby);

    
    printf("\n--- Nice to meet you! ---\n");
    printf("Name   : %s\n", name);
    printf("Age    : %d years old\n", age);
    printf("Weight : %.1f kg\n", weight);
    printf("Height : %.1f cm\n", height);
    printf("Hobby  : %s\n", hobby);
    printf("-------------------------\n");

    return 0;
}

