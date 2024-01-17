#include <iostream>
#include <stack>

int main() {
    std::stack<int> myStack;

    // Pushing elements
    myStack.push(1);
    myStack.push(2);
    myStack.push(3);

    // Popping elements
    while (!myStack.empty()) {
        std::cout << myStack.top() << "<<-- Items on top of the stack ";
        myStack.pop();
    }

    return 0;
}
