#include <iostream>
#include <list>

int main() {
    std::list<int> myList = {1, 2, 3, 4, 5};

    // Accessing elements
    std::cout << "List elements: ";
    for (int i : myList) {
        std::cout << i << " ";
    }

    // CRUD operations
    // Update (modify an element)
    int oldValue = 3;
    int newValue = 10;

    for (auto& element : myList) {
        if (element == oldValue) {
            element = newValue;
            break;
        }
    }

    // Insert (add an element at a specific position)
    int nodeValue = 4;
    int newValueInsert = 20;

    for (auto it = myList.begin(); it != myList.end(); ++it) {
        if (*it == nodeValue) {
            myList.insert(++it, newValueInsert);
            break;
        }
    }

    // Delete (remove an element)
    int valueToDelete = 2;
    myList.remove(valueToDelete);

    std::cout << "\nUpdated List elements: ";
    for (int i : myList) {
        std::cout << i << " ";
    }

    return 0;
}
