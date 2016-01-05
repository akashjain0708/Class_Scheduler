$(document).ready(function(){
	$("#signConfirmBtn").click(function(){		
		$.ajax({
			url:"/login",
			data: $("form").serialize(),
			type:"POST",
			success: function(response){
				console.log(response);				
				var resp = $.parseJSON(response);				
				if(resp.status == "OK")
				{
					alert('Thank you for signing up!');
					window.location.replace(resp.redirect);
				}
				else
				{
					$('#successField').text(resp.errorMessage);
				}
			},
			error: function(error){				
				console.log(error);				
			}
		});
	});
	$('#loginBtn').click(function(){		
		$.ajax({
			url:"/loginCheck",
			data: $("form").serialize(),
			type:"POST",
			success: function(response){
				console.log(response);				
				var resp = $.parseJSON(response);				
				if(resp.status == "OK")
				{					
					window.location.replace(resp.redirect);
				}
				else
				{
					$('#successField').text(resp.errorMessage);
				}
			},
			error: function(error){				
				console.log(error);				
			}
		});
	});
});