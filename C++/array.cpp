#include <iostream>
#include <array>
#include <list>

int main() {
    std::array<int, 5> myArray = {1, 2, 3, 4, 5};

    // Accessing elements
    std::cout << "Array elements: ";
    for (int i : myArray) {
        std::cout << i << " ";
    }

    // CRUD operations
    // Update (modify an element)
    myArray[2] = 10;

    // Insert (add an element at a specific position)
    myArray[3] = 20;

    // Delete (remove an element)
    myArray[1] = 0;

    std::cout << "\nUpdated Array elements: ";
    for (int i : myArray) {
        std::cout << i << " ";
    }

    return 0;
}
