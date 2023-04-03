function solution(n, k) {
  let num = n.toString(k);
  return num.split('0').map(Number).filter(isPrime).length;
}

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}
