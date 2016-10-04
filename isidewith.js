var output = ['Question;Yes;No;Count'];

var output = [];
var polls = $('.poll');

for(var i = 0; i < polls.length; i++) {
    var p = $($('.poll')[i]);
    output.push( [p.find('.question').html(),
		  p.find('.yes').html(),
		  p.find('.no').html(),
		  p.find('.count').html()].join(';')
	       ) 
}

console.log(output.join('\n'))
