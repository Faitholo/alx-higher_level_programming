#!/usr/bin/node

exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
