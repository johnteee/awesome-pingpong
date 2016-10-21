var i = 0;
var startTimestamp = Date.now();
process.on('message', function(m) {
  i++
  process.send(m);
  if(i > 1000000) {
    console.log(m + (Date.now() - startTimestamp));
    process.exit();
  }
});
