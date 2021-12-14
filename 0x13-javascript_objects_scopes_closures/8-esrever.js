#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {

  let rlist = [];
  while (list.length > 0) {
    rlist.push(list.pop());
  }
  return rlist;
};
