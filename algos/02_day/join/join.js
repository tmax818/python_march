/* Given an arr and a separator string, output a string of every item in the array separated by the separator.

No trailing separator at the end
Default the separator to a comma with a space after it if no separator is provided
*/
//R repeat/restate
//I two params arr str
// O str
// T talk through the solution
const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {}

module.exports = { join, arr1, arr2, arr3, arr4, arr5, separator1, separator2, separator3, separator4, separator5, expected1, expected2, expected3, expected4, expected5 };