// Функція отримання часу доби
function getTimeOfDay() {
    var hour = New Date().getHours();
    if (hour >= 7 && hour < 12) {
        return "Доброго ранку";
    } else if (hour >= 12 && hour < 17) {
        return "Добрий день";
    } else if (hour >= 17 && hour < 24) {
        return "Добрий вечір";
    } else {
        return "На добраніч";
    }
}

// Функція перевірки введення даних
function validateInput(start, end, step) {
    if (isNaN(start) || isNaN(end) || isNaN(step)) {
        return "Будь ласка, введіть цифри.";
    }
    if (start < 0 | | end < 0 | | step < 0) {
        return "Числа повинні бути позитивними.";
    }
    if (start >= end) {
        return "Початкове значення має бути меншим від кінцевого.";
    }
    if (step > (end - start)) {
        return "Крок не повинен перевищувати різницю між початковим та кінцевим значенням.";
    }
    if (step === 0) {
        return "Крок не повинен дорівнювати нулю.";
    }
    return "";
}

// Функція до розрахунку значень функції
function calculateFunction(start, end, step) {
    var znach = [];
    var func = [];
    for (var x = start; x <= end; x + = step) {
        znach.push(x);
        var y = Math.sin(x); // Приклад обчислення функції, замініть свою функцію
        func.push(y);
    }
    return [znach, func];
}

// Функція для виведення результатів на сторінку у вигляді таблиці
function displayResults(znach, func) {
    var table = "<table><tr><th>x</th><th>y</th></tr>";
    for (var i = 0; i < znach.length; i++) {
        table += "<tr><td>" + znach[i] + "</td><td>" + func[i] + "</td></tr>";
    }
    table += "</table>";
    document.getElementById("results").innerHTML = table;
}

// Відображення часу доби у footer під час завантаження сторінки
window.onload = function () {
    var greeting = getTimeOfDay();
    document.getElementById("greeting").innerText = greeting;
};