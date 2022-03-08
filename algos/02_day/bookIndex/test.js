var assert = require('assert');
const file = require('./bookIndex')
const bookIndex = require('./bookIndex').bookIndex



describe('Day 02', function () {
  describe('Book Index', function () {
    it(`should return "${file.expected1}" for "${file.nums1}"`,() => {
      assert.equal(bookIndex(file.nums1), file.expected1);
    });
  });
});
