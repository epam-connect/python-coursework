class ComplexNumber {
    constructor(real, imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    [Symbol.toPrimitive](hint) {
        if (hint === "string") {
            return `${this.real} + ${this.imaginary}i`;
        }
        if (hint === "number") {
            return this.real; // Example: Convert to real part for number operations
        }
        return `${this.real} + ${this.imaginary}i`;
    }
}

const num1 = new ComplexNumber(3, 4);
const num2 = new ComplexNumber(5, 6);

console.log(`${num1}`); // "3 + 4i"
console.log(num1 + 2);  // 5 (because `Symbol.toPrimitive` returns real part for number)
console.log(String(num2)); // "5 + 6i"
console.log("10" + 5);

