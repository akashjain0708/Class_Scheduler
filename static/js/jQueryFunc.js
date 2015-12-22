$(document).ready(function(){
	$("#signUpBtn").click(function(){
		$.ajax({
			url:'/login',
			data: $('#signUpForm').serialize(),
			type:'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});