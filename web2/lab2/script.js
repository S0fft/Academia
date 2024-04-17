// Функция для получения времени суток
function getTimeOfDay() {
    var hour = new Date().getHours();
    if (hour >= 7 && hour < 12) {
        return "Доброе утро";
    } else if (hour >= 12 && hour < 17) {
        return "Добрый день";
    } else if (hour >= 17 && hour < 24) {
        return "Добрый вечер";
    } else {
        return "Спокойной ночи";
    }
}

// Функция для проверки ввода данных
function validateInput(start, end, step) {
    if (isNaN(start) || isNaN(end) || isNaN(step)) {
        return "Пожалуйста, введите числа.";
    }
    if (start < 0 || end < 0 || step < 0) {
        return "Числа должны быть положительными.";
    }
    if (start >= end) {
        return "Начальное значение должно быть меньше конечного.";
    }
    if (step > (end - start)) {
        return "Шаг не должен превышать разницу между начальным и конечным значением.";
    }
    if (step === 0) {
        return "Шаг не должен быть равен нулю.";
    }
    return "";
}

// Функция для расчета значений функции
function calculateFunction(start, end, step) {
    var znach = [];
    var func = [];
    for (var x = start; x <= end; x += step) {
        znach.push(x);
        var y = Math.sin(x); // Пример вычисления функции, замените на свою функцию
        func.push(y);
    }
    return [znach, func];
}

// Функция для вывода результатов на страницу в виде таблицы
function displayResults(znach, func) {
    var table = "<table><tr><th>x</th><th>y</th></tr>";
    for (var i = 0; i < znach.length; i++) {
        table += "<tr><td>" + znach[i] + "</td><td>" + func[i] + "</td></tr>";
    }
    table += "</table>";
    document.getElementById("results").innerHTML = table;
}

// Отображение времени суток в footer при загрузке страницы
window.onload = function () {
    var greeting = getTimeOfDay();
    document.getElementById("greeting").innerText = greeting;
};
