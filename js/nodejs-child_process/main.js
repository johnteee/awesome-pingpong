var cp = require('child_process');
var child = cp.fork('./worker');

var i = 0;
child.on('message', function(m) {
  // Receive results from child process
  // console.log('received: ' + m);
  child.send("ping");
});

// Send child process some work
child.send('ping');
