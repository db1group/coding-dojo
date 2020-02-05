import { isDivisibleBy, isFizz, isBuzz, isFizzBuzz, isFizzOrBuzz } from './fizzbuzz.js'

test('return true if is divible by number', () => {
    expect(isDivisibleBy(9, 3)).toBeTruthy();
})

test('return true - this fizz when number is divisible by three', () => {
    expect(isFizz(9)).toBeTruthy();
})

test('return number when number is not divisible by three', () => {
    expect(isFizz(8)).toBeFalsy();
})

test('return true - this buzz when number is divisible by five', () => {
    expect(isBuzz(10)).toBeTruthy();
})

test('return number when number is not divisible by five', () => {
    expect(isBuzz(8)).toBeFalsy();
})

test('return fizzbuzz when number is divisible by three and five', () => {
    expect(isFizzBuzz(15)).toBe('FizzBuzz');
})


test('return fizz buzz fizzBuzz', () => {
    expect(isFizzOrBuzz(15)).toBe('FizzBuzz');
    expect(isFizzOrBuzz(9)).toBe('Fizz');
    expect(isFizzOrBuzz(10)).toBe('Buzz');
    expect(isFizzOrBuzz(4)).toBe(4);
})