/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

const nums2 = [1];
const expected2 = 1;

const nums3 = [];
const expected3 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums, i = 0) {
  if(i === nums.length) {
    return 0;
  }
  return nums[i] + sumArr(nums, i + 1)
}

console.log(sumArr(nums1))
console.log(sumArr(nums2))
console.log(sumArr(nums3))
// let sum = 0;
// for(let i = 0; i < nums.length; i++){
//   sum += nums[i]
// }
// return sum

// 5 + recursiveSig(4)
// 4 + recursiveSig(3)
//     3 + recursiveSig(2)
//         2 + recursiveSig(1)
//             1 + recursiveSig(0)
//                 0 is returned - base case reached, can start summing now
//                 - call stack "unwinds" now with .pop LIFO (matching indentation)
//             1 + 0 = 1 <- this sum becomes the right side of the next addition
//         2 + 1 = 3
//     3 + 3 = 6
// 4 + 6 = 10
// 5 + 10 = 15