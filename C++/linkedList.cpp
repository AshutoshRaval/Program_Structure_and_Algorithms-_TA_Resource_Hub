#include <iostream>

class Node {
public:
    int data;
    Node* next;

    Node(int value) : data(value), next(nullptr) {}
};

class LinkedList {
public:
    Node* head;

    LinkedList() : head(nullptr) {}

    // Insert at the beginning of the linked list
    void insertAtBeginning(int value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }

    // Display the linked list
    void display() {
        Node* current = head;
        std::cout << "Linked list elements: ";
        while (current) {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }

    // CRUD operations
    // Update (modify an element)
    void update(int oldValue, int newValue) {
        Node* current = head;
        while (current) {
            if (current->data == oldValue) {
                current->data = newValue;
                break;
            }
            current = current->next;
        }
    }

    // Insert (add an element at a specific position)
    void insertAfterNode(int nodeValue, int newValue) {
        Node* current = head;
        while (current) {
            if (current->data == nodeValue) {
                Node* newNode = new Node(newValue);
                newNode->next = current->next;
                current->next = newNode;
                break;
            }
            current = current->next;
        }
    }

    // Delete (remove an element)
    void remove(int value) {
        Node* current = head;
        Node* prev = nullptr;
        while (current) {
            if (current->data == value) {
                if (prev) {
                    prev->next = current->next;
                } else {
                    head = current->next;
                }
                delete current;
                break;
            }
            prev = current;
            current = current->next;
        }
    }
};

int main() {
    LinkedList myLinkedList;

    // Inserting elements at the beginning
    myLinkedList.insertAtBeginning(3);
    myLinkedList.insertAtBeginning(2);
    myLinkedList.insertAtBeginning(1);

    // Displaying the linked list
    myLinkedList.display();

    // CRUD operations
    // Update (modify an element)
    myLinkedList.update(2, 10);

    // Insert (add an element at a specific position)
    myLinkedList.insertAfterNode(1, 5);

    // Delete (remove an element)
    myLinkedList.remove(2);

    std::cout << "Updated Linked list elements: ";
    myLinkedList.display();

    return 0;
}
