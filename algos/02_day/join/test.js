var assert = require('assert');
const file = require('./join')
const join = require('./join').join



describe('Day 02', function () {
  describe('Joins', function () {
    it('should return "1, 2, 3" for [1, 2, 3] and ", ".', function () {
      assert.equal(join(file.arr1, file.separator1), file.expected1);
    });
    it(`should return "${file.expected2}" for "${file.arr2}" and "${file.separator2}".`, function () {
      assert.equal(join(file.arr2, file.separator2), file.expected2);
    });
    it(`should return "${file.expected3}" for "${file.arr3}" and "${file.separator3}".`,() => {
      assert.equal(join(file.arr3, file.separator3), file.expected3);
    });
    it(`should return "${file.expected4}" for "${file.arr4}" and "${file.separator4}".`,() => {
      assert.equal(join(file.arr4, file.separator4), file.expected4);
    });
    it(`should return "${file.expected5}" for "${file.arr5}" and "${file.separator5}".`,() => {
      assert.equal(join(file.arr5, file.separator5), file.expected5);
    });
  });
});








