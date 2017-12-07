const check = (n) => {
  if (n % 2 === 0) {
    return false
  } else {
    const sqf = Math.floor(Math.sqrt(n)) + 1
    let prime = false
    let done = false
    let d = sqf % 2 === 1 ? sqf : sqf - 1
    while (!done) {
      if (n % d === 0 && d >= 2) {
        done = true
      }
      if (d === 1) {
        prime = true
        done = true
      } else {
        d -= 2
      }
    }
    return prime
  }
}

module.exports = {
  check
}
