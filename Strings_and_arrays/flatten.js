const arrayToFlatten = [1, 2, 3, [4, 5], [6, 7, 8, [9]]]
function flatThis(arr, new_arr) {
  for (let i = 0; i < arr.length; i++) {
    if(Array.isArray(arr[i])) {
      flatThis(arr[i], new_arr)
    } else {
      new_arr.push(arr[i])
    }
  }
  return new_arr
}
console.log(flatThis(arrayToFlatten, []))
