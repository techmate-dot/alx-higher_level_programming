#!/usr/bin/node

exports.converter = function (base) {
  calc.apply(calc, arguments)
  return calc;
};

function calc (num) {
  console.log(arguments['0'] + num)
  return Number(arguments[0])
}
