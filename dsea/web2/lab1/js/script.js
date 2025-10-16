// Функция для вызова окна ввода имени пользователя
function greetUser() {
    var name = prompt("Enter your name:");
    if (name) {
        document.querySelector("header h1").textContent = "Welcome, " + name + "!";
    } else {
        document.querySelector("header h1").textContent = "Hello guest!";
    }
}

// Вызов функции при загрузке страницы
window.onload = greetUser;

// Обработчик отправки формы для вычисления арифметического выражения
document.getElementById("calcForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию
    var expression = document.getElementById("expression").value;
    var result = eval(expression); // Вычисляем результат выражения
    document.getElementById("result").textContent = "Result: " + result;
});
