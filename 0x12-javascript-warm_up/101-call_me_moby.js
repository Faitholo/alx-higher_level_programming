#!/usr/bin/node
exports.callMeMoby = function (var1, callback) {
  for (let i = 0; i < var1; i++) {
    callback(var1);
  }
};
