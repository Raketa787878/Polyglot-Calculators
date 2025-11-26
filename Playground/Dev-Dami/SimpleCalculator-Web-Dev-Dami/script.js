// script.js

// Get the display element
const resultDisplay = document.getElementById('result');

// Initialize variables
let currentInput = '';
let operator = '';
let firstOperand = null;

/**
 * Appends a number to the display.
 * @param {string} number - The number to append.
 */
function appendNumber(number) {
    if (resultDisplay.value === 'Error') {
        clearDisplay();
    }
    currentInput += number;
    resultDisplay.value = currentInput;
}

/**
 * Appends an operator and handles the logic for calculation.
 * @param {string} op - The operator to append.
 */
function appendOperator(op) {
    if (currentInput === '' && firstOperand === null) return;

    if (firstOperand === null) {
        firstOperand = parseFloat(currentInput);
    } else if (currentInput !== '') {
        calculateResult();
    }

    operator = op;
    currentInput = '';
}

/**
 * Calculates the result of the expression.
 */
function calculateResult() {
    if (firstOperand === null || currentInput === '' || operator === '') return;

    const secondOperand = parseFloat(currentInput);
    let result = 0;

    // Perform calculation based on the operator
    switch (operator) {
        case '+':
            result = firstOperand + secondOperand;
            break;
        case '-':
            result = firstOperand - secondOperand;
            break;
        case '*':
            result = firstOperand * secondOperand;
            break;
        case '/':
            if (secondOperand === 0) {
                resultDisplay.value = 'Error';
                firstOperand = null;
                currentInput = '';
                operator = '';
                return;
            }
            result = firstOperand / secondOperand;
            break;
        default:
            return;
    }

    resultDisplay.value = result;
    firstOperand = result;
    currentInput = '';
    operator = '';
}

/**
 * Clears the display and resets the calculator state.
 */
function clearDisplay() {
    currentInput = '';
    operator = '';
    firstOperand = null;
    resultDisplay.value = '';
}
