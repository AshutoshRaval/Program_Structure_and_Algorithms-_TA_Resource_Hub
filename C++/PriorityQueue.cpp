#include <iostream>
#include <queue>

int main() {
    std::priority_queue<int> myPriorityQueue;

    // Pushing elements
    myPriorityQueue.push(3);
    myPriorityQueue.push(1);
    myPriorityQueue.push(4);

    // Popping elements
    while (!myPriorityQueue.empty()) {
        std::cout << myPriorityQueue.top() << " ";
        myPriorityQueue.pop();
    }

    return 0;
}
