/**
 * This is a file level documentation comment
 * Total documentation comments: 2
 * Total functions: 4
 * Total variables: 7
 * Total comments: 6
 * Total keywords used: 12 (include, define, struct, int, char, void, return, if, else, for, while, sizeof)
 * Total identifiers: 9
 * Total literals: 8
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_SIZE 100
#define PI 3.14159

/* Structure definition */
struct Point {
    int x;
    int y;
    char label[20];
};

/**
 * Function to calculate distance between two points
 */
double calculate_distance(struct Point p1, struct Point p2) {
    int dx = p2.x - p1.x;
    int dy = p2.y - p1.y;
    return sqrt(dx * dx + dy * dy);
}

// Function to initialize a point
void init_point(struct Point* p, int x, int y, const char* label) {
    p->x = x;
    p->y = y;
    strncpy(p->label, label, 19);
    p->label[19] = '\0';
}

/* Array processing function */
int process_array(int arr[], int size) {
    int sum = 0;
    // Calculate sum of array elements
    for (int i = 0; i < size; i++) {
        if (arr[i] > 0) {
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    // Variable declarations
    struct Point p1, p2;
    int numbers[5] = {1, 2, 3, 4, 5};
    
    init_point(&p1, 0, 0, "Origin");
    init_point(&p2, 3, 4, "Point A");
    
    double dist = calculate_distance(p1, p2);
    int sum = process_array(numbers, 5);
    
    printf("Distance: %f\n", dist);
    printf("Sum: %d\n", sum);
    
    return 0;
} 