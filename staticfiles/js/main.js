
$('button').click(function(event){
event.preventDefault();
alert("Hi");
var element = $(this);
$.ajax({
	url : '/postcard/like_post/',
	method: 'GET',
	data: { 
		post_id: element.attr("data-id")},
	success: function(response){
			element.html(' '+response);
			}
	});
	
});
