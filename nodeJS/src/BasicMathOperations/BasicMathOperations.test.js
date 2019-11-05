import { sum, subtract, multiply, division } from './BasicMathOperations'

test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
});

test('subtract 3 - 1 to equal 2', () => {
    expect(subtract(3, 1)).toBe(2);
});

test('adds 2 * 2 to equal 4', () => {
    expect(multiply(2, 2)).toBe(4);
});

test('adds 6 / 2 to equal 3', () => {
    expect(division(6, 2)).toBe(3);
});
