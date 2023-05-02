const prompt = require("prompt-sync")()

const deposit = () => {
    const dep_amount = prompt("Enter the deposit amount: ")
    console.log(dep_amount)
}

deposit()