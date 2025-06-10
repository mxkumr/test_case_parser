/**
 * This is a file level documentation comment
 * Total documentation comments: 2
 * Total classes: 2
 * Total functions: 5
 * Total variables: 8
 * Total comments: 5
 * Total keywords used: 18 (class, public, private, protected, virtual, const, static, template, typename, auto, for, if, else, return, new, delete, namespace, using)
 * Total identifiers: 12
 * Total literals: 9
 */

#include <iostream>
#include <vector>
#include <string>
#include <memory>

namespace TestNamespace {

// Template class definition
template<typename T>
class Container {
private:
    std::vector<T> data;
    static const int MAX_SIZE = 100;

public:
    Container() = default;

    void add(const T& item) {
        if (data.size() < MAX_SIZE) {
            data.push_back(item);
        }
    }

    // Const member function
    size_t size() const {
        return data.size();
    }
};

/**
 * Class demonstrating inheritance and polymorphism
 */
class Shape {
protected:
    std::string name;
    double area;

public:
    Shape(const std::string& n) : name(n), area(0.0) {}
    virtual ~Shape() = default;

    virtual double calculateArea() const = 0;
    std::string getName() const { return name; }
};

class Circle : public Shape {
private:
    double radius;
    const double PI = 3.14159;

public:
    Circle(const std::string& n, double r) 
        : Shape(n), radius(r) {}

    double calculateArea() const override {
        return PI * radius * radius;
    }
};

} // namespace TestNamespace

int main() {
    using namespace TestNamespace;

    // Smart pointer usage
    auto circle = std::make_unique<Circle>("Test Circle", 5.0);
    
    // Container usage
    Container<int> numbers;
    for (int i = 0; i < 5; i++) {
        numbers.add(i * 2);
    }

    // Output results
    std::cout << "Circle name: " << circle->getName() << std::endl;
    std::cout << "Circle area: " << circle->calculateArea() << std::endl;
    std::cout << "Container size: " << numbers.size() << std::endl;

    return 0;
} 