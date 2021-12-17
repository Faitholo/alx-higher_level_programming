#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  return list.filter((value) => (value === searchElement)).length;
};
