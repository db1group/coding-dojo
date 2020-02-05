const isDivisibleBy = (number, divisor) => {
    return number % divisor == 0;
}

const isFizz = (number) => {
    return isDivisibleBy(number, 3); 
}

const isBuzz = (number) => {
    return isDivisibleBy(number, 5); 
}

const isFizzBuzz = (number) => {
    return isDivisibleBy(number,3) && isDivisibleBy(number,5) ? 'FizzBuzz' : number
}

const isFizzOrBuzz = (number) => {
    let result = '';
    if(isFizz(number)){
        result += 'Fizz';
    }
    if(isBuzz(number)){
        result += 'Buzz'
        return result;
    }
    return result == '' ? number : result;
}

export {
 isDivisibleBy,
 isFizz,
 isBuzz,
 isFizzBuzz,
 isFizzOrBuzz,
}