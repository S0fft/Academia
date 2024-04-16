// Функция для вызова окна ввода имени пользователя
function greetUser() {
    var name = prompt("Введите ваше имя:");
    if (name) {
        document.querySelector("header h1").textContent = "Здравствуйте, " + name + "!";
    } else {
        document.querySelector("header h1").textContent = "Привет Гость!";
    }
}

// Вызов функции при загрузке страницы
window.onload = greetUser;

// Обработчик отправки формы для вычисления арифметического выражения
document.getElementById("calcForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию
    var expression = document.getElementById("expression").value;
    var result = eval(expression); // Вычисляем результат выражения
    document.getElementById("result").textContent = "Результат: " + result;
});
