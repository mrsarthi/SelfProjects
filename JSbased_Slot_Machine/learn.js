const prompt = require("prompt-sync")()
const ROWS = 3;
const COLS = 3;

const SYMBOLS_COUNT = {
    A: 2,
    B: 4,
    C: 6,
    D: 8,
};

const SYMBOL_VALUES = {
    A: 5,
    B: 4,
    C: 3,
    D: 2,
};

const deposit = () => {
    while (true) {
        const dep_amount = parseFloat(prompt("Enter the deposit amount: "))
        // console.log(typeof(dep_amount))
        if (isNaN(dep_amount) || dep_amount <= 0) console.log("Try again and enter a valid deposit amount ")
        else return dep_amount
    }
}
const getBet = (amount, lines) => {
    while (true) {
        const bet = parseInt(prompt("Enter the bet per line: "))
        if (isNaN(bet) || bet > amount * lines || bet <= 0) console.log("Enter a bet per line ")
        else return bet
    }
}

const getnoofLines = () => {
    const noofLines = parseInt(prompt("Enter no. of Lines to bet on: "))
    // console.log(typeof(dep_amount))
    if (isNaN(noofLines) || noofLines <= 0 || noofLines > 3) console.log("Invalid no. of Line, try again ")
    else return noofLines
}

const spin = () => {
    const symbols = []
    for (const [symbol, count] of Object.entries(SYMBOLS_COUNT)) {
        for (let i = 0; i < count; i++) {
            symbols.push(symbol)
        }
    }
}
var amount = deposit()
var selected_lines = getnoofLines()
var bet_amount = getBet(amount, selected_lines)