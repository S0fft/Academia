#include <SFML/Graphics.hpp>

int main()
{
    sf::RenderWindow window(sf::VideoMode(800, 600), "My Drawing");

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
            {
                window.close();
            }
        }

        window.clear();

        // Рисование прямоугольника
        sf::RectangleShape rectangle(sf::Vector2f(100, 50));
        rectangle.setPosition(200, 300);
        rectangle.setFillColor(sf::Color::Green);

        window.draw(rectangle);

        window.display();
    }

    return 0;
}
