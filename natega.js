var page = require('webpage').create();

page.open('http://www.results.eng.cu.edu.eg', function(status) {
  if (status === 'success') {
    var is_checked = page.evaluate(function() {
      return document.getElementById('td45')
                 .getElementsByTagName('a')
                 .length !== 0;
    });

    if (is_checked) {
      console.log('Appeared');
    } else {
      console.log('didn\'t appear');
    }
  }
  phantom.exit();
});